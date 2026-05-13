from __future__ import annotations

"""Interactive terminal demo for the Gigamon Sentinel MCP tools.

This replaces the earlier browser demo with the lowest-friction presenter flow:
run one Python command, type normal investigation prompts, and show the tool
selection, arguments, concise summary, and raw Sentinel MCP result in the same
terminal window.
"""

import argparse
import asyncio
import json
import os
from typing import Any

from dotenv import load_dotenv

from sentinel_mcp_demo.client import MCPToolResult, SentinelMCPClient
from sentinel_mcp_demo.mock import MockSentinelMCPClient


GIGAMON_TOOLS = {
    "visibility": "Gigamon_Visibility_Posture_Summary",
    "lateral": "Gigamon_Lateral_Movement_Triage",
    "dns": "Gigamon_DNS_Anomaly_Hunt",
    "tls": "Gigamon_TLS_Risk_Summary",
    "talkers": "Gigamon_Top_Talkers_By_App",
    "ja3": "Gigamon_JA3_Threat_Match",
    "beacon": "Gigamon_Beacon_Periodicity_Hunt",
    "shadow": "Gigamon_Shadow_IT_App_Discovery",
}

TOOL_ROUTES = [
    (("ja3", "fingerprint", "tls fingerprint", "c2 fingerprint"), GIGAMON_TOOLS["ja3"]),
    (("beacon", "beaconing", "periodicity", "c2 cadence", "callback"), GIGAMON_TOOLS["beacon"]),
    (("shadow it", "shadow", "unsanctioned", "tor", "bittorrent", "personal vpn", "crypto miner"), GIGAMON_TOOLS["shadow"]),
    (("lateral", "east-west", "rdp", "smb", "ssh", "movement"), GIGAMON_TOOLS["lateral"]),
    (("dns", "domain", "lookup", "nxdomain", "servfail"), GIGAMON_TOOLS["dns"]),
    (("tls", "ssl", "cert", "certificate", "weak key", "expired cert"), GIGAMON_TOOLS["tls"]),
    (("top", "talker", "app", "bytes", "packets", "bandwidth"), GIGAMON_TOOLS["talkers"]),
]

EXAMPLE_PROMPTS = [
    "Summarize Gigamon visibility posture",
    "Show possible lateral movement",
    "Hunt DNS anomalies",
    "Summarize TLS risk",
    "Show top talkers by app",
    "Match JA3 fingerprints to known C2",
    "Hunt for beaconing periodicity",
    "Discover shadow IT applications",
]


