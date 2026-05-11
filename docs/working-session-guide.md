# Live working session guide

Use this guide when a Microsoft advisor and a Gigamon developer are on a call together. The goal is to leave the call with the developer understanding the pattern and knowing exactly where to customize it for Gigamon's own platform.

## Outcome

By the end, you should have:

| Outcome | Proof |
| --- | --- |
| Demo data in Sentinel | `GigamonCcfMcpDemo_CL` returns rows |
| Custom MCP tools published | Five Gigamon tools exist in the MCP collection |
| Terminal demo working | Prompts return Sentinel-backed results |
| Platform integration path understood | Developer knows which code to reuse in Gigamon's platform |

## Roles

| Person | Owns |
| --- | --- |
| Microsoft advisor | Azure/Sentinel setup, MCP publishing, explaining the pattern |
| Gigamon developer | Reviewing schema, KQL, tool names, and platform integration fit |

## Step 0: Confirm access

Run:

```bash
az account show
```

Confirm:

| Check | Why |
| --- | --- |
| Correct tenant | Tokens must come from the tenant with Sentinel access |
| Correct subscription | LogSeeder creates Azure resources in this subscription |
| Sentinel workspace exists | The demo writes and queries data there |
| You can publish MCP tools | Needed for the custom tool collection |

If this fails, run:

```bash
az login
az account set --subscription "<subscription-id-or-name>"
```

## Step 1: Clone the repo

```bash
git clone https://github.com/MitchellGulledge3/gigamon-sentinel-mcp-demo.git
cd gigamon-sentinel-mcp-demo
```

Show these files first:

| File | What to explain |
| --- | --- |
| `logseeder/GigamonCcfMcpDemo_CL.json` | Demo table schema based on the official Gigamon Sentinel connector |
| `mcp-tools/` | The KQL queries that become MCP tools |
| `terminal_demo.py` | The simple prompt loop that calls the tools |

## Step 2: Prepare Python

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Edit `.env`:

```text
MCP_DEMO_MODE=real
SENTINEL_MCP_COLLECTION=Gigamon-Sentinel-MCP-Demo
SENTINEL_MCP_TOOL=Gigamon_Visibility_Posture_Summary
MCP_TOOL_ARGUMENT_TEMPLATE={}
MCP_DEFAULT_ARGUMENTS={"workspaceId":"<log-analytics-workspace-customer-id>"}
```

The `workspaceId` is the Log Analytics workspace customer ID, not the Azure resource ID.

## Step 3: Seed demo data

Copy the schema into your LogSeeder repo:

```bash
cp ./logseeder/GigamonCcfMcpDemo_CL.json /path/to/sentinel-logseeder/schemas/
cd /path/to/sentinel-logseeder
```

Run LogSeeder:

```bash
pwsh -NoLogo -NoProfile -ExecutionPolicy Bypass \
  -File ./scripts/Invoke-SampleDataIngestion.ps1 \
  -TableName GigamonCcfMcpDemo_CL \
  -Schema ./schemas/GigamonCcfMcpDemo_CL.json \
  -RowCount 250 \
  -TimeWindowMinutes 1440 \
  -Deploy -Ingest
```

What this does:

| Resource | Plain-English meaning |
| --- | --- |
| Table | Where the Gigamon demo rows live |
| DCE | The ingestion endpoint |
| DCR | The mapping rule that sends fields into the table |

Checkpoint query in Sentinel:

```kql
GigamonCcfMcpDemo_CL
| summarize RowCount=count(), FirstSeen=min(TimeGenerated), LastSeen=max(TimeGenerated)
```

Stop here until `RowCount` is greater than zero. If it is zero, wait a few minutes and query again.

## Step 4: Publish MCP tools

Return to this repo:

```bash
cd /path/to/gigamon-sentinel-mcp-demo
```

Publish:

```bash
python3 scripts/publish-mcp-tools.py \
  --collection Gigamon-Sentinel-MCP-Demo \
  --workspace-id "<log-analytics-workspace-customer-id>"
```

Explain this simply:

> Each `.kql` file becomes one custom MCP tool. The tool is a safe, reusable question over the Sentinel table.

## Step 5: Run the terminal demo

Run:

```bash
python3 terminal_demo.py --show-raw
```

Paste these prompts:

```text
Summarize Gigamon visibility posture
Show possible lateral movement
Hunt DNS anomalies
Summarize TLS risk
Show top talkers by app
```

Checkpoint:

| Prompt | Success looks like |
| --- | --- |
| Visibility posture | Event count, source/destination count, apps |
| Lateral movement | Ports, flows, bytes, sources, destinations |
| DNS anomalies | Query types, failed/slow counts, names |
| TLS risk | Protocol versions, weak protocol/key/cert signals |
| Top talkers | Apps ranked by flows, bytes, packets |

## Step 6: Show where Gigamon would customize

| Area | File | Gigamon decision |
| --- | --- | --- |
| Real schema/table | `logseeder/GigamonCcfMcpDemo_CL.json` | Use demo table, real `GigamonV2_CL`, or customer table |
| Tool logic | `mcp-tools/*.kql` | Which investigations should Gigamon package? |
| Tool descriptions | `scripts/publish-mcp-tools.py` | How should tools appear to agents? |
| Prompt routing | `terminal_demo.py` | Which user phrases map to which tools? |
| Platform integration | `sentinel_mcp_demo/client.py` | Reuse the MCP client pattern inside Gigamon's app |

## Platform integration path

For Gigamon's platform, the terminal demo becomes:

```text
Gigamon UI prompt or button
        ->
Gigamon backend chooses an MCP tool
        ->
Sentinel MCP tool runs curated KQL
        ->
Gigamon UI shows summary, rows, and next action
```

The reusable code is mostly:

| Code | Reuse |
| --- | --- |
| `sentinel_mcp_demo/client.py` | MCP initialize, list tools, call tool, parse result |
| `mcp-tools/*.kql` | Security questions to productize |
| `scripts/publish-mcp-tools.py` | Tool publishing pattern |
| `terminal_demo.py` | Prompt routing and result summarization pattern |

## Fast troubleshooting

| Problem | What to do |
| --- | --- |
| `az` auth fails | Run `az login`, then set the right subscription |
| LogSeeder succeeds but no rows | Wait and rerun the query |
| MCP publish fails | Confirm account can manage Sentinel MCP tool collections |
| Terminal demo has no workspace | Fix `MCP_DEFAULT_ARGUMENTS` in `.env` |
| Tool returns no rows | Re-seed data or widen the query window |

## Suggested close

Use this close:

> This repo is the start-to-end developer path: seed Gigamon-shaped data, publish curated Sentinel MCP tools, validate them in terminal, and reuse the same pattern inside the Gigamon platform.
