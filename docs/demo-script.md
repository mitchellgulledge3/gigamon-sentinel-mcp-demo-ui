# Demo script

For a live working session with a Gigamon developer, use `docs/working-session-guide.md`. This file is the shorter presenter script.

## Setup

1. Show the official Gigamon Sentinel connector schema.
2. Show `logseeder/GigamonCcfMcpDemo_CL.json`, derived from that schema.
3. Run LogSeeder to create and seed `GigamonCcfMcpDemo_CL`.
4. Publish the MCP tools from `mcp-tools/`.
5. Start the terminal demo.

## Live prompts

1. `Summarize Gigamon visibility posture`
2. `Show possible lateral movement`
3. `Hunt DNS anomalies`
4. `Summarize TLS risk`
5. `Show top talkers by app`

## Story arc

1. **Visibility posture:** prove Gigamon telemetry is present, fresh, and useful in Sentinel.
2. **Lateral movement:** pivot to east-west/admin protocol flows that may indicate attacker movement.
3. **DNS anomalies:** look for command-and-control style lookup failures, slow responses, and suspicious names.
4. **TLS risk:** expose weak protocol, weak key, certificate, and JA3/JA3S signals.
5. **Top talkers:** prioritize response by applications, sources, destinations, bytes, and packets.

Run them in one interactive terminal:

```bash
python3 terminal_demo.py --show-raw
```

The detailed use-case and talk-track guide is in `docs/tool-use-cases.md`.

## Close

This is a developer pattern, not a one-off demo. Gigamon can ship the schema, suggested detections, and MCP tool definitions as developer assets so customer agents can reason over Gigamon visibility data in Sentinel.
