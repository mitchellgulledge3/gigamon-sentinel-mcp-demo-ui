# Source line notes

This file explains every Python and JSON source line in the demo repository. JSON files remain valid JSON in-place; line-by-line notes live here so the runnable assets are not corrupted by comments.

## `logseeder/GigamonCcfMcpDemo_CL.json`

| Line | Code | Note |
| ---: | --- | --- |
| 1 | <code>{</code> | JSON structural delimiter used to open or close an object or array. |
| 2 | <code>  &quot;columns&quot;: [</code> | Declares the LogSeeder column collection; each child object defines one table field. |
| 3 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 4 | <code>      &quot;name&quot;: &quot;TimeGenerated&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 5 | <code>      &quot;type&quot;: &quot;datetime&quot;</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 6 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 7 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 8 | <code>      &quot;name&quot;: &quot;RawData&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 9 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 10 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 11 | <code>        &quot;gigamon-ccf visibility flow: smb lateral movement candidate&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 12 | <code>        &quot;gigamon-ccf dns telemetry: suspicious lookup from workload segment&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 13 | <code>        &quot;gigamon-ccf tls telemetry: weak protocol and JA3 fingerprint observed&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 14 | <code>        &quot;gigamon-ccf application visibility: high-volume outbound transfer&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 15 | <code>        &quot;gigamon-ccf normal baseline: sanctioned business application traffic&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 16 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 17 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 18 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 19 | <code>      &quot;name&quot;: &quot;ts&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 20 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 21 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 22 | <code>        &quot;2026-05-07T18:00:00Z&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 23 | <code>        &quot;2026-05-07T18:02:00Z&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 24 | <code>        &quot;2026-05-07T18:04:00Z&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 25 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 26 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 27 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 28 | <code>      &quot;name&quot;: &quot;vendor&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 29 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 30 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 31 | <code>        &quot;Gigamon&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 32 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 33 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 34 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 35 | <code>      &quot;name&quot;: &quot;version&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 36 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 37 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 38 | <code>        &quot;6.8.00&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 39 | <code>        &quot;6.9.00&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 40 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 41 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 42 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 43 | <code>      &quot;name&quot;: &quot;generator&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 44 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 45 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 46 | <code>        &quot;GigaVUE-FM&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 47 | <code>        &quot;Gigamon Application Metadata Intelligence&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 48 | <code>        &quot;Gigamon ThreatINSIGHT&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 49 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 50 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 51 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 52 | <code>      &quot;name&quot;: &quot;dst_mac&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 53 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 54 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 55 | <code>        &quot;00:50:56:a1:10:20&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 56 | <code>        &quot;00:50:56:a1:10:21&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 57 | <code>        &quot;00:50:56:b2:44:10&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 58 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 59 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 60 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 61 | <code>      &quot;name&quot;: &quot;src_mac&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 62 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 63 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 64 | <code>        &quot;00:50:56:c0:00:08&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 65 | <code>        &quot;00:50:56:c0:00:09&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 66 | <code>        &quot;00:50:56:d4:22:18&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 67 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 68 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 69 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 70 | <code>      &quot;name&quot;: &quot;device_inbound_interface&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 71 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 72 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 73 | <code>        &quot;prod-east-west-vtap&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 74 | <code>        &quot;dmz-span-01&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 75 | <code>        &quot;core-fabric-ingress&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 76 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 77 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 78 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 79 | <code>      &quot;name&quot;: &quot;app_id&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 80 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 81 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 82 | <code>        &quot;445&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 83 | <code>        &quot;3389&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 84 | <code>        &quot;53&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 85 | <code>        &quot;443&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 86 | <code>        &quot;22&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 87 | <code>        &quot;8443&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 88 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 89 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 90 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 91 | <code>      &quot;name&quot;: &quot;src_ipv6&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 92 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 93 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 94 | <code>        &quot;&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 95 | <code>        &quot;2001:db8:10::15&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 96 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 97 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 98 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 99 | <code>      &quot;name&quot;: &quot;dst_ipv6&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 100 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 101 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 102 | <code>        &quot;&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 103 | <code>        &quot;2001:db8:20::8&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 104 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 105 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 106 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 107 | <code>      &quot;name&quot;: &quot;ip_version&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 108 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 109 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 110 | <code>        &quot;4&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 111 | <code>        &quot;6&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 112 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 113 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 114 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 115 | <code>      &quot;name&quot;: &quot;next_hdr_v6&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 116 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 117 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 118 | <code>        &quot;TCP&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 119 | <code>        &quot;UDP&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 120 | <code>        &quot;&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 121 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 122 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 123 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 124 | <code>      &quot;name&quot;: &quot;src_bytes&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 125 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 126 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 127 | <code>        &quot;42150&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 128 | <code>        &quot;984223&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 129 | <code>        &quot;1420&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 130 | <code>        &quot;8812000&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 131 | <code>        &quot;2210&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 132 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 133 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 134 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 135 | <code>      &quot;name&quot;: &quot;dst_bytes&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 136 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 137 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 138 | <code>        &quot;3201&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 139 | <code>        &quot;12002&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 140 | <code>        &quot;980&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 141 | <code>        &quot;204500&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 142 | <code>        &quot;6430&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 143 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 144 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 145 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 146 | <code>      &quot;name&quot;: &quot;src_packets&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 147 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 148 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 149 | <code>        &quot;43&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 150 | <code>        &quot;784&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 151 | <code>        &quot;4&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 152 | <code>        &quot;5210&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 153 | <code>        &quot;18&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 154 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 155 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 156 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 157 | <code>      &quot;name&quot;: &quot;dst_packets&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 158 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 159 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 160 | <code>        &quot;11&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 161 | <code>        &quot;92&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 162 | <code>        &quot;3&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 163 | <code>        &quot;302&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 164 | <code>        &quot;24&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 165 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 166 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 167 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 168 | <code>      &quot;name&quot;: &quot;start_time&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 169 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 170 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 171 | <code>        &quot;2026-05-07T18:01:01Z&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 172 | <code>        &quot;2026-05-07T18:02:18Z&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 173 | <code>        &quot;2026-05-07T18:03:44Z&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 174 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 175 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 176 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 177 | <code>      &quot;name&quot;: &quot;end_time&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 178 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 179 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 180 | <code>        &quot;2026-05-07T18:01:43Z&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 181 | <code>        &quot;2026-05-07T18:03:10Z&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 182 | <code>        &quot;2026-05-07T18:04:11Z&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 183 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 184 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 185 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 186 | <code>      &quot;name&quot;: &quot;intf_name&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 187 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 188 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 189 | <code>        &quot;prod-east-west&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 190 | <code>        &quot;internet-egress&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 191 | <code>        &quot;dmz-core&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 192 | <code>        &quot;identity-segment&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 193 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 194 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 195 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 196 | <code>      &quot;name&quot;: &quot;egress_intf_id&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 197 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 198 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 199 | <code>        &quot;101&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 200 | <code>        &quot;203&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 201 | <code>        &quot;301&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 202 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 203 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 204 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 205 | <code>      &quot;name&quot;: &quot;app_name&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 206 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 207 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 208 | <code>        &quot;smb&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 209 | <code>        &quot;rdp&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 210 | <code>        &quot;dns&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 211 | <code>        &quot;tls&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 212 | <code>        &quot;ssh&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 213 | <code>        &quot;https&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 214 | <code>        &quot;unknown-tcp&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 215 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 216 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 217 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 218 | <code>      &quot;name&quot;: &quot;id&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 219 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 220 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 221 | <code>        &quot;gigamon-demo-flow-001&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 222 | <code>        &quot;gigamon-demo-flow-002&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 223 | <code>        &quot;gigamon-demo-flow-003&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 224 | <code>        &quot;gigamon-demo-flow-004&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 225 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 226 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 227 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 228 | <code>      &quot;name&quot;: &quot;seq_num&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 229 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 230 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 231 | <code>        &quot;1001&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 232 | <code>        &quot;1002&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 233 | <code>        &quot;1003&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 234 | <code>        &quot;1004&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 235 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 236 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 237 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 238 | <code>      &quot;name&quot;: &quot;src_ip&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 239 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 240 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 241 | <code>        &quot;10.42.10.15&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 242 | <code>        &quot;10.42.10.23&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 243 | <code>        &quot;10.42.20.50&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 244 | <code>        &quot;172.16.5.11&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 245 | <code>        &quot;192.0.2.45&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 246 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 247 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 248 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 249 | <code>      &quot;name&quot;: &quot;dst_ip&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 250 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 251 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 252 | <code>        &quot;10.42.20.50&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 253 | <code>        &quot;10.42.30.21&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 254 | <code>        &quot;10.42.40.8&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 255 | <code>        &quot;198.51.100.77&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 256 | <code>        &quot;203.0.113.20&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 257 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 258 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 259 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 260 | <code>      &quot;name&quot;: &quot;protocol&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 261 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 262 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 263 | <code>        &quot;TCP&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 264 | <code>        &quot;UDP&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 265 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 266 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 267 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 268 | <code>      &quot;name&quot;: &quot;src_port&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 269 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 270 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 271 | <code>        &quot;51512&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 272 | <code>        &quot;51513&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 273 | <code>        &quot;49200&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 274 | <code>        &quot;61022&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 275 | <code>        &quot;44321&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 276 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 277 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 278 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 279 | <code>      &quot;name&quot;: &quot;dst_port&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 280 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 281 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 282 | <code>        &quot;445&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 283 | <code>        &quot;3389&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 284 | <code>        &quot;53&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 285 | <code>        &quot;443&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 286 | <code>        &quot;22&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 287 | <code>        &quot;8443&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 288 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 289 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 290 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 291 | <code>      &quot;name&quot;: &quot;dns_name&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 292 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 293 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 294 | <code>        &quot;stage-sync.contoso-lab.example&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 295 | <code>        &quot;cdn.gigamon.example&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 296 | <code>        &quot;updates.microsoft.com&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 297 | <code>        &quot;rare-beacon.bad-example.test&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 298 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 299 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 300 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 301 | <code>      &quot;name&quot;: &quot;dns_host&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 302 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 303 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 304 | <code>        &quot;stage-sync.contoso-lab.example&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 305 | <code>        &quot;rare-beacon.bad-example.test&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 306 | <code>        &quot;updates.microsoft.com&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 307 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 308 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 309 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 310 | <code>      &quot;name&quot;: &quot;dns_host_addr&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 311 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 312 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 313 | <code>        &quot;198.51.100.77&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 314 | <code>        &quot;203.0.113.20&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 315 | <code>        &quot;20.42.65.90&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 316 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 317 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 318 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 319 | <code>      &quot;name&quot;: &quot;dns_host_type&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 320 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 321 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 322 | <code>        &quot;A&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 323 | <code>        &quot;AAAA&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 324 | <code>        &quot;CNAME&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 325 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 326 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 327 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 328 | <code>      &quot;name&quot;: &quot;dns_reply_code&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 329 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 330 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 331 | <code>        &quot;NOERROR&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 332 | <code>        &quot;NXDOMAIN&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 333 | <code>        &quot;SERVFAIL&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 334 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 335 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 336 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 337 | <code>      &quot;name&quot;: &quot;dns_ttl&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 338 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 339 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 340 | <code>        &quot;60&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 341 | <code>        &quot;300&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 342 | <code>        &quot;3600&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 343 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 344 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 345 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 346 | <code>      &quot;name&quot;: &quot;dns_flags&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 347 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 348 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 349 | <code>        &quot;qr rd ra&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 350 | <code>        &quot;rd&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 351 | <code>        &quot;qr aa rd ra&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 352 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 353 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 354 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 355 | <code>      &quot;name&quot;: &quot;dns_opcode&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 356 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 357 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 358 | <code>        &quot;QUERY&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 359 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 360 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 361 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 362 | <code>      &quot;name&quot;: &quot;dns_class&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 363 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 364 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 365 | <code>        &quot;IN&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 366 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 367 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 368 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 369 | <code>      &quot;name&quot;: &quot;dns_host_class&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 370 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 371 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 372 | <code>        &quot;IN&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 373 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 374 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 375 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 376 | <code>      &quot;name&quot;: &quot;dns_host_raw&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 377 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 378 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 379 | <code>        &quot;726172652d626561636f6e&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 380 | <code>        &quot;75706461746573&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 381 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 382 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 383 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 384 | <code>      &quot;name&quot;: &quot;dns_query&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 385 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 386 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 387 | <code>        &quot;stage-sync.contoso-lab.example&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 388 | <code>        &quot;rare-beacon.bad-example.test&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 389 | <code>        &quot;updates.microsoft.com&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 390 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 391 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 392 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 393 | <code>      &quot;name&quot;: &quot;dns_query_type&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 394 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 395 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 396 | <code>        &quot;A&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 397 | <code>        &quot;AAAA&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 398 | <code>        &quot;TXT&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 399 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 400 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 401 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 402 | <code>      &quot;name&quot;: &quot;app_tags&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 403 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 404 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 405 | <code>        &quot;lateral-movement&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 406 | <code>        &quot;dns-anomaly&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 407 | <code>        &quot;tls-risk&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 408 | <code>        &quot;data-transfer&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 409 | <code>        &quot;baseline&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 410 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 411 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 412 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 413 | <code>      &quot;name&quot;: &quot;ssl_handshake_type&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 414 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 415 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 416 | <code>        &quot;client_hello&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 417 | <code>        &quot;server_hello&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 418 | <code>        &quot;certificate&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 419 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 420 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 421 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 422 | <code>      &quot;name&quot;: &quot;ssl_cipher_suite_id&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 423 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 424 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 425 | <code>        &quot;TLS_RSA_WITH_3DES_EDE_CBC_SHA&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 426 | <code>        &quot;TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 427 | <code>        &quot;TLS_AES_256_GCM_SHA384&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 428 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 429 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 430 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 431 | <code>      &quot;name&quot;: &quot;ssl_protocol_version&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 432 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 433 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 434 | <code>        &quot;TLS 1.0&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 435 | <code>        &quot;TLS 1.2&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 436 | <code>        &quot;TLS 1.3&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 437 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 438 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 439 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 440 | <code>      &quot;name&quot;: &quot;ssl_ext_sig_algorithms_len&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 441 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 442 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 443 | <code>        &quot;12&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 444 | <code>        &quot;18&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 445 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 446 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 447 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 448 | <code>      &quot;name&quot;: &quot;ssl_ext_sig_algorithm_scheme&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 449 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 450 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 451 | <code>        &quot;rsa_pkcs1_sha1&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 452 | <code>        &quot;ecdsa_secp256r1_sha256&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 453 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 454 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 455 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 456 | <code>      &quot;name&quot;: &quot;ssl_ext_sig_algorithm_hash&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 457 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 458 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 459 | <code>        &quot;sha1&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 460 | <code>        &quot;sha256&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 461 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 462 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 463 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 464 | <code>      &quot;name&quot;: &quot;ssl_ext_sig_algorithm_sig&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 465 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 466 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 467 | <code>        &quot;rsa&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 468 | <code>        &quot;ecdsa&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 469 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 470 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 471 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 472 | <code>      &quot;name&quot;: &quot;ssl_fingerprint_ja3&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 473 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 474 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 475 | <code>        &quot;769,47-53-10,0-11-10,23-24,0&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 476 | <code>        &quot;771,4865-4866-4867,0-11-10,23-24,0&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 477 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 478 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 479 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 480 | <code>      &quot;name&quot;: &quot;ssl_fingerprint_ja3s&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 481 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 482 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 483 | <code>        &quot;771,4865,0-11&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 484 | <code>        &quot;769,47,0&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 485 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 486 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 487 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 488 | <code>      &quot;name&quot;: &quot;ssl_key_share_group&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 489 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 490 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 491 | <code>        &quot;secp256r1&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 492 | <code>        &quot;x25519&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 493 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 494 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 495 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 496 | <code>      &quot;name&quot;: &quot;ssl_fingerprint_ja3_full&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 497 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 498 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 499 | <code>        &quot;weak-ja3-demo-fingerprint&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 500 | <code>        &quot;modern-ja3-demo-fingerprint&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 501 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 502 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 503 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 504 | <code>      &quot;name&quot;: &quot;ssl_fingerprint_ja3s_full&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 505 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 506 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 507 | <code>        &quot;weak-ja3s-demo-fingerprint&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 508 | <code>        &quot;modern-ja3s-demo-fingerprint&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 509 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 510 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 511 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 512 | <code>      &quot;name&quot;: &quot;ssl_common_name&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 513 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 514 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 515 | <code>        &quot;legacy-api.contoso-lab.example&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 516 | <code>        &quot;portal.contoso.com&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 517 | <code>        &quot;unknown.bad-example.test&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 518 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 519 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 520 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 521 | <code>      &quot;name&quot;: &quot;ssl_issuer&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 522 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 523 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 524 | <code>        &quot;Contoso Legacy CA&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 525 | <code>        &quot;Microsoft Azure TLS Issuing CA&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 526 | <code>        &quot;Untrusted Demo CA&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 527 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 528 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 529 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 530 | <code>      &quot;name&quot;: &quot;ssl_validity_not_before&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 531 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 532 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 533 | <code>        &quot;2024-01-01T00:00:00Z&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 534 | <code>        &quot;2025-01-01T00:00:00Z&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 535 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 536 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 537 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 538 | <code>      &quot;name&quot;: &quot;ssl_validity_not_after&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 539 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 540 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 541 | <code>        &quot;2026-04-30T00:00:00Z&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 542 | <code>        &quot;2026-12-31T00:00:00Z&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 543 | <code>        &quot;2027-05-01T00:00:00Z&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 544 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 545 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 546 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 547 | <code>      &quot;name&quot;: &quot;ssl_certificate_raw&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 548 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 549 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 550 | <code>        &quot;demo-certificate-redacted&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 551 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 552 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 553 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 554 | <code>      &quot;name&quot;: &quot;ssl_organization_name&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 555 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 556 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 557 | <code>        &quot;Contoso&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 558 | <code>        &quot;Gigamon Demo Lab&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 559 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 560 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 561 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 562 | <code>      &quot;name&quot;: &quot;ssl_content_type&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 563 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 564 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 565 | <code>        &quot;handshake&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 566 | <code>        &quot;application_data&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 567 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 568 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 569 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 570 | <code>      &quot;name&quot;: &quot;ssl_common_name_raw&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 571 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 572 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 573 | <code>        &quot;legacy-api.contoso-lab.example&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 574 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 575 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 576 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 577 | <code>      &quot;name&quot;: &quot;ssl_certificate_subject_cn&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 578 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 579 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 580 | <code>        &quot;legacy-api.contoso-lab.example&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 581 | <code>        &quot;portal.contoso.com&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 582 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 583 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 584 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 585 | <code>      &quot;name&quot;: &quot;ssl_certificate_subject_o&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 586 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 587 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 588 | <code>        &quot;Contoso&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 589 | <code>        &quot;Gigamon Demo Lab&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 590 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 591 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 592 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 593 | <code>      &quot;name&quot;: &quot;ssl_certificate_subject_c&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 594 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 595 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 596 | <code>        &quot;US&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 597 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 598 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 599 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 600 | <code>      &quot;name&quot;: &quot;ssl_certificate_dn_issuer&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 601 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 602 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 603 | <code>        &quot;CN=Contoso Legacy CA,O=Contoso,C=US&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 604 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 605 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 606 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 607 | <code>      &quot;name&quot;: &quot;ssl_certificate_issuer_c&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 608 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 609 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 610 | <code>        &quot;US&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 611 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 612 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 613 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 614 | <code>      &quot;name&quot;: &quot;ssl_certificate_subject_key_algo_raw&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 615 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 616 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 617 | <code>        &quot;rsaEncryption&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 618 | <code>        &quot;id-ecPublicKey&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 619 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 620 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 621 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 622 | <code>      &quot;name&quot;: &quot;ssl_certificate_subject_key_algo_oid_raw&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 623 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 624 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 625 | <code>        &quot;1.2.840.113549.1.1.1&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 626 | <code>        &quot;1.2.840.10045.2.1&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 627 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 628 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 629 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 630 | <code>      &quot;name&quot;: &quot;ssl_certificate_subject_key_algo_oid&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 631 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 632 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 633 | <code>        &quot;rsaEncryption&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 634 | <code>        &quot;ecPublicKey&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 635 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 636 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 637 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 638 | <code>      &quot;name&quot;: &quot;ssl_certificate_subject_key_size&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 639 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 640 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 641 | <code>        &quot;1024&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 642 | <code>        &quot;2048&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 643 | <code>        &quot;4096&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 644 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 645 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 646 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 647 | <code>      &quot;name&quot;: &quot;ssl_certificate_subject_key_value_raw&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 648 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 649 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 650 | <code>        &quot;redacted-key-material&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 651 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 652 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 653 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 654 | <code>      &quot;name&quot;: &quot;ssl_certificate_algo_raw&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 655 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 656 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 657 | <code>        &quot;sha1WithRSAEncryption&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 658 | <code>        &quot;sha256WithRSAEncryption&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 659 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 660 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 661 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 662 | <code>      &quot;name&quot;: &quot;ssl_certificate_algo_oid_raw&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 663 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 664 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 665 | <code>        &quot;1.2.840.113549.1.1.5&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 666 | <code>        &quot;1.2.840.113549.1.1.11&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 667 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 668 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 669 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 670 | <code>      &quot;name&quot;: &quot;ssl_certificate_algo_oid&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 671 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 672 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 673 | <code>        &quot;sha1WithRSAEncryption&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 674 | <code>        &quot;sha256WithRSAEncryption&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 675 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 676 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 677 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 678 | <code>      &quot;name&quot;: &quot;ssl_session_id&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 679 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 680 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 681 | <code>        &quot;demo-session-001&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 682 | <code>        &quot;demo-session-002&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 683 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 684 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 685 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 686 | <code>      &quot;name&quot;: &quot;src_inner_bytes&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 687 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 688 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 689 | <code>        &quot;0&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 690 | <code>        &quot;42000&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 691 | <code>        &quot;980000&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 692 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 693 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 694 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 695 | <code>      &quot;name&quot;: &quot;mpls&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 696 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 697 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 698 | <code>        &quot;&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 699 | <code>        &quot;label-101&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 700 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 701 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 702 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 703 | <code>      &quot;name&quot;: &quot;tcp_sport&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 704 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 705 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 706 | <code>        &quot;51512&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 707 | <code>        &quot;51513&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 708 | <code>        &quot;49200&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 709 | <code>        &quot;61022&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 710 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 711 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 712 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 713 | <code>      &quot;name&quot;: &quot;tcp_dport&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 714 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 715 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 716 | <code>        &quot;445&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 717 | <code>        &quot;3389&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 718 | <code>        &quot;443&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 719 | <code>        &quot;22&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 720 | <code>        &quot;8443&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 721 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 722 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 723 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 724 | <code>      &quot;name&quot;: &quot;udp_sport&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 725 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 726 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 727 | <code>        &quot;53001&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 728 | <code>        &quot;53002&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 729 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 730 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 731 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 732 | <code>      &quot;name&quot;: &quot;udp_dport&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 733 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 734 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 735 | <code>        &quot;53&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 736 | <code>        &quot;123&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 737 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 738 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 739 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 740 | <code>      &quot;name&quot;: &quot;app_family&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 741 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 742 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 743 | <code>        &quot;file-sharing&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 744 | <code>        &quot;remote-admin&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 745 | <code>        &quot;dns&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 746 | <code>        &quot;web&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 747 | <code>        &quot;secure-shell&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 748 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 749 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 750 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 751 | <code>      &quot;name&quot;: &quot;dst_inner_bytes&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 752 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 753 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 754 | <code>        &quot;0&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 755 | <code>        &quot;3201&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 756 | <code>        &quot;204500&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 757 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 758 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 759 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 760 | <code>      &quot;name&quot;: &quot;total_bytes&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 761 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 762 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 763 | <code>        &quot;45351&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 764 | <code>        &quot;996225&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 765 | <code>        &quot;2400&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 766 | <code>        &quot;9016500&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 767 | <code>        &quot;8640&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 768 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 769 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 770 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 771 | <code>      &quot;name&quot;: &quot;total_packets&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 772 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 773 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 774 | <code>        &quot;54&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 775 | <code>        &quot;876&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 776 | <code>        &quot;7&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 777 | <code>        &quot;5512&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 778 | <code>        &quot;42&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 779 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 780 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 781 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 782 | <code>      &quot;name&quot;: &quot;ingress_vlan_id&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 783 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 784 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 785 | <code>        &quot;120&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 786 | <code>        &quot;220&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 787 | <code>        &quot;310&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 788 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 789 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 790 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 791 | <code>      &quot;name&quot;: &quot;ip_ttl&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 792 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 793 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 794 | <code>        &quot;62&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 795 | <code>        &quot;64&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 796 | <code>        &quot;128&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 797 | <code>        &quot;255&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 798 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 799 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 800 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 801 | <code>      &quot;name&quot;: &quot;tcp_flags&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 802 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 803 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 804 | <code>        &quot;SYN&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 805 | <code>        &quot;SYN-ACK&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 806 | <code>        &quot;ACK&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 807 | <code>        &quot;RST&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 808 | <code>        &quot;FIN&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 809 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 810 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 811 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 812 | <code>      &quot;name&quot;: &quot;ip_hdr_len&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 813 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 814 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 815 | <code>        &quot;20&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 816 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 817 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 818 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 819 | <code>      &quot;name&quot;: &quot;ip_frag_flags&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 820 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 821 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 822 | <code>        &quot;DF&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 823 | <code>        &quot;MF&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 824 | <code>        &quot;&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 825 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 826 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 827 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 828 | <code>      &quot;name&quot;: &quot;tcp_ack_id&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 829 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 830 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 831 | <code>        &quot;100102&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 832 | <code>        &quot;100203&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 833 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 834 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 835 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 836 | <code>      &quot;name&quot;: &quot;tcp_hdr_len&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 837 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 838 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 839 | <code>        &quot;20&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 840 | <code>        &quot;32&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 841 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 842 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 843 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 844 | <code>      &quot;name&quot;: &quot;tcp_seq_no&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 845 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 846 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 847 | <code>        &quot;64001&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 848 | <code>        &quot;64002&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 849 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 850 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 851 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 852 | <code>      &quot;name&quot;: &quot;tcp_win_size&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 853 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 854 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 855 | <code>        &quot;64240&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 856 | <code>        &quot;8192&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 857 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 858 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 859 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 860 | <code>      &quot;name&quot;: &quot;udp_msg_len&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 861 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 862 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 863 | <code>        &quot;72&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 864 | <code>        &quot;120&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 865 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 866 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 867 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 868 | <code>      &quot;name&quot;: &quot;flow_start_usec&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 869 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 870 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 871 | <code>        &quot;101000&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 872 | <code>        &quot;220000&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 873 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 874 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 875 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 876 | <code>      &quot;name&quot;: &quot;flow_end_usec&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 877 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 878 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 879 | <code>        &quot;901000&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 880 | <code>        &quot;880000&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 881 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 882 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 883 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 884 | <code>      &quot;name&quot;: &quot;flow_start_sec&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 885 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 886 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 887 | <code>        &quot;1778176800&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 888 | <code>        &quot;1778176920&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 889 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 890 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 891 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 892 | <code>      &quot;name&quot;: &quot;flow_end_sec&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 893 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 894 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 895 | <code>        &quot;1778176860&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 896 | <code>        &quot;1778177040&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 897 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 898 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 899 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 900 | <code>      &quot;name&quot;: &quot;outer_src_ip&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 901 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 902 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 903 | <code>        &quot;10.42.10.15&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 904 | <code>        &quot;172.16.5.11&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 905 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 906 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 907 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 908 | <code>      &quot;name&quot;: &quot;outer_dst_ip&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 909 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 910 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 911 | <code>        &quot;10.42.20.50&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 912 | <code>        &quot;198.51.100.77&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 913 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 914 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 915 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 916 | <code>      &quot;name&quot;: &quot;tcpflagsyn&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 917 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 918 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 919 | <code>        &quot;true&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 920 | <code>        &quot;false&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 921 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 922 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 923 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 924 | <code>      &quot;name&quot;: &quot;tcpflagsynack&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 925 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 926 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 927 | <code>        &quot;true&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 928 | <code>        &quot;false&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 929 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 930 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 931 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 932 | <code>      &quot;name&quot;: &quot;tcpflagfin&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 933 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 934 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 935 | <code>        &quot;true&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 936 | <code>        &quot;false&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 937 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 938 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 939 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 940 | <code>      &quot;name&quot;: &quot;tcpflagrst&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 941 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 942 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 943 | <code>        &quot;true&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 944 | <code>        &quot;false&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 945 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 946 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 947 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 948 | <code>      &quot;name&quot;: &quot;tcp_rtt&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 949 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 950 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 951 | <code>        &quot;12&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 952 | <code>        &quot;35&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 953 | <code>        &quot;210&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 954 | <code>        &quot;480&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 955 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 956 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 957 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 958 | <code>      &quot;name&quot;: &quot;tcp_loss_count&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 959 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 960 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 961 | <code>        &quot;0&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 962 | <code>        &quot;1&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 963 | <code>        &quot;7&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 964 | <code>        &quot;18&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 965 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 966 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 967 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 968 | <code>      &quot;name&quot;: &quot;ip_wrong_crc&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 969 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 970 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 971 | <code>        &quot;0&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 972 | <code>        &quot;1&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 973 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 974 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 975 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 976 | <code>      &quot;name&quot;: &quot;dnp3_al_function_code&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 977 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 978 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 979 | <code>        &quot;&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 980 | <code>        &quot;READ&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 981 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 982 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 983 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 984 | <code>      &quot;name&quot;: &quot;dnp3_dl_function_code&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 985 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 986 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 987 | <code>        &quot;&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 988 | <code>        &quot;CONFIRMED_USER_DATA&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 989 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 990 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 991 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 992 | <code>      &quot;name&quot;: &quot;dnp3_dl_dir&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 993 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 994 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 995 | <code>        &quot;&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 996 | <code>        &quot;MASTER&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 997 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 998 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 999 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 1000 | <code>      &quot;name&quot;: &quot;modbus_exception_code&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 1001 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 1002 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 1003 | <code>        &quot;&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 1004 | <code>        &quot;2&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 1005 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 1006 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 1007 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 1008 | <code>      &quot;name&quot;: &quot;SSL_version&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 1009 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 1010 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 1011 | <code>        &quot;TLS 1.0&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 1012 | <code>        &quot;TLS 1.2&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 1013 | <code>        &quot;TLS 1.3&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 1014 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 1015 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 1016 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 1017 | <code>      &quot;name&quot;: &quot;http_code&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 1018 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 1019 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 1020 | <code>        &quot;200&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 1021 | <code>        &quot;403&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 1022 | <code>        &quot;404&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 1023 | <code>        &quot;500&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 1024 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 1025 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 1026 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 1027 | <code>      &quot;name&quot;: &quot;http_rtt&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 1028 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 1029 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 1030 | <code>        &quot;22&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 1031 | <code>        &quot;110&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 1032 | <code>        &quot;650&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 1033 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 1034 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 1035 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 1036 | <code>      &quot;name&quot;: &quot;tcp_rtt_app&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 1037 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 1038 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 1039 | <code>        &quot;18&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 1040 | <code>        &quot;95&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 1041 | <code>        &quot;520&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 1042 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 1043 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 1044 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 1045 | <code>      &quot;name&quot;: &quot;tcp_flag_reset&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 1046 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 1047 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 1048 | <code>        &quot;true&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 1049 | <code>        &quot;false&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 1050 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 1051 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 1052 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 1053 | <code>      &quot;name&quot;: &quot;dns_response_time&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 1054 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 1055 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 1056 | <code>        &quot;5&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 1057 | <code>        &quot;25&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 1058 | <code>        &quot;450&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 1059 | <code>        &quot;1200&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 1060 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 1061 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 1062 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 1063 | <code>      &quot;name&quot;: &quot;http_content_encoding&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 1064 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 1065 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 1066 | <code>        &quot;gzip&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 1067 | <code>        &quot;br&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 1068 | <code>        &quot;identity&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 1069 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 1070 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 1071 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 1072 | <code>      &quot;name&quot;: &quot;snmp_version&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 1073 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 1074 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 1075 | <code>        &quot;v2c&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 1076 | <code>        &quot;v3&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 1077 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 1078 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 1079 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 1080 | <code>      &quot;name&quot;: &quot;smb_version&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 1081 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 1082 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 1083 | <code>        &quot;SMB2&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 1084 | <code>        &quot;SMB3&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 1085 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 1086 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 1087 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 1088 | <code>      &quot;name&quot;: &quot;http_version&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 1089 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 1090 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 1091 | <code>        &quot;HTTP/1.1&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 1092 | <code>        &quot;HTTP/2&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 1093 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 1094 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 1095 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 1096 | <code>      &quot;name&quot;: &quot;hl7_version&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 1097 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 1098 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 1099 | <code>        &quot;&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 1100 | <code>        &quot;2.5&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 1101 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 1102 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 1103 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 1104 | <code>      &quot;name&quot;: &quot;hl7_msg_seg_name&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 1105 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 1106 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 1107 | <code>        &quot;&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 1108 | <code>        &quot;MSH&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 1109 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 1110 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 1111 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 1112 | <code>      &quot;name&quot;: &quot;dicom_pdu_data_pdv_elem_val_cs&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 1113 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 1114 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 1115 | <code>        &quot;&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 1116 | <code>        &quot;STUDY&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 1117 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 1118 | <code>    },</code> | JSON structural delimiter used to open or close an object or array. |
| 1119 | <code>    {</code> | JSON structural delimiter used to open or close an object or array. |
| 1120 | <code>      &quot;name&quot;: &quot;dicom_pdu_data_pdv_elem_val_pn&quot;,</code> | Names a Sentinel/Log Analytics column or top-level setting consumed by LogSeeder. |
| 1121 | <code>      &quot;type&quot;: &quot;string&quot;,</code> | Declares the Log Analytics data type used when LogSeeder creates the custom table. |
| 1122 | <code>      &quot;values&quot;: [</code> | Starts a realistic sample-value pool that LogSeeder randomly selects from during ingestion. |
| 1123 | <code>        &quot;&quot;,</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 1124 | <code>        &quot;DEMO^PATIENT&quot;</code> | Sample value used to generate realistic Gigamon CCF telemetry for the demo table. |
| 1125 | <code>      ]</code> | JSON structural delimiter used to open or close an object or array. |
| 1126 | <code>    }</code> | JSON structural delimiter used to open or close an object or array. |
| 1127 | <code>  ]</code> | JSON structural delimiter used to open or close an object or array. |
| 1128 | <code>}</code> | JSON structural delimiter used to open or close an object or array. |

