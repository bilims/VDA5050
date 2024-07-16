| **Field** | **Type** | **Description** | **Predefined Values** | **Example Value** |
|-----------|----------|-----------------|----------------------|-------------------|
| `headerId` | Integer | headerId of the message. The headerId is defined per topic and incremented by 1 with each sent (but not necessarily received) message. |  |  |
| `timestamp` | String | Timestamp in ISO8601 format (YYYY-MM-DDTHH:mm:ss.ssZ). |  | 1991-03-11T11:40:03.12Z |
| `version` | String | Version of the protocol [Major].[Minor].[Patch] |  | 1.3.2 |
| `manufacturer` | String | Manufacturer of the AGV |  |  |
| `serialNumber` | String | Serial number of the AGV. |  |  |
| `orderId` | String | Unique order identification of the current order or the previous finished order. The orderId is kept until a new order is received. Empty string ("") if no previous orderId is available.  |  |  |
| `orderUpdateId` | Integer | Order Update Identification to identify that an order update has been accepted by the AGV. "0" if no previous orderUpdateId is available. |  |  |
| `zoneSetId` | String | Unique ID of the zone set that the AGV currently uses for path planning. Must be the same as the one used in the order, otherwise the AGV is to reject the order.
Optional: If the AGV does not use zones, this field can be omitted. |  |  |
| `lastNodeId` | String | nodeID of last reached node or, if AGV is currently on a node, current node (e.g., "node7"). Empty string ("") if no lastNodeId is available. |  |  |
| `lastNodeSequenceId` | Integer | sequenceId of the last reached node or, if the AGV is currently on a node, sequenceId of current node.
â€œ0â€ if no lastNodeSequenceId is available.  |  |  |
| `driving` | Boolean | True: indicates that the AGV is driving and/or rotating. Other movements of the AGV (e.g., lift movements) are not included here.
False: indicates that the AGV is neither driving nor rotating  |  |  |
| `paused` | Boolean | True: AGV is currently in a paused state, either because of the push of a physical button on the AGV or because of an instantAction. The AGV can resume the order.
False: The AGV is currently not in a paused state. |  |  |
| `newBaseRequest` | Boolean | True: AGV is almost at the end of the base and will reduce speed if no new base is transmitted. Trigger for master control to send new base
False: no base update required. |  |  |
| `distanceSinceLastNode` | Number | Used by line guided vehicles to indicate the distance it has been driving past the "lastNodeId".
Distance is in meters. |  |  |
| `operatingMode` | Enum | Current operating mode of the AGV. | AUTOMATIC, SEMIAUTOMATIC, MANUAL, SERVICE, TEACHIN |  |
| `nodeStates` | Array | Array of nodeState-Objects, that need to be traversed for fulfilling the order. Empty list if idle. |  |  |
| `nodeStates[].nodeId` | String | Unique node identification |  |  |
| `nodeStates[].sequenceId` | Integer | sequenceId to discern multiple nodes with same nodeId. |  |  |
| `nodeStates[].nodeDescription` | String | Additional information on the node. |  |  |
| `nodeStates[].nodePosition` | Object | Node position. The object is defined in chapter 5.4 Topic: Order (from master control to AGV).
Optional:Master control has this information. Can be sent additionally, e.g., for debugging purposes.  |  |  |
| `nodeStates[].nodePosition.x` | Number | No description available. |  |  |
| `nodeStates[].nodePosition.y` | Number | No description available. |  |  |
| `nodeStates[].nodePosition.theta` | Number | No description available. |  |  |
| `nodeStates[].nodePosition.mapId` | String | No description available. |  |  |
| `nodeStates[].released` | Boolean | True: indicates that the node is part of the base. False: indicates that the node is part of the horizon. |  |  |
| `edgeStates` | Array | Array of edgeState-Objects, that need to be traversed for fulfilling the order, empty list if idle. |  |  |
| `edgeStates[].edgeId` | String | Unique edge identification |  |  |
| `edgeStates[].sequenceId` | Integer | sequenceId of the edge. |  |  |
| `edgeStates[].edgeDescription` | String | Additional information on the edge. |  |  |
| `edgeStates[].released` | Boolean | True indicates that the edge is part of the base. False indicates that the edge is part of the horizon. |  |  |
| `edgeStates[].trajectory` | Object | The trajectory is to be communicated as a NURBS and is defined in chapter 6.7 Implementation of the Order message.
Trajectory segments reach from the point, where the AGV starts to enter the edge to the point where it reports that the next node was traversed.  |  |  |
| `edgeStates[].trajectory.degree` | Integer | Defines the number of control points that influence any given point on the curve. Increasing the degree increases continuity. If not defined, the default value is 1. |  |  |
| `edgeStates[].trajectory.knotVector` | Array | Sequence of parameter values that determine where and how the control points affect the NURBS curve. knotVector has size of number of control points + degree + 1 |  |  |
| `edgeStates[].trajectory.controlPoints` | Array | List of JSON controlPoint objects defining the control points of the NURBS, which includes the beginning and end point. |  |  |
| `edgeStates[].trajectory.controlPoints[].x` | Number | No description available. |  |  |
| `edgeStates[].trajectory.controlPoints[].y` | Number | No description available. |  |  |
| `edgeStates[].trajectory.controlPoints[].weight` | Number | The weight, with which this control point pulls on the curve.
When not defined, the default will be 1.0. |  |  |
| `agvPosition` | Object | Defines the position on a map in world coordinates. Each floor has its own map. |  |  |
| `agvPosition.x` | Number | No description available. |  |  |
| `agvPosition.y` | Number | No description available. |  |  |
| `agvPosition.theta` | Number | No description available. |  |  |
| `agvPosition.mapId` | String | No description available. |  |  |
| `agvPosition.mapDescription` | String | No description available. |  |  |
| `agvPosition.positionInitialized` | Boolean | True: position is initialized. False: position is not initizalized. |  |  |
| `agvPosition.localizationScore` | Number | Describes the quality of the localization and therefore, can be used, e.g., by SLAM-AGV to describe how accurate the current position information is.
0.0: position unknown
1.0: position known
Optional for vehicles that cannot estimate their localization score.
Only for logging and visualization purposes |  |  |
| `agvPosition.deviationRange` | Number | Value for position deviation range in meters. Optional for vehicles that cannot estimate their deviation, e.g., grid-based localization. Only for logging and visualization purposes. |  |  |
| `velocity` | Object | The AGVs velocity in vehicle coordinates |  |  |
| `velocity.vx` | Number | The AVGs velocity in its x direction |  |  |
| `velocity.vy` | Number | The AVGs velocity in its y direction |  |  |
| `velocity.omega` | Number | The AVGs turning speed around its z axis. |  |  |
| `loads` | Array | Loads, that are currently handled by the AGV. Optional: If AGV cannot determine load state, leave the array out of the state. If the AGV can determine the load state, but the array is empty, the AGV is considered unloaded. |  |  |
| `loads[].loadId` | String | Unique identification number of the load (e.g., barcode or RFID). Empty field, if the AGV can identify the load, but did not identify the load yet. Optional, if the AGV cannot identify the load. |  |  |
| `loads[].loadType` | String | Type of load. |  |  |
| `loads[].loadPosition` | String | Indicates, which load handling/carrying unit of the AGV is used, e.g., in case the AGV has multiple spots/positions to carry loads. Optional for vehicles with only one loadPosition. |  | front, back, positionC1 |
| `loads[].boundingBoxReference` | Object | Point of reference for the location of the bounding box. The point of reference is always the center of the bounding box bottom surface (at height = 0) and is described in coordinates of the AGV coordinate system. |  |  |
| `loads[].boundingBoxReference.x` | Number | No description available. |  |  |
| `loads[].boundingBoxReference.y` | Number | No description available. |  |  |
| `loads[].boundingBoxReference.z` | Number | No description available. |  |  |
| `loads[].boundingBoxReference.theta` | Number | Orientation of the loads bounding box. Important for tugger, trains, etc. |  |  |
| `loads[].loadDimensions` | Object | Dimensions of the loads bounding box in meters. |  |  |
| `loads[].loadDimensions.length` | Number | Absolute length of the loads bounding box in meter. |  |  |
| `loads[].loadDimensions.width` | Number | Absolute width of the loads bounding box in meter. |  |  |
| `loads[].loadDimensions.height` | Number | Absolute height of the loads bounding box in meter.
Optional:
Set value only if known. |  |  |
| `loads[].weight` | Number | Absolute weight of the load measured in kg. |  |  |
| `actionStates` | Array | Contains a list of the current actions and the actions which are yet to be finished. This may include actions from previous nodes that are still in progress
When an action is completed, an updated state message is published with actionStatus set to finished and if applicable with the corresponding resultDescription. The actionStates are kept until a new order is received. |  |  |
| `actionStates[].actionId` | String | Unique actionId |  | blink_123jdaimoim234 |
| `actionStates[].actionType` | String | actionType of the action.
Optional: Only for informational or visualization purposes. Order knows the type. |  |  |
| `actionStates[].actionDescription` | String | Additional information on the current action. |  |  |
| `actionStates[].actionStatus` | Enum | WAITING: waiting for the trigger (passing the mode, entering the edge) PAUSED: paused by instantAction or external trigger FAILED: action could not be performed. | WAITING, INITIALIZING, RUNNING, FINISHED, FAILED |  |
| `actionStates[].resultDescription` | String | Description of the result, e.g., the result of a RFID-read. Errors will be transmitted in errors. |  |  |
| `batteryState` | Object | Contains all battery-related information. |  |  |
| `batteryState.batteryCharge` | Number | State of Charge in %:
If AGV only provides values for good or bad battery levels, these will be indicated as 20% (bad) and 80% (good). |  |  |
| `batteryState.batteryVoltage` | Number | Battery voltage |  |  |
| `batteryState.batteryHealth` | Number | State of health in percent. |  |  |
| `batteryState.charging` | Boolean | True: charging in progress. False: AGV is currently not charging. |  |  |
| `batteryState.reach` | Number | Estimated reach with current State of Charge in meter. |  |  |
| `errors` | Array | Array of error-objects. All active errors of the AGV should be in the list. An empty array indicates that the AGV has no active errors. |  |  |
| `errors[].errorType` | String | Type/name of error. |  |  |
| `errors[].errorReferences` | Array | No description available. |  |  |
| `errors[].errorReferences[].referenceKey` | String | References the type of reference (e.g., headerId, orderId, actionId, etc.). |  |  |
| `errors[].errorReferences[].referenceValue` | String | References the value, which belongs to the reference key. |  |  |
| `errors[].errorDescription` | String | Error description. |  |  |
| `errors[].errorLevel` | Enum | WARNING: AGV is ready to start (e.g., maintenance cycle expiration warning). FATAL: AGV is not in running condition, user intervention required (e.g., laser scanner is contaminated). | WARNING, FATAL |  |
| `information` | Array | Array of info-objects. An empty array indicates, that the AGV has no information. This should only be used for visualization or debugging – it must not be used for logic in master control. |  |  |
| `information[].infoType` | String | Type/name of information. |  |  |
| `information[].infoReferences` | Array | No description available. |  |  |
| `information[].infoReferences[].referenceKey` | String | References the type of reference (e.g., headerId, orderId, actionId, etc.). |  |  |
| `information[].infoReferences[].referenceValue` | String | References the value, which belongs to the reference key. |  |  |
| `information[].infoDescription` | String | Info of description. |  |  |
| `information[].infoLevel` | Enum | DEBUG: used for debugging. INFO: used for visualization. | INFO, DEBUG |  |
| `safetyState` | Object | Contains all safety-related information. |  |  |
| `safetyState.eStop` | Enum | Acknowledge-Type of eStop: AUTOACK: auto-acknowledgeable e-stop is activated, e.g., by bumper or protective field. MANUAL: e-stop hast to be acknowledged manually at the vehicle. REMOTE: facility e-stop has to be acknowledged remotely. NONE: no e-stop activated. | AUTOACK, MANUAL, REMOTE, NONE |  |
| `safetyState.fieldViolation` | Boolean | Protective field violation. True: field is violated. False: field is not violated. |  |  |