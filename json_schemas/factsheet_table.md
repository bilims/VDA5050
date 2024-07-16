| **Field** | **Type** | **Description** | **Predefined Values** | **Example Value** |
|-----------|----------|-----------------|----------------------|-------------------|
| `seriesName` | String | Free text generalized series name as specified by manufacturer |  |  |
| `seriesDescription` | String | Free text human readable description of the AGV type series |  |  |
| `agvKinematic` | Enum | simplified description of AGV kinematics-type. | DIFF, OMNI, THREEWHEEL |  |
| `agvClass` | Enum | Simplified description of AGV class. | FORKLIFT, CONVEYOR, TUGGER, CARRIER |  |
| `maxLoadMass` | Number | maximum loadable mass |  |  |
| `localizationTypes` | Array | simplified description of localization type |  |  |
| `navigationTypes` | Array | List of path planning types supported by the AGV, sorted by priority |  |  |
| `speedMin` | Number | minimal controlled continuous speed of the AGV |  |  |
| `speedMax` | Number | maximum speed of the AGV |  |  |
| `accelerationMax` | Number | maximum acceleration with maximum load |  |  |
| `decelerationMax` | Number | maximum deceleration with maximum load |  |  |
| `heightMin` | Number | minimum height of AGV |  |  |
| `heightMax` | Number | maximum height of AGV |  |  |
| `width` | Number | width of AGV |  |  |
| `length` | Number | length of AGV |  |  |
| `maxStringLens` | Object | maximum lengths of strings |  |  |
| `maxStringLens.msgLen` | Integer | maximum MQTT Message length |  |  |
| `maxStringLens.topicSerialLen` | Integer | maximum length of serial-number part in MQTT-topics. Affected Parameters: order.serialNumber, instantActions.serialNumber, state.SerialNumber, visualization.serialNumber, connection.serialNumber |  |  |
| `maxStringLens.topicElemLen` | Integer | maximum length of all other parts in MQTT-topics. Affected parameters: order.timestamp, order.version, order.manufacturer, instantActions.timestamp, instantActions.version, instantActions.manufacturer, state.timestamp, state.version, state.manufacturer, visualization.timestamp, visualization.version, visualization.manufacturer, connection.timestamp, connection.version, connection.manufacturer |  |  |
| `maxStringLens.idLen` | Integer | maximum length of ID-Strings. Affected parameters: order.orderId, order.zoneSetId, node.nodeId, nodePosition.mapId, action.actionId, edge.edgeId, edge.startNodeId, edge.endNodeId |  |  |
| `maxStringLens.idNumericalOnly` | Boolean | If true ID-strings need to contain numerical values only |  |  |
| `maxStringLens.enumLen` | Integer | maximum length of ENUM- and Key-Strings. Affected parameters: action.actionType, action.blockingType, edge.direction, actionParameter.key, state.operatingMode, load.loadPosition, load.loadType, actionState.actionStatus, error.errorType, error.errorLevel, errorReference.referenceKey, info.infoType, info.infoLevel, safetyState.eStop, connection.connectionState |  |  |
| `maxStringLens.loadIdLen` | Integer | maximum length of loadId Strings |  |  |
| `maxArrayLens` | Object | maximum lengths of arrays |  |  |
| `timing` | Object | timing information |  |  |
| `timing.minOrderInterval` | Number | minimum interval sending order messages to the AGV |  |  |
| `timing.minStateInterval` | Number | minimum interval for sending state-messages |  |  |
| `timing.defaultStateInterval` | Number | default interval for sending state-messages if not defined, the default value from the main document is used |  |  |
| `timing.visualizationInterval` | Number | default interval for sending messages on visualization topic |  |  |
| `optionalParameters` | Array | list of supported and/or required optional parameters. Optional parameters, that are not listed here, are assumed to be not supported by the AGV. |  |  |
| `optionalParameters[].parameter` | String | full name of optional parameter, e.g. “order.nodes.nodePosition.allowedDeviationTheta” |  |  |
| `optionalParameters[].support` | Enum | type of support for the optional parameter, the following values are possible: SUPPORTED: optional parameter is supported like specified. REQUIRED: optional parameter is required for proper AGV-operation. | SUPPORTED, REQUIRED |  |
| `optionalParameters[].description` | String | free text. Description of optional parameter. E.g. Reason, why the optional parameter ‚direction‘ is necessary for this AGV-type and which values it can contain. The parameter ‘nodeMarker’ must contain unsigned interger-numbers only. Nurbs-Support is limited to straight lines and circle segments. |  |  |
| `agvActions` | Array | list of all actions with parameters supported by this AGV. This includes standard actions specified in VDA5050 and manufacturer-specific actions |  |  |
| `agvActions[].actionType` | String | unique actionType corresponding to action.actionType |  |  |
| `agvActions[].actionDescription` | String | free text: description of the action |  |  |
| `agvActions[].actionScopes` | Array | list of allowed scopes for using this action-type. INSTANT: usable as instantAction, NODE: usable on nodes, EDGE: usable on edges. |  |  |
| `agvActions[].actionParameters` | Array | list of parameters. if not defined, the action has no parameters |  |  |
| `agvActions[].actionParameters[].key` | String | key-String for Parameter |  |  |
| `agvActions[].actionParameters[].valueDataType` | Enum | data type of Value, possible data types are: BOOL, NUMBER, INTEGER, FLOAT, STRING, OBJECT, ARRAY | BOOL, NUMBER, INTEGER, FLOAT, STRING, OBJECT, ARRAY |  |
| `agvActions[].actionParameters[].description` | String | free text: description of the parameter |  |  |
| `agvActions[].actionParameters[].isOptional` | Boolean | True: optional parameter |  |  |
| `agvActions[].resultDescription` | String | free text: description of the resultDescription |  |  |
| `wheelDefinitions` | Array | list of wheels, containing wheel-arrangement and geometry |  |  |
| `wheelDefinitions[].type` | Enum | wheel type. DRIVE, CASTER, FIXED, MECANUM | DRIVE, CASTER, FIXED, MECANUM |  |
| `wheelDefinitions[].isActiveDriven` | Boolean | True: wheel is actively driven (de: angetrieben) |  |  |
| `wheelDefinitions[].isActiveSteered` | Boolean | True: wheel is actively steered (de: aktiv gelenkt) |  |  |
| `wheelDefinitions[].position` | Object | No description available. |  |  |
| `wheelDefinitions[].position.x` | Number | [m] x-position in AGV-coordinate system |  |  |
| `wheelDefinitions[].position.y` | Number | y-position in AGV-coordinate system |  |  |
| `wheelDefinitions[].position.theta` | Number | orientation of wheel in AGV-coordinate system Necessary for fixed wheels |  |  |
| `wheelDefinitions[].diameter` | Number | nominal diameter of wheel |  |  |
| `wheelDefinitions[].width` | Number | nominal width of wheel |  |  |
| `wheelDefinitions[].centerDisplacement` | Number | nominal displacement of the wheel’s center to the rotation point (necessary for caster wheels). If the parameter is not defined, it is assumed to be 0 |  |  |
| `wheelDefinitions[].constraints` | String | free text: can be used by the manufacturer to define constraints |  |  |
| `envelopes2d` | Array | No description available. |  |  |
| `envelopes2d[].set` | String | name of the envelope curve set |  |  |
| `envelopes2d[].polygonPoints` | Array | envelope curve as a x/y-polygon polygon is assumed as closed and must be non-self-intersecting |  |  |
| `envelopes2d[].polygonPoints[].x` | Number | x-position of polygon-point |  |  |
| `envelopes2d[].polygonPoints[].y` | Number |  y-position of polygon-point |  |  |
| `envelopes2d[].description` | String | free text: description of envelope curve set |  |  |
| `envelopes3d` | Array | list of AGV-envelope curves in 3D (german: „Hüllkurven“) |  |  |
| `envelopes3d[].set` | String | name of the envelope curve set |  |  |
| `envelopes3d[].format` | String | format of data e.g. DXF |  |  |
| `envelopes3d[].data` | Object | 3D-envelope curve data, format specified in ‚format‘ |  |  |
| `envelopes3d[].url` | String | protocol and url-definition for downloading the 3D-envelope curve data e.g. ftp://xxx.yyy.com/ac4dgvhoif5tghji |  |  |
| `envelopes3d[].description` | Integer | free text: description of envelope curve set |  |  |
| `loadPositions` | Array | list of load positions / load handling devices. This lists contains the valid values for the oarameter “state.loads[].loadPosition” and for the action parameter “lhd” of the actions pick and drop. If this list doesn’t exist or is empty, the AGV has no load handling device. |  |  |
| `loadSets` | Array | list of load-sets that can be handled by the AGV |  |  |
| `loadSets[].setName` | String | Unique name of the load set, e.g. DEFAULT, SET1, ... |  |  |
| `loadSets[].loadType` | String | type of load e.g. EPAL, XLT1200, …. |  |  |
| `loadSets[].loadPositions` | Array | list of load positions btw. load handling devices, this load-set is valid for. If this parameter does not exist or is empty, this load-set is valid for all load handling devices on this AGV. |  |  |
| `loadSets[].boundingBoxReference` | Object | bounding box reference as defined in parameter loads[] in state-message |  |  |
| `loadSets[].boundingBoxReference.x` | Number | x-coordinate of the point of reference. |  |  |
| `loadSets[].boundingBoxReference.y` | Number | y-coordinate of the point of reference. |  |  |
| `loadSets[].boundingBoxReference.z` | Number | z-coordinate of the point of reference. |  |  |
| `loadSets[].boundingBoxReference.theta` | Integer | Orientation of the loads bounding box. Important for tugger trains, etc. |  |  |
| `loadSets[].loadDimensions` | Object | No description available. |  |  |
| `loadSets[].loadDimensions.length` | Number | Absolute length of the load´s bounding box. |  |  |
| `loadSets[].loadDimensions.width` | Number | Absolute width of the load´s bounding bo |  |  |
| `loadSets[].loadDimensions.height` | Number | Absolute height of the load´s bounding box. Optional: Set value only if known. |  |  |
| `loadSets[].maxWeigth` | Number | maximum weight of loadtype |  |  |
| `loadSets[].minLoadhandlingHeight` | Number | minimum allowed height for handling of this load-type and –weight. References to boundingBoxReference |  |  |
| `loadSets[].maxLoadhandlingHeight` | Number | maximum allowed height for handling of this load-type and –weight. references to boundingBoxReference |  |  |
| `loadSets[].minLoadhandlingDepth` | Number | minimum allowed depth for this load-type and –weight. references to boundingBoxReference |  |  |
| `loadSets[].maxLoadhandlingDepth` | Number | maximum allowed depth for this load-type and –weight. references to boundingBoxReference |  |  |
| `loadSets[].minLoadhandlingTilt` | Number | minimum allowed tilt for this load-type and –weight |  |  |
| `loadSets[].maxLoadhandlingTilt` | Number | maximum allowed tilt for this load-type and –weight |  |  |
| `loadSets[].agvSpeedLimit` | Number | maximum allowed speed for this load-type and –weight |  |  |
| `loadSets[].agvAccelerationLimit` | Number | maximum allowed acceleration for this load-type and –weight |  |  |
| `loadSets[].agvDecelerationLimit` | Number | maximum allowed deceleration for this load-type and –weight |  |  |
| `loadSets[].pickTime` | Number | approx. time for picking up the load |  |  |
| `loadSets[].dropTime` | Number | approx. time for dropping the load |  |  |
| `loadSets[].description` | Number | free text description of the load handling set |  |  |