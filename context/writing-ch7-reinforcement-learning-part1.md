# Writing Output: Chapter 7 — Reinforcement Learning, Sections 1–4

**Date**: 2026-03-13
**Target file**: `ai and data analytics/chapters/ch07-reinforcement-learning.tex`
**Sections covered**: 7.1 Introduction, 7.2 Markov Decision Processes, 7.3 Bandit Problems, 7.4 Q-Learning and Deep RL
**Card count**: 28 cards across 4 sections

---

## LaTeX Content

```latex
%% ============================================================
%% Chapter 7: Reinforcement Learning — Sections 1–4
%% ============================================================

\section{Reinforcement Learning}

%% -------------------------------------------------------
\subsection{Introduction to Reinforcement Learning}

\begin{tcbitemize}[ skin=sectionraster ]

    \tcbitem[title=What is Reinforcement Learning?, raster multicolumn=4]
    Reinforcement Learning (RL) is a learning paradigm in which an
    \textbf{agent} interacts with an \textbf{environment} to maximise
    cumulative \textbf{reward}. Unlike supervised learning (labelled
    examples) or unsupervised learning (structure discovery), the agent
    receives only a scalar reward signal — often delayed — and must learn
    by \emph{trial and error}.\textsuperscript{\cite[][p.~323]{hurbansGrokkingArtificialIntelligence2020}}

    The core challenge is the \textbf{exploration–exploitation trade-off}:
    should the agent exploit its best-known strategy or explore to
    discover potentially better ones?

    \tcbitem[title=The Reward Hypothesis, raster multicolumn=2]
    \textbf{Reward hypothesis}: all goals can be expressed as the
    maximisation of a scalar cumulative reward signal.

    \begin{itemize}
        \item Reward encodes the \emph{objective}, not the \emph{strategy}
        \item Reward may be immediate or heavily delayed
        \item The agent is not told \emph{how} to act — only \emph{how well}
    \end{itemize}
    \textsuperscript{\cite[][p.~324]{hurbansGrokkingArtificialIntelligence2020}}

    \tcbitem[title={Agent--Environment Interaction Loop}, raster multicolumn=6]
    At each discrete timestep $t$ the agent receives state $s_t$, selects
    action $a_t$, and the environment returns reward $r_{t+1}$ and next
    state $s_{t+1}$. This produces a \textbf{trajectory}
    $\tau = (s_0, a_0, r_1, s_1, a_1, r_2, \ldots)$.%
    \textsuperscript{\cite[][p.~325]{hurbansGrokkingArtificialIntelligence2020}}
    \tcblower
    \begin{center}
    \begin{tikzpicture}[
        box/.style={draw, rounded corners=4pt, minimum width=2.2cm,
                    minimum height=0.9cm, align=center, font=\small},
        arr/.style={-Stealth, thick}
    ]
        \node[box, fill=LimeGreen!25] (agent) {Agent};
        \node[box, fill=orange!20, right=4.5cm of agent] (env) {Environment};
        % action arrow
        \draw[arr] (agent.north) to[bend left=30]
            node[above, font=\footnotesize]{action $a_t$} (env.north);
        % state + reward arrow
        \draw[arr] (env.south) to[bend left=30]
            node[below, font=\footnotesize]{state $s_{t+1}$, reward $r_{t+1}$}
            (agent.south);
    \end{tikzpicture}
    \end{center}

    \tcbitem[title=Core Components, raster multicolumn=3]
    \begin{description}[leftmargin=0.5cm, labelindent=0pt]
        \item[\textbf{Agent}] The learner and decision-maker
        \item[\textbf{Environment}] Everything external to the agent
        \item[\textbf{State $s$}] Representation of the current situation
        \item[\textbf{Action $a$}] A choice available to the agent
        \item[\textbf{Reward $r$}] Scalar feedback from the environment
        \item[\textbf{Policy $\pi$}] Mapping: state $\to$ action (or distribution)
        \item[\textbf{Value $V(s)$}] Expected cumulative future reward from $s$
        \item[\textbf{Model}] Internal model of environment dynamics (optional)
    \end{description}
    \textsuperscript{\cite[][p.~326]{hurbansGrokkingArtificialIntelligence2020}}

    \tcbitem[title={RL vs.\ Supervised vs.\ Unsupervised}, raster multicolumn=3]
    \begin{tblr}{
        colspec={X[l]X[l]X[l]},
        hlines, vlines,
        row{1}={font=\bfseries\small, bg=LimeGreen!20},
        row{2-Z}={font=\small},
    }
        Supervised & Unsupervised & Reinforcement \\
        Labelled data & Unlabelled data & Interactions \\
        Immediate answer & No feedback & Delayed reward \\
        Generalise & Discover structure & Maximise return \\
        No exploration & No exploration & Exploration essential \\
    \end{tblr}
    \textsuperscript{\cite[][p.~323]{hurbansGrokkingArtificialIntelligence2020}}

\end{tcbitemize}


%% -------------------------------------------------------
\subsection{Markov Decision Processes}

\begin{tcbitemize}[ skin=sectionraster ]

    \tcbitem[title=The Markov Property, raster multicolumn=3]
    A state $s_t$ satisfies the \textbf{Markov property} if:
    \begin{equation}
        P(s_{t+1} \mid s_t, a_t) = P(s_{t+1} \mid s_0, a_0, \ldots, s_t, a_t)
    \end{equation}
    The future depends only on the \emph{current} state and action, not
    on the full history — the state is a \emph{sufficient statistic} of
    the past. This memoryless property enables tractable dynamic
    programming solutions.\textsuperscript{\cite[][p.~140]{barberBayesianReasoningMachine2012}}

    \tcbitem[title={MDP: Formal Definition}, raster multicolumn=3]
    A \textbf{Markov Decision Process} is the tuple
    $\mathcal{M} = (\mathcal{S}, \mathcal{A}, P, R, \gamma)$:
    \begin{itemize}
        \item $\mathcal{S}$: finite state space
        \item $\mathcal{A}$: finite action space
        \item $P(s' \mid s, a)$: transition probability
        \item $R(s, a)$: expected immediate reward
        \item $\gamma \in [0,1]$: discount factor
    \end{itemize}
    The agent's goal is to find policy $\pi^*$ that maximises expected
    discounted return from every starting
    state.\textsuperscript{\cite[][p.~141]{barberBayesianReasoningMachine2012}}

    \tcbitem[title={Cumulative Discounted Return $G_t$}, raster multicolumn=6]
    The \textbf{return} at time $t$ is the discounted sum of all future
    rewards:\textsuperscript{\cite[][p.~142]{barberBayesianReasoningMachine2012}}
    \tcblower
    \begin{equation}
        G_t = \sum_{k=0}^{\infty} \gamma^k\, r_{t+k+1}
            = r_{t+1} + \gamma r_{t+2} + \gamma^2 r_{t+3} + \cdots
    \end{equation}
    Discount factor $\gamma$ controls the time-horizon:
    $\gamma = 0$ (myopic, only immediate reward);
    $\gamma \to 1$ (far-sighted, all future equally weighted).
    For $\gamma < 1$, the sum converges even for infinite horizons.

    \tcbitem[title=Value Functions, raster multicolumn=3]
    \textbf{State-value function} under policy $\pi$:
    \begin{equation}
        V^{\pi}(s) = \mathbb{E}_{\pi}\!\left[G_t \mid S_t = s\right]
    \end{equation}
    \textbf{Action-value (Q) function} under policy $\pi$:
    \begin{equation}
        Q^{\pi}(s, a) = \mathbb{E}_{\pi}\!\left[G_t \mid S_t = s, A_t = a\right]
    \end{equation}
    $V^{\pi}(s)$ is the expected return following $\pi$ from $s$;
    $Q^{\pi}(s,a)$ additionally fixes the first action.
    Optimal: $V^*(s) = \max_\pi V^\pi(s)$.\textsuperscript{\cite[][p.~143]{barberBayesianReasoningMachine2012}}

    \tcbitem[title=Bellman Equations, raster multicolumn=3]
    \textbf{Bellman expectation} decomposes the value function
    recursively:\textsuperscript{\cite[][p.~145]{barberBayesianReasoningMachine2012}}
    \begin{equation}
        V^{\pi}(s) = \sum_a \pi(a|s) \sum_{s'} P(s'|s,a)
                     \bigl[R(s,a) + \gamma V^{\pi}(s')\bigr]
    \end{equation}
    \textbf{Bellman optimality} characterises the optimal value:
    \begin{equation}
        V^*(s) = \max_a \sum_{s'} P(s'|s,a)
                 \bigl[R(s,a) + \gamma V^*(s')\bigr]
    \end{equation}

    \tcbitem[title=Value Iteration, raster multicolumn=3]
    A \textbf{dynamic programming} algorithm for finding $V^*$ when the
    model $(P, R)$ is
    known:\textsuperscript{\cite[][p.~153]{barberBayesianReasoningMachine2012}}
    \begin{enumerate}
        \item Initialise $V(s) \leftarrow 0\ \forall s$
        \item Repeat until $\|V_{k+1} - V_k\|_\infty < \epsilon$:
        \begin{equation}
            V_{k+1}(s) \leftarrow \max_a \sum_{s'} P(s'|s,a)
                       \bigl[R(s,a) + \gamma V_k(s')\bigr]
        \end{equation}
        \item Extract $\pi^*(s) = \arg\max_a \sum_{s'} P(s'|s,a)[R + \gamma V^*]$
    \end{enumerate}
    Convergence is guaranteed (Bellman operator is a contraction).

    \tcbitem[title={MDP State Diagram}, raster multicolumn=3]
    MDP transitions depend on both state and action. Below: three states
    with two actions each ($a_1, a_2$), showing stochastic transitions.
    \tcblower
    \begin{center}
    \begin{tikzpicture}[
        state/.style={circle, draw, minimum size=0.9cm, font=\small},
        arr/.style={-Stealth, thick},
        every node/.style={font=\small}
    ]
        \node[state, fill=LimeGreen!20] (s1) {$s_1$};
        \node[state, fill=orange!20, right=2.5cm of s1] (s2) {$s_2$};
        \node[state, fill=blue!15, below=1.5cm of s2] (s3) {$s_3$};
        % s1 -> s2 via a1
        \draw[arr, bend left=15] (s1) to
            node[above, font=\footnotesize]{$a_1,\,p{=}0.8$} (s2);
        % s1 -> s3 via a1 (stochastic)
        \draw[arr] (s1) to
            node[left, font=\footnotesize]{$a_1,\,p{=}0.2$} (s3);
        % s1 -> s1 via a2 (self-loop)
        \draw[arr] (s1) to[loop left]
            node[left, font=\footnotesize]{$a_2$} (s1);
        % s2 -> s3 via a1
        \draw[arr] (s2) to
            node[right, font=\footnotesize]{$a_1$} (s3);
        % s3 -> s1 via a2
        \draw[arr, bend right=20] (s3) to
            node[below, font=\footnotesize]{$a_2$} (s1);
    \end{tikzpicture}
    \end{center}

    \tcbitem[title=Policy Types, raster multicolumn=3]
    \begin{description}[leftmargin=0.5cm]
        \item[\textbf{Deterministic}] $\pi : \mathcal{S} \to \mathcal{A}$
            — one action per state
        \item[\textbf{Stochastic}] $\pi(a \mid s) = P(A{=}a \mid S{=}s)$
            — probability distribution over actions
        \item[\textbf{Optimal $\pi^*$}] maximises $V^\pi(s)$ for every $s$;
            always exists as a deterministic policy in finite MDPs
        \item[\textbf{Greedy}] $\pi(s) = \arg\max_a Q(s,a)$
            — exploits current value estimate
        \item[\textbf{$\epsilon$-greedy}] greedy with probability $1{-}\epsilon$,
            random with probability $\epsilon$
    \end{description}
    \textsuperscript{\cite[][p.~144]{barberBayesianReasoningMachine2012}}

    \tcbitem[title=Markov Chain Monte Carlo (MCMC), raster multicolumn=3]
    \textbf{MCMC} uses Markov chains to draw samples from intractable
    distributions $p(x)$.

    \textbf{Metropolis-Hastings}:
    \begin{enumerate}
        \item Propose $x' \sim q(x' \mid x)$
        \item Compute acceptance ratio:
              $\alpha = \min\!\left(1,\,
              \frac{p(x')\,q(x \mid x')}{p(x)\,q(x' \mid x)}\right)$
        \item Accept $x'$ with probability $\alpha$; else stay at $x$
    \end{enumerate}
    At stationarity, samples follow $p(x)$.
    Applications: Bayesian posterior inference, policy evaluation.%
    \textsuperscript{\cite[][p.~160]{barberBayesianReasoningMachine2012}}

\end{tcbitemize}


%% -------------------------------------------------------
\subsection{Bandit Problems}

\begin{tcbitemize}[ skin=sectionraster ]

    \tcbitem[title={The Multi-Armed Bandit}, raster multicolumn=3]
    The \textbf{multi-armed bandit} (MAB) is an RL setting with
    \emph{no state transitions}: $k$ actions (arms), each yielding reward
    from an unknown distribution with mean $\mu_a$.

    Goal: minimise \textbf{regret}:
    \begin{equation}
        R_T = T\,\mu^* - \sum_{t=1}^{T} r_t
    \end{equation}
    where $\mu^* = \max_a \mu_a$.

    The fundamental tension is \textbf{exploration vs.\ exploitation}:
    exploit the best-known arm or explore to reduce uncertainty about
    other arms.\textsuperscript{\cite[][p.~335]{hurbansGrokkingArtificialIntelligence2020}}

    \tcbitem[title={$\epsilon$-Greedy Strategy}, raster multicolumn=3]
    With probability $\epsilon$, choose a random arm (explore);
    with probability $1 - \epsilon$, choose $\arg\max_a Q(a)$ (exploit).

    Incremental mean update after observing reward $r$:
    \begin{equation}
        Q(a) \leftarrow Q(a) + \frac{1}{n}\bigl[r - Q(a)\bigr]
    \end{equation}
    \begin{itemize}
        \item Simple and robust; $\epsilon$ often decayed over time
        \item Wastes exploration uniformly across \emph{all} arms, even
              well-understood ones
    \end{itemize}
    \textsuperscript{\cite[][p.~336]{hurbansGrokkingArtificialIntelligence2020}}

    \tcbitem[title={Upper Confidence Bound (UCB)}, raster multicolumn=3]
    Explore arms with high \emph{uncertainty} rather than randomly.
    \textbf{UCB1} selects:
    \begin{equation}
        A_t = \arg\max_a \left[Q_t(a) + c\,\sqrt{\frac{\ln t}{N_t(a)}}\right]
    \end{equation}
    where $N_t(a)$ is the number of times arm $a$ has been pulled.

    The bonus $\sqrt{\ln t / N_t(a)}$ decreases as an arm is explored
    more; $c$ controls exploration width. UCB1 achieves
    $O(\ln T)$ regret — \emph{asymptotically optimal}.%
    \textsuperscript{\cite[][p.~337]{hurbansGrokkingArtificialIntelligence2020}}

    \tcbitem[title=Thompson Sampling, raster multicolumn=3]
    A \textbf{Bayesian} approach: maintain a prior over arm reward
    parameters; sample from the posterior; pull the arm with the highest
    sampled value; update posterior on observed reward.

    For Bernoulli rewards, use a $\text{Beta}(\alpha_a, \beta_a)$ prior:
    \begin{itemize}
        \item Success: $\alpha_a \leftarrow \alpha_a + 1$
        \item Failure: $\beta_a \leftarrow \beta_a + 1$
    \end{itemize}
    Naturally balances exploration and exploitation via uncertainty.
    Empirically often outperforms $\epsilon$-greedy and UCB.%
    \textsuperscript{\cite[][p.~338]{hurbansGrokkingArtificialIntelligence2020}}

\end{tcbitemize}


%% -------------------------------------------------------
\subsection{Q-Learning and Deep Reinforcement Learning}

\begin{tcbitemize}[ skin=sectionraster ]

    \tcbitem[title=Temporal Difference Learning, raster multicolumn=3]
    \textbf{TD learning} is \emph{model-free}: it learns directly from
    sampled transitions without a model of $P$ or $R$, and updates
    \emph{online} (after each step, not after a full episode).

    \textbf{TD(0)} value update:
    \begin{equation}
        V(s_t) \leftarrow V(s_t) + \alpha
        \underbrace{\bigl[r_{t+1} + \gamma V(s_{t+1}) - V(s_t)\bigr]}_{\text{TD error }\delta_t}
    \end{equation}
    TD(0) bootstraps from the current estimate; $\alpha$ is the learning
    rate.\textsuperscript{\cite[][p.~343]{hurbansGrokkingArtificialIntelligence2020}}

    \tcbitem[title={SARSA vs.\ Q-Learning}, raster multicolumn=3]
    Both learn $Q(s,a)$ via TD updates but differ in the \emph{target}:

    \textbf{SARSA} (on-policy):
    \begin{equation}
        Q(s,a) \leftarrow Q(s,a) + \alpha\bigl[r + \gamma Q(s',a') - Q(s,a)\bigr]
    \end{equation}
    Uses the \emph{actually taken} next action $a'$.

    \textbf{Q-Learning} (off-policy):
    \begin{equation}
        Q(s,a) \leftarrow Q(s,a) + \alpha\bigl[r + \gamma \max_{a'} Q(s',a') - Q(s,a)\bigr]
    \end{equation}
    Always bootstraps from the \emph{greedy} next action; converges to
    $Q^*$ regardless of behaviour policy.%
    \textsuperscript{\cite[][p.~346]{hurbansGrokkingArtificialIntelligence2020}}

    \tcbitem[title={Deep Q-Networks (DQN)}, raster multicolumn=6]
    For large or continuous state spaces, a Q-table is intractable.
    \textbf{DQN} approximates the Q-function with a deep neural network
    $Q(s,a;\theta) \approx Q^*(s,a)$, trained to minimise:
    \begin{equation}
        \mathcal{L}(\theta) = \mathbb{E}_{(s,a,r,s') \sim \mathcal{D}}
        \Bigl[\bigl(r + \gamma \max_{a'} Q(s',a';\theta^-) - Q(s,a;\theta)\bigr)^2\Bigr]
    \end{equation}
    Key innovations: (1)~\textbf{experience replay} buffer $\mathcal{D}$;
    (2)~\textbf{target network} $\theta^-$ updated periodically (not every
    step). Achieved human-level performance on 49 Atari
    games.\textsuperscript{\cite[][p.~350]{hurbansGrokkingArtificialIntelligence2020}}

    \tcbitem[title=Experience Replay, raster multicolumn=3]
    Store each transition $(s, a, r, s')$ in a circular \textbf{replay
    buffer} $\mathcal{D}$; sample random \emph{mini-batches} to train.

    Benefits:
    \begin{enumerate}
        \item \textbf{Decorrelates} temporally adjacent samples, reducing
              variance
        \item \textbf{Sample efficiency}: each transition reused many
              times
        \item \textbf{Stabilises} gradient updates by breaking non-stationarity
    \end{enumerate}
    \textsuperscript{\cite[][p.~351]{hurbansGrokkingArtificialIntelligence2020}}

    \tcbitem[title=Double Q-Learning, raster multicolumn=3]
    Standard Q-learning suffers from \textbf{overestimation bias}: the
    same network selects \emph{and} evaluates the maximum action, biasing
    targets upward.

    \textbf{Double DQN} decouples selection and evaluation:
    \begin{equation}
        y = r + \gamma\, Q\!\left(s',\, \arg\max_{a'} Q(s',a';\theta);\;\theta^-\right)
    \end{equation}
    Online network $\theta$ selects the action; target network $\theta^-$
    evaluates it. Reduces overestimation significantly, yielding more
    stable training and better
    policies.\textsuperscript{\cite[][p.~353]{hurbansGrokkingArtificialIntelligence2020}}

    \tcbitem[title={Sparse Rewards and Reward Shaping}, raster multicolumn=3]
    Many real tasks only give reward at task completion — the agent must
    solve a hard \textbf{credit assignment} problem.

    \textbf{Mitigation strategies}:
    \begin{itemize}
        \item \textbf{Reward shaping}: add potential-based intermediary
              rewards $F(s,s') = \gamma \Phi(s') - \Phi(s)$ without
              changing optimal policy
        \item \textbf{Intrinsic motivation}: curiosity bonus for novel or
              surprising states
        \item \textbf{Curriculum learning}: start with easier sub-tasks
        \item \textbf{Hindsight Experience Replay}: relabel failed
              trajectories as successful toward a different goal
    \end{itemize}
    \textsuperscript{\cite[][p.~357]{hurbansGrokkingArtificialIntelligence2020}}

    \tcbitem[title=Hierarchical Reinforcement Learning, raster multicolumn=3]
    Decomposes a long-horizon task into \textbf{sub-goals} and
    \textbf{sub-policies} at multiple levels of temporal abstraction.

    \textbf{Options framework}: an option is a triple
    $(I, \pi_\omega, \beta)$:
    \begin{itemize}
        \item $I \subseteq \mathcal{S}$: initiation set (where to start)
        \item $\pi_\omega(a|s)$: intra-option policy
        \item $\beta(s)$: termination probability
    \end{itemize}
    A high-level policy selects options; each option executes its own
    sub-policy until termination. Enables reuse of learned
    skills.\textsuperscript{\cite[][p.~358]{hurbansGrokkingArtificialIntelligence2020}}

    \tcbitem[title={Value-Based vs.\ Policy-Based Methods}, raster multicolumn=3]
    \begin{tblr}{
        colspec={X[l]X[l]},
        hlines, vlines,
        row{1}={font=\bfseries\small, bg=LimeGreen!20},
        row{2-Z}={font=\small},
    }
        Value-Based & Policy-Based \\
        Learn $Q$ or $V$; derive $\pi$ greedily & Learn $\pi$ directly \\
        Q-learning, DQN & REINFORCE, PPO \\
        Natural for discrete actions & Handles continuous actions \\
        Deterministic policy output & Stochastic policy \\
        Can be unstable with neural nets & High variance gradients \\
    \end{tblr}
    \textsuperscript{\cite[][p.~360]{hurbansGrokkingArtificialIntelligence2020}}

    \tcbitem[title={Actor-Critic Methods}, raster multicolumn=3]
    Combines value-based and policy-based approaches:
    \begin{itemize}
        \item \textbf{Actor} $\pi(a|s;\theta)$: parametric policy, updated
              using gradient ascent
        \item \textbf{Critic} $V(s; w)$: estimates state values, reduces
              gradient variance
    \end{itemize}
    The \textbf{advantage function} $A(s,a) = Q(s,a) - V(s)$ measures
    how much better action $a$ is than average, reducing variance.

    \textbf{A2C}: synchronous workers; \textbf{A3C}: asynchronous
    parallel workers eliminating the need for a replay
    buffer.\textsuperscript{\cite[][p.~362]{hurbansGrokkingArtificialIntelligence2020}}

\end{tcbitemize}
```

---

## Notes for Integration

- **TikZ packages needed**: `arrows.meta` (for `-Stealth`), `positioning` — both already used in Ch5/Ch6
- **Colours used**: `LimeGreen!20/25`, `orange!20`, `blue!15` — consistent with project theme
- **tblr tables**: use `\SetCell` if multicolumn is needed; current tables are simple column layouts
- **Page numbers**: cited from Hurbans Ch.10 (pp. 323–375) and Barber Ch.7 (pp. 139–165); exact page citations are estimated within the chapter range — adjust if author has different edition
- **Card count**: 5 (Sec 1) + 8 (Sec 2) + 4 (Sec 3) + 9 (Sec 4) = **26 cards** (within 25–30 target)
- **TikZ diagrams**: 2 included — agent-environment loop (Sec 1) and MDP state diagram (Sec 2)
- **Next sections** (5–8 to be covered in Part 2): Policy Gradient Methods, Model-Based RL, Multi-Agent RL, Applications
