# Gigamon Sentinel MCP tool use cases and demo story

This document explains the story each custom MCP tool tells, the value it creates for Gigamon and Microsoft Sentinel customers, and how to present the tool in a live terminal demo.

## Executive narrative

Gigamon gives security teams deep network visibility. Microsoft Sentinel gives them a cloud-native investigation and correlation plane. Custom MCP tools turn Gigamon's Sentinel data into reusable agent capabilities.

If you are new to Microsoft security tooling, read the demo like this:

| Layer | What it does |
| --- | --- |
| Gigamon | Produces rich network metadata such as flows, apps, DNS, TLS, sources, and destinations |
| Microsoft Sentinel | Stores and investigates security data in a Log Analytics workspace |
| KQL | Asks precise questions over the Sentinel data |
| MCP | Wraps those questions as tools an agent or app can safely call |
| Terminal demo | Shows the tool calls without requiring Teams, browser setup, or a custom UI |

The demo is strongest when positioned as a developer pattern:

1. Gigamon ships or publishes focused tool definitions around the questions its telemetry is uniquely good at answering.
2. The customer's Sentinel workspace remains the system of record for the data.
3. Agents and applications call tools such as "summarize visibility posture" or "triage lateral movement" instead of asking a general-purpose model to invent KQL.
4. The result is faster triage, repeatable investigation logic, and a clear path for Gigamon developers to package high-value detection and visibility workflows.

## Demo flow

Run the tools in this order:

```bash
python3 terminal_demo.py --prompt "Summarize Gigamon visibility posture" --show-raw
python3 terminal_demo.py --prompt "Show possible lateral movement" --show-raw
python3 terminal_demo.py --prompt "Hunt DNS anomalies" --show-raw
python3 terminal_demo.py --prompt "Summarize TLS risk" --show-raw
python3 terminal_demo.py --prompt "Show top talkers by app" --show-raw
```

This order tells a complete SOC analyst story:

1. Start broad: confirm Gigamon visibility exists and has useful coverage.
2. Investigate attacker movement: look for east-west/admin protocol activity.
3. Investigate command-and-control indicators: look at DNS failures and unusual query patterns.
4. Investigate encrypted traffic risk: weak TLS, certificate, and JA3 signals.
5. Prioritize response: identify top applications and talkers creating the largest network footprint.

## Latest real demo output

These values came from the current seeded Sentinel table during the terminal run:

| Tool | Live signal observed |
| --- | --- |
| `Gigamon_Visibility_Posture_Summary` | 231 Gigamon events, 5 sources, 5 destinations, 481,166,985 bytes, TCP/UDP, apps including DNS, HTTPS, RDP, unknown TCP, TLS, SSH, and SMB |
| `Gigamon_Lateral_Movement_Triage` | 45 candidate flows on destination port 22 totaling 100,531,587 bytes; additional notable ports included 53, 445, 3389, 8443, and 443 |
| `Gigamon_DNS_Anomaly_Hunt` | 92 TXT queries, 59 failed responses, 45 slow responses, query names including `stage-sync.contoso-lab.example`, `rare-beacon.bad-example.test`, and `updates.microsoft.com` |
| `Gigamon_TLS_Risk_Summary` | 88 TLS 1.0 sessions, 25 weak-key observations, 29 expiring-soon observations, common names including `legacy-api.contoso-lab.example` and `unknown.bad-example.test` |
| `Gigamon_Top_Talkers_By_App` | Top row showed RDP over TCP with 6 flows and 27,099,651 bytes; other high-volume rows included HTTPS, TLS, SMB, unknown TCP, DNS, and SSH |

The exact counts can change as the LogSeeder time window ages, but the story and tool value remain the same.

## Tool 1: `Gigamon_Visibility_Posture_Summary`

### Prompt

```text
Summarize Gigamon visibility posture
```

### What the tool answers

This tool answers: "Do we have meaningful Gigamon visibility in this Sentinel workspace, and what does that visibility cover?"

It summarizes:

