# Research Notes: Ch7 Reinforcement Learning — Sections 5–7

## Sources Used
- Hurbans (2020) Ch.10 "Reinforcement learning with Q-learning", pp. 323–349 — bib key: `hurbansGrokkingArtificialIntelligence2020`
- Barber (2012) Ch.1 "Probabilistic Reasoning" pp. 7–24, Ch.2 "Basic Graph Concepts" pp. 25–32, Ch.3 "Belief Networks" pp. 33–56 — bib key: `barberBayesianReasoningMachine2012`
- Ness (2025) Causal AI — bib key: `nessCausalAI2025`
- Downey (2016) Think Bayes — bib key: `downeyThinkBayes2016`

## New bib entries added to references.bib:
- `suttonReinforcementLearningIntroduction2018` — Sutton & Barto, RL: An Introduction, 2nd ed., MIT Press 2018
- `pearlCausalityModelsReasoning2009` — Pearl, Causality: Models, Reasoning and Inference, 2nd ed., CUP 2009
- `pearlBookWhyNew2018` — Pearl & Mackenzie, The Book of Why, Basic Books 2018
- `pearlCausalInferenceStatistics2016` — Pearl, Glymour, Jewell, Causal Inference in Statistics: A Primer, Wiley 2016
- `hernanCausalInferenceWhat2020` — Hernán & Robins, Causal Inference: What If, CRC Press 2020

---

## Section 5: RL Approaches

