# Research Notes: Chapter 15 — Multi-Agent Systems

**Date**: 2026-03-14
**Agent**: Research+Writer (Sonnet 4.6)

---

## Sources Consulted

### Bibliography entries used
| BibTeX key | Resource | Used for |
|---|---|---|
| `wooldridgeIntroductionMultiAgentSystems2009` | Wooldridge, An Introduction to MultiAgent Systems, 2nd ed., Wiley 2009 | All foundational topics: agent definition, BDI, environment types, reactive/deliberative/hybrid agents, communication, coordination, negotiation, game theory |
| `weissMultiagentSystems2013` | Weiss, Multiagent Systems, MIT Press 2013 | MAS overview, coordination mechanisms, MARL, blackboard systems |
| `shohamMultiagentSystemsAlgorithmic2009` | Shoham & Leyton-Brown, Multiagent Systems, Cambridge 2009 | Game theory, Nash equilibrium, Shapley value, auctions, mechanism design, social choice |
| `bellifeministeDevelopingMultiAgentSystems2007` | Bellifemine et al., Developing MAS with JADE, Wiley 2007 | FIPA standards, JADE, interaction protocols, message structure |
| `bordiniMultiAgentProgramming2009` | Bordini et al., Multi-Agent Programming, Springer 2009 | BDI/AgentSpeak; Further Reading only |
| `paolucciAgentBasedManufacturing2005` | Paolucci & Sacile, Agent-Based Manufacturing, CRC 2005 | Holonic manufacturing, JADE in CPS, scheduling agents |
| `talukdarASYNCHRONOUSTEAMSCOOPERATION` | Talukdar et al., ASYNCHRONOUS TEAMS paper | A-Teams cooperative architecture |
| `suttonReinforcementLearningIntroduction2018` | Sutton & Barto, RL Introduction 2018 | MARL non-stationarity, policy gradient extension |
| `chopraSupplyChainManagement2019` | Chopra & Meindl, Supply Chain Management, Pearson 2019 | Supply chain coordination context |
| `panJobShopSchedulingRL2021` | Zhao et al., Deep RL for Dynamic VRP, 2021 | RL-based scheduling reference |
| `lanhamAIAgentsAction2025` | Lanham, AI Agents in Action, Manning 2025 | Modern LLM-based multi-agent frameworks; Further Reading |

### New bibliography entries added
Six new entries were added to `bibliography/references.bib` at the top of the file:
- `weissMultiagentSystems2013`
- `shohamMultiagentSystemsAlgorithmic2009`
- `bellifeministeDevelopingMultiAgentSystems2007`
- `bordiniMultiAgentProgramming2009`
- `wooldridgeIntroductionMultiAgentSystems2009`
- `paolucciAgentBasedManufacturing2005`

---

## Key Concepts Extracted

### Agent Definition (RAPS framework)
- Reactivity, Autonomy, Proactivity, Social ability (Wooldridge 2009, p. 28)
- Environment taxonomy: observable/deterministic/episodic/static/discrete

### BDI Architecture
- Beliefs (knowledge), Desires (motivational states), Intentions (committed goals)
- Practical implementations: AgentSpeak, Jason
- Deliberation: desire-to-intention selection then plan generation then execution

### FIPA Standards
- FIPA-ACL performatives: inform, request, propose, agree, refuse, query-if
- Platform services: AMS, DF, MTS
- Interaction protocols: Request, Contract Net, auctions

### Agent Type Taxonomy
- Deliberative: symbolic world model + planner (STRIPS/PDDL)
- Reactive: subsumption architecture (Brooks) — stimulus-response, no model
- Hybrid: TouringMachines (3 concurrent layers), InteRRaP (3 vertical layers)

### Communication
- Speech act theory: locution, illocution, perlocution
- FIPA-ACL message fields: performative, sender, receiver, content, language, ontology, conversation-id
- Ontologies: RDF triples, OWL class hierarchies, ontology alignment tools

### Coordination
- Task sharing vs result sharing
- Blackboard systems: KS agents + blackboard + scheduler
- A-Teams (Talukdar): asynchronous, indirect communication via shared solution pool
- Commitment protocols, Partial Global Planning

### Negotiation
- Monotonic Concession Protocol (Zeuthen): both agents concede toward agreement
- Argumentation: threats, rewards, precedent, self-interest appeals

### Game Theory
- Normal-form games: N, A_i, u_i
- Nash Equilibrium: no unilateral deviation improves payoff
- Dominant strategies: best action regardless of others
- Pareto optimality: no reallocation makes everyone better
- Social choice: plurality, Borda, Condorcet, approval voting; Arrow's impossibility
- Shapley value formula for fair coalition payoff distribution
- Auction types: English, Dutch, first-price, Vickrey (second-price)
- Mechanism design: VCG for efficiency + incentive compatibility

### MARL
- Non-stationarity: each agent's learning changes others' environment
- IQL: independent Q-learners; simple but non-convergent
- CTDE paradigm: centralised training, decentralised execution
- QMIX: value decomposition with monotone mixing network; IGM principle
- MADDPG: centralised critic, decentralised actor, DDPG base
- MAPPO: PPO in CTDE framework; strong on cooperative SMAC benchmark
- AlphaStar: league training, transformer memory, pointer networks
- Applications: warehouse robots, traffic signal control, multi-UAV, energy grid

### Industry Applications
- Supply chain: bullwhip effect mitigation via shared demand signals
- Job-shop scheduling: job/machine/supervisor agent hierarchy; RL-based scheduling
- JADE: FIPA-compliant Java middleware for industrial deployment
- Holonic Manufacturing: order/resource/product holons, plug-and-produce reconfigurability
