from __future__ import annotations

"""Publish the demo KQL files as Microsoft Sentinel custom MCP tools.

This script is deliberately small and dependency-light so a Gigamon developer can
copy it into another reference repo, inspect every HTTP payload, and understand
exactly how KQL turns into an MCP tool. The script expects Azure CLI to already
be signed in to a tenant/subscription that can manage Sentinel custom MCP tools.
"""

import argparse
import json
import pathlib
import subprocess
import sys
import urllib.error
import urllib.request

SENTINEL_RESOURCE_ID = "4500ebfb-89b6-4b14-a480-7f749797bfcd"
API_BASE = "https://api.securityplatform.microsoft.com/aiprimitives/mcpToolCollections"

# Friendly tool descriptions are stored next to the publisher so the KQL files
# can stay focused on query logic while the MCP metadata stays easy to review.
DESCRIPTIONS = {
    "Gigamon_Visibility_Posture_Summary": "Summarize Gigamon visibility posture across events, sources, destinations, protocols, apps, and bytes.",
    "Gigamon_Lateral_Movement_Triage": "Triage possible east-west lateral movement using SMB, RDP, SSH, interfaces, bytes, RTT, and source/destination pairs.",
    "Gigamon_DNS_Anomaly_Hunt": "Hunt DNS anomalies such as failed lookups, slow responses, suspicious query names, and affected source IPs.",
    "Gigamon_TLS_Risk_Summary": "Summarize TLS risk using protocol versions, weak key sizes, expiring certificates, issuers, CNs, and JA3 signals.",
    "Gigamon_Top_Talkers_By_App": "Rank Gigamon-observed applications by bytes, packets, sources, and destinations.",
    "Gigamon_JA3_Threat_Match": "Match observed TLS JA3 / JA3S fingerprints against a known-bad list (Cobalt Strike, Sliver, Trickbot, Emotet, RATs) and return hit counts, sample clients, SNIs, and issuers.",
    "Gigamon_Beacon_Periodicity_Hunt": "Detect command-and-control beaconing by measuring inter-arrival-time periodicity (jitter, IQR ratio) per src/dst/port flow pair.",
    "Gigamon_Shadow_IT_App_Discovery": "Discover unsanctioned applications (P2P, Tor, consumer VPN, remote-access, crypto-mining, censorship-bypass) using Gigamon Application Intelligence labels.",
}


def az_token() -> str:
    """Return a Sentinel Platform Services bearer token from Azure CLI."""

    # Azure CLI handles the interactive/device auth experience; the script only
    # asks for the resource-specific token Sentinel custom MCP APIs require.
    completed = subprocess.run(
        [
            "az",
            "account",
            "get-access-token",
            "--resource",
            SENTINEL_RESOURCE_ID,
            "--query",
            "accessToken",
            "-o",
            "tsv",
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout.strip()


def request(method: str, url: str, token: str, payload: dict) -> dict:
    """Send one authenticated JSON request to the Sentinel MCP management API."""

    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        method=method,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        # Keep the API response body in the exception so publishing failures are
        # actionable without rerunning curl or opening a network trace.
        details = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"{method} {url} failed: HTTP {exc.code}: {details}") from exc


def tool_payload(collection: str, workspace_id: str, query_path: pathlib.Path) -> dict:
    """Build the custom MCP tool payload for a single `.kql` file."""

    name = query_path.stem
    return {
        "name": name,
        "title": name.replace("_", " "),
        "description": DESCRIPTIONS[name],
        "collectionName": collection,
        "properties": {
            "mcpToolType": "Kqs",
            # Sentinel executes this KQL when the MCP tool is called.
            "queryFormat": query_path.read_text().strip(),
            # The custom MCP API expects a JSON-schema object here. The most
            # important input for these tools is the Log Analytics workspace ID.
            "arguments": {
                "type": "object",
                "properties": {
                    "workspaceId": {
                        "type": "string",
                        "description": "Log Analytics workspace/customer ID to query.",
                    }
                },
                "required": ["workspaceId"],
            },
            "defaultArgumentValues": {"workspaceId": workspace_id},
        },
    }


def main() -> int:
    """Parse CLI flags, publish the collection, then publish every KQL tool."""

    parser = argparse.ArgumentParser(description="Publish Gigamon KQL files as Sentinel custom MCP tools.")
    parser.add_argument("--collection", default="Gigamon-Sentinel-MCP-Demo")
    parser.add_argument("--workspace-id", required=True)
    parser.add_argument("--tools-dir", default=str(pathlib.Path(__file__).parents[1] / "mcp-tools"))
    args = parser.parse_args()

    token = az_token()
    collection_payload = {
        "name": args.collection,
        "title": "Gigamon Sentinel MCP Demo",
        "description": "Custom Sentinel MCP tools for a Gigamon CCF end-to-end developer demo.",
    }
    print(f"Publishing collection: {args.collection}")
    try:
        print(json.dumps(request("PUT", f"{API_BASE}/{args.collection}", token, collection_payload), indent=2))
    except RuntimeError as exc:
        if "HTTP 409" in str(exc):
            print(f"  (collection {args.collection} already exists — continuing)")
        else:
            raise

    # Each KQL filename becomes the MCP tool name, which keeps source control,
    # Sentinel, and the terminal prompt router aligned.
    for query_path in sorted(pathlib.Path(args.tools_dir).glob("*.kql")):
        payload = tool_payload(args.collection, args.workspace_id, query_path)
        print(f"\nPublishing tool: {payload['name']}")
        print(json.dumps(request("PUT", f"{API_BASE}/{args.collection}/tools/{payload['name']}", token, payload), indent=2))

    return 0


if __name__ == "__main__":
    sys.exit(main())