| Output field | Meaning |
| --- | --- |
| `Events` | Volume of Gigamon records in the current query window |
| `FirstSeen` / `LastSeen` | Time span covered by the sample |
| `UniqueSources` | Breadth of observed source IPs |
| `UniqueDestinations` | Breadth of observed destination IPs |
| `TotalBytes` | Approximate traffic volume represented by the records |
| `Protocols` | Network protocols seen in the data |
| `Apps` | Application names identified from Gigamon metadata |
| `AppFamilies` | Higher-level application categories |

### Customer value

This is the executive and SOC lead entry point. It proves the connector is not merely ingesting rows; it is producing useful network context that can frame an investigation.

Value adds:

1. Validates that Gigamon telemetry is present and fresh.
2. Shows coverage across protocols, applications, sources, and destinations.
3. Gives an analyst confidence before they pivot into more specific tools.
4. Creates a simple "health and visibility" tool that can be embedded in customer workflows.

### Demo talk track

> I start with posture because every investigation depends on coverage. This MCP tool gives me a quick answer: how much Gigamon data is in Sentinel, what protocols and apps are visible, and whether the time window is fresh enough for triage. This is the first tool a SOC analyst or responder would call before deeper pivots.

### Why Gigamon should ship this kind of tool

Gigamon can make the connector feel alive by packaging visibility summaries as a first-class capability. Customers often struggle to understand whether telemetry is complete enough to support an investigation. A posture tool makes visibility measurable, explainable, and agent-callable.

## Tool 2: `Gigamon_Lateral_Movement_Triage`

### Prompt

```text
Show possible lateral movement
```

### What the tool answers

This tool answers: "Which internal or administrative traffic patterns deserve lateral movement review?"

It focuses on destination ports and flow characteristics commonly associated with administrative access, file sharing, or suspicious movement:

| Output field | Meaning |
| --- | --- |
| `dst_port` | Destination port grouping, such as SSH `22`, SMB `445`, or RDP `3389` |
| `FlowCount` | Number of matching flows |
| `TotalBytes` | Total traffic volume for that port group |
| `MaxRttMs` | Maximum observed round-trip time, useful for latency or unusual path clues |
| `Sources` | Source IPs participating in candidate movement |
| `Destinations` | Destination IPs reached |
| `Apps` | Applications associated with those flows |
| `Interfaces` | Gigamon-observed interface or segment context |

### Customer value

This tool turns Gigamon east-west network visibility into a first-response triage aid.

Value adds:

1. Surfaces movement-like traffic without requiring the analyst to remember the KQL.
2. Identifies candidate source and destination systems for endpoint follow-up.
3. Shows whether activity crosses important network segments or interfaces.
4. Helps SOC teams prioritize high-volume or high-count administrative protocol activity.

### Demo talk track

> After posture, I pivot to lateral movement. I am not asking a model to guess what lateral movement means. Gigamon can encode the right KQL into an MCP tool: look at administrative protocols, show candidate flows, show source and destination systems, and preserve the network segment context. That is a much safer agent pattern than free-form query generation.

### Story from the latest run

The latest run found the largest candidate group on destination port `22` with 45 flows and 100,531,587 bytes. Other rows included ports `53`, `445`, `3389`, `8443`, and `443`.

The story to tell:

1. SSH volume is high enough to review first.
2. SMB and RDP are also present, so the analyst should inspect identity and endpoint context.
3. Sources and destinations are already listed, making it easy to pivot to Sentinel incidents, Defender device timelines, or firewall controls.

### Why Gigamon should ship this kind of tool

Gigamon has the network vantage point to expose east-west movement patterns that endpoint-only tools can miss. Packaging this as an MCP tool gives customers a repeatable investigation primitive: "show me movement candidates" becomes one callable capability.

## Tool 3: `Gigamon_DNS_Anomaly_Hunt`

### Prompt

```text
Hunt DNS anomalies
```

### What the tool answers

This tool answers: "Are there DNS behaviors that suggest beaconing, staging, failed domain generation, or suspicious infrastructure?"

It summarizes DNS activity by query type and failure/latency characteristics:

| Output field | Meaning |
| --- | --- |
| `dns_query_type` | Query type such as A, AAAA, or TXT |
| `Queries` | Total query count |
| `SlowQueries` | Queries with high response time |
| `FailedQueries` | Queries that returned failure-like response codes |
| `QueryNames` | Representative domains observed |
| `ReplyCodes` | DNS response codes such as NXDOMAIN, SERVFAIL, or NOERROR |
| `SourceIps` | Sources generating the DNS activity |

