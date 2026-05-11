# Gigamon Sentinel MCP Demo (UI publish variant)

> **Variant:** This repo publishes the custom MCP tools through the **Microsoft Defender portal UI** ("Save as tool" flow), with no API publishing script. For the API-driven variant, see [`gigamon-sentinel-mcp-demo`](https://github.com/MitchellGulledge3/gigamon-sentinel-mcp-demo).

This repo is a GitHub-ready reference implementation for a Gigamon developer who wants to show an end-to-end Microsoft Sentinel custom MCP tool integration.

The purpose is not to ship another generic chatbot. The purpose is to show how an ISV can expose focused, high-value security capabilities as **MCP tools** over the data they already bring into Microsoft Sentinel. Once those tools exist, a terminal demo, an ISV product experience, a Copilot-style UI, or another agent runtime can call the same capability.

## The story in one sentence

Gigamon has rich network visibility in Sentinel; MCP turns that visibility into reusable agent tools such as "summarize posture," "triage lateral movement," "hunt DNS anomalies," and "summarize TLS risk."

## Architecture at a glance

```mermaid
flowchart LR
    A["🛰️ Gigamon network telemetry<br/>(CCF / deep observability)"] -->|LogSeeder<br/>DCE + DCR| B[("📊 Microsoft Sentinel<br/>GigamonCcfMcpDemo_CL")]
    B --> C["📜 KQL tools<br/>mcp-tools/*.kql"]
    C -->|"Defender portal<br/>'Save as tool' (UI)"| D["🧰 Sentinel MCP Collection<br/>Gigamon-Sentinel-MCP-Demo"]
    D --> E["🤖 VS Code · Copilot Studio<br/>Foundry · Claude · ChatGPT"]
    D --> F["💻 terminal_demo.py<br/>(local agent)"]
    style A fill:#1f6feb,stroke:#1f6feb,color:#fff
    style B fill:#0969da,stroke:#0969da,color:#fff
    style D fill:#8250df,stroke:#8250df,color:#fff
```

## Recommended path for a live working session

If you are walking through this with a Gigamon developer, start here:

[`docs/working-session-guide.md`](docs/working-session-guide.md)

That guide is the most methodical path. It has roles, copy/paste commands, checkpoints, troubleshooting, and the exact places Gigamon would customize the pattern for their own platform.

## New to Sentinel? Read this first

| Term | Plain-English meaning |
| --- | --- |
| Microsoft Sentinel | Microsoft's cloud SIEM. It helps security teams collect logs, detect threats, investigate incidents, and respond. |
| Log Analytics workspace | The Azure data store Sentinel uses for logs. Think "database for security telemetry." |
| Table | A named set of rows in the workspace. This demo writes to `GigamonCcfMcpDemo_CL`. |
| KQL | Kusto Query Language. This is the query language used to search Sentinel logs. |
| LogSeeder | A sample-data tool that creates a table and inserts realistic demo rows. |
| DCE | Data Collection Endpoint. The Azure ingestion URL where custom log data is sent. |
| DCR | Data Collection Rule. The Azure rule that maps incoming data into the right table and columns. |
| MCP tool | A callable tool an agent can use. In this repo, each MCP tool runs one curated KQL query. |

The short version: **LogSeeder puts Gigamon-shaped rows into Sentinel; KQL asks useful security questions; MCP wraps those questions so an agent or app can call them.**

## What this demo proves

A Gigamon developer can:

1. Start from the official Sentinel connector table schema.
2. Use Sentinel LogSeeder to create a demo custom table and seed realistic telemetry.
3. Publish high-value KQL questions as Sentinel custom MCP tools.
4. Call those tools from a simple terminal prompt loop or any future agent runtime.

## Architecture

```text
Official Gigamon Sentinel schema
        |
        v
LogSeeder demo schema + sample value pools
        |
        v
GigamonCcfMcpDemo_CL in Log Analytics / Sentinel
        |
        v
KQL-backed custom Sentinel MCP tools
        |
        v
Interactive terminal demo that routes natural prompts to those tools
```

## What gets created

| Asset | Created by | Why it exists |
| --- | --- | --- |
| `GigamonCcfMcpDemo_CL` table | LogSeeder | Stores demo Gigamon CCF-style telemetry in Sentinel |
| Data Collection Endpoint | LogSeeder/Azure Monitor | Provides the ingestion endpoint for custom logs |
| Data Collection Rule | LogSeeder/Azure Monitor | Maps JSON fields into the custom table columns |
| `Gigamon-Sentinel-MCP-Demo` collection | Defender portal "Save as tool" UI | Groups the custom MCP tools |
| Five MCP tools | Defender portal "Save as tool" UI | Expose repeatable Gigamon investigation questions |
| Terminal demo | `terminal_demo.py` | Lets a presenter call the tools from a prompt |

## Why this matters for Gigamon developers

The developer does not have to guess what an agent might need. They can package a small set of opinionated tools around the security questions Gigamon is best positioned to answer:

| Developer asset | Why it helps |
| --- | --- |
| Official table schema | Keeps the demo aligned to the real Gigamon Sentinel connector |
| LogSeeder schema | Lets a developer or seller stand up demo data without waiting on a live appliance |
| KQL files | Make the security logic inspectable, reviewable, and versionable |
| MCP publisher script | Converts KQL into callable custom tools |
| Terminal demo | Shows the end-to-end tool call without Teams, browser, or admin-consent friction |
| Source annotations | Helps a developer understand and customize every moving part |

## Demo table

The demo table is `GigamonCcfMcpDemo_CL`. It uses the same column names and types as the official Sentinel Gigamon CCF table schema from:

```text
https://raw.githubusercontent.com/Azure/Azure-Sentinel/master/Solutions/Gigamon%20Connector/Data%20Connectors/Gigamon_CCF/Gigamon_table.json
```

The table name is intentionally different from `GigamonV2_CL` so the demo never collides with a production connector table.

The companion file `logseeder/GigamonCcfMcpDemo_CL.annotated.jsonc` explains the schema in a comment-friendly format. Keep `GigamonCcfMcpDemo_CL.json` as valid JSON for LogSeeder.

## End-to-end use case

**Use case:** a SOC analyst asks whether Gigamon network visibility data shows lateral movement, DNS anomalies, or TLS risk during a suspected intrusion.

The MCP tools expose that investigation as reusable capabilities:

| Tool | Purpose |
| --- | --- |
| `Gigamon_Visibility_Posture_Summary` | Executive posture summary: events, sources, destinations, apps, protocols, bytes |
| `Gigamon_Lateral_Movement_Triage` | Triage SMB/RDP/SSH east-west movement candidates |
| `Gigamon_DNS_Anomaly_Hunt` | Hunt suspicious or slow DNS activity |
| `Gigamon_TLS_Risk_Summary` | Summarize weak TLS, weak keys, expiring certs, JA3/JA3S signals |
| `Gigamon_Top_Talkers_By_App` | Find top applications, sources, destinations, bytes, packets |

For the full narrative, value proposition, latest real outputs, and talk track for each tool, see [`docs/tool-use-cases.md`](docs/tool-use-cases.md).

## Prerequisites

You need:

1. **Azure CLI** authenticated to the Sentinel workspace subscription.
2. **A Log Analytics workspace** with Microsoft Sentinel enabled.
3. **Permission to create custom log ingestion resources:** custom tables, DCRs, and DCEs.
4. **PowerShell 7** for LogSeeder.
5. **Python 3.9+** for the MCP publishing helper and terminal demo.
6. **Access to Sentinel custom MCP tool collection APIs** so the KQL files can be published as tools.

For the existing Mitchell demo workspace, the configured workspace customer ID is:

```text
77429a58-865a-4764-8429-aaacdfe3cb73
```

## Seed data with LogSeeder

This step creates the custom table and sends demo rows into Sentinel. If you are new to Azure Monitor ingestion, the important part is that LogSeeder hides most of the plumbing: it creates or reuses a DCE, creates a DCR, maps the schema, and posts sample data.

Copy `logseeder/GigamonCcfMcpDemo_CL.json` into your `sentinel-logseeder/schemas/` folder, then run:

```bash
cp /path/to/gigamon-sentinel-mcp-demo/logseeder/GigamonCcfMcpDemo_CL.json ./schemas/
cd /path/to/sentinel-logseeder
pwsh -NoLogo -NoProfile -ExecutionPolicy Bypass \
  -File ./scripts/Invoke-SampleDataIngestion.ps1 \
  -TableName GigamonCcfMcpDemo_CL \
  -Schema ./schemas/GigamonCcfMcpDemo_CL.json \
  -RowCount 250 \
  -TimeWindowMinutes 1440 \
  -Deploy -Ingest
```

Verify rows:

```kql
GigamonCcfMcpDemo_CL
| summarize RowCount=count(), FirstSeen=min(TimeGenerated), LastSeen=max(TimeGenerated)
```

If the query returns zero rows immediately after ingestion, wait a few minutes and query again. New custom tables and DCR mappings can take time to become queryable.

Useful validation queries:

```kql
GigamonCcfMcpDemo_CL
| summarize Events=count(), Apps=make_set(app_name, 20), Protocols=make_set(protocol, 10)
```

```kql
GigamonCcfMcpDemo_CL
| where dst_port in ("445", "3389", "22")
| summarize Flows=count(), Bytes=sum(tolong(total_bytes)) by dst_port, app_name
| order by Bytes desc
```

```kql
GigamonCcfMcpDemo_CL
| where app_name == "dns" or dst_port == "53"
| summarize Queries=count(), Failed=countif(dns_reply_code in ("NXDOMAIN", "SERVFAIL")) by dns_query_type
```

## Publish custom MCP tools (UI flow)

This variant of the demo does **not** include an API publisher script. Instead, you save each KQL query as a custom MCP tool by hand in the Microsoft Defender portal's Advanced Hunting page using the **Save as tool** flow.

Suggested collection name:

```text
Gigamon-Sentinel-MCP-Demo
```

Full step-by-step walkthrough (with field-by-field guidance and the official Microsoft Learn links):

➡️ [`docs/publish-tools-via-ui.md`](docs/publish-tools-via-ui.md)

Short version:

1. Open https://security.microsoft.com → **Hunting** → **Advanced hunting**.
2. Paste a KQL file from `mcp-tools/`, run it once to confirm rows.
3. Click **Save as tool** (context menu or KQL box menu).
4. In the flyout, set **Name** = the `.kql` filename without extension, paste the matching **Description**, choose or create the `Gigamon-Sentinel-MCP-Demo` **Collection**, set the **Default workspace** to your Sentinel workspace.
5. Repeat for every `.kql` file in `mcp-tools/`.

Reference: [Create and use custom Microsoft Sentinel MCP tools (preview)](https://learn.microsoft.com/azure/sentinel/datalake/sentinel-mcp-create-custom-tool)

## Terminal demo

Run the included interactive terminal demo:

```bash
cd /path/to/gigamon-sentinel-mcp-demo
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Edit `.env` and set:

```text
MCP_DEFAULT_ARGUMENTS={"workspaceId":"<log-analytics-workspace-customer-id>"}
```

Then start the app:

```bash
python3 terminal_demo.py --show-raw
```

Type prompts like:

```text
Summarize Gigamon visibility posture
Show possible lateral movement
Hunt DNS anomalies
Summarize TLS risk
Show top talkers by app
```

For a single command you can paste into a demo script, run:

```bash
python3 terminal_demo.py --prompt "Show possible lateral movement" --show-raw
```

The terminal demo has a simple prompt router:

| Prompt contains | Tool selected |
| --- | --- |
| `lateral`, `east-west`, `rdp`, `smb`, `ssh` | `Gigamon_Lateral_Movement_Triage` |
| `dns`, `domain`, `lookup`, `nxdomain`, `servfail` | `Gigamon_DNS_Anomaly_Hunt` |
| `tls`, `ssl`, `cert`, `certificate`, `ja3` | `Gigamon_TLS_Risk_Summary` |
| `top`, `talker`, `app`, `bytes`, `packets` | `Gigamon_Top_Talkers_By_App` |
| anything else | `Gigamon_Visibility_Posture_Summary` |

This router is intentionally simple. In a production ISV app, this could be replaced with an LLM planner, a workflow engine, or explicit UI buttons.

## Troubleshooting quick hits

| Symptom | Likely cause | Fix |
| --- | --- | --- |
| `az` token errors | Azure CLI is not signed in or points to the wrong tenant/subscription | Run `az login` and `az account set --subscription <id>` |
| Ingestion succeeds but queries return 0 rows | Table/DCR propagation delay | Wait a few minutes and rerun the KQL |
| MCP publish fails with permission errors | Missing Sentinel custom MCP management permission | Use an account with access to publish tool collections |
| Terminal demo says workspace is missing | `.env` does not contain `MCP_DEFAULT_ARGUMENTS` | Set `{"workspaceId":"<workspace-customer-id>"}` |
| Tool returns no rows | Demo data aged out or was not ingested | Re-run LogSeeder with a fresh `TimeWindowMinutes` |

## Talk track

> Gigamon does not need to ship a whole chatbot to participate in agent workflows. The developer ships focused tools over the data they know best. Microsoft Sentinel handles the data plane, MCP gives the tool contract, and any agent surface can call the capability.

## Source notes

The repo includes detailed notes for developers who want to customize the implementation:

| File | Purpose |
| --- | --- |
| `docs/source-line-notes.md` | Line-by-line explanation for every Python and JSON file in the repo |
| `logseeder/GigamonCcfMcpDemo_CL.annotated.jsonc` | Commented companion to the LogSeeder JSON schema |

JSON does not support comments, so the runnable `.json` files stay valid and the comments live in `.jsonc` or Markdown.

## How to adapt this for production

For a real Gigamon-delivered asset, replace the demo pieces as follows:

| Demo piece | Production direction |
| --- | --- |
| `GigamonCcfMcpDemo_CL` | Use the real `GigamonV2_CL` table or customer-selected table |
| LogSeeder sample values | Use real product telemetry from the connector |
| Static prompt router | Use explicit product UI actions or an agent planner |
| Terminal demo | Embed the same tool calls into a Gigamon console, Copilot-like app, or partner integration |
| Single workspace ID | Let customer configuration choose the Sentinel workspace |

## Files

| Path | Purpose |
| --- | --- |
| `logseeder/GigamonCcfMcpDemo_CL.json` | LogSeeder schema derived from the official Gigamon connector schema |
| `logseeder/GigamonCcfMcpDemo_CL.annotated.jsonc` | Commented explanation of the schema without breaking valid JSON |
| `mcp-tools/*.kql` | KQL definitions for custom Sentinel MCP tools |
| `docs/publish-tools-via-ui.md` | Step-by-step UI walkthrough for saving the KQL files as Sentinel custom MCP tools |
| `terminal_demo.py` | Interactive terminal prompt loop that routes prompts to the Gigamon MCP tools |
| `sentinel_mcp_demo/` | Minimal Sentinel MCP client used by the terminal demo |
| `docs/demo-script.md` | Step-by-step presenter script |
| `docs/working-session-guide.md` | Methodical live-call walkthrough for Microsoft + Gigamon |
| `docs/tool-use-cases.md` | Detailed use-case, value-add, and story guide for every MCP tool |
| `docs/source-line-notes.md` | Exhaustive source-line notes for Python and JSON files |
