| **Field** | **Type** | **Description** | **Predefined Values** | **Example Value** |
|-----------|----------|-----------------|----------------------|-------------------|
| `headerId` | Integer | headerId of the message. The headerId is defined per topic and incremented by 1 with each sent (but not necessarily received) message. |  |  |
| `timestamp` | String | Timestamp in ISO8601 format (YYYY-MM-DDTHH:mm:ss.ssZ). |  | 1991-03-11T11:40:03.12Z |
| `version` | String | Version of the protocol [Major].[Minor].[Patch] |  | 1.3.2 |
| `manufacturer` | String | Manufacturer of the AGV |  |  |
| `serialNumber` | String | Serial number of the AGV. |  |  |
| `agvPosition` | Object | The AGVs position |  |  |
| `agvPosition.x` | Number | No description available. |  |  |
| `agvPosition.y` | Number | No description available. |  |  |
| `agvPosition.theta` | Number | No description available. |  |  |
| `agvPosition.mapId` | String | No description available. |  |  |
| `agvPosition.positionInitialized` | Boolean | True if the AGVs position is initialized, false, if position is not initizalized. |  |  |
| `agvPosition.localizationScore` | Number | Localization score for SLAM based vehicles, if the AGV can communicate it. |  |  |
| `agvPosition.deviationRange` | Number | Value for position deviation range in meters. Can be used if the AGV is able to derive it. |  |  |
| `velocity` | Object | The AGVs velocity in vehicle coordinates |  |  |
| `velocity.vx` | Number | No description available. |  |  |
| `velocity.vy` | Number | No description available. |  |  |
| `velocity.omega` | Number | No description available. |  |  |