def parse_json_env(name: str, default: dict[str, Any]) -> dict[str, Any]:
    """Read an environment variable that must contain a JSON object."""

    raw = os.getenv(name)
    if not raw:
        return default
    try:
        value = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(f"{name} must be valid JSON: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError(f"{name} must be a JSON object.")
    return value


def render_arguments(message: str, template: str, defaults: dict[str, Any]) -> dict[str, Any]:
    """Render the prompt into the MCP argument template and merge defaults."""

    rendered = template.replace("{message}", message)
    try:
        args = json.loads(rendered)
    except json.JSONDecodeError as exc:
        raise ValueError(f"MCP_TOOL_ARGUMENT_TEMPLATE rendered invalid JSON: {exc}") from exc
    if not isinstance(args, dict):
        raise ValueError("MCP_TOOL_ARGUMENT_TEMPLATE must render to a JSON object.")
    return {**args, **defaults}


def select_tool(prompt: str) -> str:
    """Choose the Gigamon MCP tool that best matches the typed prompt."""

    configured = os.getenv("SENTINEL_MCP_TOOL", "").strip()
    prompt_lower = prompt.lower()
    for keywords, tool_name in TOOL_ROUTES:
        if any(keyword in prompt_lower for keyword in keywords):
            return tool_name
    return configured or GIGAMON_TOOLS["visibility"]


def create_mcp_client() -> SentinelMCPClient | MockSentinelMCPClient:
    """Create either the real Sentinel MCP client or the offline mock client."""

    mode = os.getenv("MCP_DEMO_MODE", "mock").strip().lower()
    if mode == "real":
        return SentinelMCPClient(
            collection=os.getenv("SENTINEL_MCP_COLLECTION"),
            server_url=os.getenv("SENTINEL_MCP_SERVER_URL"),
        )
    if mode == "mock":
        return MockSentinelMCPClient()
    raise ValueError("MCP_DEMO_MODE must be 'mock' or 'real'.")


def dataset_rows(result: MCPToolResult) -> list[dict[str, Any]]:
    """Extract Kusto PrimaryResult rows from the raw MCP text content."""

    rows: list[dict[str, Any]] = []
    for item in result.content:
        if item.get("type") != "text":
            continue
        text = str(item.get("text", ""))
        try:
            frames = json.loads(text)
        except json.JSONDecodeError:
            continue
        if not isinstance(frames, list):
            continue
        primary = next(
            (
                frame
                for frame in frames
                if isinstance(frame, dict)
                and frame.get("FrameType") == "DataTable"
                and frame.get("TableKind") == "PrimaryResult"
            ),
            None,
        )
        if not primary:
            continue
        columns = [column.get("ColumnName", "") for column in primary.get("Columns", [])]
        for row in primary.get("Rows", []):
            rows.append({columns[index]: value for index, value in enumerate(row) if index < len(columns)})
    return rows


def summarize(prompt: str, tool_name: str, rows: list[dict[str, Any]], raw_text: str) -> str:
    """Create a presenter-friendly summary from the first returned row."""

    if not rows:
        return raw_text or f"{tool_name} completed for: {prompt}"

    row = rows[0]
    if tool_name == GIGAMON_TOOLS["lateral"]:
        return (
            f"Lateral movement triage found {row.get('FlowCount')} candidate flows on destination port "
            f"{row.get('dst_port')}, totaling {row.get('TotalBytes')} bytes. Sources: {row.get('Sources')}. "
            f"Destinations: {row.get('Destinations')}."
        )
    if tool_name == GIGAMON_TOOLS["dns"]:
        return (
            f"DNS anomaly hunt found {row.get('Queries')} {row.get('dns_query_type')} queries, "
            f"with {row.get('FailedQueries')} failed and {row.get('SlowQueries')} slow responses. "
            f"Queries: {row.get('QueryNames')}."
        )
    if tool_name == GIGAMON_TOOLS["tls"]:
        return (
            f"TLS risk summary found {row.get('Sessions')} sessions for {row.get('ProtocolVersion')}. "
            f"Weak protocol sessions: {row.get('WeakProtocol')}; weak key observations: {row.get('WeakKey')}; "
            f"expiring soon: {row.get('ExpiringSoon')}."
        )
    if tool_name == GIGAMON_TOOLS["talkers"]:
        return (
            f"Top talkers shows {row.get('app_name')} / {row.get('app_family')} over {row.get('protocol')} "
            f"with {row.get('Flows')} flows and {row.get('Bytes')} bytes. Top sources: {row.get('TopSources')}."
        )
    if tool_name == GIGAMON_TOOLS["ja3"]:
        return (
            f"JA3 hunt: {row.get('TotalHandshakes')} handshakes — "
            f"{row.get('UniqueJa3')} unique JA3, {row.get('UniqueJa3s')} unique JA3S. "
            f"Known-bad hits: {row.get('KnownBadHits')}. "
            f"Hit fingerprints: {row.get('KnownBadJa3Samples')}. "
            f"Clients seen: {row.get('TopClients')} → SNIs: {row.get('TopSnis')}."
        )
    if tool_name == GIGAMON_TOOLS["beacon"]:
        return (
            f"Beacon hunt: analyzed {row.get('FlowsAnalyzed')} flows across "
            f"{row.get('CandidatePairs')} src/dst pairs. "
            f"Beaconing pairs: {row.get('BeaconingPairs')} "
            f"(fast<60s: {row.get('FastBeacons')}, slow≥10m: {row.get('SlowBeacons')}). "
            f"Top beaconing sources: {row.get('TopBeaconingSources')}; "
            f"top destinations: {row.get('TopBeaconingDests')}; "
            f"ports: {row.get('TopBeaconingPorts')}; apps: {row.get('TopBeaconingApps')}."
        )
    if tool_name == GIGAMON_TOOLS["shadow"]:
        return (
            f"Shadow IT discovery: {row.get('ShadowFlows')} flows, "
            f"{row.get('ShadowBytes')} bytes across {row.get('ShadowSources')} hosts. "
            f"Categories seen: {row.get('CategoriesSeen')}. "
            f"High-risk category hits: {row.get('HighRiskCategoryHit')}. "
            f"Sample sources: {row.get('SampleSourceIps')}."
        )

    return (
        f"Visibility posture found {row.get('Events')} Gigamon events across "
        f"{row.get('UniqueSources')} sources and {row.get('UniqueDestinations')} destinations, "
        f"totaling {row.get('TotalBytes')} bytes. Apps: {row.get('Apps')}."
    )


async def run_prompt(prompt: str, *, show_raw: bool) -> None:
    """Call the selected MCP tool once and print the result."""

    tool_name = select_tool(prompt)
    template = os.getenv("MCP_TOOL_ARGUMENT_TEMPLATE", '{"query":"{message}"}')
    defaults = parse_json_env("MCP_DEFAULT_ARGUMENTS", {})
    arguments = render_arguments(prompt, template, defaults)

    print(f"\nPrompt: {prompt}")
    print(f"Tool:   {tool_name}")
    print(f"Args:   {json.dumps(arguments, sort_keys=True)}")
    print("Status: calling Sentinel MCP...\n")

    client = create_mcp_client()
    await client.connect()
    try:
        result = await client.call_tool(tool_name, arguments)
    finally:
        await client.close()

    rows = dataset_rows(result)
    raw_text = result.text or json.dumps(result.content, indent=2)
    print("Summary")
    print("-------")
    print(summarize(prompt, tool_name, rows, raw_text))

    if show_raw:
        print("\nRaw MCP result")
        print("--------------")
        print(raw_text)


async def interactive_loop(show_raw: bool) -> None:
    """Run the live terminal prompt loop until the presenter exits."""

    print("Gigamon Sentinel MCP Terminal Demo")
    print("Type a prompt and press Enter. Type 'examples' to list prompts or 'quit' to exit.\n")
    print("Examples:")
    for prompt in EXAMPLE_PROMPTS:
        print(f"  - {prompt}")

    while True:
        try:
            prompt = input("\ngigamon-mcp> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            return

        if not prompt:
            continue
        if prompt.lower() in {"quit", "exit", "q"}:
            return
        if prompt.lower() == "examples":
            for example in EXAMPLE_PROMPTS:
                print(f"  - {example}")
            continue

        try:
            await run_prompt(prompt, show_raw=show_raw)
        except Exception as exc:
            print(f"Error: {exc}")


def main() -> None:
    """Load configuration, parse flags, and start the terminal demo."""

    load_dotenv()
    parser = argparse.ArgumentParser(description="Run the Gigamon Sentinel MCP terminal demo.")
    parser.add_argument("--prompt", help="Run one prompt and exit instead of starting the interactive loop.")
    parser.add_argument("--show-raw", action="store_true", help="Print the formatted raw MCP/Kusto result.")
    args = parser.parse_args()

    if args.prompt:
        asyncio.run(run_prompt(args.prompt, show_raw=args.show_raw))
    else:
        asyncio.run(interactive_loop(show_raw=args.show_raw))


if __name__ == "__main__":
    main()