## `scripts/publish-mcp-tools.py`

| Line | Code | Note |
| ---: | --- | --- |
| 1 | <code>from __future__ import annotations</code> | Enables postponed annotation evaluation so type hints stay lightweight and forward-compatible. |
| 2 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 3 | <code>&quot;&quot;&quot;Publish the demo KQL files as Microsoft Sentinel custom MCP tools.</code> | Docstring text that explains the purpose of this module, class, or function. |
| 4 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 5 | <code>This script is deliberately small and dependency-light so a Gigamon developer can</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 6 | <code>copy it into another reference repo, inspect every HTTP payload, and understand</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 7 | <code>exactly how KQL turns into an MCP tool. The script expects Azure CLI to already</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 8 | <code>be signed in to a tenant/subscription that can manage Sentinel custom MCP tools.</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 9 | <code>&quot;&quot;&quot;</code> | Docstring text that explains the purpose of this module, class, or function. |
| 10 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 11 | <code>import argparse</code> | Imports a standard library or dependency needed by this module. |
| 12 | <code>import json</code> | Imports a standard library or dependency needed by this module. |
| 13 | <code>import pathlib</code> | Imports a standard library or dependency needed by this module. |
| 14 | <code>import subprocess</code> | Imports a standard library or dependency needed by this module. |
| 15 | <code>import sys</code> | Imports a standard library or dependency needed by this module. |
| 16 | <code>import urllib.error</code> | Imports a standard library or dependency needed by this module. |
| 17 | <code>import urllib.request</code> | Imports a standard library or dependency needed by this module. |
| 18 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 19 | <code>SENTINEL_RESOURCE_ID = &quot;4500ebfb-89b6-4b14-a480-7f749797bfcd&quot;</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 20 | <code>API_BASE = &quot;https://api.securityplatform.microsoft.com/aiprimitives/mcpToolCollections&quot;</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 21 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 22 | <code># Friendly tool descriptions are stored next to the publisher so the KQL files</code> | Developer note explaining why the adjacent code exists or how it fits the demo. |
| 23 | <code># can stay focused on query logic while the MCP metadata stays easy to review.</code> | Developer note explaining why the adjacent code exists or how it fits the demo. |
| 24 | <code>DESCRIPTIONS = {</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 25 | <code>    &quot;Gigamon_Visibility_Posture_Summary&quot;: &quot;Summarize Gigamon visibility posture across events, sources, destinations, protocols, apps, and bytes.&quot;,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 26 | <code>    &quot;Gigamon_Lateral_Movement_Triage&quot;: &quot;Triage possible east-west lateral movement using SMB, RDP, SSH, interfaces, bytes, RTT, and source/destination pairs.&quot;,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 27 | <code>    &quot;Gigamon_DNS_Anomaly_Hunt&quot;: &quot;Hunt DNS anomalies such as failed lookups, slow responses, suspicious query names, and affected source IPs.&quot;,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 28 | <code>    &quot;Gigamon_TLS_Risk_Summary&quot;: &quot;Summarize TLS risk using protocol versions, weak key sizes, expiring certificates, issuers, CNs, and JA3 signals.&quot;,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 29 | <code>    &quot;Gigamon_Top_Talkers_By_App&quot;: &quot;Rank Gigamon-observed applications by bytes, packets, sources, and destinations.&quot;,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 30 | <code>}</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 31 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 32 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 33 | <code>def az_token() -&gt; str:</code> | Defines a function; async functions are awaited by the terminal demo or MCP client. |
| 34 | <code>    &quot;&quot;&quot;Return a Sentinel Platform Services bearer token from Azure CLI.&quot;&quot;&quot;</code> | Docstring text that explains the purpose of this module, class, or function. |
| 35 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 36 | <code>    # Azure CLI handles the interactive/device auth experience; the script only</code> | Developer note explaining why the adjacent code exists or how it fits the demo. |
| 37 | <code>    # asks for the resource-specific token Sentinel custom MCP APIs require.</code> | Developer note explaining why the adjacent code exists or how it fits the demo. |
| 38 | <code>    completed = subprocess.run(</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 39 | <code>        [</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 40 | <code>            &quot;az&quot;,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 41 | <code>            &quot;account&quot;,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 42 | <code>            &quot;get-access-token&quot;,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 43 | <code>            &quot;--resource&quot;,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 44 | <code>            SENTINEL_RESOURCE_ID,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 45 | <code>            &quot;--query&quot;,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 46 | <code>            &quot;accessToken&quot;,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 47 | <code>            &quot;-o&quot;,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 48 | <code>            &quot;tsv&quot;,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 49 | <code>        ],</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 50 | <code>        check=True,</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 51 | <code>        capture_output=True,</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 52 | <code>        text=True,</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 53 | <code>    )</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 54 | <code>    return completed.stdout.strip()</code> | Returns the computed value to the caller. |
| 55 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 56 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 57 | <code>def request(method: str, url: str, token: str, payload: dict) -&gt; dict:</code> | Defines a function; async functions are awaited by the terminal demo or MCP client. |
| 58 | <code>    &quot;&quot;&quot;Send one authenticated JSON request to the Sentinel MCP management API.&quot;&quot;&quot;</code> | Docstring text that explains the purpose of this module, class, or function. |
| 59 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 60 | <code>    body = json.dumps(payload).encode(&quot;utf-8&quot;)</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 61 | <code>    req = urllib.request.Request(</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 62 | <code>        url,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 63 | <code>        data=body,</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 64 | <code>        method=method,</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 65 | <code>        headers={</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 66 | <code>            &quot;Authorization&quot;: f&quot;Bearer {token}&quot;,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 67 | <code>            &quot;Content-Type&quot;: &quot;application/json&quot;,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 68 | <code>        },</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 69 | <code>    )</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 70 | <code>    try:</code> | Handles an operation that can fail while preserving clear error behavior or cleanup. |
| 71 | <code>        with urllib.request.urlopen(req) as response:</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 72 | <code>            return json.loads(response.read().decode(&quot;utf-8&quot;))</code> | Returns the computed value to the caller. |
| 73 | <code>    except urllib.error.HTTPError as exc:</code> | Handles an operation that can fail while preserving clear error behavior or cleanup. |
| 74 | <code>        # Keep the API response body in the exception so publishing failures are</code> | Developer note explaining why the adjacent code exists or how it fits the demo. |
| 75 | <code>        # actionable without rerunning curl or opening a network trace.</code> | Developer note explaining why the adjacent code exists or how it fits the demo. |
| 76 | <code>        details = exc.read().decode(&quot;utf-8&quot;, errors=&quot;replace&quot;)</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 77 | <code>        raise RuntimeError(f&quot;{method} {url} failed: HTTP {exc.code}: {details}&quot;) from exc</code> | Surfaces a configuration or runtime error instead of silently hiding it. |
| 78 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 79 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 80 | <code>def tool_payload(collection: str, workspace_id: str, query_path: pathlib.Path) -&gt; dict:</code> | Defines a function; async functions are awaited by the terminal demo or MCP client. |
| 81 | <code>    &quot;&quot;&quot;Build the custom MCP tool payload for a single `.kql` file.&quot;&quot;&quot;</code> | Docstring text that explains the purpose of this module, class, or function. |
| 82 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 83 | <code>    name = query_path.stem</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 84 | <code>    return {</code> | Returns the computed value to the caller. |
| 85 | <code>        &quot;name&quot;: name,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 86 | <code>        &quot;title&quot;: name.replace(&quot;_&quot;, &quot; &quot;),</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 87 | <code>        &quot;description&quot;: DESCRIPTIONS[name],</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 88 | <code>        &quot;collectionName&quot;: collection,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 89 | <code>        &quot;properties&quot;: {</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 90 | <code>            &quot;mcpToolType&quot;: &quot;Kqs&quot;,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 91 | <code>            # Sentinel executes this KQL when the MCP tool is called.</code> | Developer note explaining why the adjacent code exists or how it fits the demo. |
| 92 | <code>            &quot;queryFormat&quot;: query_path.read_text().strip(),</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 93 | <code>            # The custom MCP API expects a JSON-schema object here. The most</code> | Developer note explaining why the adjacent code exists or how it fits the demo. |
| 94 | <code>            # important input for these tools is the Log Analytics workspace ID.</code> | Developer note explaining why the adjacent code exists or how it fits the demo. |
| 95 | <code>            &quot;arguments&quot;: {</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 96 | <code>                &quot;type&quot;: &quot;object&quot;,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 97 | <code>                &quot;properties&quot;: {</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 98 | <code>                    &quot;workspaceId&quot;: {</code> | Passes the Log Analytics workspace customer ID required by Sentinel MCP tool execution. |
| 99 | <code>                        &quot;type&quot;: &quot;string&quot;,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 100 | <code>                        &quot;description&quot;: &quot;Log Analytics workspace/customer ID to query.&quot;,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 101 | <code>                    }</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 102 | <code>                },</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 103 | <code>                &quot;required&quot;: [&quot;workspaceId&quot;],</code> | Passes the Log Analytics workspace customer ID required by Sentinel MCP tool execution. |
| 104 | <code>            },</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 105 | <code>            &quot;defaultArgumentValues&quot;: {&quot;workspaceId&quot;: workspace_id},</code> | Passes the Log Analytics workspace customer ID required by Sentinel MCP tool execution. |
| 106 | <code>        },</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 107 | <code>    }</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 108 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 109 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 110 | <code>def main() -&gt; int:</code> | Defines a function; async functions are awaited by the terminal demo or MCP client. |
| 111 | <code>    &quot;&quot;&quot;Parse CLI flags, publish the collection, then publish every KQL tool.&quot;&quot;&quot;</code> | Docstring text that explains the purpose of this module, class, or function. |
| 112 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 113 | <code>    parser = argparse.ArgumentParser(description=&quot;Publish Gigamon KQL files as Sentinel custom MCP tools.&quot;)</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 114 | <code>    parser.add_argument(&quot;--collection&quot;, default=&quot;Gigamon-Sentinel-MCP-Demo&quot;)</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 115 | <code>    parser.add_argument(&quot;--workspace-id&quot;, required=True)</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 116 | <code>    parser.add_argument(&quot;--tools-dir&quot;, default=str(pathlib.Path(__file__).parents[1] / &quot;mcp-tools&quot;))</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 117 | <code>    args = parser.parse_args()</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 118 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 119 | <code>    token = az_token()</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 120 | <code>    collection_payload = {</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 121 | <code>        &quot;name&quot;: args.collection,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 122 | <code>        &quot;title&quot;: &quot;Gigamon Sentinel MCP Demo&quot;,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 123 | <code>        &quot;description&quot;: &quot;Custom Sentinel MCP tools for a Gigamon CCF end-to-end developer demo.&quot;,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 124 | <code>    }</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 125 | <code>    print(f&quot;Publishing collection: {args.collection}&quot;)</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 126 | <code>    print(json.dumps(request(&quot;PUT&quot;, f&quot;{API_BASE}/{args.collection}&quot;, token, collection_payload), indent=2))</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 127 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 128 | <code>    # Each KQL filename becomes the MCP tool name, which keeps source control,</code> | Developer note explaining why the adjacent code exists or how it fits the demo. |
| 129 | <code>    # Sentinel, and the terminal prompt router aligned.</code> | Developer note explaining why the adjacent code exists or how it fits the demo. |
| 130 | <code>    for query_path in sorted(pathlib.Path(args.tools_dir).glob(&quot;*.kql&quot;)):</code> | Iterates over a collection or stream to process multiple values. |
| 131 | <code>        payload = tool_payload(args.collection, args.workspace_id, query_path)</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 132 | <code>        print(f&quot;\nPublishing tool: {payload[&#x27;name&#x27;]}&quot;)</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 133 | <code>        print(json.dumps(request(&quot;PUT&quot;, f&quot;{API_BASE}/{args.collection}/tools/{payload[&#x27;name&#x27;]}&quot;, token, payload), indent=2))</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 134 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 135 | <code>    return 0</code> | Returns the computed value to the caller. |
| 136 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 137 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 138 | <code>if __name__ == &quot;__main__&quot;:</code> | Branches behavior based on configuration, input, or response shape. |
| 139 | <code>    sys.exit(main())</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |

## `sentinel_mcp_demo/__init__.py`

| Line | Code | Note |
| ---: | --- | --- |
| 1 | <code>&quot;&quot;&quot;Local Sentinel MCP chatbot demo package.&quot;&quot;&quot;</code> | Docstring text that explains the purpose of this module, class, or function. |
| 2 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |

## `sentinel_mcp_demo/client.py`

| Line | Code | Note |
| ---: | --- | --- |
| 1 | <code>from __future__ import annotations</code> | Enables postponed annotation evaluation so type hints stay lightweight and forward-compatible. |
| 2 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 3 | <code>&quot;&quot;&quot;Minimal async client for Sentinel custom MCP collections.</code> | Docstring text that explains the purpose of this module, class, or function. |
| 4 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 5 | <code>The terminal demo only needs three MCP operations: initialize the session,</code> | Implements the MCP JSON-RPC lifecycle used by Sentinel custom tool endpoints. |
| 6 | <code>discover tools, and call one selected tool. This module keeps that flow explicit</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 7 | <code>so Gigamon developers can see the exact JSON-RPC messages and authentication</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 8 | <code>choices instead of hiding them behind a large framework.</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 9 | <code>&quot;&quot;&quot;</code> | Docstring text that explains the purpose of this module, class, or function. |
| 10 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 11 | <code>import json</code> | Imports a standard library or dependency needed by this module. |
| 12 | <code>import os</code> | Imports a standard library or dependency needed by this module. |
| 13 | <code>from dataclasses import dataclass</code> | Imports a standard library or dependency needed by this module. |
| 14 | <code>from itertools import count</code> | Imports a standard library or dependency needed by this module. |
| 15 | <code>from typing import Any</code> | Imports a standard library or dependency needed by this module. |
| 16 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 17 | <code>import httpx</code> | Imports a standard library or dependency needed by this module. |
| 18 | <code>from azure.identity.aio import ClientSecretCredential, DefaultAzureCredential</code> | Imports a standard library or dependency needed by this module. |
| 19 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 20 | <code>SENTINEL_RESOURCE_ID = &quot;4500ebfb-89b6-4b14-a480-7f749797bfcd&quot;</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 21 | <code>SENTINEL_SCOPE = f&quot;{SENTINEL_RESOURCE_ID}/.default&quot;</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 22 | <code>CUSTOM_COLLECTION_BASE = &quot;https://sentinel.microsoft.com/mcp/custom&quot;</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 23 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 24 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 25 | <code>@dataclass</code> | Uses dataclass generation for a small structured value object. |
| 26 | <code>class MCPTool:</code> | Defines a class that groups state and behavior for this part of the demo. |
| 27 | <code>    &quot;&quot;&quot;Small local representation of a tool returned by `tools/list`.&quot;&quot;&quot;</code> | Docstring text that explains the purpose of this module, class, or function. |
| 28 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 29 | <code>    name: str</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 30 | <code>    description: str = &quot;&quot;</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 31 | <code>    input_schema: dict[str, Any] | None = None</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 32 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 33 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 34 | <code>@dataclass</code> | Uses dataclass generation for a small structured value object. |
| 35 | <code>class MCPToolResult:</code> | Defines a class that groups state and behavior for this part of the demo. |
| 36 | <code>    &quot;&quot;&quot;Normalized result shape returned by `tools/call`.&quot;&quot;&quot;</code> | Docstring text that explains the purpose of this module, class, or function. |
| 37 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 38 | <code>    tool_name: str</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 39 | <code>    content: list[dict[str, Any]]</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 40 | <code>    is_error: bool = False</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 41 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 42 | <code>    @property</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 43 | <code>    def text(self) -&gt; str:</code> | Defines a function; async functions are awaited by the terminal demo or MCP client. |
| 44 | <code>        &quot;&quot;&quot;Render text content into a display-friendly string for the terminal.&quot;&quot;&quot;</code> | Docstring text that explains the purpose of this module, class, or function. |
| 45 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 46 | <code>        if not self.content:</code> | Branches behavior based on configuration, input, or response shape. |
| 47 | <code>            return &quot;&quot;</code> | Returns the computed value to the caller. |
| 48 | <code>        parts: list[str] = []</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 49 | <code>        for item in self.content:</code> | Iterates over a collection or stream to process multiple values. |
| 50 | <code>            if item.get(&quot;type&quot;) == &quot;text&quot;:</code> | Branches behavior based on configuration, input, or response shape. |
| 51 | <code>                parts.append(format_tool_text(str(item.get(&quot;text&quot;, &quot;&quot;))))</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 52 | <code>            else:</code> | Branches behavior based on configuration, input, or response shape. |
| 53 | <code>                parts.append(json.dumps(item, indent=2))</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 54 | <code>        return &quot;\n&quot;.join(parts)</code> | Returns the computed value to the caller. |
| 55 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 56 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 57 | <code>def format_tool_text(text: str) -&gt; str:</code> | Defines a function; async functions are awaited by the terminal demo or MCP client. |
| 58 | <code>    &quot;&quot;&quot;Format Kusto V2 DataSet JSON returned by Sentinel MCP into a readable table.&quot;&quot;&quot;</code> | Docstring text that explains the purpose of this module, class, or function. |
| 59 | <code>    try:</code> | Handles an operation that can fail while preserving clear error behavior or cleanup. |
| 60 | <code>        frames = json.loads(text)</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 61 | <code>    except json.JSONDecodeError:</code> | Handles an operation that can fail while preserving clear error behavior or cleanup. |
| 62 | <code>        return text</code> | Returns the computed value to the caller. |
| 63 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 64 | <code>    if not isinstance(frames, list):</code> | Branches behavior based on configuration, input, or response shape. |
| 65 | <code>        return text</code> | Returns the computed value to the caller. |
| 66 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 67 | <code>    primary = next(</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 68 | <code>        (</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 69 | <code>            frame</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 70 | <code>            for frame in frames</code> | Iterates over a collection or stream to process multiple values. |
| 71 | <code>            if isinstance(frame, dict)</code> | Branches behavior based on configuration, input, or response shape. |
| 72 | <code>            and frame.get(&quot;FrameType&quot;) == &quot;DataTable&quot;</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 73 | <code>            and frame.get(&quot;TableKind&quot;) == &quot;PrimaryResult&quot;</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 74 | <code>        ),</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 75 | <code>        None,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 76 | <code>    )</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 77 | <code>    if not primary:</code> | Branches behavior based on configuration, input, or response shape. |
| 78 | <code>        return text</code> | Returns the computed value to the caller. |
| 79 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 80 | <code>    # Kusto V2 responses carry column metadata separately from row arrays, so we</code> | Developer note explaining why the adjacent code exists or how it fits the demo. |
| 81 | <code>    # rebuild name/value alignment before showing the result to a human.</code> | Developer note explaining why the adjacent code exists or how it fits the demo. |
| 82 | <code>    columns = [col.get(&quot;ColumnName&quot;, &quot;&quot;) for col in primary.get(&quot;Columns&quot;, [])]</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 83 | <code>    rows = primary.get(&quot;Rows&quot;, [])</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 84 | <code>    if not columns:</code> | Branches behavior based on configuration, input, or response shape. |
| 85 | <code>        return text</code> | Returns the computed value to the caller. |
| 86 | <code>    if not rows:</code> | Branches behavior based on configuration, input, or response shape. |
| 87 | <code>        return &quot;Query completed successfully, but returned no rows.&quot;</code> | Returns the computed value to the caller. |
| 88 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 89 | <code>    rendered_rows = [[str(value) for value in row] for row in rows]</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 90 | <code>    widths = [</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 91 | <code>        max(len(str(columns[i])), *(len(row[i]) if i &lt; len(row) else 0 for row in rendered_rows))</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 92 | <code>        for i in range(len(columns))</code> | Iterates over a collection or stream to process multiple values. |
| 93 | <code>    ]</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 94 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 95 | <code>    header = &quot; | &quot;.join(str(columns[i]).ljust(widths[i]) for i in range(len(columns)))</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 96 | <code>    divider = &quot;-+-&quot;.join(&quot;-&quot; * width for width in widths)</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 97 | <code>    body = [</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 98 | <code>        &quot; | &quot;.join((row[i] if i &lt; len(row) else &quot;&quot;).ljust(widths[i]) for i in range(len(columns)))</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 99 | <code>        for row in rendered_rows</code> | Iterates over a collection or stream to process multiple values. |
| 100 | <code>    ]</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 101 | <code>    return &quot;\n&quot;.join([header, divider, *body])</code> | Returns the computed value to the caller. |
| 102 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 103 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 104 | <code>class SentinelMCPError(RuntimeError):</code> | Defines a class that groups state and behavior for this part of the demo. |
| 105 | <code>    &quot;&quot;&quot;Raised when the MCP server or Sentinel management surface rejects a call.&quot;&quot;&quot;</code> | Docstring text that explains the purpose of this module, class, or function. |
| 106 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 107 | <code>    pass</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 108 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 109 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 110 | <code>class SentinelMCPClient:</code> | Defines a class that groups state and behavior for this part of the demo. |
| 111 | <code>    &quot;&quot;&quot;Async Sentinel MCP client used by the local terminal demo.&quot;&quot;&quot;</code> | Docstring text that explains the purpose of this module, class, or function. |
| 112 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 113 | <code>    def __init__(</code> | Defines a function; async functions are awaited by the terminal demo or MCP client. |
| 114 | <code>        self,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 115 | <code>        *,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 116 | <code>        collection: str | None = None,</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 117 | <code>        server_url: str | None = None,</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 118 | <code>        timeout_seconds: float = 120.0,</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 119 | <code>    ) -&gt; None:</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 120 | <code>        # The demo can use either a collection name or a full server URL. The</code> | Developer note explaining why the adjacent code exists or how it fits the demo. |
| 121 | <code>        # collection name is easiest for developers; the URL escape hatch helps</code> | Developer note explaining why the adjacent code exists or how it fits the demo. |
| 122 | <code>        # if Sentinel changes endpoint routing or a proxy is introduced.</code> | Developer note explaining why the adjacent code exists or how it fits the demo. |
| 123 | <code>        if server_url:</code> | Branches behavior based on configuration, input, or response shape. |
| 124 | <code>            self.server_url = server_url.rstrip(&quot;/&quot;)</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 125 | <code>        elif collection:</code> | Branches behavior based on configuration, input, or response shape. |
| 126 | <code>            self.server_url = f&quot;{CUSTOM_COLLECTION_BASE}/{collection.removeprefix(&#x27;custom/&#x27;)}&quot;</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 127 | <code>        else:</code> | Branches behavior based on configuration, input, or response shape. |
| 128 | <code>            raise ValueError(&quot;Set either collection or server_url.&quot;)</code> | Surfaces a configuration or runtime error instead of silently hiding it. |
| 129 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 130 | <code>        self.timeout_seconds = timeout_seconds</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 131 | <code>        self._http: httpx.AsyncClient | None = None</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 132 | <code>        self._request_ids = count(1)</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 133 | <code>        self.tools: list[MCPTool] = []</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 134 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 135 | <code>    async def connect(self) -&gt; None:</code> | Defines a function; async functions are awaited by the terminal demo or MCP client. |
| 136 | <code>        &quot;&quot;&quot;Authenticate, initialize the MCP session, and cache available tools.&quot;&quot;&quot;</code> | Docstring text that explains the purpose of this module, class, or function. |
| 137 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 138 | <code>        token = await self._get_token()</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 139 | <code>        self._http = httpx.AsyncClient(</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 140 | <code>            headers={</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 141 | <code>                &quot;Authorization&quot;: f&quot;Bearer {token}&quot;,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 142 | <code>                &quot;Content-Type&quot;: &quot;application/json&quot;,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 143 | <code>                &quot;Accept&quot;: &quot;application/json, text/event-stream&quot;,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 144 | <code>            },</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 145 | <code>            timeout=httpx.Timeout(self.timeout_seconds),</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 146 | <code>        )</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 147 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 148 | <code>        await self._send_request(</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 149 | <code>            &quot;initialize&quot;,</code> | Implements the MCP JSON-RPC lifecycle used by Sentinel custom tool endpoints. |
| 150 | <code>            {</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 151 | <code>                &quot;protocolVersion&quot;: &quot;2024-11-05&quot;,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 152 | <code>                &quot;capabilities&quot;: {},</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 153 | <code>                &quot;clientInfo&quot;: {&quot;name&quot;: &quot;local-sentinel-mcp-chatbot&quot;, &quot;version&quot;: &quot;1.0.0&quot;},</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 154 | <code>            },</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 155 | <code>        )</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 156 | <code>        await self._send_notification(&quot;notifications/initialized&quot;, {})</code> | Implements the MCP JSON-RPC lifecycle used by Sentinel custom tool endpoints. |
| 157 | <code>        self.tools = await self.list_tools()</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 158 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 159 | <code>    async def close(self) -&gt; None:</code> | Defines a function; async functions are awaited by the terminal demo or MCP client. |
| 160 | <code>        &quot;&quot;&quot;Dispose the underlying HTTP client.&quot;&quot;&quot;</code> | Docstring text that explains the purpose of this module, class, or function. |
| 161 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 162 | <code>        if self._http:</code> | Branches behavior based on configuration, input, or response shape. |
| 163 | <code>            await self._http.aclose()</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 164 | <code>            self._http = None</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 165 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 166 | <code>    async def list_tools(self) -&gt; list[MCPTool]:</code> | Defines a function; async functions are awaited by the terminal demo or MCP client. |
| 167 | <code>        &quot;&quot;&quot;Fetch tool metadata from the custom Sentinel MCP collection.&quot;&quot;&quot;</code> | Docstring text that explains the purpose of this module, class, or function. |
| 168 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 169 | <code>        response = await self._send_request(&quot;tools/list&quot;, {})</code> | Implements the MCP JSON-RPC lifecycle used by Sentinel custom tool endpoints. |
| 170 | <code>        return [</code> | Returns the computed value to the caller. |
| 171 | <code>            MCPTool(</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 172 | <code>                name=item[&quot;name&quot;],</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 173 | <code>                description=item.get(&quot;description&quot;, &quot;&quot;),</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 174 | <code>                input_schema=item.get(&quot;inputSchema&quot;, {}),</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 175 | <code>            )</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 176 | <code>            for item in response.get(&quot;tools&quot;, [])</code> | Iterates over a collection or stream to process multiple values. |
| 177 | <code>        ]</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 178 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 179 | <code>    async def call_tool(self, tool_name: str, arguments: dict[str, Any] | None = None) -&gt; MCPToolResult:</code> | Defines a function; async functions are awaited by the terminal demo or MCP client. |
| 180 | <code>        &quot;&quot;&quot;Call one MCP tool by name with a JSON-object argument payload.&quot;&quot;&quot;</code> | Docstring text that explains the purpose of this module, class, or function. |
| 181 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 182 | <code>        response = await self._send_request(</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 183 | <code>            &quot;tools/call&quot;,</code> | Implements the MCP JSON-RPC lifecycle used by Sentinel custom tool endpoints. |
| 184 | <code>            {&quot;name&quot;: tool_name, &quot;arguments&quot;: arguments or {}},</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 185 | <code>        )</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 186 | <code>        return MCPToolResult(</code> | Returns the computed value to the caller. |
| 187 | <code>            tool_name=tool_name,</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 188 | <code>            content=response.get(&quot;content&quot;, []),</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 189 | <code>            is_error=response.get(&quot;isError&quot;, False),</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 190 | <code>        )</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 191 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 192 | <code>    async def _get_token(self) -&gt; str:</code> | Defines a function; async functions are awaited by the terminal demo or MCP client. |
| 193 | <code>        &quot;&quot;&quot;Resolve credentials from environment first, then fall back to Azure CLI/browser auth.&quot;&quot;&quot;</code> | Docstring text that explains the purpose of this module, class, or function. |
| 194 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 195 | <code>        tenant_id = os.getenv(&quot;AZURE_TENANT_ID&quot;)</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 196 | <code>        client_id = os.getenv(&quot;AZURE_CLIENT_ID&quot;)</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 197 | <code>        client_secret = os.getenv(&quot;AZURE_CLIENT_SECRET&quot;)</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 198 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 199 | <code>        if tenant_id and client_id and client_secret:</code> | Branches behavior based on configuration, input, or response shape. |
| 200 | <code>            # Service-principal auth is useful for unattended demos or hosted apps.</code> | Developer note explaining why the adjacent code exists or how it fits the demo. |
| 201 | <code>            async with ClientSecretCredential(</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 202 | <code>                tenant_id=tenant_id,</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 203 | <code>                client_id=client_id,</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 204 | <code>                client_secret=client_secret,</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 205 | <code>            ) as credential:</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 206 | <code>                return (await credential.get_token(SENTINEL_SCOPE)).token</code> | Returns the computed value to the caller. |
| 207 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 208 | <code>        # DefaultAzureCredential supports Azure CLI sign-in, managed identity,</code> | Developer note explaining why the adjacent code exists or how it fits the demo. |
| 209 | <code>        # Visual Studio Code credentials, and other local developer flows.</code> | Developer note explaining why the adjacent code exists or how it fits the demo. |
| 210 | <code>        async with DefaultAzureCredential() as credential:</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 211 | <code>            return (await credential.get_token(SENTINEL_SCOPE)).token</code> | Returns the computed value to the caller. |
| 212 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 213 | <code>    async def _send_request(self, method: str, params: dict[str, Any]) -&gt; dict[str, Any]:</code> | Defines a function; async functions are awaited by the terminal demo or MCP client. |
| 214 | <code>        &quot;&quot;&quot;Send a JSON-RPC request and normalize either JSON or SSE responses.&quot;&quot;&quot;</code> | Docstring text that explains the purpose of this module, class, or function. |
| 215 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 216 | <code>        if not self._http:</code> | Branches behavior based on configuration, input, or response shape. |
| 217 | <code>            raise SentinelMCPError(&quot;Client is not connected.&quot;)</code> | Surfaces a configuration or runtime error instead of silently hiding it. |
| 218 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 219 | <code>        request_id = next(self._request_ids)</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 220 | <code>        payload = {</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 221 | <code>            &quot;jsonrpc&quot;: &quot;2.0&quot;,</code> | Implements the MCP JSON-RPC lifecycle used by Sentinel custom tool endpoints. |
| 222 | <code>            &quot;id&quot;: request_id,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 223 | <code>            &quot;method&quot;: method,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 224 | <code>            &quot;params&quot;: params,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 225 | <code>        }</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 226 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 227 | <code>        async with self._http.stream(&quot;POST&quot;, f&quot;{self.server_url}/&quot;, json=payload) as response:</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 228 | <code>            if response.status_code not in (200, 202):</code> | Branches behavior based on configuration, input, or response shape. |
| 229 | <code>                body = await response.aread()</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 230 | <code>                raise SentinelMCPError(f&quot;HTTP {response.status_code}: {body.decode(errors=&#x27;replace&#x27;)}&quot;)</code> | Surfaces a configuration or runtime error instead of silently hiding it. |
| 231 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 232 | <code>            content_type = response.headers.get(&quot;content-type&quot;, &quot;&quot;)</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 233 | <code>            if &quot;text/event-stream&quot; in content_type:</code> | Branches behavior based on configuration, input, or response shape. |
| 234 | <code>                # Sentinel MCP may stream JSON-RPC results over SSE, so the demo</code> | Developer note explaining why the adjacent code exists or how it fits the demo. |
| 235 | <code>                # supports both simple JSON and streaming responses.</code> | Developer note explaining why the adjacent code exists or how it fits the demo. |
| 236 | <code>                return await self._parse_sse_response(response, request_id)</code> | Returns the computed value to the caller. |
| 237 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 238 | <code>            body = await response.aread()</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 239 | <code>            if not body:</code> | Branches behavior based on configuration, input, or response shape. |
| 240 | <code>                return {}</code> | Returns the computed value to the caller. |
| 241 | <code>            message = json.loads(body)</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 242 | <code>            if &quot;error&quot; in message:</code> | Branches behavior based on configuration, input, or response shape. |
| 243 | <code>                raise SentinelMCPError(message[&quot;error&quot;].get(&quot;message&quot;, str(message[&quot;error&quot;])))</code> | Surfaces a configuration or runtime error instead of silently hiding it. |
| 244 | <code>            return message.get(&quot;result&quot;, message)</code> | Returns the computed value to the caller. |
| 245 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 246 | <code>    async def _send_notification(self, method: str, params: dict[str, Any]) -&gt; None:</code> | Defines a function; async functions are awaited by the terminal demo or MCP client. |
| 247 | <code>        &quot;&quot;&quot;Send a JSON-RPC notification, which has no response ID/result.&quot;&quot;&quot;</code> | Docstring text that explains the purpose of this module, class, or function. |
| 248 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 249 | <code>        if not self._http:</code> | Branches behavior based on configuration, input, or response shape. |
| 250 | <code>            raise SentinelMCPError(&quot;Client is not connected.&quot;)</code> | Surfaces a configuration or runtime error instead of silently hiding it. |
| 251 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 252 | <code>        await self._http.post(</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 253 | <code>            f&quot;{self.server_url}/&quot;,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 254 | <code>            json={&quot;jsonrpc&quot;: &quot;2.0&quot;, &quot;method&quot;: method, &quot;params&quot;: params},</code> | Implements the MCP JSON-RPC lifecycle used by Sentinel custom tool endpoints. |
| 255 | <code>        )</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 256 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 257 | <code>    async def _parse_sse_response(self, response: httpx.Response, request_id: int) -&gt; dict[str, Any]:</code> | Defines a function; async functions are awaited by the terminal demo or MCP client. |
| 258 | <code>        &quot;&quot;&quot;Collect SSE data frames until the matching JSON-RPC result appears.&quot;&quot;&quot;</code> | Docstring text that explains the purpose of this module, class, or function. |
| 259 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 260 | <code>        data_lines: list[str] = []</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 261 | <code>        async for line in response.aiter_lines():</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 262 | <code>            if line.startswith(&quot;data:&quot;):</code> | Branches behavior based on configuration, input, or response shape. |
| 263 | <code>                data_lines.append(line.removeprefix(&quot;data:&quot;).strip())</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 264 | <code>                continue</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 265 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 266 | <code>            if line == &quot;&quot; and data_lines:</code> | Branches behavior based on configuration, input, or response shape. |
| 267 | <code>                result = self._parse_sse_message(&quot;&quot;.join(data_lines), request_id)</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 268 | <code>                data_lines = []</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 269 | <code>                if result is not None:</code> | Branches behavior based on configuration, input, or response shape. |
| 270 | <code>                    return result</code> | Returns the computed value to the caller. |
| 271 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 272 | <code>        if data_lines:</code> | Branches behavior based on configuration, input, or response shape. |
| 273 | <code>            result = self._parse_sse_message(&quot;&quot;.join(data_lines), request_id)</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 274 | <code>            if result is not None:</code> | Branches behavior based on configuration, input, or response shape. |
| 275 | <code>                return result</code> | Returns the computed value to the caller. |
| 276 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 277 | <code>        raise SentinelMCPError(&quot;SSE stream ended without a JSON-RPC result.&quot;)</code> | Surfaces a configuration or runtime error instead of silently hiding it. |
| 278 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 279 | <code>    @staticmethod</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 280 | <code>    def _parse_sse_message(data: str, request_id: int) -&gt; dict[str, Any] | None:</code> | Defines a function; async functions are awaited by the terminal demo or MCP client. |
| 281 | <code>        &quot;&quot;&quot;Parse one SSE data payload and return only the result for our request.&quot;&quot;&quot;</code> | Docstring text that explains the purpose of this module, class, or function. |
| 282 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 283 | <code>        try:</code> | Handles an operation that can fail while preserving clear error behavior or cleanup. |
| 284 | <code>            message = json.loads(data)</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 285 | <code>        except json.JSONDecodeError:</code> | Handles an operation that can fail while preserving clear error behavior or cleanup. |
| 286 | <code>            return None</code> | Returns the computed value to the caller. |
| 287 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 288 | <code>        if message.get(&quot;id&quot;) != request_id and &quot;result&quot; not in message:</code> | Branches behavior based on configuration, input, or response shape. |
| 289 | <code>            return None</code> | Returns the computed value to the caller. |
| 290 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 291 | <code>        if &quot;error&quot; in message:</code> | Branches behavior based on configuration, input, or response shape. |
| 292 | <code>            raise SentinelMCPError(message[&quot;error&quot;].get(&quot;message&quot;, str(message[&quot;error&quot;])))</code> | Surfaces a configuration or runtime error instead of silently hiding it. |
| 293 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 294 | <code>        return message.get(&quot;result&quot;, message)</code> | Returns the computed value to the caller. |

## `sentinel_mcp_demo/mock.py`

| Line | Code | Note |
| ---: | --- | --- |
| 1 | <code>from __future__ import annotations</code> | Enables postponed annotation evaluation so type hints stay lightweight and forward-compatible. |
| 2 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 3 | <code>&quot;&quot;&quot;Mock MCP client used when the terminal demo runs without Azure connectivity.</code> | Docstring text that explains the purpose of this module, class, or function. |
| 4 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 5 | <code>The mock intentionally mirrors the small interface exposed by `SentinelMCPClient`</code> | Connects the terminal demo to the Sentinel custom MCP collection. |
| 6 | <code>so the rest of the terminal app can switch between `MCP_DEMO_MODE=mock` and</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 7 | <code>`MCP_DEMO_MODE=real` without branching throughout the codebase.</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 8 | <code>&quot;&quot;&quot;</code> | Docstring text that explains the purpose of this module, class, or function. |
| 9 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 10 | <code>import json</code> | Imports a standard library or dependency needed by this module. |
| 11 | <code>from typing import Any</code> | Imports a standard library or dependency needed by this module. |
| 12 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 13 | <code>from .client import MCPTool, MCPToolResult</code> | Imports a standard library or dependency needed by this module. |
| 14 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 15 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 16 | <code>class MockSentinelMCPClient:</code> | Defines a class that groups state and behavior for this part of the demo. |
| 17 | <code>    &quot;&quot;&quot;Return deterministic MCP-like results for offline presenter practice.&quot;&quot;&quot;</code> | Docstring text that explains the purpose of this module, class, or function. |
| 18 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 19 | <code>    def __init__(self) -&gt; None:</code> | Defines a function; async functions are awaited by the terminal demo or MCP client. |
| 20 | <code>        self.tools = [</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 21 | <code>            MCPTool(</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 22 | <code>                name=&quot;Gigamon_Visibility_Posture_Summary&quot;,</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 23 | <code>                description=&quot;Summarize Gigamon visibility posture across sources, destinations, apps, and bytes.&quot;,</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 24 | <code>                input_schema={</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 25 | <code>                    &quot;type&quot;: &quot;object&quot;,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 26 | <code>                    &quot;properties&quot;: {&quot;workspaceId&quot;: {&quot;type&quot;: &quot;string&quot;}},</code> | Passes the Log Analytics workspace customer ID required by Sentinel MCP tool execution. |
| 27 | <code>                },</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 28 | <code>            ),</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 29 | <code>            MCPTool(</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 30 | <code>                name=&quot;Gigamon_Lateral_Movement_Triage&quot;,</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 31 | <code>                description=&quot;Triage possible east-west movement over SMB, RDP, and SSH.&quot;,</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 32 | <code>                input_schema={</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 33 | <code>                    &quot;type&quot;: &quot;object&quot;,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 34 | <code>                    &quot;properties&quot;: {&quot;workspaceId&quot;: {&quot;type&quot;: &quot;string&quot;}},</code> | Passes the Log Analytics workspace customer ID required by Sentinel MCP tool execution. |
| 35 | <code>                },</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 36 | <code>            ),</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 37 | <code>            MCPTool(</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 38 | <code>                name=&quot;Gigamon_DNS_Anomaly_Hunt&quot;,</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 39 | <code>                description=&quot;Hunt DNS anomalies using query types, reply codes, and response times.&quot;,</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 40 | <code>                input_schema={</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 41 | <code>                    &quot;type&quot;: &quot;object&quot;,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 42 | <code>                    &quot;properties&quot;: {&quot;workspaceId&quot;: {&quot;type&quot;: &quot;string&quot;}},</code> | Passes the Log Analytics workspace customer ID required by Sentinel MCP tool execution. |
| 43 | <code>                },</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 44 | <code>            ),</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 45 | <code>            MCPTool(</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 46 | <code>                name=&quot;Gigamon_TLS_Risk_Summary&quot;,</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 47 | <code>                description=&quot;Summarize weak TLS protocol, key length, certificate, and JA3 signals.&quot;,</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 48 | <code>                input_schema={&quot;type&quot;: &quot;object&quot;, &quot;properties&quot;: {&quot;workspaceId&quot;: {&quot;type&quot;: &quot;string&quot;}}},</code> | Passes the Log Analytics workspace customer ID required by Sentinel MCP tool execution. |
| 49 | <code>            ),</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 50 | <code>            MCPTool(</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 51 | <code>                name=&quot;Gigamon_Top_Talkers_By_App&quot;,</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 52 | <code>                description=&quot;Rank applications by flows, bytes, packets, sources, and destinations.&quot;,</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 53 | <code>                input_schema={&quot;type&quot;: &quot;object&quot;, &quot;properties&quot;: {&quot;workspaceId&quot;: {&quot;type&quot;: &quot;string&quot;}}},</code> | Passes the Log Analytics workspace customer ID required by Sentinel MCP tool execution. |
| 54 | <code>            ),</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 55 | <code>        ]</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 56 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 57 | <code>    async def connect(self) -&gt; None:</code> | Defines a function; async functions are awaited by the terminal demo or MCP client. |
| 58 | <code>        &quot;&quot;&quot;Match the real client&#x27;s async connect method without doing network I/O.&quot;&quot;&quot;</code> | Docstring text that explains the purpose of this module, class, or function. |
| 59 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 60 | <code>        return None</code> | Returns the computed value to the caller. |
| 61 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 62 | <code>    async def close(self) -&gt; None:</code> | Defines a function; async functions are awaited by the terminal demo or MCP client. |
| 63 | <code>        &quot;&quot;&quot;Match the real client&#x27;s async close method without owning resources.&quot;&quot;&quot;</code> | Docstring text that explains the purpose of this module, class, or function. |
| 64 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 65 | <code>        return None</code> | Returns the computed value to the caller. |
| 66 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 67 | <code>    async def list_tools(self) -&gt; list[MCPTool]:</code> | Defines a function; async functions are awaited by the terminal demo or MCP client. |
| 68 | <code>        &quot;&quot;&quot;Return static tool metadata in the same shape as `tools/list`.&quot;&quot;&quot;</code> | Docstring text that explains the purpose of this module, class, or function. |
| 69 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 70 | <code>        return self.tools</code> | Returns the computed value to the caller. |
| 71 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 72 | <code>    async def call_tool(self, tool_name: str, arguments: dict[str, Any] | None = None) -&gt; MCPToolResult:</code> | Defines a function; async functions are awaited by the terminal demo or MCP client. |
| 73 | <code>        &quot;&quot;&quot;Return a deterministic text result shaped like an MCP tool response.&quot;&quot;&quot;</code> | Docstring text that explains the purpose of this module, class, or function. |
| 74 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 75 | <code>        args = arguments or {}</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 76 | <code>        workspace = args.get(&quot;workspaceId&quot;) or &quot;mock-workspace&quot;</code> | Passes the Log Analytics workspace customer ID required by Sentinel MCP tool execution. |
| 77 | <code>        text = {</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 78 | <code>            &quot;Gigamon_Visibility_Posture_Summary&quot;: (</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 79 | <code>                f&quot;Visibility posture for {workspace}: 274 Gigamon events across 24 sources and 19 destinations.\n&quot;</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 80 | <code>                &quot;- Top apps: https, dns, smb, rdp, ssh\n&quot;</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 81 | <code>                &quot;- Total bytes observed: 3.8 GB\n&quot;</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 82 | <code>                &quot;- Recommended action: pivot into lateral movement and DNS tools for investigation depth&quot;</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 83 | <code>            ),</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 84 | <code>            &quot;Gigamon_Lateral_Movement_Triage&quot;: (</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 85 | <code>                f&quot;Lateral movement triage for {workspace}: elevated SMB/RDP/SSH east-west activity.\n&quot;</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 86 | <code>                &quot;- 31 candidate flows on ports 445, 3389, and 22\n&quot;</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 87 | <code>                &quot;- Top sources: 10.12.4.18, 10.12.4.23\n&quot;</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 88 | <code>                &quot;- Recommended action: isolate the top source and validate endpoint identity&quot;</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 89 | <code>            ),</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 90 | <code>            &quot;Gigamon_DNS_Anomaly_Hunt&quot;: (</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 91 | <code>                f&quot;DNS anomaly hunt for {workspace}: suspicious lookup pattern detected.\n&quot;</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 92 | <code>                &quot;- Failed responses: NXDOMAIN and SERVFAIL\n&quot;</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 93 | <code>                &quot;- Slow query family: TXT and A lookups\n&quot;</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 94 | <code>                &quot;- Recommended action: review queried domains and source workload owner&quot;</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 95 | <code>            ),</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 96 | <code>            &quot;Gigamon_TLS_Risk_Summary&quot;: (</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 97 | <code>                f&quot;TLS risk summary for {workspace}: weak crypto and JA3 observations require review.\n&quot;</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 98 | <code>                &quot;- Weak protocol: TLS 1.0 / TLS 1.1\n&quot;</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 99 | <code>                &quot;- Weak key observations: 1024-bit RSA\n&quot;</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 100 | <code>                &quot;- Recommended action: map issuer/common-name pairs to application owners&quot;</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 101 | <code>            ),</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 102 | <code>            &quot;Gigamon_Top_Talkers_By_App&quot;: (</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 103 | <code>                f&quot;Top talkers for {workspace}: https and unknown-tcp dominate byte volume.\n&quot;</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 104 | <code>                &quot;- Top source: 10.12.8.44\n&quot;</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 105 | <code>                &quot;- Top destination: 52.239.148.88\n&quot;</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 106 | <code>                &quot;- Recommended action: verify sanctioned app ownership for high-volume transfers&quot;</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 107 | <code>            ),</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 108 | <code>        }.get(tool_name, f&quot;Mock result for {tool_name}:\n{json.dumps(args, indent=2)}&quot;)</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 109 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 110 | <code>        return MCPToolResult(</code> | Returns the computed value to the caller. |
| 111 | <code>            tool_name=tool_name,</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 112 | <code>            content=[{&quot;type&quot;: &quot;text&quot;, &quot;text&quot;: text}],</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 113 | <code>            is_error=False,</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 114 | <code>        )</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |

## `terminal_demo.py`

| Line | Code | Note |
| ---: | --- | --- |
| 1 | <code>from __future__ import annotations</code> | Enables postponed annotation evaluation so type hints stay lightweight and forward-compatible. |
| 2 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 3 | <code>&quot;&quot;&quot;Interactive terminal demo for the Gigamon Sentinel MCP tools.</code> | Docstring text that explains the purpose of this module, class, or function. |
| 4 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 5 | <code>This replaces the earlier browser demo with the lowest-friction presenter flow:</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 6 | <code>run one Python command, type normal investigation prompts, and show the tool</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 7 | <code>selection, arguments, concise summary, and raw Sentinel MCP result in the same</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 8 | <code>terminal window.</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 9 | <code>&quot;&quot;&quot;</code> | Docstring text that explains the purpose of this module, class, or function. |
| 10 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 11 | <code>import argparse</code> | Imports a standard library or dependency needed by this module. |
| 12 | <code>import asyncio</code> | Imports a standard library or dependency needed by this module. |
| 13 | <code>import json</code> | Imports a standard library or dependency needed by this module. |
| 14 | <code>import os</code> | Imports a standard library or dependency needed by this module. |
| 15 | <code>from typing import Any</code> | Imports a standard library or dependency needed by this module. |
| 16 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 17 | <code>from dotenv import load_dotenv</code> | Imports a standard library or dependency needed by this module. |
| 18 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 19 | <code>from sentinel_mcp_demo.client import MCPToolResult, SentinelMCPClient</code> | Imports a standard library or dependency needed by this module. |
| 20 | <code>from sentinel_mcp_demo.mock import MockSentinelMCPClient</code> | Imports a standard library or dependency needed by this module. |
| 21 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 22 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 23 | <code>GIGAMON_TOOLS = {</code> | Maps user-facing Gigamon investigation intents to concrete custom MCP tool names. |
| 24 | <code>    &quot;visibility&quot;: &quot;Gigamon_Visibility_Posture_Summary&quot;,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 25 | <code>    &quot;lateral&quot;: &quot;Gigamon_Lateral_Movement_Triage&quot;,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 26 | <code>    &quot;dns&quot;: &quot;Gigamon_DNS_Anomaly_Hunt&quot;,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 27 | <code>    &quot;tls&quot;: &quot;Gigamon_TLS_Risk_Summary&quot;,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 28 | <code>    &quot;talkers&quot;: &quot;Gigamon_Top_Talkers_By_App&quot;,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 29 | <code>}</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 30 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 31 | <code>TOOL_ROUTES = [</code> | Maps user-facing Gigamon investigation intents to concrete custom MCP tool names. |
| 32 | <code>    ((&quot;lateral&quot;, &quot;east-west&quot;, &quot;rdp&quot;, &quot;smb&quot;, &quot;ssh&quot;, &quot;movement&quot;), GIGAMON_TOOLS[&quot;lateral&quot;]),</code> | Maps user-facing Gigamon investigation intents to concrete custom MCP tool names. |
| 33 | <code>    ((&quot;dns&quot;, &quot;domain&quot;, &quot;lookup&quot;, &quot;nxdomain&quot;, &quot;servfail&quot;), GIGAMON_TOOLS[&quot;dns&quot;]),</code> | Maps user-facing Gigamon investigation intents to concrete custom MCP tool names. |
| 34 | <code>    ((&quot;tls&quot;, &quot;ssl&quot;, &quot;cert&quot;, &quot;certificate&quot;, &quot;ja3&quot;, &quot;weak key&quot;), GIGAMON_TOOLS[&quot;tls&quot;]),</code> | Maps user-facing Gigamon investigation intents to concrete custom MCP tool names. |
| 35 | <code>    ((&quot;top&quot;, &quot;talker&quot;, &quot;app&quot;, &quot;bytes&quot;, &quot;packets&quot;, &quot;bandwidth&quot;), GIGAMON_TOOLS[&quot;talkers&quot;]),</code> | Maps user-facing Gigamon investigation intents to concrete custom MCP tool names. |
| 36 | <code>]</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 37 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 38 | <code>EXAMPLE_PROMPTS = [</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 39 | <code>    &quot;Summarize Gigamon visibility posture&quot;,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 40 | <code>    &quot;Show possible lateral movement&quot;,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 41 | <code>    &quot;Hunt DNS anomalies&quot;,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 42 | <code>    &quot;Summarize TLS risk&quot;,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 43 | <code>    &quot;Show top talkers by app&quot;,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 44 | <code>]</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 45 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 46 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 47 | <code>def parse_json_env(name: str, default: dict[str, Any]) -&gt; dict[str, Any]:</code> | Defines a function; async functions are awaited by the terminal demo or MCP client. |
| 48 | <code>    &quot;&quot;&quot;Read an environment variable that must contain a JSON object.&quot;&quot;&quot;</code> | Docstring text that explains the purpose of this module, class, or function. |
| 49 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 50 | <code>    raw = os.getenv(name)</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 51 | <code>    if not raw:</code> | Branches behavior based on configuration, input, or response shape. |
| 52 | <code>        return default</code> | Returns the computed value to the caller. |
| 53 | <code>    try:</code> | Handles an operation that can fail while preserving clear error behavior or cleanup. |
| 54 | <code>        value = json.loads(raw)</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 55 | <code>    except json.JSONDecodeError as exc:</code> | Handles an operation that can fail while preserving clear error behavior or cleanup. |
| 56 | <code>        raise ValueError(f&quot;{name} must be valid JSON: {exc}&quot;) from exc</code> | Surfaces a configuration or runtime error instead of silently hiding it. |
| 57 | <code>    if not isinstance(value, dict):</code> | Branches behavior based on configuration, input, or response shape. |
| 58 | <code>        raise ValueError(f&quot;{name} must be a JSON object.&quot;)</code> | Surfaces a configuration or runtime error instead of silently hiding it. |
| 59 | <code>    return value</code> | Returns the computed value to the caller. |
| 60 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 61 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 62 | <code>def render_arguments(message: str, template: str, defaults: dict[str, Any]) -&gt; dict[str, Any]:</code> | Defines a function; async functions are awaited by the terminal demo or MCP client. |
| 63 | <code>    &quot;&quot;&quot;Render the prompt into the MCP argument template and merge defaults.&quot;&quot;&quot;</code> | Docstring text that explains the purpose of this module, class, or function. |
| 64 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 65 | <code>    rendered = template.replace(&quot;{message}&quot;, message)</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 66 | <code>    try:</code> | Handles an operation that can fail while preserving clear error behavior or cleanup. |
| 67 | <code>        args = json.loads(rendered)</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 68 | <code>    except json.JSONDecodeError as exc:</code> | Handles an operation that can fail while preserving clear error behavior or cleanup. |
| 69 | <code>        raise ValueError(f&quot;MCP_TOOL_ARGUMENT_TEMPLATE rendered invalid JSON: {exc}&quot;) from exc</code> | Surfaces a configuration or runtime error instead of silently hiding it. |
| 70 | <code>    if not isinstance(args, dict):</code> | Branches behavior based on configuration, input, or response shape. |
| 71 | <code>        raise ValueError(&quot;MCP_TOOL_ARGUMENT_TEMPLATE must render to a JSON object.&quot;)</code> | Surfaces a configuration or runtime error instead of silently hiding it. |
| 72 | <code>    return {**args, **defaults}</code> | Returns the computed value to the caller. |
| 73 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 74 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 75 | <code>def select_tool(prompt: str) -&gt; str:</code> | Defines a function; async functions are awaited by the terminal demo or MCP client. |
| 76 | <code>    &quot;&quot;&quot;Choose the Gigamon MCP tool that best matches the typed prompt.&quot;&quot;&quot;</code> | Docstring text that explains the purpose of this module, class, or function. |
| 77 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 78 | <code>    configured = os.getenv(&quot;SENTINEL_MCP_TOOL&quot;, &quot;&quot;).strip()</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 79 | <code>    prompt_lower = prompt.lower()</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 80 | <code>    for keywords, tool_name in TOOL_ROUTES:</code> | Iterates over a collection or stream to process multiple values. |
| 81 | <code>        if any(keyword in prompt_lower for keyword in keywords):</code> | Branches behavior based on configuration, input, or response shape. |
| 82 | <code>            return tool_name</code> | Returns the computed value to the caller. |
| 83 | <code>    return configured or GIGAMON_TOOLS[&quot;visibility&quot;]</code> | Returns the computed value to the caller. |
| 84 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 85 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 86 | <code>def create_mcp_client() -&gt; SentinelMCPClient | MockSentinelMCPClient:</code> | Defines a function; async functions are awaited by the terminal demo or MCP client. |
| 87 | <code>    &quot;&quot;&quot;Create either the real Sentinel MCP client or the offline mock client.&quot;&quot;&quot;</code> | Docstring text that explains the purpose of this module, class, or function. |
| 88 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 89 | <code>    mode = os.getenv(&quot;MCP_DEMO_MODE&quot;, &quot;mock&quot;).strip().lower()</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 90 | <code>    if mode == &quot;real&quot;:</code> | Branches behavior based on configuration, input, or response shape. |
| 91 | <code>        return SentinelMCPClient(</code> | Returns the computed value to the caller. |
| 92 | <code>            collection=os.getenv(&quot;SENTINEL_MCP_COLLECTION&quot;),</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 93 | <code>            server_url=os.getenv(&quot;SENTINEL_MCP_SERVER_URL&quot;),</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 94 | <code>        )</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 95 | <code>    if mode == &quot;mock&quot;:</code> | Branches behavior based on configuration, input, or response shape. |
| 96 | <code>        return MockSentinelMCPClient()</code> | Returns the computed value to the caller. |
| 97 | <code>    raise ValueError(&quot;MCP_DEMO_MODE must be &#x27;mock&#x27; or &#x27;real&#x27;.&quot;)</code> | Surfaces a configuration or runtime error instead of silently hiding it. |
| 98 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 99 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 100 | <code>def dataset_rows(result: MCPToolResult) -&gt; list[dict[str, Any]]:</code> | Defines a function; async functions are awaited by the terminal demo or MCP client. |
| 101 | <code>    &quot;&quot;&quot;Extract Kusto PrimaryResult rows from the raw MCP text content.&quot;&quot;&quot;</code> | Docstring text that explains the purpose of this module, class, or function. |
| 102 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 103 | <code>    rows: list[dict[str, Any]] = []</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 104 | <code>    for item in result.content:</code> | Iterates over a collection or stream to process multiple values. |
| 105 | <code>        if item.get(&quot;type&quot;) != &quot;text&quot;:</code> | Branches behavior based on configuration, input, or response shape. |
| 106 | <code>            continue</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 107 | <code>        text = str(item.get(&quot;text&quot;, &quot;&quot;))</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 108 | <code>        try:</code> | Handles an operation that can fail while preserving clear error behavior or cleanup. |
| 109 | <code>            frames = json.loads(text)</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 110 | <code>        except json.JSONDecodeError:</code> | Handles an operation that can fail while preserving clear error behavior or cleanup. |
| 111 | <code>            continue</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 112 | <code>        if not isinstance(frames, list):</code> | Branches behavior based on configuration, input, or response shape. |
| 113 | <code>            continue</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 114 | <code>        primary = next(</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 115 | <code>            (</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 116 | <code>                frame</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 117 | <code>                for frame in frames</code> | Iterates over a collection or stream to process multiple values. |
| 118 | <code>                if isinstance(frame, dict)</code> | Branches behavior based on configuration, input, or response shape. |
| 119 | <code>                and frame.get(&quot;FrameType&quot;) == &quot;DataTable&quot;</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 120 | <code>                and frame.get(&quot;TableKind&quot;) == &quot;PrimaryResult&quot;</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 121 | <code>            ),</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 122 | <code>            None,</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 123 | <code>        )</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 124 | <code>        if not primary:</code> | Branches behavior based on configuration, input, or response shape. |
| 125 | <code>            continue</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 126 | <code>        columns = [column.get(&quot;ColumnName&quot;, &quot;&quot;) for column in primary.get(&quot;Columns&quot;, [])]</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 127 | <code>        for row in primary.get(&quot;Rows&quot;, []):</code> | Iterates over a collection or stream to process multiple values. |
| 128 | <code>            rows.append({columns[index]: value for index, value in enumerate(row) if index &lt; len(columns)})</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 129 | <code>    return rows</code> | Returns the computed value to the caller. |
| 130 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 131 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 132 | <code>def summarize(prompt: str, tool_name: str, rows: list[dict[str, Any]], raw_text: str) -&gt; str:</code> | Defines a function; async functions are awaited by the terminal demo or MCP client. |
| 133 | <code>    &quot;&quot;&quot;Create a presenter-friendly summary from the first returned row.&quot;&quot;&quot;</code> | Docstring text that explains the purpose of this module, class, or function. |
| 134 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 135 | <code>    if not rows:</code> | Branches behavior based on configuration, input, or response shape. |
| 136 | <code>        return raw_text or f&quot;{tool_name} completed for: {prompt}&quot;</code> | Returns the computed value to the caller. |
| 137 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 138 | <code>    row = rows[0]</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 139 | <code>    if tool_name == GIGAMON_TOOLS[&quot;lateral&quot;]:</code> | Branches behavior based on configuration, input, or response shape. |
| 140 | <code>        return (</code> | Returns the computed value to the caller. |
| 141 | <code>            f&quot;Lateral movement triage found {row.get(&#x27;FlowCount&#x27;)} candidate flows on destination port &quot;</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 142 | <code>            f&quot;{row.get(&#x27;dst_port&#x27;)}, totaling {row.get(&#x27;TotalBytes&#x27;)} bytes. Sources: {row.get(&#x27;Sources&#x27;)}. &quot;</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 143 | <code>            f&quot;Destinations: {row.get(&#x27;Destinations&#x27;)}.&quot;</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 144 | <code>        )</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 145 | <code>    if tool_name == GIGAMON_TOOLS[&quot;dns&quot;]:</code> | Branches behavior based on configuration, input, or response shape. |
| 146 | <code>        return (</code> | Returns the computed value to the caller. |
| 147 | <code>            f&quot;DNS anomaly hunt found {row.get(&#x27;Queries&#x27;)} {row.get(&#x27;dns_query_type&#x27;)} queries, &quot;</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 148 | <code>            f&quot;with {row.get(&#x27;FailedQueries&#x27;)} failed and {row.get(&#x27;SlowQueries&#x27;)} slow responses. &quot;</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 149 | <code>            f&quot;Queries: {row.get(&#x27;QueryNames&#x27;)}.&quot;</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 150 | <code>        )</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 151 | <code>    if tool_name == GIGAMON_TOOLS[&quot;tls&quot;]:</code> | Branches behavior based on configuration, input, or response shape. |
| 152 | <code>        return (</code> | Returns the computed value to the caller. |
| 153 | <code>            f&quot;TLS risk summary found {row.get(&#x27;Sessions&#x27;)} sessions for {row.get(&#x27;ProtocolVersion&#x27;)}. &quot;</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 154 | <code>            f&quot;Weak protocol sessions: {row.get(&#x27;WeakProtocol&#x27;)}; weak key observations: {row.get(&#x27;WeakKey&#x27;)}; &quot;</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 155 | <code>            f&quot;expiring soon: {row.get(&#x27;ExpiringSoon&#x27;)}.&quot;</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 156 | <code>        )</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 157 | <code>    if tool_name == GIGAMON_TOOLS[&quot;talkers&quot;]:</code> | Branches behavior based on configuration, input, or response shape. |
| 158 | <code>        return (</code> | Returns the computed value to the caller. |
| 159 | <code>            f&quot;Top talkers shows {row.get(&#x27;app_name&#x27;)} / {row.get(&#x27;app_family&#x27;)} over {row.get(&#x27;protocol&#x27;)} &quot;</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 160 | <code>            f&quot;with {row.get(&#x27;Flows&#x27;)} flows and {row.get(&#x27;Bytes&#x27;)} bytes. Top sources: {row.get(&#x27;TopSources&#x27;)}.&quot;</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 161 | <code>        )</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 162 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 163 | <code>    return (</code> | Returns the computed value to the caller. |
| 164 | <code>        f&quot;Visibility posture found {row.get(&#x27;Events&#x27;)} Gigamon events across &quot;</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 165 | <code>        f&quot;{row.get(&#x27;UniqueSources&#x27;)} sources and {row.get(&#x27;UniqueDestinations&#x27;)} destinations, &quot;</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 166 | <code>        f&quot;totaling {row.get(&#x27;TotalBytes&#x27;)} bytes. Apps: {row.get(&#x27;Apps&#x27;)}.&quot;</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 167 | <code>    )</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 168 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 169 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 170 | <code>async def run_prompt(prompt: str, *, show_raw: bool) -&gt; None:</code> | Defines a function; async functions are awaited by the terminal demo or MCP client. |
| 171 | <code>    &quot;&quot;&quot;Call the selected MCP tool once and print the result.&quot;&quot;&quot;</code> | Docstring text that explains the purpose of this module, class, or function. |
| 172 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 173 | <code>    tool_name = select_tool(prompt)</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 174 | <code>    template = os.getenv(&quot;MCP_TOOL_ARGUMENT_TEMPLATE&quot;, &#x27;{&quot;query&quot;:&quot;{message}&quot;}&#x27;)</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 175 | <code>    defaults = parse_json_env(&quot;MCP_DEFAULT_ARGUMENTS&quot;, {})</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 176 | <code>    arguments = render_arguments(prompt, template, defaults)</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 177 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 178 | <code>    print(f&quot;\nPrompt: {prompt}&quot;)</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 179 | <code>    print(f&quot;Tool:   {tool_name}&quot;)</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 180 | <code>    print(f&quot;Args:   {json.dumps(arguments, sort_keys=True)}&quot;)</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 181 | <code>    print(&quot;Status: calling Sentinel MCP...\n&quot;)</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 182 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 183 | <code>    client = create_mcp_client()</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 184 | <code>    await client.connect()</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 185 | <code>    try:</code> | Handles an operation that can fail while preserving clear error behavior or cleanup. |
| 186 | <code>        result = await client.call_tool(tool_name, arguments)</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 187 | <code>    finally:</code> | Handles an operation that can fail while preserving clear error behavior or cleanup. |
| 188 | <code>        await client.close()</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 189 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 190 | <code>    rows = dataset_rows(result)</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 191 | <code>    raw_text = result.text or json.dumps(result.content, indent=2)</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 192 | <code>    print(&quot;Summary&quot;)</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 193 | <code>    print(&quot;-------&quot;)</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 194 | <code>    print(summarize(prompt, tool_name, rows, raw_text))</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 195 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 196 | <code>    if show_raw:</code> | Branches behavior based on configuration, input, or response shape. |
| 197 | <code>        print(&quot;\nRaw MCP result&quot;)</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 198 | <code>        print(&quot;--------------&quot;)</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 199 | <code>        print(raw_text)</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 200 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 201 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 202 | <code>async def interactive_loop(show_raw: bool) -&gt; None:</code> | Defines a function; async functions are awaited by the terminal demo or MCP client. |
| 203 | <code>    &quot;&quot;&quot;Run the live terminal prompt loop until the presenter exits.&quot;&quot;&quot;</code> | Docstring text that explains the purpose of this module, class, or function. |
| 204 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 205 | <code>    print(&quot;Gigamon Sentinel MCP Terminal Demo&quot;)</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 206 | <code>    print(&quot;Type a prompt and press Enter. Type &#x27;examples&#x27; to list prompts or &#x27;quit&#x27; to exit.\n&quot;)</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 207 | <code>    print(&quot;Examples:&quot;)</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 208 | <code>    for prompt in EXAMPLE_PROMPTS:</code> | Iterates over a collection or stream to process multiple values. |
| 209 | <code>        print(f&quot;  - {prompt}&quot;)</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 210 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 211 | <code>    while True:</code> | Iterates over a collection or stream to process multiple values. |
| 212 | <code>        try:</code> | Handles an operation that can fail while preserving clear error behavior or cleanup. |
| 213 | <code>            prompt = input(&quot;\ngigamon-mcp&gt; &quot;).strip()</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 214 | <code>        except (EOFError, KeyboardInterrupt):</code> | Handles an operation that can fail while preserving clear error behavior or cleanup. |
| 215 | <code>            print()</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 216 | <code>            return</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 217 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 218 | <code>        if not prompt:</code> | Branches behavior based on configuration, input, or response shape. |
| 219 | <code>            continue</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 220 | <code>        if prompt.lower() in {&quot;quit&quot;, &quot;exit&quot;, &quot;q&quot;}:</code> | Branches behavior based on configuration, input, or response shape. |
| 221 | <code>            return</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 222 | <code>        if prompt.lower() == &quot;examples&quot;:</code> | Branches behavior based on configuration, input, or response shape. |
| 223 | <code>            for example in EXAMPLE_PROMPTS:</code> | Iterates over a collection or stream to process multiple values. |
| 224 | <code>                print(f&quot;  - {example}&quot;)</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 225 | <code>            continue</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 226 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 227 | <code>        try:</code> | Handles an operation that can fail while preserving clear error behavior or cleanup. |
| 228 | <code>            await run_prompt(prompt, show_raw=show_raw)</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 229 | <code>        except Exception as exc:</code> | Handles an operation that can fail while preserving clear error behavior or cleanup. |
| 230 | <code>            print(f&quot;Error: {exc}&quot;)</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 231 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 232 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 233 | <code>def main() -&gt; None:</code> | Defines a function; async functions are awaited by the terminal demo or MCP client. |
| 234 | <code>    &quot;&quot;&quot;Load configuration, parse flags, and start the terminal demo.&quot;&quot;&quot;</code> | Docstring text that explains the purpose of this module, class, or function. |
| 235 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 236 | <code>    load_dotenv()</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |
| 237 | <code>    parser = argparse.ArgumentParser(description=&quot;Run the Gigamon Sentinel MCP terminal demo.&quot;)</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 238 | <code>    parser.add_argument(&quot;--prompt&quot;, help=&quot;Run one prompt and exit instead of starting the interactive loop.&quot;)</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 239 | <code>    parser.add_argument(&quot;--show-raw&quot;, action=&quot;store_true&quot;, help=&quot;Print the formatted raw MCP/Kusto result.&quot;)</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 240 | <code>    args = parser.parse_args()</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 241 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 242 | <code>    if args.prompt:</code> | Branches behavior based on configuration, input, or response shape. |
| 243 | <code>        asyncio.run(run_prompt(args.prompt, show_raw=args.show_raw))</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 244 | <code>    else:</code> | Branches behavior based on configuration, input, or response shape. |
| 245 | <code>        asyncio.run(interactive_loop(show_raw=args.show_raw))</code> | Assigns configuration, intermediate state, or response data used later in the flow. |
| 246 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 247 | <code>&nbsp;</code> | Blank separator line that improves readability and groups related statements. |
| 248 | <code>if __name__ == &quot;__main__&quot;:</code> | Branches behavior based on configuration, input, or response shape. |
| 249 | <code>    main()</code> | Executable Python statement that supports the end-to-end Gigamon MCP demo flow. |

