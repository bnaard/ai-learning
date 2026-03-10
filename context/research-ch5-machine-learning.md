# Research Notes: Chapter 5 — Machine Learning

## Status: COMPLETE

---

## Section-by-Section Research

---

### 1. INTRODUCTION TO MACHINE LEARNING

#### 1.1 Regression & Classification

**Core concept:** Machine learning tasks divide into regression (predicting a continuous real value) and classification (predicting a discrete class label). Regression uses squared loss $\ell(y,\hat{y}) = (y - \hat{y})^2$; classification uses zero/one loss or surrogate losses.

**Key formulas:**
- Expected loss: $\varepsilon = \mathbb{E}_{(x,y)\sim\mathcal{D}}[\ell(y, f(x))]$
- Training error: $\hat{\varepsilon} = \frac{1}{N}\sum_{n=1}^{N} \ell(y_n, f(x_n))$
- Classification evaluation: Accuracy, Precision, Recall, F1-score, ROC-AUC
- Regression evaluation: MSE, RMSE, MAE, $R^2$

**Key insight:** The fundamental trade-off in ML is between underfitting (model too simple, high bias) and overfitting (model too complex, high variance). The "inductive bias" of a learning algorithm determines which solutions it prefers when data alone is insufficient.

**Diagram suggestion:** YES -- a bias-variance trade-off diagram showing error vs. model complexity.

**Citation:** `\cite[pp.~8--25]{iiiCourseMachineLearning}`

#### 1.2 Supervised & Unsupervised Learning

**Core concept:** Supervised learning uses labeled training data to learn a mapping from inputs to outputs (classification, regression). Unsupervised learning works with unlabeled data to discover hidden structure (clustering, dimensionality reduction). The key distinction: classification asks "which known class does x belong to?" while clustering asks "what natural groups exist in the data?"

**Key insight:** Classification algorithms (logistic regression, SVM, random forest, k-NN) optimize a loss function with respect to known labels. Clustering algorithms (k-means, DBSCAN, hierarchical clustering, GMM) optimize within-cluster cohesion and between-cluster separation without labels.

**Diagram suggestion:** YES -- a mind-map showing ML taxonomy: Supervised (Classification, Regression) vs Unsupervised (Clustering, Dimensionality Reduction) vs Reinforcement Learning.

**Citation:** `\cite[pp.~323--324]{hurbansGrokkingArtificialIntelligence2020}`

#### 1.3 Reinforcement Learning

**Core concept:** Reinforcement learning (RL) is an area of ML inspired by behavioral psychology where an agent learns through cumulative rewards or penalties for actions taken in a dynamic environment. Unlike supervised learning (labels given) or unsupervised learning (no labels), RL uses feedback from actions to learn which actions or sequences of actions are most beneficial toward an ultimate goal.

