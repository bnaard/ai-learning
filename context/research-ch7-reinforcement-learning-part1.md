# Research Notes: Chapter 7 — Reinforcement Learning, Sections 1–4

**Date**: 2026-03-13
**Sources**: Hurbans (2020) Ch.10 (PDF pp. 323–375), Barber (2012) Ch.7 (PDF pp. 139–165)
**BibTeX keys**: `hurbansGrokkingArtificialIntelligence2020`, `barberBayesianReasoningMachine2012`

---

## Section 1: Introduction to Reinforcement Learning

### What is RL?
- RL is a paradigm where an **agent** learns by **interacting with an environment** and receiving feedback in the form of **rewards** or **penalties**
- Unlike supervised learning (labelled data) or unsupervised learning (structure discovery), RL learns through **trial and error**
- The goal: find a policy that maximises cumulative future reward
- Hurbans frames RL as "goal-directed learning from interaction" — the agent is not told what actions to take but discovers which actions yield the most reward

### The Reward Hypothesis
- All goals can be described as maximising a scalar signal called reward
- This is a fundamental assumption of RL; all agent objectives are encoded in the reward function
- Reward can be immediate or delayed — the agent must balance short-term vs long-term gain

### Agent–Environment Interaction
- At each timestep t:
  - Agent observes **state** s_t
  - Agent takes **action** a_t
  - Environment transitions to **next state** s_{t+1}
  - Environment emits **reward** r_{t+1}
- This loop continues until a terminal state or indefinitely
- The interaction forms a **trajectory**: s_0, a_0, r_1, s_1, a_1, r_2, ...

### Core Components
- **Agent**: The learner/decision-maker
- **Environment**: Everything external to the agent
- **State (s)**: A representation of the current situation
- **Action (a)**: A choice made by the agent
- **Reward (r)**: Scalar feedback from the environment
- **Policy (π)**: Mapping from states to actions (or probability distributions over actions)
- **Value function V(s)**: Expected cumulative future reward from state s
- **Model**: Agent's internal representation of environment dynamics (optional — model-free vs model-based)

### RL vs Supervised/Unsupervised Learning
| Aspect | Supervised | Unsupervised | Reinforcement |
|--------|-----------|--------------|---------------|
| Data | Labelled | Unlabelled | Interactions |
| Feedback | Immediate correct answer | None | Delayed reward signal |
| Goal | Generalise from examples | Discover structure | Maximise cumulative reward |
| Exploration | Not needed | Not needed | Essential |

---

## Section 2: Markov Decision Processes (MDPs)

### Markov Property
- A state has the **Markov property** if the future is independent of the past given the present:
  P(s_{t+1} | s_t, a_t) = P(s_{t+1} | s_0, a_0, ..., s_t, a_t)
- "The present state contains all relevant history" — memoryless
- This simplification makes tractable solutions possible

