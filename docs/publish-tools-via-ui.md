# Publish KQL files as Sentinel custom MCP tools — UI walkthrough

This repo intentionally has **no publisher script**. Instead, you save each KQL query in `mcp-tools/` as a custom Sentinel MCP tool by hand, using the **Save as tool** flow in the Microsoft Defender portal's Advanced Hunting experience.

This is the same outcome as a script-based publish, just via the UI. Use this when you want to demo the no-code path or when API publishing is not available in your tenant.

---

## Prerequisites

From the official docs:

- A workspace with **Microsoft Sentinel data lake** enabled and a **Microsoft Defender** license.
- One of these roles to create custom tools: **Security Operator**, **Security Admin**, or **Global Admin**.
- **Security Reader** or **Global Reader** to invoke them later.

Reference: [Create and use custom Microsoft Sentinel MCP tools (preview)](https://learn.microsoft.com/azure/sentinel/datalake/sentinel-mcp-create-custom-tool)

---

## Step-by-step

Repeat steps 1–6 once **per `.kql` file** in `mcp-tools/`.

### 1. Open the Defender portal Advanced Hunting page

Go to https://security.microsoft.com → **Investigation & response** → **Hunting** → **Advanced hunting**.

### 2. Paste the KQL query

Open the matching `mcp-tools/<ToolName>.kql` file in this repo, copy the full query, and paste it into the Advanced Hunting query window.

### 3. Run the query at least once to confirm it returns rows

This validates the query against the workspace before you save it as a tool. If it returns 0 rows, top up demo data with LogSeeder (see the main README) before continuing.

### 4. Click **Save as tool**

Two places to find this:

- **Context menu** (right-click) on the saved query
- **KQL query box menu** (the "..." or kebab menu in the editor)

See the screenshots in the [official docs](https://learn.microsoft.com/azure/sentinel/datalake/sentinel-mcp-create-custom-tool#create-custom-tools-with-kql-queries).

### 5. Fill in the **Save tool** flyout

| Field | What to enter |
| --- | --- |
| **Name** | Use the `.kql` filename (without extension), e.g. `Gigamon_Visibility_Posture_Summary` or `BigID_Sensitive_Data_Posture_Summary`. The name should be discoverable so the AI model picks the right tool. |
| **Description** | Copy the matching description from the table at the bottom of this file. |
| **Collection** | First time through, click **Create new collection** and use the suggested collection name from the per-tool table. After that, pick the same collection for the remaining tools. |
| **Default workspace** | Pick the workspace you ingested demo data into. This becomes the default `workspaceId` used by the agent if a prompt doesn't specify one. |
| **Parameters (optional)** | Leave empty for these demo tools — the queries don't reference any `{ParameterName}` placeholders. |

### 6. Click **Save**

The tool is now visible in your custom MCP collection and any agent connected to that collection can call it.

---

## Verify the tools are live

After saving all five tools:

1. In the Defender portal go to **Sentinel** → **MCP** → **Tool collections** (or follow the link in the Save tool confirmation toast).
2. Confirm the collection exists with your five tools listed.
3. The collection MCP server URL is:

   ```
   https://sentinel.microsoft.com/mcp/custom/<your collection name>
   ```

   Use that URL when wiring the collection into VS Code, Copilot Studio, Foundry, or the terminal demo in this repo.

---

## Use the tools you just created

Once the tools are saved in the UI, point the included terminal demo at the collection (no script needed):

```bash
cd <this repo>
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Edit .env so SENTINEL_MCP_COLLECTION matches the collection name you typed in step 5
python3 terminal_demo.py --show-raw
```

Or wire the collection into another surface using these official guides:

- [Visual Studio Code](https://learn.microsoft.com/azure/sentinel/datalake/sentinel-mcp-use-tool-visual-studio-code)
- [Microsoft Copilot Studio](https://learn.microsoft.com/azure/sentinel/datalake/sentinel-mcp-use-tool-copilot-studio)
- [Microsoft Foundry](https://learn.microsoft.com/azure/sentinel/datalake/sentinel-mcp-use-tool-azure-ai-foundry)
- [ChatGPT or Claude](https://learn.microsoft.com/azure/sentinel/datalake/sentinel-mcp-chatgpt-claude-connector)

---

## Useful links

- [Create and use custom Microsoft Sentinel MCP tools (preview)](https://learn.microsoft.com/azure/sentinel/datalake/sentinel-mcp-create-custom-tool)
- [Tool collection in Microsoft Sentinel MCP server (overview)](https://learn.microsoft.com/azure/sentinel/datalake/sentinel-mcp-tools-overview)
- [Get started with Microsoft Sentinel MCP server](https://learn.microsoft.com/azure/sentinel/datalake/sentinel-mcp-get-started)
- [Best practices for tool descriptions](https://learn.microsoft.com/azure/sentinel/datalake/sentinel-mcp-create-custom-tool)
- [Advanced hunting in Microsoft Defender](https://learn.microsoft.com/defender-xdr/advanced-hunting-microsoft-defender)

---

## Per-tool details for this repo

Suggested **collection name:** `Gigamon-Sentinel-MCP-Demo`

| `.kql` file | Tool name (use as-is) | Description |
| --- | --- | --- |
| `mcp-tools/Gigamon_Visibility_Posture_Summary.kql` | `Gigamon_Visibility_Posture_Summary` | Summarize Gigamon visibility posture across events, sources, destinations, protocols, apps, and bytes. |
| `mcp-tools/Gigamon_Lateral_Movement_Triage.kql` | `Gigamon_Lateral_Movement_Triage` | Triage possible east-west lateral movement using SMB, RDP, SSH, interfaces, bytes, RTT, and source/destination pairs. |
| `mcp-tools/Gigamon_DNS_Anomaly_Hunt.kql` | `Gigamon_DNS_Anomaly_Hunt` | Hunt DNS anomalies such as failed lookups, slow responses, suspicious query names, and affected source IPs. |
| `mcp-tools/Gigamon_TLS_Risk_Summary.kql` | `Gigamon_TLS_Risk_Summary` | Summarize TLS risk using protocol versions, weak key sizes, expiring certificates, issuers, CNs, and JA3 signals. |
| `mcp-tools/Gigamon_Top_Talkers_By_App.kql` | `Gigamon_Top_Talkers_By_App` | Rank Gigamon-observed applications by bytes, packets, sources, and destinations. |
