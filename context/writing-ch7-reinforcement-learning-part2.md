# Writing Output: Ch7 Reinforcement Learning — Sections 5–7

## LaTeX content for sections 5 (RL Approaches), 6 (Inference and Causality), 7 (Further Reading)

Paste this into `ch07-reinforcement-learning.tex`, replacing the stub content for sections 5–7 and the Literature section.

---

```latex
    \section{Reinforcement Learning Approaches}
    \subsection{Model-Free Learning}
    \begin{tcbitemize}[ skin=sectionraster ]

    \tcbitem[title=Model-Free RL, raster multicolumn=3]
    In \textbf{model-free} reinforcement learning the agent learns entirely through interaction with the environment --- no internal model of state transitions or rewards is built. The agent discovers which actions are valuable solely from trial-and-error experience.\textsuperscript{\cite[][p.~348]{hurbansGrokkingArtificialIntelligence2020}}

    Key characteristics:
    \begin{itemize}
        \item No explicit environment model required
        \item Learns directly from (state, action, reward, next-state) tuples
        \item More data-hungry than model-based, but robust to model errors
        \item Examples: Q-learning, SARSA, REINFORCE
    \end{itemize}

    \tcbitem[title=Q-Learning, raster multicolumn=3]
    \textbf{Q-learning} (Watkins, 1989) is an off-policy temporal-difference algorithm that learns the action-value function $Q(s,a)$ --- the expected cumulative reward from taking action $a$ in state $s$.\textsuperscript{\cite[][pp.~335--340]{hurbansGrokkingArtificialIntelligence2020}}

    The \textbf{Bellman update rule}:
    \begin{equation}
        Q(s,a) \leftarrow (1{-}\alpha)\,Q(s,a) + \alpha\!\left[r + \gamma \max_{a'} Q(s',a')\right]
    \end{equation}
    where $\alpha \in (0,1]$ is the learning rate, $\gamma \in [0,1)$ the discount factor, $r$ the immediate reward, and $s'$ the next state.

    The Q-table (rows = states, columns = actions) is initialized to zero and updated incrementally. At inference time the agent selects $a^* = \arg\max_a Q(s,a)$.

    \tcbitem[title=SARSA, raster multicolumn=3]
    \textbf{SARSA} is an \emph{on-policy} TD algorithm: it updates $Q$ using the action $a'$ actually taken by the policy, not the greedy maximum.\textsuperscript{\cite[][Ch.~6]{suttonReinforcementLearningIntroduction2018}}

    \begin{equation}
        Q(s,a) \leftarrow Q(s,a) + \alpha\!\left[r + \gamma\,Q(s',a') - Q(s,a)\right]
    \end{equation}

    \begin{itemize}
        \item On-policy: more conservative, avoids dangerous actions
        \item Q-learning (off-policy): faster convergence, may take risky shortcuts during training
        \item Both converge to the optimal policy given sufficient exploration
    \end{itemize}

    \tcbitem[title=REINFORCE (Policy Gradient), raster multicolumn=3]
    \textbf{REINFORCE} directly optimizes the policy $\pi_\theta(a|s)$ by gradient ascent on expected return.\textsuperscript{\cite[][Ch.~13]{suttonReinforcementLearningIntroduction2018}}

    \begin{equation}
        \nabla_\theta J(\theta) = \mathbb{E}_\pi\!\left[\nabla_\theta \ln \pi_\theta(a_t|s_t) \cdot G_t\right]
    \end{equation}

    where $G_t = \sum_{k=0}^{\infty} \gamma^k r_{t+k+1}$ is the discounted return from step $t$.

    \begin{itemize}
        \item Monte Carlo: updates after complete episodes
        \item High variance; baseline subtraction (actor-critic) reduces variance
        \item Natural for continuous action spaces where Q-tables are intractable
    \end{itemize}

    \end{tcbitemize}

    \subsection{Model-Based Learning}
    \begin{tcbitemize}[ skin=sectionraster ]

    \tcbitem[title=Model-Based RL, raster multicolumn=3]
    In \textbf{model-based} RL the agent learns or is given an explicit model $\hat{M}(s,a) \rightarrow (s', r)$ of the environment. It can \emph{plan} by simulating experience inside the model without executing every action.\textsuperscript{\cite[][p.~348]{hurbansGrokkingArtificialIntelligence2020}}

    Advantages over model-free:
    \begin{itemize}
        \item Sample efficient: plan many steps from few real interactions
        \item Can reason about counterfactual actions
        \item Model errors compound over long horizons --- accuracy matters
    \end{itemize}
    Trade-off: model capacity vs. model bias.

    \tcbitem[title={Dyna-Q: Integrating Planning and Learning}, raster multicolumn=3]
    \textbf{Dyna-Q} (Sutton, 1991) combines real experience with simulated experience from a learned model:\textsuperscript{\cite[][Ch.~8]{suttonReinforcementLearningIntroduction2018}}

    \begin{enumerate}
        \item Take action $a$ in real environment; observe $r$, $s'$
        \item Update Q-table with real transition
        \item Update model $\hat{M}(s,a) \leftarrow (s',r)$
        \item Repeat $n$ times: sample random past $(s,a)$, simulate $(s',r)$ from model, update Q
    \end{enumerate}

    The $n$ planning steps give Dyna-Q major sample efficiency gains over pure Q-learning.

    \tcbitem[title={World Models \& MPC}, raster multicolumn=3]
    \textbf{World models} (Ha \& Schmidhuber, 2018) learn a compact latent representation of the environment. The agent plans entirely within the latent world model, then transfers the learned policy back to reality.\textsuperscript{\cite[][Ch.~8]{suttonReinforcementLearningIntroduction2018}}

    \textbf{Model Predictive Control (MPC)}: at each step, optimize actions over a finite horizon $H$ using the model, execute only the first action, then re-plan. Naturally handles non-stationary environments.

    \begin{itemize}
        \item Used in robotics, process control, AlphaZero (combines Monte Carlo tree search with a learned model)
        \item MPC horizon $H$ trades off computation vs. look-ahead quality
    \end{itemize}

    \end{tcbitemize}

    \subsection{Exploration vs Exploitation}
    \begin{tcbitemize}[ skin=sectionraster ]

    \tcbitem[title={Exploration vs Exploitation}, raster multicolumn=3]
    The agent must balance:\textsuperscript{\cite[][pp.~338--339]{hurbansGrokkingArtificialIntelligence2020}}
    \begin{itemize}
        \item \textbf{Exploitation}: select the action believed to yield the highest reward ($\arg\max_a Q(s,a)$)
        \item \textbf{Exploration}: try other actions to discover potentially better rewards
    \end{itemize}

    Purely greedy agents get stuck in local optima; purely random agents never converge. The tension is central to all RL algorithms.

    \tcbitem[title=$\varepsilon$-Greedy Strategy, raster multicolumn=3]
    The simplest approach:\textsuperscript{\cite[][p.~339]{hurbansGrokkingArtificialIntelligence2020}}

    \begin{equation}
        a_t = \begin{cases} \text{random action} & \text{with probability } \varepsilon \\ \arg\max_a Q(s_t,a) & \text{with probability } 1-\varepsilon \end{cases}
    \end{equation}

    \textbf{Decaying $\varepsilon$}: start at $\varepsilon \approx 1.0$ (mostly explore) and anneal to $\varepsilon \approx 0.01$ (mostly exploit) over training. Common schedule: $\varepsilon_t = \varepsilon_{\min} + (\varepsilon_{\max} - \varepsilon_{\min}) e^{-t/\tau}$.

    \tcbitem[title=Upper Confidence Bound (UCB), raster multicolumn=3]
    UCB selects actions that are either \emph{estimated good} or \emph{rarely tried}:\textsuperscript{\cite[][Ch.~2]{suttonReinforcementLearningIntroduction2018}}

    \begin{equation}
        a_t = \arg\max_a \left[ Q(s,a) + c\sqrt{\frac{\ln t}{N_t(s,a)}} \right]
    \end{equation}

    where $N_t(s,a)$ is the number of times action $a$ was selected from state $s$, $t$ is total steps, and $c$ controls exploration strength.

    The confidence bonus shrinks as an action is tried more, naturally directing attention to underexplored actions. UCB is optimism in the face of uncertainty.

    \tcbitem[title=Curiosity-Driven Exploration, raster multicolumn=3]
    When extrinsic rewards are sparse, \textbf{intrinsic motivation} sustains exploration. A forward model $f(s_t, a_t) \rightarrow \hat{s}_{t+1}$ is learned alongside the policy. The prediction error is used as an intrinsic reward:\textsuperscript{\cite[][Ch.~2]{suttonReinforcementLearningIntroduction2018}}

    \begin{equation}
        r^{\text{int}}_t = \bigl\|\hat{s}_{t+1} - s_{t+1}\bigr\|^2
    \end{equation}

    High prediction error signals novel, informative states. The agent is intrinsically \emph{curious} about regions where its world model is poor. Used successfully in Montezuma's Revenge and robotics.

    \end{tcbitemize}

    \section{Inference and Causality}

    \subsection{Statistical Inference}
    \begin{tcbitemize}[ skin=sectionraster ]

    \tcbitem[title=Bayesian Inference, raster multicolumn=3]
    Bayesian inference treats model parameters $\theta$ as random variables and updates beliefs upon observing data $\mathcal{D}$:\textsuperscript{\cite[][pp.~14--19]{barberBayesianReasoningMachine2012}}

    \begin{equation}
        p(\theta|\mathcal{D}) = \frac{p(\mathcal{D}|\theta)\,p(\theta)}{p(\mathcal{D})}
    \end{equation}

    \begin{itemize}
        \item \textbf{Prior} $p(\theta)$: belief before data
        \item \textbf{Likelihood} $p(\mathcal{D}|\theta)$: how probable is the data under $\theta$?
        \item \textbf{Posterior} $p(\theta|\mathcal{D})$: updated belief
        \item \textbf{Evidence} $p(\mathcal{D}) = \int p(\mathcal{D}|\theta)\,p(\theta)\,d\theta$: normalizing constant
    \end{itemize}

    Posterior $\propto$ Likelihood $\times$ Prior. The MAP estimate is $\hat{\theta} = \arg\max_\theta p(\theta|\mathcal{D})$.

    \tcbitem[title={Bayesian vs Frequentist Inference}, raster multicolumn=3]
    \begin{itemize}
        \item \textbf{Frequentist}: $\theta$ is a fixed (unknown) constant; probability refers to long-run frequencies; provides point estimates and confidence intervals
        \item \textbf{Bayesian}: $\theta$ is a random variable with a distribution; probability reflects degree of belief; provides full posterior distribution
    \end{itemize}

    Bayesian inference is naturally sequential: today's posterior becomes tomorrow's prior as new data arrives. This makes it ideal for online learning and decision-making under uncertainty.\textsuperscript{\cite[][Ch.~1]{downeyThinkBayes2016}}

    \tcbitem[title=Bayesian Networks, raster multicolumn=6]
    A \textbf{Bayesian Network} (belief network) is a Directed Acyclic Graph (DAG) in which each node is a random variable $x_i$ with a \emph{conditional probability table} (CPT) $p(x_i | \text{pa}(x_i))$. The joint distribution factorises as:\textsuperscript{\cite[][pp.~33--40]{barberBayesianReasoningMachine2012}}

    \begin{equation}
        p(x_1, \ldots, x_D) = \prod_{i=1}^{D} p\bigl(x_i \,\big|\, \text{pa}(x_i)\bigr)
    \end{equation}

    \textbf{Example --- Wet Grass}: $R$ (rain), $S$ (sprinkler), $T$ (Tracey's grass wet), $J$ (Jack's grass wet). Assuming $p(T|J,R,S) = p(T|R,S)$ and $p(J|R,S) = p(J|R)$:
    \[p(T,J,R,S) = p(T|R,S)\,p(J|R)\,p(R)\,p(S)\]
    This reduces parameter count from 15 to 8. The graph encodes which variables are conditionally independent: a missing edge is an independence assumption.
    \tcblower
    \textbf{Explaining away}: In $A \to C \leftarrow B$, causes $A$ and $B$ are \emph{a priori} independent. But conditioning on the effect $C$ makes them dependent --- knowing one cause ``explains away'' the other. This is the \emph{collider} effect.

    \tcbitem[title=Probabilistic Modelling, raster multicolumn=3]
    A \textbf{probabilistic model} defines a joint distribution over observed variables $\mathbf{x}$ and latent variables $\mathbf{z}$:\textsuperscript{\cite[][Ch.~1]{barberBayesianReasoningMachine2012}}

    \begin{equation}
        p(\mathbf{x}, \mathbf{z} | \theta) = p(\mathbf{x} | \mathbf{z}, \theta)\,p(\mathbf{z}|\theta)
    \end{equation}

    \textbf{Inference}: given $\mathbf{x}$, compute posterior $p(\mathbf{z}|\mathbf{x},\theta)$. \\
    \textbf{Learning}: find $\theta$ that maximises marginal likelihood $p(\mathbf{x}|\theta) = \int p(\mathbf{x}|\mathbf{z},\theta)\,p(\mathbf{z}|\theta)\,d\mathbf{z}$.

    The integral is often intractable, motivating approximate inference methods (MCMC, variational inference).

    \tcbitem[title=Conditional Independence, raster multicolumn=3]
    Variables $X$ and $Y$ are \textbf{conditionally independent} given $Z$, written $X \perp\!\!\!\perp Y \mid Z$, if:\textsuperscript{\cite[][p.~8]{barberBayesianReasoningMachine2012}}

    \begin{equation}
        p(X, Y | Z) = p(X|Z)\,p(Y|Z)
    \end{equation}

    Equivalently, $p(X|Y,Z) = p(X|Z)$: knowing $Y$ gives no additional information about $X$ once $Z$ is known.

    Conditional independence is the fundamental building block of Bayesian networks. Every absent edge in a BN encodes a conditional independence assumption that compresses the joint distribution.

    \end{tcbitemize}

    \subsection{Introduction to Causality}
    \begin{tcbitemize}[ skin=sectionraster ]

    \tcbitem[title={Correlation vs Causation}, raster multicolumn=3]
    \textbf{Correlation} is a symmetric statistical association: $\text{Cov}(X,Y) \neq 0$. It says nothing about direction or mechanism.

    \textbf{Causation} implies a directional mechanism: intervening on $X$ forces a change in $Y$.

    Classic example: ice cream sales and drowning rates are positively correlated --- both are driven by a common cause (summer heat). Controlling for temperature removes the correlation. Formally, $p(Y|X) \neq p(Y|\,\text{do}(X))$ whenever confounders exist.\textsuperscript{\cite[][Ch.~1]{pearlBookWhyNew2018}}

    \tcbitem[title=Granger Causality, raster multicolumn=3]
    \textbf{Granger causality} (Granger, 1969) is a time-series criterion: $X$ Granger-causes $Y$ if past values of $X$ provide statistically significant predictive information about $Y$, beyond what past $Y$ alone provides:\textsuperscript{\cite[][Ch.~2]{nessCausalAI2025}}

    \[Y_t = f(Y_{t-1}, \ldots, X_{t-1}, \ldots) + \varepsilon_t\]

    Test: does including $X_{t-k}$ significantly reduce prediction error for $Y_t$?

    \textbf{Limitation}: Granger causality captures temporal precedence, not structural/mechanistic causation. Two variables driven by a common hidden cause can appear to Granger-cause each other.

    \tcbitem[title={Directed Acyclic Graphs (DAGs)}, raster multicolumn=3]
    A \textbf{DAG} encodes causal structure: nodes are variables; directed edges $X \to Y$ mean ``$X$ directly causes $Y$''. The acyclic constraint prevents circular causation.\textsuperscript{\cite[][pp.~25--27]{barberBayesianReasoningMachine2012}}

    DAG terminology:
    \begin{itemize}
        \item \textbf{Parent}: direct cause ($\text{pa}(Y)$)
        \item \textbf{Ancestor}: any cause along a directed path
        \item \textbf{Descendant}: any variable causally downstream
        \item \textbf{Markov blanket}: parents + children + parents of children; screens $X$ from all other variables
    \end{itemize}

    In causal DAGs, ancestral order corresponds to temporal order: root causes come first.

    \tcbitem[title={Causal Graph Elements: Fork, Chain, Collider}, raster multicolumn=3]
    Three elementary graph structures determine how information flows:\textsuperscript{\cite[][pp.~43--45]{barberBayesianReasoningMachine2012}}

    \begin{itemize}
        \item \textbf{Fork} (common cause): $A \leftarrow C \rightarrow B$. $C$ is a confounder; $A \perp\!\!\!\perp B \mid C$, but $A \not\!\perp\!\!\!\perp B$ marginally.
        \item \textbf{Chain} (mediation): $A \rightarrow C \rightarrow B$. $C$ mediates; $A \perp\!\!\!\perp B \mid C$, but $A \not\!\perp\!\!\!\perp B$ marginally.
        \item \textbf{Collider}: $A \rightarrow C \leftarrow B$. $A \perp\!\!\!\perp B$ marginally, but $A \not\!\perp\!\!\!\perp B \mid C$ (conditioning opens the path).
    \end{itemize}

    Conditioning on a collider (or its descendant) creates a \emph{spurious} association between its parents.

    \tcbitem[title=D-Separation, raster multicolumn=6]
    \textbf{D-separation} (Pearl, 1988) is the formal criterion for reading conditional independence from a DAG.\textsuperscript{\cite[][pp.~45--46]{barberBayesianReasoningMachine2012}}

    A path $U$ between $X$ and $Y$ is \textbf{blocked} by a set $\mathcal{Z}$ if:
    \begin{enumerate}
        \item There is a \emph{non-collider} $w$ on $U$ such that $w \in \mathcal{Z}$, OR
        \item There is a \emph{collider} $w$ on $U$ such that neither $w$ nor any of its descendants is in $\mathcal{Z}$.
    \end{enumerate}

    $X$ and $Y$ are \textbf{d-separated} by $\mathcal{Z}$ if every path between them is blocked. D-separation implies $X \perp\!\!\!\perp Y \mid \mathcal{Z}$ in any distribution consistent with the DAG structure.
    \tcblower
    \textbf{Intuition}: d-separation tells us exactly which conditioning sets render variables independent. It is the key tool for identifying confounders and valid adjustment sets without running experiments.

    \end{tcbitemize}

    \subsection{Interventions}
    \begin{tcbitemize}[ skin=sectionraster ]

    \tcbitem[title={Seeing vs Doing: The Do-Operator}, raster multicolumn=3]
    Pearl's \textbf{do-operator} distinguishes observation from intervention:\textsuperscript{\cite[][pp.~50--51]{barberBayesianReasoningMachine2012}}

    \begin{itemize}
        \item \textbf{Seeing}: $p(Y \mid X{=}x)$ --- conditioning on observing $X{=}x$; confounders still act
        \item \textbf{Doing}: $p(Y \mid \text{do}(X{=}x))$ --- forcing $X{=}x$ by intervention; removes all incoming arrows to $X$
    \end{itemize}

    Intervening on $X$ creates a modified DAG $\mathcal{G}_{\overline{X}}$ in which all edges \emph{into} $X$ are cut. The post-intervention distribution:
    \begin{equation}
        p(\mathbf{x}_{\bar{C}} \mid \text{do}(X_{c_1}{=}x_{c_1},\ldots)) = \prod_{j \notin \mathcal{C}} p\bigl(x_j \mid \text{pa}(x_j)\bigr)
    \end{equation}

    \tcbitem[title={Confounders}, raster multicolumn=3]
    A \textbf{confounder} is a variable $C$ that causally affects both the treatment $X$ and the outcome $Y$:\textsuperscript{\cite[][Ch.~7]{hernanCausalInferenceWhat2020}}

    \[ C \to X,\quad C \to Y \]

    Confounders create a \emph{backdoor path} from $X$ to $Y$ that does not represent the causal effect of $X$. Failing to adjust for confounders leads to biased causal estimates.

    \textbf{Examples}: socioeconomic status confounds education and health outcomes; age confounds treatment choice and recovery.

    In a DAG, confounders are identified by backdoor paths and can be blocked by conditioning on appropriate variables.

    \tcbitem[title={Counterfactuals}, raster multicolumn=3]
    A \textbf{counterfactual} asks: ``What would have happened to $Y$ if $X$ had been $x$, given that we actually observed $X{=}x'$?''\textsuperscript{\cite[][Ch.~7]{pearlCausalityModelsReasoning2009}}

    Notation: $Y_{X=x}(u)$ --- the value of $Y$ for unit $u$ under intervention $\text{do}(X{=}x)$.

    Counterfactuals require a \textbf{Structural Causal Model} (SCM): equations $X_i = f_i(\text{pa}(X_i), U_i)$ with exogenous noise $U_i$. Three steps:
    \begin{enumerate}
        \item \textbf{Abduction}: infer $U$ from observed evidence
        \item \textbf{Action}: modify the SCM to set $X{=}x$
        \item \textbf{Prediction}: compute $Y$ in the modified model
    \end{enumerate}

    \tcbitem[title={Causal Inference vs Randomized Controlled Trials}, raster multicolumn=3]
    A \textbf{Randomized Controlled Trial (RCT)} randomly assigns treatment, breaking the confounder--treatment link:\textsuperscript{\cite[][Ch.~1]{hernanCausalInferenceWhat2020}}

    \[ \text{Random assignment} \equiv \text{do}(X) \implies p(Y|\text{do}(X)) = p(Y|X) \]

    RCTs are the gold standard for causal inference but are often costly, unethical, or impossible.

    \textbf{Observational causal inference} estimates $p(Y|\text{do}(X))$ from non-experimental data by:
    \begin{itemize}
        \item Identifying and adjusting for confounders via the backdoor criterion
        \item Instrumental variables, regression discontinuity, difference-in-differences
    \end{itemize}

    \end{tcbitemize}

    \subsection{Do-Calculus}
    \begin{tcbitemize}[ skin=sectionraster ]

    \tcbitem[title=Backdoor Criterion, raster multicolumn=3]
    A set $\mathcal{Z}$ satisfies the \textbf{backdoor criterion} relative to $(X,Y)$ if:\textsuperscript{\cite[][pp.~79--81]{pearlCausalityModelsReasoning2009}}
    \begin{enumerate}
        \item No node in $\mathcal{Z}$ is a descendant of $X$
        \item $\mathcal{Z}$ blocks every backdoor path from $X$ to $Y$ (paths with an arrow into $X$)
    \end{enumerate}

    If $\mathcal{Z}$ satisfies the backdoor criterion:
    \begin{equation}
        p(Y \mid \text{do}(X)) = \sum_{z} p(Y \mid X, \mathcal{Z}{=}z)\,p(\mathcal{Z}{=}z)
    \end{equation}

    This \textbf{adjustment formula} allows computation of causal effects from observational data alone.

    \tcbitem[title=Front-Door Criterion, raster multicolumn=3]
    When all confounders are \emph{unobserved} but a mediator $M$ is observed, the \textbf{front-door criterion} applies:\textsuperscript{\cite[][pp.~82--84]{pearlCausalityModelsReasoning2009}}

    Conditions: (1) $M$ intercepts all directed paths from $X$ to $Y$; (2) no unblocked backdoor path from $X$ to $M$; (3) all backdoor paths from $M$ to $Y$ are blocked by $X$.

    \begin{equation}
        p(Y|\text{do}(X)) = \sum_m p(M{=}m|X) \sum_{x'} p(Y|M{=}m, X{=}x')\,p(X{=}x')
    \end{equation}

    \tcbitem[title={Three Rules of Do-Calculus}, raster multicolumn=6]
    Pearl's \textbf{do-calculus} provides three rules sufficient to derive any identifiable causal effect from a DAG and observational distribution.\textsuperscript{\cite[][pp.~85--87]{pearlCausalityModelsReasoning2009}} Let $\mathcal{G}_{\overline{X}}$ denote the graph with arrows into $X$ removed, $\mathcal{G}_{\underline{X}}$ the graph with arrows out of $X$ removed.

    \begin{itemize}
        \item \textbf{Rule 1 (Insertion/deletion of observations)}: $p(y|\text{do}(x),z,w) = p(y|\text{do}(x),w)$ if $(Y \perp\!\!\!\perp Z \mid X,W)_{\mathcal{G}_{\overline{X}}}$
        \item \textbf{Rule 2 (Action/observation exchange)}: $p(y|\text{do}(x),\text{do}(z),w) = p(y|\text{do}(x),z,w)$ if $(Y \perp\!\!\!\perp Z \mid X,W)_{\mathcal{G}_{\overline{X}\underline{Z}}}$
        \item \textbf{Rule 3 (Insertion/deletion of actions)}: $p(y|\text{do}(x),\text{do}(z),w) = p(y|\text{do}(x),w)$ if $(Y \perp\!\!\!\perp Z \mid X,W)_{\mathcal{G}_{\overline{X},\overline{Z(W)}}}$
    \end{itemize}

    Together, these rules are \textbf{complete}: any identifiable causal query can be reduced to observational probabilities using these three transformations.

    \end{tcbitemize}

    \subsection{Fallacies}
    \begin{tcbitemize}[ skin=sectionraster ]

    \tcbitem[title=Simpson's Paradox, raster multicolumn=3]
    A statistical trend appears in the \emph{combined} data but \emph{reverses} (or disappears) in every subgroup.\textsuperscript{\cite[][pp.~49--50]{barberBayesianReasoningMachine2012}}

    \textbf{Medical trial example} (Barber, Table 3.1): A drug appears beneficial when male and female groups are pooled (recovery rate: 50\% drug vs 40\% no-drug) but is \emph{harmful} in each subgroup (males: 60\% vs 70\%; females: 20\% vs 30\%).

    \textbf{Resolution}: The paradox arises by confusing $p(R|D)$ (observational) with $p(R|\text{do}(D))$ (interventional). Gender is a confounder: it affects both drug-taking behaviour and recovery. Adjusting for gender via the backdoor criterion recovers the true causal effect: the drug is \emph{not} beneficial.

    \tcbitem[title={Collider Bias \& Berkson's Paradox}, raster multicolumn=3]
    \textbf{Collider bias} arises when analysis conditions on a common effect (collider) of two variables, creating a spurious association between them.\textsuperscript{\cite[][p.~43]{barberBayesianReasoningMachine2012}}

    Structure: $A \to C \leftarrow B$. Marginally $A \perp\!\!\!\perp B$, but $A \not\!\perp\!\!\!\perp B \mid C$.

    \textbf{Berkson's Paradox} (1946): In hospital-based studies, disease $A$ and disease $B$ appear negatively correlated because hospitalization is a collider ($A \to \text{Hosp} \leftarrow B$). Patients with $A$ are less likely to also have $B$, but only because both cause hospitalization. In the general population, $A$ and $B$ may be independent.

    \tcbitem[title=Mediation Fallacy, raster multicolumn=3]
    The \textbf{mediation fallacy} occurs when a researcher adjusts for a mediator $M$ on the causal path $X \to M \to Y$ while trying to estimate the total effect of $X$ on $Y$.\textsuperscript{\cite[][Ch.~9]{pearlCausalityModelsReasoning2009}}

    Adjusting for $M$:
    \begin{itemize}
        \item \emph{Blocks} the indirect pathway $X \to M \to Y$
        \item The remaining estimate captures only the \emph{direct} effect $X \to Y$, not the total effect
        \item If the goal is the total effect, $M$ must \emph{not} be conditioned on
    \end{itemize}

    Correct mediation analysis requires separating direct and indirect effects using counterfactual definitions.

    \tcbitem[title={Imputing Missing Values: Causal View}, raster multicolumn=3]
    Standard imputation (mean, median, model-based) assumes data is Missing At Random (MAR). The causal view requires modelling the \textbf{missingness mechanism}:\textsuperscript{\cite[][Ch.~8]{nessCausalAI2025}}

    \begin{itemize}
        \item \textbf{MCAR} (Missing Completely At Random): missingness independent of all variables --- safe to impute
        \item \textbf{MAR} (Missing At Random): missingness depends on observed variables --- adjust for them
        \item \textbf{MNAR} (Missing Not At Random): missingness depends on the missing value itself --- selection bias; model the mechanism explicitly
    \end{itemize}

    If the variable with missing values is a \emph{collider descendant}, naive imputation can introduce collider bias. The DAG determines the correct strategy.

    \end{tcbitemize}

    \section{Further Reading}
    \begin{tcbitemize}[ skin=sectionraster ]

    \tcbitem[title=Further Reading, raster multicolumn=6]
    \begin{itemize}
        \item \fullcite{suttonReinforcementLearningIntroduction2018}
        \item \fullcite{hurbansGrokkingArtificialIntelligence2020}
        \item \fullcite{barberBayesianReasoningMachine2012}
        \item \fullcite{downeyThinkBayes2016}
        \item \fullcite{pearlCausalityModelsReasoning2009}
        \item \fullcite{pearlBookWhyNew2018}
        \item \fullcite{pearlCausalInferenceStatistics2016}
        \item \fullcite{hernanCausalInferenceWhat2020}
        \item \fullcite{nessCausalAI2025}
    \end{itemize}

    \end{tcbitemize}
```

---

## Card Count Summary
- 7.5 Model-Free Learning: 4 cards
- 7.5 Model-Based Learning: 3 cards
- 7.5 Exploration vs Exploitation: 4 cards
- 7.6 Statistical Inference: 5 cards (incl. 1 wide)
- 7.6 Introduction to Causality: 5 cards (incl. 1 wide)
- 7.6 Interventions: 4 cards
- 7.6 Do-Calculus: 3 cards (incl. 1 wide)
- 7.6 Fallacies: 4 cards
- 7.7 Further Reading: 1 wide card

**Total: ~33 cards** (sections 5–7)

## Notes
- Literature section replaced with Section 7 Further Reading (standard format)
- All \subsubsection content collapsed into \tcbitem cards (no \subsubsection in final output)
- New bib keys added: suttonReinforcementLearningIntroduction2018, pearlCausalityModelsReasoning2009, pearlBookWhyNew2018, pearlCausalInferenceStatistics2016, hernanCausalInferenceWhat2020