**Key formulas -- Q-Learning update (Bellman equation adaptation):**
$$Q(s, a) \leftarrow (1 - \alpha) \cdot Q(s, a) + \alpha \cdot \bigl(r + \gamma \cdot \max_{a'} Q(s', a')\bigr)$$
where $\alpha$ is the learning rate, $\gamma$ is the discount factor, $r$ is the immediate reward, $s'$ is the next state, and $\max_{a'} Q(s', a')$ is the maximum Q-value over all actions in the next state.

**Key components:**
- **Agent:** The learner/decision maker
- **Environment:** The world the agent interacts with
- **State:** Current situation of the agent
- **Action:** Choices available to the agent
- **Reward:** Feedback signal (positive or negative)
- **Markov Decision Process (MDP):** Mathematical framework for RL

**Life cycle:** Initialize Q-table -> For each episode: observe state -> choose action (exploration vs exploitation) -> receive reward -> update Q-table -> repeat until convergence.

**Key insight:** RL balances exploration (trying new actions) vs exploitation (using known good actions). The discount factor $\gamma$ controls how much the agent values future rewards vs immediate rewards. RL is most useful for sequential decision problems (games, robotics, strategic planning).

**Diagram suggestion:** YES -- the Agent-Environment interaction loop (Agent -> Action -> Environment -> State/Reward -> Agent).

**Citation:** `\cite[pp.~323--345]{hurbansGrokkingArtificialIntelligence2020}`

---

### 2. CLUSTERING

#### 2.1 Introduction to Clustering

**Core concept:** Clustering is unsupervised learning that partitions data into groups (clusters) such that objects within a cluster are more similar to each other than to objects in other clusters. There are no predefined class labels; the algorithm discovers structure from the data alone.

**Key evaluation metrics:**
- Silhouette coefficient: measures how similar an object is to its own cluster vs. neighboring clusters
- Within-cluster sum of squares (WCSS/inertia)
- Between-cluster variance
- Domain expert judgment

**Major clustering families:**
- Partitioning methods (K-means): divide data into K non-overlapping clusters
- Hierarchical methods: build nested cluster hierarchy (agglomerative or divisive)
- Density-based methods (DBSCAN): find arbitrarily shaped clusters as dense regions
- Model-based methods (GMM/EM): assume data generated from mixture of distributions

**Citation:** `\cite[pp.~166--168]{iiiCourseMachineLearning}`, `\cite[pp.~443--445]{hanDataMiningConcepts2012}`

#### 2.2 K-Means

**Core concept:** K-means partitions N data points into K clusters by alternating between (1) assigning each point to its nearest cluster centroid and (2) recomputing each centroid as the mean of its assigned points. The algorithm minimizes the within-cluster sum of squared distances.

**Key formula -- K-Means objective:**
$$\mathcal{L}(\mathbf{z}, \boldsymbol{\mu}) = \sum_{k=1}^{K} \sum_{n:\, z_n = k} \|\mathbf{x}_n - \boldsymbol{\mu}_k\|^2$$

**Algorithm:**
1. Initialize $K$ cluster centers $\boldsymbol{\mu}_1, \ldots, \boldsymbol{\mu}_K$ (randomly or via K-means++)
2. **Assign:** $z_n \leftarrow \arg\min_k \|\mathbf{x}_n - \boldsymbol{\mu}_k\|^2$ for each data point $n$
3. **Update:** $\boldsymbol{\mu}_k \leftarrow \frac{1}{|C_k|}\sum_{n \in C_k} \mathbf{x}_n$ for each cluster $k$
4. Repeat steps 2--3 until convergence

**Initialization -- K-means++ (p. 168-169):**
- First center chosen uniformly at random
- Each subsequent center chosen with probability proportional to $D(\mathbf{x})^2$ (squared distance to nearest existing center)
- Guarantee: $\mathbb{E}[\hat{\mathcal{L}}] \leq 8(\log K + 2)\mathcal{L}^{(\text{opt})}$

**Choosing K:**
- Elbow method: plot WCSS vs K, pick the "elbow"
- BIC: $\arg\min_K \hat{\mathcal{L}}_K + K\log D$
- AIC: $\arg\min_K \hat{\mathcal{L}}_K + 2KD$

**Key insight:** K-means always converges (monotonically decreasing objective) but only to a local optimum. Initialization matters greatly. Assumes spherical, equally-sized clusters. Complexity: $O(nKdT)$ where $n$ = points, $K$ = clusters, $d$ = dimensions, $T$ = iterations.

**Diagram suggestion:** YES -- step-by-step illustration showing initial random centroids, assignment, update, convergence.

**Citation:** `\cite[pp.~166--170]{iiiCourseMachineLearning}`

#### 2.3 Expectation Maximization (EM)

**Core concept:** EM is a general iterative algorithm for maximum likelihood estimation in models with latent (hidden) variables. In clustering, EM fits a Gaussian Mixture Model (GMM) where each cluster is modeled as a Gaussian distribution. Unlike K-means (hard assignments), EM computes soft (probabilistic) cluster memberships.

**Key formulas -- GMM with EM:**

**E-step** (compute responsibilities / soft assignments):
$$z_{n,k} = \frac{\theta_k \, \mathcal{N}(\mathbf{x}_n \mid \boldsymbol{\mu}_k, \boldsymbol{\Sigma}_k)}{\sum_{j=1}^{K} \theta_j \, \mathcal{N}(\mathbf{x}_n \mid \boldsymbol{\mu}_j, \boldsymbol{\Sigma}_j)}$$

**M-step** (re-estimate parameters):
$$\theta_k = \frac{1}{N}\sum_{n=1}^{N} z_{n,k}, \qquad \boldsymbol{\mu}_k = \frac{\sum_n z_{n,k}\,\mathbf{x}_n}{\sum_n z_{n,k}}, \qquad \boldsymbol{\Sigma}_k = \frac{\sum_n z_{n,k}(\mathbf{x}_n - \boldsymbol{\mu}_k)(\mathbf{x}_n - \boldsymbol{\mu}_k)^\top}{\sum_n z_{n,k}}$$

**General EM principle:**
- Log-likelihood: $\ell(\boldsymbol{\theta}) = \sum_n \log \sum_{y_n} p(\mathbf{x}_n, y_n \mid \boldsymbol{\theta})$
- Maximizes a lower bound via Jensen's inequality; each iteration is guaranteed to increase (or maintain) $\ell(\boldsymbol{\theta})$

**Key insight:** EM generalizes K-means: when GMM covariances are forced to be $\sigma^2 \mathbf{I}$ and $\sigma \to 0$, the soft assignments become hard and EM reduces to K-means. EM can model elliptical clusters of different sizes and shapes, while K-means cannot.

**Diagram suggestion:** YES -- comparison of K-means (hard, circular boundaries) vs EM (soft, elliptical boundaries) on the same data.

**Citation:** `\cite[pp.~175--180]{iiiCourseMachineLearning}`

#### 2.4 DBSCAN

**Core concept:** DBSCAN (Density-Based Spatial Clustering of Applications with Noise) discovers clusters as dense regions of points separated by regions of low density. It does not require specifying the number of clusters beforehand and can find arbitrarily shaped clusters while marking low-density points as noise/outliers.

**Key parameters:**
- $\varepsilon$ (eps): radius of a neighborhood
- MinPts: minimum number of points to form a dense region

**Key definitions:**
- **Core point:** has at least MinPts neighbors within radius $\varepsilon$
- **Border point:** within $\varepsilon$ of a core point but has fewer than MinPts neighbors itself
- **Noise point:** neither core nor border -- an outlier
- **Directly density-reachable:** point $q$ is directly density-reachable from core point $p$ if $q \in N_\varepsilon(p)$
- **Density-connected:** $p$ and $q$ are density-connected if there exists a point $o$ such that both $p$ and $q$ are density-reachable from $o$

**Algorithm:**
1. For each unvisited point $p$: find $N_\varepsilon(p)$
2. If $|N_\varepsilon(p)| \geq \text{MinPts}$: start new cluster, expand by finding all density-reachable points
3. Else: mark $p$ as noise (may later become border point)

**Key insight:** DBSCAN requires no preset $K$, naturally identifies outliers, and finds non-convex clusters. However, it struggles with clusters of varying densities and is sensitive to the choice of $\varepsilon$ and MinPts. Complexity: $O(n \log n)$ with spatial indexing (e.g., R-tree), $O(n^2)$ without.

**Diagram suggestion:** YES -- show core points, border points, and noise points in a 2D scatter, with $\varepsilon$-neighborhoods drawn.

**Citation:** `\cite[pp.~471--477]{hanDataMiningConcepts2012}`

#### 2.5 Hierarchical Clustering

**Core concept:** Hierarchical clustering builds a tree-like nested decomposition of data (a dendrogram). Agglomerative (bottom-up) starts with each point as its own cluster and merges the two closest clusters at each step. Divisive (top-down) starts with one cluster and recursively splits.

**Linkage criteria (distance between clusters):**
- **Single linkage:** $d(C_i, C_j) = \min_{p \in C_i, q \in C_j} d(p, q)$ -- tends to produce long, chain-shaped clusters
- **Complete linkage:** $d(C_i, C_j) = \max_{p \in C_i, q \in C_j} d(p, q)$ -- produces compact, spherical clusters
- **Average linkage (UPGMA):** $d(C_i, C_j) = \frac{1}{|C_i||C_j|}\sum_{p \in C_i}\sum_{q \in C_j} d(p, q)$ -- compromise
- **Ward's method:** merges pair that minimizes increase in total within-cluster variance

**Algorithm (Agglomerative):**
1. Start: each data point is its own cluster
2. Compute distance matrix between all cluster pairs
3. Merge the two closest clusters
4. Update distance matrix
5. Repeat until one cluster (or desired $K$ clusters) remain
6. Cut the dendrogram at desired level to obtain $K$ clusters

**Key insight:** The dendrogram provides a complete hierarchy -- no need to specify $K$ in advance (cut at any level). However, merges are irreversible, making the algorithm sensitive to early decisions. Complexity: $O(n^2 \log n)$ for efficient implementations, $O(n^3)$ naive.

**Diagram suggestion:** YES -- a dendrogram showing the merge history of 6-8 data points.

**Citation:** `\cite[pp.~457--467]{hanDataMiningConcepts2012}`

---

### 3. REGRESSION

#### 3.1 Linear & Non-linear Regression

**Core concept:** Linear regression fits a linear function $\hat{y} = \mathbf{w}^\top \mathbf{x} + b$ to minimize the sum of squared residuals. Non-linear regression extends this to polynomial or other basis function expansions $\hat{y} = \sum_j w_j \phi_j(\mathbf{x})$, which is still linear in the parameters.

**Key formulas:**
- Ordinary Least Squares (OLS): $\min_{\mathbf{w}} \|\mathbf{X}\mathbf{w} - \mathbf{y}\|^2$
- Normal equation: $\hat{\mathbf{w}} = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y}$
- Polynomial regression (degree $d$): feature map $\mathbf{x} \mapsto [1, x, x^2, \ldots, x^d]$, then apply linear regression in the expanded feature space

