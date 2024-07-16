| **Field** | **Type** | **Description** | **Predefined Values** | **Example Value** |
|-----------|----------|-----------------|----------------------|-------------------|
| `headerId` | Integer | Header ID of the message. The headerId is defined per topic and incremented by 1 with each sent (but not necessarily received) message. |  |  |
| `timestamp` | String | Timestamp in ISO8601 format (YYYY-MM-DDTHH:mm:ss.ssZ). |  | 1991-03-11T11:40:03.12Z |
| `version` | String | Version of the protocol [Major].[Minor].[Patch] |  | 1.3.2 |
| `manufacturer` | String | Manufacturer of the AGV. |  |  |
| `serialNumber` | String | Serial number of the AGV. |  |  |
| `connectionState` | Enum | ONLINE: connection between AGV and broker is active. OFFLINE: connection between AGV and broker has gone offline in a coordinated way. CONNECTIONBROKEN: The connection between AGV and broker has unexpectedly ended. | ONLINE, OFFLINE, CONNECTIONBROKEN |  |