### MDP Formal Definition
- MDP = (S, A, P, R, γ) where:
  - S: finite set of states
  - A: finite set of actions
  - P(s'|s,a): transition probability function
  - R(s,a): expected reward for taking action a in state s
  - γ ∈ [0,1]: discount factor

### Discount Factor γ
- Controls preference for immediate vs future rewards
- γ = 0: myopic (only immediate reward matters)
- γ = 1: far-sighted (all future rewards equally weighted)
- Practical values: γ = 0.9 to 0.99
- Also ensures convergence for infinite-horizon problems

### Cumulative Discounted Return
- G_t = r_{t+1} + γ·r_{t+2} + γ²·r_{t+3} + ... = Σ_{k=0}^∞ γ^k · r_{t+k+1}
- The agent seeks to maximise E[G_t]

### Policy Types
- **Deterministic policy**: π(s) = a (one action per state)
- **Stochastic policy**: π(a|s) = P(A=a|S=s) (probability distribution over actions)
- **Optimal policy π***: maximises expected return from every state

### Value Functions
- **State-value function**: V^π(s) = E_π[G_t | S_t = s]
  - Expected return starting from state s, following policy π
- **Action-value function (Q-function)**: Q^π(s,a) = E_π[G_t | S_t = s, A_t = a]
  - Expected return starting from s, taking action a, then following π

### Bellman Equations
- **Bellman Expectation Equation** for V:
  V^π(s) = Σ_a π(a|s) · Σ_{s'} P(s'|s,a) · [R(s,a) + γ · V^π(s')]
- **Bellman Optimality Equation**:
  V*(s) = max_a Σ_{s'} P(s'|s,a) · [R(s,a) + γ · V*(s')]
  Q*(s,a) = Σ_{s'} P(s'|s,a) · [R(s,a) + γ · max_{a'} Q*(s',a')]

### Value Iteration
- Dynamic programming algorithm to find V*
- Initialise V(s) = 0 for all s
- Repeat until convergence: V(s) ← max_a Σ_{s'} P(s'|s,a) [R(s,a) + γ·V(s')]
- Extract policy: π*(s) = argmax_a Σ_{s'} P(s'|s,a) [R(s,a) + γ·V(s')]
- Guaranteed convergence (contraction mapping)

### MCMC (Markov Chain Monte Carlo)
- Uses Markov chains to sample from complex probability distributions
- **Metropolis-Hastings algorithm**:
  1. Start at state x
  2. Propose new state x' from proposal distribution q(x'|x)
  3. Accept with probability α = min(1, [p(x')·q(x|x')] / [p(x)·q(x'|x)])
  4. If rejected, stay at x
- Applications: Bayesian inference, sampling from posterior distributions

---

## Section 3: Bandit Problems

### Single-Arm Bandit
- Simplest RL setting: one action, one reward distribution
- Agent must estimate the expected reward μ via repeated pulls
- No state transitions — purely an estimation problem

### Multi-Arm Bandit
- k slot machines, each with unknown reward distribution
- Agent must balance **exploration** (trying new arms) vs **exploitation** (using best-known arm)
- Regret: R_T = T·μ* - Σ_{t=1}^T r_t (difference from always choosing best arm)

### Exploration Strategies

**ε-greedy**:
- With probability ε: choose random arm (explore)
- With probability 1-ε: choose arm with highest estimated reward (exploit)
- Simple, effective; ε usually decays over time
- Estimated reward: Q(a) ← Q(a) + (1/n)[r - Q(a)] (incremental mean update)

**Upper Confidence Bound (UCB)**:
- A_t = argmax_a [Q_t(a) + c · √(ln t / N_t(a))]
- Confidence bonus: arms tried less often get higher priority
- Optimistic in face of uncertainty: "try what you haven't explored enough"
- UCB1 is asymptotically optimal

**Thompson Sampling**:
- Bayesian approach: maintain prior distribution over reward parameters
- Sample from posterior, pick arm with highest sampled value
- Update posterior after observing reward
- For Bernoulli rewards: Beta(α, β) prior; update α or β based on success/failure
- Often outperforms ε-greedy and UCB in practice

---

## Section 4: Q-Learning and Deep RL

### Temporal Difference (TD) Learning
- Model-free: learns directly from experience, no environment model needed
- Updates value estimates before episode completion (unlike Monte Carlo)
- **TD(0) update**:
  V(s_t) ← V(s_t) + α[r_{t+1} + γ·V(s_{t+1}) - V(s_t)]
- TD error: δ_t = r_{t+1} + γ·V(s_{t+1}) - V(s_t)
- TD(λ): eligibility traces, bridges TD(0) and Monte Carlo

### SARSA (On-policy TD)
- Updates Q using the action actually taken: Q(s,a) ← Q(s,a) + α[r + γ·Q(s',a') - Q(s,a)]
- On-policy: learns about the current behaviour policy

### Q-Learning (Off-policy TD)
- **Watkins' Q-learning**:
  Q(s,a) ← Q(s,a) + α[r + γ·max_{a'}Q(s',a') - Q(s,a)]
- Off-policy: always updates using greedy max regardless of actual action taken
- Converges to Q* under standard conditions
- Separates behaviour policy (exploration) from target policy (greedy)

### Deep Q-Networks (DQN)
- Replace Q-table with deep neural network: Q(s,a;θ) ≈ Q*(s,a)
- Input: state representation (e.g., raw pixels for Atari)
- Output: Q-value for each action
- Breakthrough: Mnih et al. (2015) — human-level Atari performance

### Experience Replay
- Store transitions (s,a,r,s') in **replay buffer** D
- Sample random mini-batches to train network
- Benefits:
  1. Breaks temporal correlations between consecutive samples
  2. More sample-efficient (each transition used multiple times)
  3. Stabilises training

### Double Q-Learning
- Problem with standard Q-learning: **overestimation bias**
  - max operator uses same values for selection and evaluation
- Double DQN: use online network to select action, target network to evaluate it:
  target = r + γ · Q(s', argmax_{a'} Q(s',a';θ); θ-)
- Reduces overestimation, improves stability

### Sparse Rewards and Reward Shaping
- Many real problems have sparse rewards (only at task completion)
- Learning is extremely slow with sparse rewards
- Solutions:
  - **Reward shaping**: Add intermediate rewards (e.g., potential-based shaping)
  - **Intrinsic motivation**: Curiosity bonuses for novel states
  - **Curriculum learning**: Gradually increase task difficulty
  - **Hindsight Experience Replay (HER)**: Learn from failed episodes by relabelling goals

### Hierarchical Reinforcement Learning
- Decompose problem into sub-goals and sub-policies
- **Options framework**: option = (I, π, β) — initiation set, intra-option policy, termination condition
- High-level policy selects options; low-level executes them
- Benefits: faster learning, better transfer, reusable skills

### Value-Based vs Policy-Based Methods
| Aspect | Value-Based | Policy-Based |
|--------|------------|--------------|
| Approach | Learn Q or V, derive policy | Learn policy directly |
| Examples | Q-learning, DQN | REINFORCE, PPO |
| Discrete actions | Natural | Can handle continuous |
| Convergence | Guaranteed (tabular) | Can converge to local optima |

### Actor-Critic Methods
- Combines value-based (critic) and policy-based (actor) approaches
- **Actor**: policy π(a|s;θ) — selects actions
- **Critic**: value function V(s;w) — evaluates states
- **Advantage function**: A(s,a) = Q(s,a) - V(s) — how much better is action a than average
- **A2C (Advantage Actor-Critic)**: synchronous, stable training
- **A3C (Asynchronous A3C)**: multiple parallel workers, no experience replay needed

---

## Key Citations
- Hurbans (2020), pp. 323–375: RL chapter — agent-environment loop, components, Q-learning, DQN
- Barber (2012), pp. 139–165: MDPs, Bellman equations, value iteration, policy iteration

## TikZ Diagrams Planned
1. Agent-environment interaction loop (Section 1)
2. MDP state transition diagram with 3-4 states (Section 2)