**Key insight:** The model is "linear" in the parameters, not necessarily in the input features. Polynomial regression of degree $d$ can overfit for large $d$; regularization (Ridge/Lasso) is needed to control complexity. The bias-variance trade-off is directly visible: degree 1 = high bias, high degree = high variance.

**Diagram suggestion:** YES -- plot showing data points with linear fit, quadratic fit, and high-degree polynomial overfitting.

**Citation:** `\cite[pp.~86--97]{iiiCourseMachineLearning}`, `\cite{fischerMaschinellesLernenDummies2024}` (Kapitel 9)

#### 3.2 Logistic Regression

**Core concept:** Despite its name, logistic regression is a classification method. It models the probability of class membership using the logistic (sigmoid) function. For binary classification, it maps a linear combination of features to a probability in $[0, 1]$.

**Key formulas:**
- Sigmoid function: $\sigma(z) = \frac{1}{1 + e^{-z}}$
- Model: $P(y = 1 \mid \mathbf{x}) = \sigma(\mathbf{w}^\top \mathbf{x} + b) = \frac{1}{1 + \exp[-(\mathbf{w}^\top \mathbf{x} + b)]}$
- Log-odds (logit): $\log\frac{P(y=1|\mathbf{x})}{1 - P(y=1|\mathbf{x})} = \mathbf{w}^\top\mathbf{x} + b$
- Logistic loss: $\ell^{(\log)}(y, \hat{y}) = \log(1 + \exp[-y \hat{y}])$
- Trained via maximum likelihood / gradient descent (no closed-form solution)

