| **Field** | **Type** | **Description** | **Predefined Values** | **Example Value** |
|-----------|----------|-----------------|----------------------|-------------------|
| `headerId` | Integer | headerId of the message. The headerId is defined per topic and incremented by 1 with each sent (but not necessarily received) message. |  |  |
| `timestamp` | String | Timestamp in ISO8601 format (YYYY-MM-DDTHH:mm:ss.ssZ). |  | 1991-03-11T11:40:03.12Z |
| `version` | String | Version of the protocol [Major].[Minor].[Patch] |  | 1.3.2 |
| `manufacturer` | String | Manufacturer of the AGV |  |  |
| `serialNumber` | String | Serial number of the AGV. |  |  |
| `orderId` | String | Order Identification. This is to be used to identify multiple order messages that belong to the same order. |  |  |
| `orderUpdateId` | Integer | orderUpdate identification. Is unique per orderId. If an order update is rejected, this field is to be passed in the rejection message. |  |  |
| `zoneSetId` | String | Unique identifier of the zone set that the AGV has to use for navigation or that was used by MC for planning.
Optional: Some MC systems do not use zones. Some AGVs do not understand zones. Do not add to message if no zones are used. |  |  |
| `nodes` | Array | Array of nodes objects to be traversed for fulfilling the order. One node is enough for a valid order. Leave edge list empty for that case. |  |  |
| `nodes[].nodeId` | String | Unique node identification |  | pumpenhaus_1, MONTAGE |
| `nodes[].sequenceId` | Integer | Number to track the sequence of nodes and edges in an order and to simplify order updates.
The main purpose is to distinguish between a node which is passed more than once within one orderId. The variable sequenceId runs across all nodes and edges of the same order and is reset when a new orderId is issued. |  |  |
| `nodes[].nodeDescription` | String | Additional information on the node. |  |  |
| `nodes[].released` | Boolean | True indicates that the node is part of the base. False indicates that the node is part of the horizon. |  |  |
| `nodes[].nodePosition` | Object | Defines the position on a map in world coordinates. Each floor has its own map. All maps must use the same project specific global origin. 
Optional for vehicle-types that do not require the node position (e.g., line-guided vehicles). |  |  |
| `nodes[].nodePosition.x` | Number | X-position on the map in reference to the map coordinate system. Precision is up to the specific implementation. |  |  |
| `nodes[].nodePosition.y` | Number | Y-position on the map in reference to the map coordinate system. Precision is up to the specific implementation. |  |  |
| `nodes[].nodePosition.theta` | Number | Absolute orientation of the AGV on the node. 
Optional: vehicle can plan the path by itself.
If defined, the AGV has to assume the theta angle on this node. If previous edge disallows rotation, the AGV must rotate on the node. If following edge has a differing orientation defined but disallows rotation, the AGV is to rotate on the node to the edges desired rotation before entering the edge. |  |  |
| `nodes[].nodePosition.allowedDeviationXy` | Number | Indicates how exact an AGV has to drive over a node in order for it to count as traversed.
If = 0: no deviation is allowed (no deviation means within the normal tolerance of the AGV manufacturer).
If > 0: allowed deviation-radius in meters. If the AGV passes a node within the deviation-radius, the node is considered to have been traversed. |  |  |
| `nodes[].nodePosition.allowedDeviationTheta` | Number | Indicates how big the deviation of theta angle can be. 
The lowest acceptable angle is theta - allowedDeviationTheta and the highest acceptable angle is theta + allowedDeviationTheta. |  |  |
| `nodes[].nodePosition.mapId` | String | Unique identification of the map in which the position is referenced.
Each map has the same origin of coordinates. When an AGV uses an elevator, e.g., leading from a departure floor to a target floor, it will disappear off the map of the departure floor and spawn in the related lift node on the map of the target floor. |  |  |
| `nodes[].nodePosition.mapDescription` | String | Additional information on the map. |  |  |
| `nodes[].actions` | Array | Array of actions to be executed on a node. Empty array, if no actions required. |  |  |
| `edges` | Array | Directional connection between two nodes. Array of edge objects to be traversed for fulfilling the order. One node is enough for a valid order. Leave edge list empty for that case. |  |  |
| `edges[].edgeId` | String | Unique edge identification |  |  |
| `edges[].sequenceId` | Integer | Number to track the sequence of nodes and edges in an order and to simplify order updates. The variable sequenceId runs across all nodes and edges of the same order and is reset when a new orderId is issued. |  |  |
| `edges[].edgeDescription` | String | Additional information on the edge. |  |  |
| `edges[].released` | Boolean | True indicates that the edge is part of the base. False indicates that the edge is part of the horizon. |  |  |
| `edges[].startNodeId` | String | The nodeId of the start node. |  |  |
| `edges[].endNodeId` | String | The nodeId of the end node. |  |  |
| `edges[].maxSpeed` | Number | Permitted maximum speed on the edge in m/s. Speed is defined by the fastest measurement of the vehicle. |  |  |
| `edges[].maxHeight` | Number | Permitted maximum height of the vehicle, including the load, on edge in meters. |  |  |
| `edges[].minHeight` | Number | Permitted minimal height of the load handling device on the edge in meters |  |  |
| `edges[].orientation` | Number | Orientation of the AGV on the edge. The value orientationType defines if it has to be interpreted relative to the global project specific map coordinate system or tangential to the edge. In case of interpreted tangential to the edge 0.0 = forwards and PI = backwards. Example: orientation Pi/2 rad will lead to a rotation of 90 degrees. 
If AGV starts in different orientation, rotate the vehicle on the edge to the desired orientation if rotationAllowed is set to True. If rotationAllowed is False, rotate before entering the edge. If that is not possible, reject the order. 
If no trajectory is defined, apply the rotation to the direct path between the two connecting nodes of the edge. If a trajectory is defined for the edge, apply the orientation to the trajectory. |  |  |
| `edges[].orientationType` | String | Enum {GLOBALGLOBAL, TANGENTIALTANGENTIAL}: 
"GLOBAL"- relative to the global project specific map coordinate system; 
"TANGENTIAL"- tangential to the edge. 
If not defined, the default value is "TANGENTIAL". |  |  |
| `edges[].direction` | String | Sets direction at junctions for line-guided or wire-guided vehicles, to be defined initially (vehicle-individual). |  | left, right, straight, 433MHz |
| `edges[].rotationAllowed` | Boolean | True: rotation is allowed on the edge. False: rotation is not allowed on the edge. 
Optional: No limit, if not set. |  |  |
| `edges[].maxRotationSpeed` | Number | Maximum rotation speed in rad/s. 
Optional: No limit, if not set. |  |  |
| `edges[].length` | Number | Distance of the path from startNode to endNode in meters. 
Optional: This value is used by line-guided AGVs to decrease their speed before reaching a stop position. |  |  |
| `edges[].trajectory` | Object | Trajectory JSON-object for this edge as a NURBS. Defines the curve, on which the AGV should move between startNode and endNode. 
Optional: Can be omitted, if AGV cannot process trajectories or if AGV plans its own trajectory. |  |  |
| `edges[].trajectory.degree` | Integer | Defines the number of control points that influence any given point on the curve. Increasing the degree increases continuity. If not defined, the default value is 1. |  |  |
| `edges[].trajectory.knotVector` | Array | Sequence of parameter values that determines where and how the control points affect the NURBS curve. knotVector has size of number of control points + degree + 1. |  |  |
| `edges[].trajectory.controlPoints` | Array | List of JSON controlPoint objects defining the control points of the NURBS, which includes the beginning and end point. |  |  |
| `edges[].trajectory.controlPoints[].x` | Number | X coordinate described in the world coordinate system. |  |  |
| `edges[].trajectory.controlPoints[].y` | Number | Y coordinate described in the world coordinate system. |  |  |
| `edges[].trajectory.controlPoints[].weight` | Number | The weight, with which this control point pulls on the curve. When not defined, the default will be 1.0. |  |  |
| `edges[].actions` | Array | Array of action objects with detailed information. |  |  |
| `actionType` | String | Name of action as described in the first column of "Actions and Parameters". Identifies the function of the action. |  |  |
| `actionId` | String | Unique ID to identify the action and map them to the actionState in the state. Suggestion: Use UUIDs. |  |  |
| `actionDescription` | String | Additional information on the action. |  |  |
| `blockingType` | Enum | Regulates if the action is allowed to be executed during movement and/or parallel to other actions.
none: action can happen in parallel with others, including movement.
soft: action can happen simultaneously with others, but not while moving.
hard: no other actions can be performed while this action is running. | NONE, SOFT, HARD |  |
| `actionParameters` | Array | Array of actionParameter-objects for the indicated action e. g. deviceId, loadId, external Triggers. |  |  |
| `actionParameters[].key` | String | The key of the action parameter. |  | duration, direction, signal |
| `actionParameters[].value` | Array/boolean/number/string | The value of the action parameter |  | 103.2, left, True, ['arrays', 'are', 'also', 'valid'] |