### 5.1 Model-Free Learning
- **Definition**: Agent learns solely through trial-and-error interactions with environment; no internal model of dynamics
- **Q-learning** (Watkins, 1989): off-policy TD control; learns Q(s,a) = expected cumulative reward
  - Update rule (Bellman-based):
    Q(s,a) ← (1-α)Q(s,a) + α[r + γ · max_{a'} Q(s',a')]
  - α = learning rate, γ = discount factor, r = reward
  - Q-table: rows=states, columns=actions; initialized to 0
- **SARSA**: on-policy TD; updates using the action actually taken: Q(s,a) ← Q(s,a) + α[r + γQ(s',a') - Q(s,a)]
- **REINFORCE** (policy gradient): Monte Carlo; gradient ∇_θ J(θ) = E[∇_θ log π_θ(a|s) · G_t] where G_t is return
- Source: Hurbans pp. 335–349, Sutton & Barto Ch. 6–13

### 5.2 Model-Based Learning
- **Definition**: Agent builds/uses an internal model M(s,a) = (s', r) of environment dynamics; can plan ahead without executing
- **Dyna-Q**: Combines Q-learning with a learned model; uses simulated experience from model + real experience
- **World models**: Generative model of environment; agent plans inside latent world model (Ha & Schmidhuber 2018)
- **Model Predictive Control (MPC)**: Plans over finite horizon using model; re-plans at each step
- Key tradeoff: model-based is sample-efficient but errors in model compound; model-free is robust but data-hungry
- Source: Hurbans p. 348, Sutton & Barto Ch. 8

### 5.3 Exploration vs Exploitation
- **Exploration**: Try new actions to discover better rewards
- **Exploitation**: Use known best action to maximize current reward
- **ε-greedy**: With prob ε select random action; otherwise select argmax Q(s,a). Simple but effective
- **UCB (Upper Confidence Bound)**: a* = argmax[Q(s,a) + c√(ln t / N(s,a))]; automatically trades off exploration based on uncertainty
- **Curiosity-driven exploration**: Intrinsic reward = prediction error of a learned forward model; agent curious about novel states
- **Decay schedules**: ε decays from 1.0 to 0.01 over training; balances early exploration / late exploitation
- Source: Hurbans pp. 338–339 (chance of random move), Sutton & Barto Ch. 2

---

## Section 6: Inference and Causality

### 6.1 Statistical Inference

#### Bayesian Inference
- Bayes' theorem: p(θ|D) = p(D|θ)p(θ) / p(D)
  - Posterior ∝ Likelihood × Prior
  - p(D) = ∫ p(D|θ)p(θ) dθ (normalizing constant / evidence)
- MAP estimate: θ_MAP = argmax_θ p(θ|D)
- Bayesian updating: posterior of today = prior of tomorrow (sequential)
- Distinction: frequentist = θ is fixed unknown; Bayesian = θ has a distribution
- Source: Barber pp. 14–19

#### Bayesian Networks
- A BN is a DAG where each node is a RV with a conditional probability table (CPT): p(x_i | pa(x_i))
- Joint distribution factorizes: p(x_1,...,x_D) = ∏_i p(x_i | pa(x_i))
- Example: Wet grass network — R, S → T, R → J; p(T,J,R,S) = p(T|R,S)p(J|R)p(R)p(S)
- CPTs encode conditional independence; reduces exponential storage to linear
- "Explaining away": conditioning on a common effect makes independent causes dependent
- Source: Barber pp. 33–40

#### Probabilistic Modelling
- Probabilistic model: specifies joint distribution over variables of interest
- Forward model / generative model: samples data from p(D|θ)
- Inference: given observations, compute posterior over latent variables
- Key challenge: intractable normalization (marginalizing over all parameters)
- Source: Barber Ch. 1, Downey Think Bayes

### 6.2 Introduction to Causality

#### Correlation vs Causation
- Correlation: statistical association; X and Y move together
- Causation: X directly influences Y; changing X forces change in Y
- Classic confusion: ice cream sales and drownings are correlated (both driven by summer/temperature confounder)
- "Correlation does not imply causation" — but we can test for it with proper tools

#### Granger Causality
- Time-series based: X Granger-causes Y if past X improves prediction of Y beyond past Y alone
- Limitation: purely predictive, not structural — captures temporal precedence, not mechanism
- Source: context, Ness 2025

#### Directed Acyclic Graphs (DAGs)
- DAG: nodes = variables, directed edges = direct causal influence, no cycles
- Ancestral order: parents always come before children (corresponds to temporal order in causal models)
- Enables reading conditional independence statements directly from graph structure
- Source: Barber pp. 25–27, 40

#### Elements of Causal Graphs: Collider, Chain, Fork
- **Fork**: A ← C → B; C is common cause; A and B correlated but independent given C
- **Chain**: A → C → B; C mediates; A and B dependent unconditionally; independent given C
- **Collider**: A → C ← B; C is common effect; A and B independent unconditionally; dependent given C ("explaining away")
- Conditioning on a collider or its descendant opens a blocked path (creates spurious association)
- Source: Barber pp. 43–45

#### D-Separation
- Formal criterion for reading conditional independence from DAG structure
- Path U between X and Y is *blocked* by Z if:
  1. A non-collider w on U is in Z (blocks the path), OR
  2. A collider w on U is NOT in Z and no descendant of w is in Z
- X and Y are d-separated by Z if ALL paths between them are blocked → X ⊥⊥ Y | Z
- d-separation implies conditional independence in any consistent distribution
- Source: Barber pp. 45–46

### 6.3 Interventions

#### Seeing vs Doing
- Observational inference: p(Y|X=x) — conditioning on seeing X=x
- Interventional inference: p(Y|do(X=x)) — setting X=x by external intervention
- Intervening on X cuts all incoming arrows to X in the DAG (surgical removal of parental links)
- The do-operator makes the difference explicit: p(Y|X=x) ≠ p(Y|do(X=x)) when confounders exist
- Source: Barber pp. 50–51, Pearl 2009

#### Confounders & Counterfactuals
- Confounder: variable that causally affects both treatment X and outcome Y
- Omitting confounders from analysis creates spurious causal claims
- Counterfactual: "What would Y have been if X had been x, given that we actually observed X=x'?"
- Counterfactuals require the structural causal model (SCM); not identifiable from observations alone without assumptions
- Source: Pearl 2009, Ness 2025

#### Causal Inference vs RCTs
- RCT (Randomized Controlled Trial): randomly assign treatment; breaks confounder-treatment link; gold standard
- Random assignment ≡ intervening (do operator); p(Y|do(X)) = p(Y|X) in an RCT
- Observational causal inference: estimate causal effects without randomization using DAG structure + adjustment
- Source: Barber p. 50, Hernan & Robins 2020

### 6.4 Do-Calculus

#### Front- and Backdoor Criterion
- **Backdoor criterion**: Set Z blocks all "backdoor paths" (confounding paths into treatment X)
  - Backdoor path: any path from X to Y with an arrow INTO X
  - If Z satisfies backdoor: p(Y|do(X)) = Σ_z p(Y|X,Z) · p(Z)  [adjustment formula]
- **Front-door criterion**: Used when all confounders are unobserved but a mediator M is observed
  - p(Y|do(X)) = Σ_m p(M|X) · Σ_x' p(Y|M,X') · p(X')
- Source: Pearl 2009, Ness 2025

#### Three Rules of Do-Calculus (Pearl)
- Provide complete calculus for deriving causal effects from observational data + DAG
- Rule 1: Insertion/deletion of observations: p(Y|do(X),Z,W) = p(Y|do(X),W) if (Y ⊥⊥ Z | X,W) in modified graph
- Rule 2: Action/observation exchange: p(Y|do(X),do(Z),W) = p(Y|do(X),Z,W) if (Y ⊥⊥ Z | X,W) in graph where arrows into Z are removed
- Rule 3: Insertion/deletion of actions: p(Y|do(X),do(Z),W) = p(Y|do(X),W) if (Y ⊥⊥ Z | X,W) in graph where Z and its non-ancestors' arrows removed
- Together they are sound and complete for identifying any causal query
- Source: Pearl 2009, Ness 2025

### 6.5 Fallacies

#### Mediation Fallacy
- Adjusting for a mediator M on the causal path X → M → Y blocks the causal effect of interest
- Direct effect (X→Y) and indirect effect (X→M→Y) must be distinguished
- Controlling for mediator gives neither total effect nor direct effect correctly

#### Collider Bias (Berkson's Paradox)
- Conditioning on a collider variable creates spurious correlation between its parents
- **Berkson's Paradox** (1946): In hospital data, two independent diseases appear negatively correlated because hospitalization is a collider
- Example: A → Hospitalized ← B; conditioning on hospitalized makes A and B appear correlated

#### Simpson's Paradox
- Aggregated data shows opposite trend to every subgroup
- Classic example (Barber p. 49, table 3.1): Drug appears helpful in combined data but harmful in each subgroup (male/female)
- Resolution: Ask causal question. p(R|D) ≠ p(R|do(D)); need to condition on the confounder (gender)
- The aggregated result mixes observational and interventional reasoning
- Source: Barber pp. 49–50

#### Missing Value Imputation: Causal vs Data-Driven
- Data-driven: impute mean, median, or model-based prediction — treats missingness as random
- Causal view: missingness mechanism must be modeled; MCAR/MAR/MNAR distinctions matter
- Imputing collider descendants can introduce bias; must understand why data is missing
- Source: Ness 2025, Pearl 2009

---

## Section 7: Further Reading
References for the chapter:
- Sutton & Barto: `suttonReinforcementLearningIntroduction2018`
- Hurbans: `hurbansGrokkingArtificialIntelligence2020`
- Barber: `barberBayesianReasoningMachine2012`
- Pearl Causality: `pearlCausalityModelsReasoning2009`
- Pearl Book of Why: `pearlBookWhyNew2018`
- Pearl Primer: `pearlCausalInferenceStatistics2016`
- Hernan & Robins: `hernanCausalInferenceWhat2020`
- Ness: `nessCausalAI2025`
- Downey Think Bayes: `downeyThinkBayes2016`