**Key insight:** Logistic regression is the linear model analog for classification. It provides calibrated probabilities (unlike SVM), is computationally efficient, and serves as a building block for neural networks (the sigmoid activation). The logistic loss is a smooth, convex surrogate for the 0/1 loss.

**Diagram suggestion:** YES -- S-shaped sigmoid curve mapping $\mathbf{w}^\top\mathbf{x}$ to probability.

**Citation:** `\cite[pp.~89--90]{iiiCourseMachineLearning}`, `\cite[pp.~402--403]{hanDataMiningConcepts2012}`

#### 3.3 Quantile Regression

**Core concept:** Unlike ordinary regression (which estimates the conditional mean), quantile regression estimates conditional quantiles (e.g., median, 10th percentile, 90th percentile) of the response variable. This is especially useful when the distribution of the response is asymmetric or when one is interested in the tails of the distribution.

**Key formula -- Quantile loss (check function/pinball loss):**
$$\rho_\tau(u) = u \cdot (\tau - \mathbf{1}_{u < 0}) = \begin{cases} \tau \cdot u & \text{if } u \geq 0 \\ (\tau - 1) \cdot u & \text{if } u < 0 \end{cases}$$
where $\tau \in (0, 1)$ is the quantile level and $u = y - \hat{y}$.

- Objective: $\min_{\mathbf{w}} \sum_{n=1}^{N} \rho_\tau(y_n - \mathbf{w}^\top\mathbf{x}_n)$
- For $\tau = 0.5$: reduces to median regression (minimizes mean absolute error)

**Key insight:** Quantile regression provides a more complete picture of the conditional distribution than mean regression alone. It is robust to outliers (especially median regression) and does not assume normality or homoscedasticity. Multiple quantiles together give prediction intervals.

**Diagram suggestion:** OPTIONAL -- showing multiple quantile regression lines ($\tau = 0.1, 0.5, 0.9$) on a scatter plot.

**Citation:** Based on general ML knowledge; no specific page from provided sources. Recommend citing Koenker, R. (2005), Quantile Regression, Cambridge University Press.

#### 3.4 Multivariate Regression

**Core concept:** Multivariate regression extends simple linear regression to multiple input features (multiple regression: multiple predictors, one response) or multiple output variables (multivariate: multiple responses simultaneously). The model becomes $\hat{\mathbf{Y}} = \mathbf{X}\mathbf{W}$ where $\mathbf{W}$ is a matrix of coefficients.

**Key formulas:**
- Multiple regression: $\hat{y} = w_0 + w_1 x_1 + w_2 x_2 + \cdots + w_D x_D = \mathbf{w}^\top \mathbf{x}$
- Normal equation (same form): $\hat{\mathbf{W}} = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{Y}$
- For $D$ features and $K$ response variables: $\mathbf{W}$ is a $D \times K$ matrix