### Customer value

DNS is one of the best places to find early command-and-control and staging behavior. This tool lets an analyst ask for DNS anomalies without building DNS-specific KQL.

Value adds:

1. Highlights failed and slow DNS behaviors.
2. Groups by query type, which helps identify unusual TXT or AAAA patterns.
3. Gives representative query names for quick domain reputation review.
4. Lists source IPs so responders can pivot to affected workloads.

### Demo talk track

> Now I ask the DNS tool. This is a perfect example of an ISV MCP tool: Gigamon knows how to expose DNS metadata, and Sentinel stores it. The tool returns failed queries, slow queries, reply codes, domains, and source IPs in one response. That is exactly the kind of repeatable investigation step an agent should call.

### Story from the latest run

The latest run found 92 TXT queries, 59 failed responses, and 45 slow responses. Representative query names included:

```text
stage-sync.contoso-lab.example
rare-beacon.bad-example.test
updates.microsoft.com
```

The story to tell:

1. TXT queries are often worth reviewing because they can carry encoded data or configuration.
2. NXDOMAIN and SERVFAIL counts suggest failed resolution patterns that could align with staging or domain-generation behavior.
3. `rare-beacon.bad-example.test` is an obvious demo domain that makes the risk easy to explain.

### Why Gigamon should ship this kind of tool

DNS investigation is high-value but often noisy. Gigamon can use its metadata to pre-package the right aggregations and make DNS hunts easier for SOC analysts and agentic workflows.

## Tool 4: `Gigamon_TLS_Risk_Summary`

### Prompt

```text
Summarize TLS risk
```

### What the tool answers

This tool answers: "Which encrypted sessions show weak protocols, weak keys, certificate concerns, or fingerprint signals worth reviewing?"

It summarizes TLS characteristics:

| Output field | Meaning |
| --- | --- |
| `ProtocolVersion` | TLS protocol version observed |
| `Sessions` | Number of sessions for that protocol version |
| `WeakProtocol` | Count of sessions using legacy protocol versions |
| `WeakKey` | Count of observations with weak key size |
| `ExpiringSoon` | Count of certificate observations nearing expiration |
| `CommonNames` | Certificate common names |
| `Issuers` | Certificate issuers |
| `Ja3` | JA3 client fingerprints |

### Customer value

Encrypted traffic is often where attackers hide. This tool helps analysts quickly identify weak cryptography, risky certificates, and fingerprint patterns.

Value adds:

1. Highlights TLS 1.0 and TLS 1.1 risk.
2. Flags weak key observations.
3. Surfaces expiring certificate risk.
4. Gives common names, issuers, and JA3 values for threat-hunting pivots.

### Demo talk track

> The TLS tool shows that the same Gigamon data can support both security operations and exposure management. We can summarize weak protocol usage, weak keys, certificate issuers, common names, and JA3 fingerprints. This is useful for incident response, threat hunting, and hygiene programs.

### Story from the latest run

The latest run found:

| Signal | Value |
| --- | --- |
| TLS 1.0 sessions | 88 |
| Weak key observations in TLS 1.0 row | 25 |
| Expiring-soon observations in TLS 1.0 row | 29 |
| Common names | `legacy-api.contoso-lab.example`, `unknown.bad-example.test`, `portal.contoso.com` |
| Issuers | `Contoso Legacy CA`, `Untrusted Demo CA`, `Microsoft Azure TLS Issuing CA` |

The story to tell:

1. TLS 1.0 is a hygiene issue and a risk signal.
2. `legacy-api.contoso-lab.example` gives a clear owner-remediation path.
3. `unknown.bad-example.test` plus `Untrusted Demo CA` gives a hunt/remediation storyline.
4. JA3 values create a pivot into client fingerprint-based hunting.

### Why Gigamon should ship this kind of tool

Gigamon can turn encrypted-traffic metadata into agent-callable exposure management. Customers do not just get raw TLS fields; they get a packaged risk summary they can operationalize.

## Tool 5: `Gigamon_Top_Talkers_By_App`

