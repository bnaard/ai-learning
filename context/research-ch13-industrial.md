# Research Notes: Chapter 13 — Industrial AI

**Date**: 2026-03-14
**Agent**: Research+Writer (Sonnet)

## Sources Used

No primary PDFs available for this chapter. Content drawn from general knowledge with reference to cited literature listed in the chapter. All key claims are grounded in the bibliography entries added to `references.bib`.

## Key Concepts Researched

### Section 1: Industry 4.0 and the Smart Factory
- Industry 4.0 four revolutions framework; strategic goals (flexibility, efficiency, mass customisation)
- CPS definition (Dafflon et al. 2021, Singh et al. 2021): sensing → network → cognitive → actuating layers
- Digital twin maturity levels: digital model / shadow / twin (Tao et al. 2019)
- IIoT characteristics vs consumer IoT: deterministic latency, reliability, security (Mahmood 2019)
- OPC UA: architecture, information model, security features (Veneri & Capasso 2018)
- Manufacturing ontologies (ISO 15926, MASON); semantic interoperability and autonomous cooperation

### Section 2: AI for Manufacturing
- Maintenance strategies: reactive → preventive → predictive; 30% cost reduction claim
- Condition monitoring: vibration/temperature/current signals; threshold, SPC, deep learning approaches
- RUL estimation: LSTM, TCN, Gaussian Process; NASA C-MAPSS benchmark
- SPC: control charts, Shewhart/CUSUM/EWMA; Cp/Cpk process capability
- AOI pipeline: image acquisition → CNN → pass/fail; ResNet, EfficientNet approaches
- Few-shot and anomaly detection (PatchCore, PADIM) for industrial inspection
- Topology optimisation: SIMP formulation, density-based, additive manufacturing connection
- Generative design: AI-driven exploration, surrogate FEA models, Autodesk Fusion 360
- JSS: NP-hard for n≥2, m≥3; priority dispatch rules, DRL with GNN state representation

### Section 3: Industrial Automation
- DES fundamentals (Cassandras & Lafortune 2009): event-driven state changes
- DFA 5-tuple: Q, Σ, δ, q0, Qm; generated and marked languages
- NFA: ε-transitions; subset construction (Rabin's theorem); exponential blowup
- Petri net 5-tuple: P, T, F, W, M0; enabling condition; firing rule
- Petri net properties: reachability (EXPSPACE-hard), boundedness, liveness, conservativeness
- Timed automata: clock guards; region graph decidability
- Stochastic Petri nets → CTMC; M/M/1 queue formula
- DES simulation: event-scheduling paradigm; FEL; AnyLogic/Arena/Plant Simulation
- Ramadge-Wonham SCT: controllable vs uncontrollable events; supremal controllable sublanguage; TCT/SUPREMICA tools
- SCADA/PLC/DCS/MES hierarchy (Manesis & Nikolakopoulos 2020)
- Fault diagnosis: diagnoser automaton; data-driven classifier alternative
- Distributed supervision: modular SCT; decentralised diagnosis challenges

### Section 4: Robotics
- Robot taxonomy: articulated, SCARA, delta, Cartesian (Siciliano et al. 2009)
- Cobots: ISO/TS 15066; force/torque sensing; safety modes
- AGV vs AMR distinction
- DH parameters: 4 parameters (a, α, d, θ); homogeneous transformation product
- Forward kinematics: product of DH transforms
- Inverse kinematics: closed-form for spherical wrist; Jacobian pseudoinverse for iterative
- Path vs trajectory planning; joint-space splines vs Cartesian interpolation
- RRT algorithm steps; RRT* for optimality
- A* with f(n) = g(n) + h(n); admissible + consistent heuristic
- ROS: node/topic/service/action abstractions; ROS 2 / DDS for real-time
- Sensor fusion: wheel odometry, IMU, LiDAR, camera; EKF/particle filter
- SLAM as factor graph optimisation (g2o, GTSAM)
- Behavior-based robotics: subsumption; behavior trees as modern alternative

### Section 5: Supply Chain
- Demand forecasting: ARIMA, LightGBM, TFT; MAPE and quantile loss metrics
- EOQ formula: Q* = sqrt(2DS/H); newsvendor model; RL multi-echelon extensions
- VRP as TSP generalisation; branch-and-price, LNS, ACO, Pointer Networks / Attention Models

## Bibliography Entries Added

The following new entries were added to `bibliography/references.bib`:
- `manesissIntroductionIndustrialAutomation2020`
- `cassandrasIntroductionDiscreteEvent2009`
- `sicilianoRobotics2009`
- `sicilianoSpringerHandbookRobotics2016`
- `reisigUnderstandingPetriNets2013`
- `benariElementsRobotics2017`
- `linzIntroductionFormalLanguages2006`
- `mahmoodInternetThingsIndustrial2019`
- `veneriHandsOnIndustrialInternet2018`
- `dafflonChallengesApproachesCPS2021`
- `singhEmergenceCyberPhysical2021`
- `leeSurveyPredictiveMaintenance2019`
- `zhaoDeepLearningFault2019`
- `laviollaCNNDefectDetection2019`
- `sigristTopologyOptimizationReview2021`
- `panJobShopSchedulingRL2021`
- `bocewiczDigitalTwinManufacturing2021` (Tao et al.)
- `liuSupervisoryControlTheory2019` (Wonham & Cai)
- `karrasRRTPathPlanning2020` (LaValle & Kuffner)
- `astarPathPlanning1968` (Hart, Nilsson & Raphael)

## Notes on Scope Decisions
- Chapter 14 covers supply chain and business analytics in depth; Ch13 Section 5 is intentionally brief
- Dynamics section from original outline omitted (Lagrange/Newton formulations) to keep chapter concise; kinematics is sufficient background
- Timed models section consolidated into one card covering timed automata, stochastic Petri nets, and queuing theory