**Key insight:** As the number of features grows, multicollinearity becomes a problem (correlated features destabilize $(\mathbf{X}^\top\mathbf{X})^{-1}$). This motivates regularization techniques (Ridge, Lasso). Feature selection becomes critical. The curse of dimensionality means that with $D$ features, you need exponentially more data to maintain the same estimation quality.

**Diagram suggestion:** OPTIONAL -- 3D scatter with regression plane for 2-predictor case.

**Citation:** `\cite[pp.~86--97]{iiiCourseMachineLearning}`

#### 3.5 Lasso & Ridge Regression

**Core concept:** Lasso and Ridge regression add penalty terms to OLS to prevent overfitting. Ridge (L2) shrinks all coefficients uniformly; Lasso (L1) drives some coefficients exactly to zero, performing automatic feature selection.

**Key formulas:**

**Ridge Regression (L2 regularization):**
$$\min_{\mathbf{w}} \frac{1}{2}\|\mathbf{X}\mathbf{w} - \mathbf{y}\|^2 + \frac{\lambda}{2}\|\mathbf{w}\|_2^2$$
- Closed-form solution: $\hat{\mathbf{w}} = (\mathbf{X}^\top\mathbf{X} + \lambda\mathbf{I})^{-1}\mathbf{X}^\top\mathbf{y}$
- Regularizer: $\|\mathbf{w}\|_2^2 = \sum_d w_d^2$
- Effect: shrinks all weights toward zero but never exactly to zero

**Lasso Regression (L1 regularization):**
$$\min_{\mathbf{w}} \frac{1}{2}\|\mathbf{X}\mathbf{w} - \mathbf{y}\|^2 + \lambda\|\mathbf{w}\|_1$$
- No closed-form solution (requires iterative methods: coordinate descent, ISTA)
- Regularizer: $\|\mathbf{w}\|_1 = \sum_d |w_d|$
- Effect: drives some weights exactly to zero $\Rightarrow$ sparse models / feature selection

**Elastic Net (combines both):**
$$\min_{\mathbf{w}} \frac{1}{2}\|\mathbf{X}\mathbf{w} - \mathbf{y}\|^2 + \lambda_1\|\mathbf{w}\|_1 + \lambda_2\|\mathbf{w}\|_2^2$$

**Key insight:** Smaller $p$-norms (L1 vs L2) yield sparser solutions. Ridge handles multicollinearity well (stable solution even when $\mathbf{X}^\top\mathbf{X}$ is ill-conditioned). Lasso performs feature selection, producing interpretable models. The parameter $\lambda$ controls the bias-variance trade-off: $\lambda \to 0$ gives OLS (low bias, high variance); $\lambda \to \infty$ gives null model (high bias, low variance).

**Diagram suggestion:** YES -- geometric interpretation: L1 constraint (diamond) vs L2 constraint (circle) in 2D weight space, showing why L1 produces sparse solutions (corners of the diamond).

**Citation:** `\cite[pp.~91--97]{iiiCourseMachineLearning}`, `\cite{fischerMaschinellesLernenDummies2024}` (Kapitel 9: Lasso-Regression, Ridge-Regression)

---

### 4. SUPPORT VECTOR MACHINES

#### 4.1 Introduction to SVMs

**Core concept:** A Support Vector Machine is a discriminative classifier that finds the maximum margin hyperplane separating two classes. It transforms the original data into a higher-dimensional space (via the kernel trick) where a linear separator can be found, enabling non-linear decision boundaries in the original input space.

**Key formulas:**

**Separating hyperplane:** $\mathbf{w} \cdot \mathbf{x} + b = 0$

**Margin:** $\gamma = \frac{2}{\|\mathbf{w}\|}$ (distance between the two margin hyperplanes)

**Hard-margin SVM optimization:**
$$\min_{\mathbf{w},b} \frac{1}{2}\|\mathbf{w}\|^2 \quad \text{s.t.} \quad y_n(\mathbf{w}\cdot\mathbf{x}_n + b) \geq 1 \; \forall n$$

**Soft-margin SVM (allows misclassification):**
$$\min_{\mathbf{w},b,\boldsymbol{\xi}} \frac{1}{2}\|\mathbf{w}\|^2 + C\sum_{n=1}^{N}\xi_n \quad \text{s.t.} \quad y_n(\mathbf{w}\cdot\mathbf{x}_n + b) \geq 1 - \xi_n, \; \xi_n \geq 0$$

**Decision function (via support vectors):**
$$d(\mathbf{x}) = \text{sign}\left(\sum_{i=1}^{l} y_i \alpha_i K(\mathbf{x}_i, \mathbf{x}) + b_0\right)$$

