| **Field** | **Type** | **Description** | **Predefined Values** | **Example Value** |
|-----------|----------|-----------------|----------------------|-------------------|
| `headerId` | Integer | headerId of the message. The headerId is defined per topic and incremented by 1 with each sent (but not necessarily received) message. |  |  |
| `timestamp` | String | Timestamp in ISO8601 format (YYYY-MM-DDTHH:mm:ss.ssZ). |  | 1991-03-11T11:40:03.12Z |
| `version` | String | Version of the protocol [Major].[Minor].[Patch] |  | 1.3.2 |
| `manufacturer` | String | Manufacturer of the AGV |  |  |
| `serialNumber` | String | Serial number of the AGV. |  |  |
| `actions` | Array | No description available. |  |  |
| `actions[].actionType` | String | Name of action as described in the first column of "Actions and Parameters". Identifies the function of the action. |  |  |
| `actions[].actionId` | String | Unique ID to identify the action and map them to the actionState in the state. Suggestion: Use UUIDs. |  |  |
| `actions[].actionDescription` | String | Additional information on the action. |  |  |
| `actions[].blockingType` | Enum | Regulates if the action is allowed to be executed during movement and/or parallel to other actions.
none: action can happen in parallel with others, including movement.
soft: action can happen simultaneously with others, but not while moving.
hard: no other actions can be performed while this action is running. | NONE, SOFT, HARD |  |
| `actions[].actionParameters` | Array | Array of actionParameter-objects for the indicated action e. g. deviceId, loadId, external Triggers. |  |  |
| `actions[].actionParameters[].key` | String | The key of the action parameter. |  | duration, direction, signal |
| `actions[].actionParameters[].value` | Array/boolean/number/string | The value of the action parameter |  | 103.2, left, True, ['arrays', 'are', 'also', 'valid'] |