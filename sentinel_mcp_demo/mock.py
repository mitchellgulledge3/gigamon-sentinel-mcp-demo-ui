from __future__ import annotations

"""Mock MCP client used when the terminal demo runs without Azure connectivity.

The mock intentionally mirrors the small interface exposed by `SentinelMCPClient`
so the rest of the terminal app can switch between `MCP_DEMO_MODE=mock` and
`MCP_DEMO_MODE=real` without branching throughout the codebase.
"""

import json
from typing import Any

from .client import MCPTool, MCPToolResult


class MockSentinelMCPClient:
    """Return deterministic MCP-like results for offline presenter practice."""

    def __init__(self) -> None:
        self.tools = [
            MCPTool(
                name="Gigamon_Visibility_Posture_Summary",
                description="Summarize Gigamon visibility posture across sources, destinations, apps, and bytes.",
                input_schema={
                    "type": "object",
                    "properties": {"workspaceId": {"type": "string"}},
                },
            ),
            MCPTool(
                name="Gigamon_Lateral_Movement_Triage",
                description="Triage possible east-west movement over SMB, RDP, and SSH.",
                input_schema={
                    "type": "object",
                    "properties": {"workspaceId": {"type": "string"}},
                },
            ),
            MCPTool(
                name="Gigamon_DNS_Anomaly_Hunt",
                description="Hunt DNS anomalies using query types, reply codes, and response times.",
                input_schema={
                    "type": "object",
                    "properties": {"workspaceId": {"type": "string"}},
                },
            ),
            MCPTool(
                name="Gigamon_TLS_Risk_Summary",
                description="Summarize weak TLS protocol, key length, certificate, and JA3 signals.",
                input_schema={"type": "object", "properties": {"workspaceId": {"type": "string"}}},
            ),
            MCPTool(
                name="Gigamon_Top_Talkers_By_App",
                description="Rank applications by flows, bytes, packets, sources, and destinations.",
                input_schema={"type": "object", "properties": {"workspaceId": {"type": "string"}}},
            ),
            MCPTool(
                name="Gigamon_JA3_Threat_Match",
                description="Match observed JA3/JA3S TLS fingerprints to known-bad C2 / RAT signatures.",
                input_schema={"type": "object", "properties": {"workspaceId": {"type": "string"}}},
            ),
            MCPTool(
                name="Gigamon_Beacon_Periodicity_Hunt",
                description="Detect C2 beaconing by computing per-flow inter-arrival jitter and IQR per (src,dst,port).",
                input_schema={"type": "object", "properties": {"workspaceId": {"type": "string"}}},
            ),
            MCPTool(
                name="Gigamon_Shadow_IT_App_Discovery",
                description="Discover unsanctioned apps (P2P, Tor, consumer VPN, RMM, personal cloud, crypto-mining) and the affected hosts.",
                input_schema={"type": "object", "properties": {"workspaceId": {"type": "string"}}},
            ),
        ]

    async def connect(self) -> None:
        """Match the real client's async connect method without doing network I/O."""

        return None

    async def close(self) -> None:
        """Match the real client's async close method without owning resources."""

        return None

    async def list_tools(self) -> list[MCPTool]:
        """Return static tool metadata in the same shape as `tools/list`."""

        return self.tools

    async def call_tool(self, tool_name: str, arguments: dict[str, Any] | None = None) -> MCPToolResult:
        """Return a deterministic text result shaped like an MCP tool response."""

        args = arguments or {}
        workspace = args.get("workspaceId") or "mock-workspace"
        text = {
            "Gigamon_Visibility_Posture_Summary": (
                f"Visibility posture for {workspace}: 274 Gigamon events across 24 sources and 19 destinations.\n"
                "- Top apps: https, dns, smb, rdp, ssh\n"
                "- Total bytes observed: 3.8 GB\n"
                "- Recommended action: pivot into lateral movement and DNS tools for investigation depth"
            ),
            "Gigamon_Lateral_Movement_Triage": (
                f"Lateral movement triage for {workspace}: elevated SMB/RDP/SSH east-west activity.\n"
                "- 31 candidate flows on ports 445, 3389, and 22\n"
                "- Top sources: 10.12.4.18, 10.12.4.23\n"
                "- Recommended action: isolate the top source and validate endpoint identity"
            ),
            "Gigamon_DNS_Anomaly_Hunt": (
                f"DNS anomaly hunt for {workspace}: suspicious lookup pattern detected.\n"
                "- Failed responses: NXDOMAIN and SERVFAIL\n"
                "- Slow query family: TXT and A lookups\n"
                "- Recommended action: review queried domains and source workload owner"
            ),
            "Gigamon_TLS_Risk_Summary": (
                f"TLS risk summary for {workspace}: weak crypto and JA3 observations require review.\n"
                "- Weak protocol: TLS 1.0 / TLS 1.1\n"
                "- Weak key observations: 1024-bit RSA\n"
                "- Recommended action: map issuer/common-name pairs to application owners"
            ),
            "Gigamon_Top_Talkers_By_App": (
                f"Top talkers for {workspace}: https and unknown-tcp dominate byte volume.\n"
                "- Top source: 10.12.8.44\n"
                "- Top destination: 52.239.148.88\n"
                "- Recommended action: verify sanctioned app ownership for high-volume transfers"
            ),
            "Gigamon_JA3_Threat_Match": (
                f"JA3 threat match for {workspace}: 536 hits on known-bad fingerprints across 9 unique JA3s.\n"
                "- Top families: Cobalt Strike, Sliver, Trickbot, Emotet, Tor, Adwind RAT\n"
                "- Top affected source: 10.12.4.23 (118 hits)\n"
                "- Recommended action: pivot into endpoint EDR to validate the implant and isolate the host"
            ),
            "Gigamon_Beacon_Periodicity_Hunt": (
                f"Beacon periodicity hunt for {workspace}: 7 (src,dst,port) pairs match the C2 beacon profile.\n"
                "- Filter: jitter < 0.25, IQR ratio < 0.3, median gap >= 15s\n"
                "- Top pair: 10.12.8.44 -> 185.62.190.4:443 (median gap 60s, jitter 0.08)\n"
                "- Recommended action: correlate with TLS risk and JA3 results, then block egress"
            ),
            "Gigamon_Shadow_IT_App_Discovery": (
                f"Shadow IT discovery for {workspace}: 12 unsanctioned apps observed.\n"
                "- Risk categories: P2P, Tor, consumer VPN, RMM, personal cloud, crypto-mining\n"
                "- Top apps: bittorrent, tor, anydesk, megasync, xmrig\n"
                "- Recommended action: send findings to IT for policy and licensing follow-up"
            ),
        }.get(tool_name, f"Mock result for {tool_name}:\n{json.dumps(args, indent=2)}")

        return MCPToolResult(
            tool_name=tool_name,
            content=[{"type": "text", "text": text}],
            is_error=False,
        )