**Key insight:** The complexity of the learned classifier depends on the number of support vectors, not the dimensionality of the feature space. This makes SVMs resistant to overfitting even in very high dimensions. The $C$ parameter trades off margin width vs classification errors.

**Diagram suggestion:** YES -- 2D plot showing the maximum margin hyperplane with support vectors highlighted on both sides.

**Citation:** `\cite[pp.~98--101]{iiiCourseMachineLearning}`, `\cite[pp.~408--413]{hanDataMiningConcepts2012}`

#### 4.2 SVM for Classification

**Core concept:** SVMs excel at binary classification. For non-linearly separable data, the kernel trick maps data into a high-dimensional feature space where a linear separator exists, without explicitly computing the transformation.

**Key kernels:**
- **Polynomial kernel:** $K(\mathbf{x}_i, \mathbf{x}_j) = (\mathbf{x}_i \cdot \mathbf{x}_j + 1)^h$
- **Gaussian RBF kernel:** $K(\mathbf{x}_i, \mathbf{x}_j) = \exp\left(-\frac{\|\mathbf{x}_i - \mathbf{x}_j\|^2}{2\sigma^2}\right)$
- **Sigmoid kernel:** $K(\mathbf{x}_i, \mathbf{x}_j) = \tanh(\kappa \, \mathbf{x}_i \cdot \mathbf{x}_j - \delta)$

**Kernel trick essence:** $K(\mathbf{x}_i, \mathbf{x}_j) = \phi(\mathbf{x}_i) \cdot \phi(\mathbf{x}_j)$ -- compute dot products in the high-dimensional space without ever explicitly constructing $\phi(\mathbf{x})$.

**Multiclass extension:** One-vs-One (train $\binom{K}{2}$ classifiers) or One-vs-All (train $K$ classifiers).

**Key insight:** SVM training always finds a global optimum (convex QP), unlike neural networks which have many local minima. The kernel chosen does not generally make a large difference in accuracy in practice.

**Diagram suggestion:** Already covered in 4.1.

**Citation:** `\cite[pp.~128--140]{iiiCourseMachineLearning}`, `\cite[pp.~413--415]{hanDataMiningConcepts2012}`

#### 4.3 SVM for Regression (SVR)

**Core concept:** Support Vector Regression uses the same maximum-margin principle but for regression. Instead of minimizing all residuals, SVR tolerates errors up to $\varepsilon$ (the $\varepsilon$-insensitive tube) and only penalizes predictions that fall outside this tube.

**Key formula -- $\varepsilon$-SVR:**
$$\min_{\mathbf{w},b,\boldsymbol{\xi},\boldsymbol{\xi}^*} \frac{1}{2}\|\mathbf{w}\|^2 + C\sum_{n=1}^{N}(\xi_n + \xi_n^*)$$
subject to:
$$y_n - \mathbf{w}\cdot\mathbf{x}_n - b \leq \varepsilon + \xi_n, \quad \mathbf{w}\cdot\mathbf{x}_n + b - y_n \leq \varepsilon + \xi_n^*, \quad \xi_n, \xi_n^* \geq 0$$

**Key insight:** SVR produces sparse solutions (only data points outside the $\varepsilon$-tube contribute as support vectors). The $\varepsilon$ parameter controls the width of the "tube of indifference." Like classification SVMs, kernels can be used for non-linear regression.

**Diagram suggestion:** YES -- regression line with the $\varepsilon$-tube shown and support vectors highlighted outside the tube.

**Citation:** `\cite[pp.~98--101]{iiiCourseMachineLearning}`

---

### 5. DECISION TREES

#### 5.1 Introduction to Decision Trees

**Core concept:** A decision tree is a divide-and-conquer model where internal nodes represent tests on features, branches represent outcomes, and leaf nodes represent predictions (class labels or values). The tree is built greedily by selecting at each node the feature that best separates the data.

**Key algorithm -- Greedy construction (ID3/C4.5/CART):**
1. If all examples have the same label (or no features remain): create LEAF with majority label
2. For each feature $f$: compute a splitting criterion score
3. Select the feature with the best score; create internal node
4. Partition data by feature values; recurse on each partition

**Splitting criteria:**
- **Information Gain** (used by ID3/C4.5): $\text{Gain}(A) = H(D) - \sum_{v} \frac{|D_v|}{|D|} H(D_v)$
  where $H(D) = -\sum_k p_k \log_2 p_k$ (entropy)
- **Gain Ratio** (C4.5): $\text{GainRatio}(A) = \frac{\text{Gain}(A)}{\text{SplitInfo}(A)}$ -- corrects bias toward multi-valued attributes
- **Gini Index** (CART): $\text{Gini}(D) = 1 - \sum_{k} p_k^2$