### Prompt

```text
Show top talkers by app
```

### What the tool answers

This tool answers: "Which applications, sources, and destinations are producing the largest traffic footprint?"

It ranks traffic by application and protocol:

| Output field | Meaning |
| --- | --- |
| `app_name` | Gigamon-observed application name |
| `app_family` | Higher-level application category |
| `protocol` | Transport protocol |
| `Flows` | Number of flows |
| `Bytes` | Total byte volume |
| `Packets` | Total packet volume |
| `Sources` | Number of source IPs |
| `Destinations` | Number of destination IPs |
| `TopSources` | Representative top source IPs |
| `TopDestinations` | Representative top destination IPs |

### Customer value

Top talkers help analysts and network/security teams decide where to look first. During an incident, the largest application traffic may reveal exfiltration, misconfiguration, unauthorized admin traffic, or risky dependencies.

Value adds:

1. Prioritizes investigation by byte volume and flow count.
2. Connects application visibility to source/destination context.
3. Helps identify unsanctioned or unexpected application behavior.
4. Gives a clean entry point for executive or operational reporting.

### Demo talk track

> I close with top talkers because it turns the investigation into prioritization. We have posture, movement, DNS, and TLS risk. Now we ask what is driving the most traffic. The tool ranks application/protocol pairs by bytes and packets, then gives top sources and destinations for follow-up.

### Story from the latest run

The latest run showed RDP over TCP as the top row:

| Field | Value |
| --- | --- |
| App | `rdp` |
| Protocol | `TCP` |
| Flows | 6 |
| Bytes | 27,099,651 |
| Top sources | `192.0.2.45`, `10.42.10.15`, `172.16.5.11`, `10.42.20.50` |
| Top destinations | `10.42.20.50`, `10.42.30.21`, `203.0.113.20`, `198.51.100.77` |

The story to tell:

1. Remote-admin traffic is present and high enough to review.
2. Public documentation IP ranges appear in the sample, which keeps the demo safe while still realistic.
3. High-volume application rows can be linked back to lateral movement and TLS risk tools.

### Why Gigamon should ship this kind of tool

Traffic prioritization is a natural Gigamon strength. Packaging top talkers as a tool makes it useful to SOC agents, network operations, exposure management, and incident response.

## Combined customer value

Together, these tools show that Gigamon can ship an MCP-ready investigation pack:

| Outcome | How the tools support it |
| --- | --- |
| Faster triage | Analysts ask a prompt instead of writing KQL from scratch |
| Safer agent behavior | The model calls curated tools instead of inventing queries |
| Better use of network telemetry | Gigamon metadata becomes operationally useful inside Sentinel |
| Repeatable workflows | Every customer can run the same tool logic over their own workspace |
| Developer extensibility | New tools can be added by writing a KQL file and publishing it |

## Suggested productized tool pack

For a Gigamon developer audience, position this as the seed of a productized pack:

| Pack item | Description |
| --- | --- |
| `Visibility_Posture_Summary` | Health, freshness, and coverage summary |
| `Lateral_Movement_Triage` | East-west/admin protocol investigation |
| `DNS_Anomaly_Hunt` | Failed, slow, rare, or suspicious DNS pattern hunting |
| `TLS_Risk_Summary` | Weak protocol, weak key, certificate, JA3/JA3S analysis |
| `Top_Talkers_By_App` | Prioritized app/source/destination traffic ranking |
| `Exfiltration_Candidate_Triage` | Future tool to rank outbound bytes to unusual destinations |
| `Shadow_IT_App_Discovery` | Future tool to identify unexpected applications |
| `Segment_Visibility_Gaps` | Future tool to identify missing or low-volume segments |

## How to extend the demo

To add another tool:

1. Create a new `.kql` file in `mcp-tools/`.
2. In the Defender portal, paste the query into Advanced hunting and use **Save → Save as tool** to publish it into the `Gigamon-Sentinel-MCP-Demo` collection (see `docs/publish-tools-via-ui.md`).
3. Add prompt keywords to `terminal_demo.py`.
4. Add the tool to this document with the use case, value, talk track, and expected output.

This pattern is intentionally simple because the core idea is the tool contract, not the demo shell.