**Pruning:** Prevents overfitting by removing branches that provide little predictive power:
- Pre-pruning: stop growing when improvement is below a threshold
- Post-pruning: grow full tree, then remove subtrees that don't improve validation accuracy

**Key insight:** Decision trees are highly interpretable ("white box") models. Their inductive bias favors short trees (Occam's Razor). They handle both numerical and categorical features natively. However, they are unstable (small data changes can produce very different trees) and tend to overfit. This motivates ensemble methods (Random Forest, Gradient Boosting).

**Diagram suggestion:** YES -- a small decision tree (3-4 levels) with feature tests at nodes and class labels at leaves.

**Citation:** `\cite[pp.~8--20]{iiiCourseMachineLearning}`, `\cite[pp.~330--344]{hanDataMiningConcepts2012}`

#### 5.2 Decision Trees for Classification

**Core concept:** Classification trees predict class labels. At each leaf, the predicted class is the majority class of training examples reaching that leaf. The tree construction optimizes a purity criterion (Information Gain, Gini Index) to create leaves that are as "pure" as possible.

**Key formulas:**
- **Entropy:** $H(D) = -\sum_{k=1}^{K} p_k \log_2 p_k$ where $p_k$ = fraction of class $k$ in dataset $D$
- **Gini impurity:** $\text{Gini}(D) = 1 - \sum_{k=1}^{K} p_k^2$
- **Information Gain:** $\text{Gain}(D, A) = H(D) - \sum_{v \in \text{Values}(A)} \frac{|D_v|}{|D|} H(D_v)$

**Key insight:** C4.5 (Quinlan, 1993) uses Gain Ratio to avoid bias toward features with many values. CART (Breiman et al., 1984) uses Gini and always creates binary splits. Random Forests aggregate many trees trained on bootstrap samples with random feature subsets to reduce variance.

**Citation:** `\cite[pp.~330--344]{hanDataMiningConcepts2012}`, `\cite[pp.~8--20]{iiiCourseMachineLearning}`

#### 5.3 Decision Trees for Regression

**Core concept:** Regression trees predict continuous values instead of class labels. At each leaf, the prediction is the mean (or median) of training target values reaching that leaf. Splits are chosen to minimize variance (or squared error) of the target variable within each partition.

**Key formula -- Splitting criterion for regression:**
$$\text{Minimize:} \quad \sum_{n \in D_{\text{left}}} (y_n - \bar{y}_{\text{left}})^2 + \sum_{n \in D_{\text{right}}} (y_n - \bar{y}_{\text{right}})^2$$

**Key insight:** Regression trees create a piecewise-constant approximation of the target function. Ensemble methods (Random Forests, Gradient Boosted Trees) dramatically improve performance. Gradient Boosted Regression Trees (GBRT) are among the most successful ML algorithms for structured/tabular data.

**Diagram suggestion:** OPTIONAL -- step function approximation produced by a regression tree.

**Citation:** `\cite[pp.~8--20]{iiiCourseMachineLearning}`

---

### 6. GENETIC ALGORITHMS

#### 6.1 Introduction to Genetic Algorithms

**Core concept:** A genetic algorithm (GA) is a metaheuristic optimization technique inspired by biological evolution. It maintains a population of candidate solutions (chromosomes) that evolve over generations through selection, crossover (recombination), and mutation to find good solutions to optimization problems.

**Key terminology:**
- **Chromosome:** A candidate solution, consisting of genes
- **Gene:** A single unit/position in the chromosome
- **Allele:** The value stored in a gene
- **Genotype:** The encoded representation (e.g., binary string)
- **Phenotype:** The actual solution the genotype represents
- **Population:** A collection of chromosomes
- **Fitness function:** Evaluates how good a solution is

**GA Life Cycle:**
1. **Encode solution space** -- choose representation (binary, real-valued, permutation)
2. **Set parameters** -- population size, mutation rate, crossover rate, number of generations
3. **Create initial population** -- random valid solutions
4. **Evaluate fitness** -- compute fitness for each individual
5. **Select parents** -- based on fitness (roulette wheel, tournament selection)
6. **Reproduce offspring** -- crossover + mutation
7. **Populate next generation** -- select survivors
8. **Repeat** steps 4-7 until stopping condition (convergence, max generations, fitness threshold)

**Crossover operators:**
- **Single-point crossover:** One cut point; swap tails between parents
- **Two-point crossover:** Two cut points; swap middle segment
- **Uniform crossover:** Each gene independently chosen from either parent (via a mask)

**Mutation:** Randomly flip bits (binary) or perturb values (real-valued) with a small probability. Maintains diversity and prevents premature convergence.

**Selection probability (roulette wheel):**
$$P_i = \frac{f_i}{\sum_{j=1}^{N} f_j}$$
where $f_i$ is the fitness of individual $i$.

**Key insight:** GAs balance exploration (mutation, diverse initial population) and exploitation (selection of fit individuals). They don't require the fitness function to be differentiable, continuous, or even mathematically defined -- only evaluable. They find "good enough" solutions efficiently for problems where brute force is infeasible (e.g., Knapsack Problem: brute force $2^{26} \approx 67M$ evaluations vs GA $\sim$10K-100K evaluations with comparable quality).

**Diagram suggestion:** YES -- the GA life cycle flowchart (8 steps), and a diagram of single-point crossover on binary chromosomes.

**Citation:** `\cite[pp.~91--127]{hurbansGrokkingArtificialIntelligence2020}`

#### 6.2 Applications of Genetic Algorithms

**Core concept:** GAs are applicable to a wide range of optimization problems, especially those with large, complex, or discontinuous search spaces where gradient-based methods fail.

**Application domains:**
- **Combinatorial optimization:** Traveling Salesman Problem, Knapsack Problem, scheduling, bin packing
- **Engineering design:** structural optimization, circuit design, antenna design
- **Machine learning:** hyperparameter tuning, neural architecture search, feature selection
- **Bioinformatics:** protein folding, gene regulatory network inference
- **Finance:** portfolio optimization, trading strategy development
- **Robotics:** path planning, controller design
- **Game AI:** evolving strategies, level generation

**Configurable parameters that affect performance:**
- **Chromosome encoding:** must match the problem domain (binary, real-value, order/permutation, tree)
- **Population size:** larger = more diversity but slower computation
- **Mutation rate:** too low = premature convergence; too high = random search
- **Crossover rate:** controls how much genetic material is exchanged
- **Selection pressure:** balance between exploiting best solutions and maintaining diversity
- **Stopping condition:** fixed generations, fitness threshold, or stagnation detection

**Key insight:** Genetic algorithms are robust to noise in the fitness function (stochastic character) and do not require gradient information, making them suitable for black-box optimization. However, they provide no guarantee of finding the global optimum and can be computationally expensive compared to specialized algorithms when such algorithms exist.

**Diagram suggestion:** OPTIONAL -- comparison table: brute force vs GA performance (iterations, time, solution quality).

**Citation:** `\cite[pp.~91--127]{hurbansGrokkingArtificialIntelligence2020}`, `\cite{fischerMaschinellesLernenDummies2024}` (Kapitel 6: Genetische Algorithmen)

---

## Summary of Sources Consulted

| Source | BibTeX Key | Sections Used | Pages |
|--------|-----------|---------------|-------|
| Daume III -- A Course in Machine Learning | `iiiCourseMachineLearning` | Decision Trees, Linear Models, SVM, Kernels, K-Means, EM | pp. 8-20, 86-101, 128-140, 166-180 |
| Hurbans -- Grokking AI Algorithms | `hurbansGrokkingArtificialIntelligence2020` | Genetic Algorithms, Reinforcement Learning | pp. 91-127, 323-345 |
| Han et al. -- Data Mining: Concepts and Techniques | `hanDataMiningConcepts2012` | DBSCAN, Hierarchical Clustering, Decision Trees, SVM, Classification | pp. 330-344, 408-415, 457-477 |
| Fischer -- Maschinelles Lernen fur Dummies | `fischerMaschinellesLernenDummies2024` | Regression (Linear, Lasso, Ridge, Polynomial), Clustering, GA, SVM | Kapitel 6-9 |

---

## Diagram Recommendations Summary

| Section | Diagram Type | Priority |
|---------|-------------|----------|
| Intro: ML Taxonomy | Mind-map: Supervised/Unsupervised/RL | HIGH |
| Reinforcement Learning | Agent-Environment loop (MDP cycle) | HIGH |
| K-Means | Step-by-step iteration visualization | HIGH |
| EM vs K-Means | Side-by-side comparison (hard vs soft) | MEDIUM |
| DBSCAN | Core/Border/Noise point illustration | HIGH |
| Hierarchical Clustering | Dendrogram | HIGH |
| Linear vs Polynomial Regression | Fit comparison plot | MEDIUM |
| Logistic Regression | Sigmoid curve | MEDIUM |
| Lasso vs Ridge | L1 diamond vs L2 circle in weight space | HIGH |
| SVM | Max-margin hyperplane with support vectors | HIGH |
| Decision Tree | Example tree with feature tests at nodes | HIGH |
| Genetic Algorithm | Life cycle flowchart + crossover diagram | HIGH |
