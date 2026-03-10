# Chapter 5, Sections 3–7 — LaTeX Content

Paste this block into `ch05-machine-learning.tex`, replacing the stub lines from `\section{Regression}` through (but not including) `\section{Literature}`.

```latex
    \section{Regression}

    % ---- 5.3.1 Linear & Non-linear Regression -------------------------------------------------------
    \subsection{Linear \& Non-linear Regression}

    \begin{tcbitemize}[ skin=sectionraster ]
        \tcbitem[title={Linear Regression and the Normal Equation}, raster multicolumn=6]
        Linear regression fits a linear function $\hat{y} = \mathbf{w}^\top \mathbf{x} + b$ by minimizing the sum of squared residuals (Ordinary Least Squares)\textsuperscript{\cite[][pp.~86--90]{iiiCourseMachineLearning}}. When the design matrix $\mathbf{X}$ has full column rank, the unique minimizer is given in closed form by the normal equation.
        \tcblower
        \begin{equation}
            \underbrace{\min_{\mathbf{w}} \|\mathbf{X}\mathbf{w} - \mathbf{y}\|^2}_{\text{OLS objective}}
            \quad\Longrightarrow\quad
            \hat{\mathbf{w}} = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{y}
        \end{equation}

        \tcbitem[title={Polynomial and Non-linear Regression}, raster multicolumn=6]
        Non-linear regression extends the linear model by mapping inputs through basis functions $\phi_j(\mathbf{x})$, e.g.\ polynomial features $[1, x, x^2, \ldots, x^d]$\textsuperscript{\cite[][pp.~90--97]{iiiCourseMachineLearning}}. The model remains \emph{linear in the parameters} $\mathbf{w}$, so the normal equation still applies. High-degree polynomials can overfit (high variance), motivating regularization.
        \tcblower
        \begin{equation}
            \hat{y} = \sum_{j=0}^{d} w_j\, x^j = \mathbf{w}^\top \boldsymbol{\phi}(x),
            \qquad \boldsymbol{\phi}(x) = [1,\, x,\, x^2,\, \ldots,\, x^d]^\top
        \end{equation}
    \end{tcbitemize}

    % ---- 5.3.2 Logistic Regression ------------------------------------------------------------------
    \subsection{Logistic Regression}

    \begin{tcbitemize}[ skin=sectionraster, halign lower=center ]
        \tcbitem[title={Logistic Regression as a Classification Model}, raster multicolumn=6]
        Despite its name, logistic regression is a \emph{classification} method. It models the probability of class membership by mapping a linear combination of features through the logistic (sigmoid) function $\sigma$, squashing any real value into the interval $[0, 1]$\textsuperscript{\cite[][pp.~89--90]{iiiCourseMachineLearning}}. Training maximizes the likelihood (no closed-form solution; gradient descent is used).
        \tcblower
        \begin{equation}
            P(y = 1 \mid \mathbf{x}) = \sigma\!\left(\mathbf{w}^\top \mathbf{x} + b\right) = \frac{1}{1 + \exp\!\left[-\!\left(\mathbf{w}^\top \mathbf{x} + b\right)\right]}
        \end{equation}

        \tcbitem[title={The Sigmoid Curve and Log-Odds}, raster multicolumn=6]
        The sigmoid function produces the characteristic S-shaped curve shown below\textsuperscript{\cite[][p.89]{iiiCourseMachineLearning}}. In log-odds (logit) form, the model is linear: $\log\frac{P(y=1|\mathbf{x})}{1-P(y=1|\mathbf{x})} = \mathbf{w}^\top\mathbf{x} + b$. The logistic loss $\ell^{(\log)}(y,\hat{y}) = \log(1 + \exp[-y\hat{y}])$ is a smooth, convex surrogate for the 0/1 loss.
        \tcblower
        \begin{tikzpicture}[scale=1.0]
            \begin{scope}[xscale=0.55, yscale=2.2]
                % axes
                \draw[->] (-5.5,0) -- (5.5,0) node[right, font=\small] {$z = \mathbf{w}^\top\mathbf{x}+b$};
                \draw[->] (0,-0.08) -- (0,1.15) node[above, font=\small] {$\sigma(z)$};
                % dashed reference lines
                \draw[dashed, gray!60] (-5.5,1) -- (5.5,1);
                \draw[dashed, gray!60] (-5.5,0.5) -- (5.5,0.5);
                % tick marks
                \foreach \x in {-4,-2,0,2,4} {
                    \draw (\x,0.03) -- (\x,-0.03);
                    \node[below, font=\tiny] at (\x,0) {\x};
                }
                \node[left, font=\tiny] at (0,1)   {$1$};
                \node[left, font=\tiny] at (0,0.5) {$0.5$};
                % sigmoid curve
                \draw[thick, blue!70!black, domain=-5:5, samples=80]
                    plot (\x, {1/(1+exp(-\x))});
                % decision boundary marker
                \filldraw[red] (0,0.5) circle (2pt);
                \node[right, font=\tiny, text=red] at (0.1, 0.58) {decision boundary};
            \end{scope}
        \end{tikzpicture}
    \end{tcbitemize}

    % ---- 5.3.3 Quantile Regression ------------------------------------------------------------------
    \subsection{Quantile Regression}

    \begin{tcbitemize}[ skin=sectionraster ]
        \tcbitem[title={Quantile Regression and the Pinball Loss}, raster multicolumn=6]
        Quantile regression estimates conditional \emph{quantiles} of the response (e.g.\ the median, or the 10th and 90th percentiles) rather than the conditional mean. It is robust to outliers and makes no assumption of normality or homoscedasticity; fitting multiple quantile levels together yields a full prediction interval. The loss function (pinball loss) applies asymmetric linear penalties.
        \tcblower
        \begin{equation}
            \rho_\tau(u) =
            \begin{cases}
                \tau \cdot u       & u \geq 0 \\
                (\tau - 1)\cdot u  & u < 0
            \end{cases},
            \quad
            \min_{\mathbf{w}} \sum_{n=1}^{N} \rho_\tau\!\left(y_n - \mathbf{w}^\top\mathbf{x}_n\right),
            \quad \tau \in (0,1)
        \end{equation}
    \end{tcbitemize}

    % ---- 5.3.4 Multivariate Regression --------------------------------------------------------------
    \subsection{Multivariate Regression}

    \begin{tcbitemize}[ skin=sectionraster ]
        \tcbitem[title={Multiple and Multivariate Regression}, raster multicolumn=6]
        Multiple regression extends linear regression to $D$ input features ($\hat{y} = w_0 + w_1 x_1 + \cdots + w_D x_D$); multivariate regression further allows $K$ response variables simultaneously, with coefficient matrix $\mathbf{W} \in \mathbb{R}^{D \times K}$\textsuperscript{\cite[][pp.~86--97]{iiiCourseMachineLearning}}. The same normal equation applies. As $D$ grows, multicollinearity can destabilize $(\mathbf{X}^\top\mathbf{X})^{-1}$, motivating regularization.
        \tcblower
        \begin{equation}
            \hat{\mathbf{Y}} = \mathbf{X}\mathbf{W},
            \qquad
            \hat{\mathbf{W}} = (\mathbf{X}^\top\mathbf{X})^{-1}\mathbf{X}^\top\mathbf{Y}
            \quad (D \text{ features},\; K \text{ responses})
        \end{equation}
    \end{tcbitemize}

    % ---- 5.3.5 Lasso & Ridge Regression -------------------------------------------------------------
    \subsection{Lasso \& Ridge Regression}

    \begin{tcbitemize}[ skin=sectionraster, halign lower=center ]
        \tcbitem[title={Ridge Regression (L2) and Lasso (L1)}, raster multicolumn=6]
        Regularized regression adds a penalty on the weights to prevent overfitting\textsuperscript{\cite[][pp.~91--97]{iiiCourseMachineLearning}}. Ridge (L2) shrinks all coefficients uniformly and has a closed-form solution. Lasso (L1) drives some coefficients \emph{exactly} to zero, performing automatic feature selection; it requires iterative solvers (coordinate descent, ISTA). The hyperparameter $\lambda$ controls the bias-variance trade-off.
        \tcblower
        \begin{equation}
            \underbrace{\min_{\mathbf{w}} \tfrac{1}{2}\|\mathbf{X}\mathbf{w}-\mathbf{y}\|^2 + \tfrac{\lambda}{2}\|\mathbf{w}\|_2^2}_{\text{Ridge: } \hat{\mathbf{w}}=(\mathbf{X}^\top\mathbf{X}+\lambda\mathbf{I})^{-1}\mathbf{X}^\top\mathbf{y}}
            \qquad
            \underbrace{\min_{\mathbf{w}} \tfrac{1}{2}\|\mathbf{X}\mathbf{w}-\mathbf{y}\|^2 + \lambda\|\mathbf{w}\|_1}_{\text{Lasso: no closed form}}
        \end{equation}

        \tcbitem[title={Elastic Net and the Geometry of Sparsity}, raster multicolumn=6]
        Elastic Net combines both penalties ($\lambda_1\|\mathbf{w}\|_1 + \lambda_2\|\mathbf{w}\|_2^2$), inheriting Lasso's sparsity and Ridge's stability under multicollinearity\textsuperscript{\cite[][pp.~91--97]{iiiCourseMachineLearning}}. The geometric picture below explains \emph{why} L1 gives sparse solutions: the OLS contours first touch the L1 diamond at a corner (where a coordinate is zero), whereas L1 ellipsoid contacts are typically at smooth points.
        \tcblower
        \begin{tikzpicture}[scale=1.1]
            % ---- coordinate axes ----
            \draw[->] (-1.8,0) -- (1.8,0) node[right, font=\small] {$w_1$};
            \draw[->] (0,-1.8) -- (0,1.8) node[above, font=\small] {$w_2$};

            % ---- L2 circle (Ridge constraint) ----
            \draw[thick, blue!70!black] (0,0) circle (1.0);
            \node[blue!70!black, font=\small] at (1.25, 0.85) {L2};

            % ---- L1 diamond (Lasso constraint) ----
            \draw[thick, red!70!black]
                (1.0,0) -- (0,1.0) -- (-1.0,0) -- (0,-1.0) -- cycle;
            \node[red!70!black, font=\small] at (-1.35, 0.55) {L1};

            % ---- OLS contour ellipses (centered off-axis to show contact) ----
            \draw[dashed, gray!70, rotate=20] (0.8,0.5) ellipse (0.6 and 0.35);
            \draw[dashed, gray!70, rotate=20] (0.8,0.5) ellipse (0.9 and 0.6);
            \node[gray!60, font=\tiny] at (1.3,-0.9) {OLS contours};

            % ---- contact points ----
            % L1 corner contact (sparse solution: w1=0 or w2=0)
            \filldraw[red!70!black]  (0, 1.0) circle (2.5pt);
            \node[right, font=\tiny, text=red!70!black] at (0.05, 1.1) {sparse};

            % L2 smooth contact
            \filldraw[blue!70!black] (0.72, 0.69) circle (2.5pt);
            \node[right, font=\tiny, text=blue!70!black] at (0.73, 0.58) {dense};
        \end{tikzpicture}
    \end{tcbitemize}

    % ===========================================================================================
    \section{Support Vector Machines}

    % ---- 5.4.1 Introduction to SVMs ----------------------------------------------------------------
    \subsection{Introduction to Support Vector Machines}

    \begin{tcbitemize}[ skin=sectionraster, halign lower=center ]
        \tcbitem[title={Maximum Margin Hyperplane}, raster multicolumn=6]
        A Support Vector Machine finds the unique hyperplane $\mathbf{w}\cdot\mathbf{x} + b = 0$ that maximizes the geometric margin $\gamma = 2/\|\mathbf{w}\|$ between the two classes\textsuperscript{\cite[][pp.~98--101]{iiiCourseMachineLearning}}. Only the training points closest to the hyperplane — the \emph{support vectors} — determine the solution. The complexity of the learned classifier depends on the number of support vectors, not the dimensionality of the input space.
        \tcblower
        \begin{tikzpicture}[scale=1.05]
            % ---- class A points (circles, top-right) ----
            \foreach \px/\py in {2.8/2.5, 3.5/1.9, 3.1/3.2, 4.0/2.8} {
                \draw[blue!70!black, thick] (\px,\py) circle (4pt);
            }
            % ---- class B points (crosses, bottom-left) ----
            \foreach \px/\py in {0.5/1.2, 1.2/0.6, 0.8/2.0, 1.5/1.5} {
                \draw[red!70!black, thick]
                    (\px-0.12,\py-0.12) -- (\px+0.12,\py+0.12)
                    (\px+0.12,\py-0.12) -- (\px-0.12,\py+0.12);
            }
            % ---- decision hyperplane ----
            \draw[thick, black] (1.0,3.5) -- (3.5,0.3) node[below right, font=\small] {$\mathbf{w}\cdot\mathbf{x}+b=0$};
            % ---- margin hyperplanes ----
            \draw[dashed, gray]  (0.4,3.5) -- (2.9,0.3);
            \draw[dashed, gray]  (1.6,3.5) -- (4.1,0.3) node[below right, font=\tiny, gray] {};
            % ---- margin brace ----
            \draw[<->, thick, gray!80] (0.7,3.5) -- (1.3,3.5)
                node[midway, above, font=\tiny] {$\gamma = \frac{2}{\|\mathbf{w}\|}$};
            % ---- support vector highlights ----
            \filldraw[blue!70!black]  (2.8,2.5) circle (4pt);
            \node[above right, font=\tiny, blue!70!black] at (2.8,2.5) {SV};
            \filldraw[red!70!black]   (1.5,1.5) circle (4pt);
            \node[below right, font=\tiny, red!70!black]  at (1.5,1.5) {SV};
            % ---- legend ----
            \draw[blue!70!black, thick] (4.4,3.2) circle (4pt);
            \node[right, font=\tiny] at (4.55,3.2) {Class $+1$};
            \draw[red!70!black, thick]
                (4.28,2.7)--(4.52,2.7) (4.4,2.58)--(4.4,2.82);
            \node[right, font=\tiny] at (4.55,2.7) {Class $-1$};
        \end{tikzpicture}

        \tcbitem[title={Hard-Margin vs.\ Soft-Margin SVM}, raster multicolumn=6]
        Hard-margin SVM requires the data to be linearly separable; soft-margin SVM introduces slack variables $\xi_n \geq 0$ to allow misclassifications, controlled by the cost parameter $C$\textsuperscript{\cite[][pp.~98--101]{iiiCourseMachineLearning}}. Large $C$ penalizes errors heavily (narrow margin, risk of overfitting); small $C$ permits more errors (wider margin, better generalization).
        \tcblower
        \begin{equation}
            \min_{\mathbf{w},b,\boldsymbol{\xi}}\; \frac{1}{2}\|\mathbf{w}\|^2 + C\sum_{n=1}^{N}\xi_n
            \quad\text{s.t.}\quad
            y_n(\mathbf{w}\cdot\mathbf{x}_n + b) \geq 1 - \xi_n,\;\; \xi_n \geq 0 \;\;\forall n
        \end{equation}
    \end{tcbitemize}

    % ---- 5.4.2 SVM for Classification --------------------------------------------------------------
    \subsection{SVM for Classification}

    \begin{tcbitemize}[ skin=sectionraster ]
        \tcbitem[title={The Kernel Trick}, raster multicolumn=6]
        For non-linearly separable data, the kernel trick maps inputs into a high-dimensional feature space $\phi(\mathbf{x})$ where a linear separator exists — without ever computing $\phi$ explicitly\textsuperscript{\cite[][pp.~128--140]{iiiCourseMachineLearning}}. The decision function depends only on inner products, which the kernel $K(\mathbf{x}_i,\mathbf{x}_j) = \phi(\mathbf{x}_i)\cdot\phi(\mathbf{x}_j)$ computes directly. SVM training always finds a global optimum (convex QP).
        \tcblower
        \begin{tblr}{|Q[l,m,wd=3.2cm]|X|}
            \hline
            \textbf{Kernel}      & \textbf{Formula}                                                                                      \\
            \hline
            Linear               & $K(\mathbf{x}_i,\mathbf{x}_j) = \mathbf{x}_i\cdot\mathbf{x}_j$                                       \\
            \hline
            Polynomial (degree $h$) & $K(\mathbf{x}_i,\mathbf{x}_j) = (\mathbf{x}_i\cdot\mathbf{x}_j + 1)^h$                            \\
            \hline
            Gaussian RBF         & $K(\mathbf{x}_i,\mathbf{x}_j) = \exp\!\left(-\dfrac{\|\mathbf{x}_i-\mathbf{x}_j\|^2}{2\sigma^2}\right)$ \\
            \hline
            Sigmoid              & $K(\mathbf{x}_i,\mathbf{x}_j) = \tanh(\kappa\,\mathbf{x}_i\cdot\mathbf{x}_j - \delta)$              \\
            \hline
        \end{tblr}

        \tcbitem[title={Multiclass SVMs}, raster multicolumn=6]
        SVMs are inherently binary classifiers. Two standard strategies extend them to $K$ classes\textsuperscript{\cite[][pp.~413--415]{hanDataMiningConcepts2012}}. \emph{One-vs-All} trains $K$ classifiers (class $k$ against all others) and assigns the class with the highest decision score. \emph{One-vs-One} trains $\binom{K}{2}$ binary classifiers and uses majority voting. The decision function for a new point is $d(\mathbf{x}) = \operatorname{sign}\!\left(\sum_{i} y_i \alpha_i K(\mathbf{x}_i, \mathbf{x}) + b_0\right)$.
    \end{tcbitemize}

    % ---- 5.4.3 SVM for Regression ------------------------------------------------------------------
    \subsection{SVM for Regression}

    \begin{tcbitemize}[ skin=sectionraster ]
        \tcbitem[title={Support Vector Regression (SVR) and the $\varepsilon$-Tube}, raster multicolumn=6]
        Support Vector Regression applies the maximum-margin principle to regression by defining an $\varepsilon$-insensitive tube around the predicted function\textsuperscript{\cite[][pp.~98--101]{iiiCourseMachineLearning}}. Residuals smaller than $\varepsilon$ incur zero loss; residuals outside the tube are penalized linearly via slack variables $\xi_n, \xi_n^* \geq 0$. Only points outside the tube become support vectors, yielding sparse solutions.
        \tcblower
        \begin{equation}
            \min_{\mathbf{w},b,\boldsymbol{\xi},\boldsymbol{\xi}^*}\; \frac{1}{2}\|\mathbf{w}\|^2 + C\sum_{n=1}^{N}(\xi_n + \xi_n^*)
            \quad\text{s.t.}\quad
            \left|y_n - \mathbf{w}\cdot\mathbf{x}_n - b\right| \leq \varepsilon + \max(\xi_n, \xi_n^*),\;\; \xi_n,\xi_n^* \geq 0
        \end{equation}
    \end{tcbitemize}

    % ===========================================================================================
    \section{Decision Trees \& Ensemble Methods}

    % ---- 5.5.1 Introduction to Decision Trees ------------------------------------------------------
    \subsection{Introduction to Decision Trees}

    \begin{tcbitemize}[ skin=sectionraster, halign lower=center ]
        \tcbitem[title={Decision Trees: Structure and Construction}, raster multicolumn=6]
        A decision tree partitions the feature space recursively: each internal node applies a test on one feature, each branch follows an outcome, and each leaf assigns a prediction\textsuperscript{\cite[][pp.~8--20]{iiiCourseMachineLearning}}. The tree is built greedily (ID3, C4.5, CART) by choosing at each step the feature split that maximizes a purity criterion. Decision trees are highly interpretable but unstable — small data changes can produce very different trees.
        \tcblower
        \begin{tikzpicture}[
            level distance=1.4cm,
            level 1/.style={sibling distance=5.2cm},
            level 2/.style={sibling distance=2.5cm},
            every node/.style={font=\small},
            edge from parent/.style={draw, -}
        ]
            \node[draw, rounded corners, fill=blue!12, minimum width=2.6cm, minimum height=0.6cm]
                {Age $\leq 30$?}
                child {
                    node[draw, rounded corners, fill=blue!12, minimum width=2.2cm, minimum height=0.6cm]
                        {Income $>$ 50k?}
                    child {
                        node[draw, fill=green!25, minimum width=1.6cm, minimum height=0.55cm]
                            {\textbf{Yes}}
                        edge from parent node[left, font=\tiny] {yes}
                    }
                    child {
                        node[draw, fill=red!20, minimum width=1.6cm, minimum height=0.55cm]
                            {\textbf{No}}
                        edge from parent node[right, font=\tiny] {no}
                    }
                    edge from parent node[left, font=\tiny] {yes}
                }
                child {
                    node[draw, rounded corners, fill=blue!12, minimum width=2.2cm, minimum height=0.6cm]
                        {Student?}
                    child {
                        node[draw, fill=green!25, minimum width=1.6cm, minimum height=0.55cm]
                            {\textbf{Yes}}
                        edge from parent node[left, font=\tiny] {yes}
                    }
                    child {
                        node[draw, fill=red!20, minimum width=1.6cm, minimum height=0.55cm]
                            {\textbf{No}}
                        edge from parent node[right, font=\tiny] {no}
                    }
                    edge from parent node[right, font=\tiny] {no}
                };
        \end{tikzpicture}

        \tcbitem[title={Splitting Criteria and Pruning}, raster multicolumn=6]
        The split at each node is chosen to maximize impurity reduction\textsuperscript{\cite[][pp.~330--344]{hanDataMiningConcepts2012}}. Pre-pruning stops growth early (threshold on gain); post-pruning grows a full tree then removes subtrees that do not improve validation accuracy. Both strategies reduce overfitting.
        \tcblower
        \begin{tblr}{|Q[l,m,wd=2.4cm]|X|Q[l,m,wd=2.6cm]|}
            \hline
            \textbf{Algorithm} & \textbf{Splitting criterion}                                           & \textbf{Split type}   \\
            \hline
            ID3                & Information Gain $= H(D) - \sum_v \tfrac{|D_v|}{|D|}H(D_v)$           & Multi-way             \\
            \hline
            C4.5               & Gain Ratio $= \text{Gain}(A)/\text{SplitInfo}(A)$                     & Multi-way             \\
            \hline
            CART               & Gini Index $= 1 - \sum_k p_k^2$                                       & Binary                \\
            \hline
        \end{tblr}
    \end{tcbitemize}

    % ---- 5.5.2 Decision Trees for Classification ----------------------------------------------------
    \subsection{Decision Trees for Classification}

    \begin{tcbitemize}[ skin=sectionraster ]
        \tcbitem[title={Entropy, Gini, and Information Gain}, raster multicolumn=6]
        Classification trees assign the majority class of training examples reaching each leaf\textsuperscript{\cite[][pp.~330--344]{hanDataMiningConcepts2012}}. Purity at a node is measured by \emph{entropy} (used by ID3/C4.5) or the \emph{Gini index} (used by CART). Information Gain selects the feature that reduces entropy the most. C4.5 normalizes by SplitInfo to avoid bias toward features with many distinct values.
        \tcblower
        \begin{equation}
            H(D) = -\sum_{k=1}^{K} p_k \log_2 p_k,
            \qquad
            \text{Gini}(D) = 1 - \sum_{k=1}^{K} p_k^2,
            \qquad
            \text{Gain}(D,A) = H(D) - \sum_{v} \frac{|D_v|}{|D|}\,H(D_v)
        \end{equation}
    \end{tcbitemize}

    % ---- 5.5.3 Decision Trees for Regression --------------------------------------------------------
    \subsection{Decision Trees for Regression}

    \begin{tcbitemize}[ skin=sectionraster ]
        \tcbitem[title={Regression Trees: Piecewise-Constant Approximation}, raster multicolumn=6]
        Regression trees predict the \emph{mean} target value of training examples in each leaf\textsuperscript{\cite[][pp.~8--20]{iiiCourseMachineLearning}}. Splits are chosen to minimize the weighted sum of within-leaf variances (squared error). The result is a piecewise-constant approximation of the target function. Ensemble methods (Random Forests, Gradient Boosted Trees) dramatically improve regression tree performance on real data.
        \tcblower
        \begin{equation}
            \text{Split criterion:} \quad
            \min_{A,\, t}\;\sum_{n \in D_{\text{left}}}\!\!(y_n - \bar{y}_{\text{left}})^2
            +\sum_{n \in D_{\text{right}}}\!\!(y_n - \bar{y}_{\text{right}})^2,
            \quad
            \hat{y}_{\text{leaf}} = \frac{1}{|D_{\text{leaf}}|}\sum_{n \in D_{\text{leaf}}} y_n
        \end{equation}
    \end{tcbitemize}

    % ---- 5.5.4 Random Forests -----------------------------------------------------------------------
    \subsection{Random Forests}

    \begin{tcbitemize}[ skin=sectionraster ]
        \tcbitem[title={Bagging and the Random Forest Algorithm}, raster multicolumn=6]
        A Random Forest trains $T$ decision trees on \emph{bootstrap} samples (sampling $N$ points with replacement) and combines their predictions by majority vote (classification) or averaging (regression)\textsuperscript{\cite[][pp.~586--588]{hanDataMiningConcepts2012}}. At each split, only a random subset of $m \approx \sqrt{D}$ features is considered. This double randomization decorrelates the individual trees and drastically reduces variance while keeping bias low.
        \tcblower
        \begin{equation}
            \hat{y}(\mathbf{x}) = \frac{1}{T} \sum_{t=1}^{T} h_t(\mathbf{x}),
            \quad
            \text{bootstrap sample: } \mathcal{D}_t \sim \mathcal{D} \text{ with replacement},
            \quad
            m \approx \sqrt{D} \text{ features per split}
        \end{equation}

        \tcbitem[title={Out-of-Bag Error and Feature Importance}, raster multicolumn=6]
        Each bootstrap sample leaves out roughly 37\% of the training points (out-of-bag, OOB)\textsuperscript{\cite[][p.588]{hanDataMiningConcepts2012}}. Predicting each training point with the trees that did \emph{not} train on it gives a free, unbiased estimate of generalization error without a separate validation set. Feature importance is measured by how much prediction accuracy drops when a feature's values are randomly permuted (permutation importance).
    \end{tcbitemize}

    % ---- 5.5.5 Gradient Boosting --------------------------------------------------------------------
    \subsection{Gradient Boosting}

    \begin{tcbitemize}[ skin=sectionraster ]
        \tcbitem[title={Gradient Boosting: Sequential Error Correction}, raster multicolumn=6]
        Gradient Boosting builds an ensemble sequentially: each new tree $h_t$ fits the \emph{negative gradient} (pseudo-residuals) of the loss of the current ensemble\textsuperscript{\cite[][p.590]{hanDataMiningConcepts2012}}. For squared-error loss, these pseudo-residuals equal the ordinary residuals $y_n - F_{t-1}(\mathbf{x}_n)$. A learning rate $\eta$ (shrinkage) scales each tree's contribution to prevent overfitting.
        \tcblower
        \begin{equation}
            F_t(\mathbf{x}) = F_{t-1}(\mathbf{x}) + \eta\, h_t(\mathbf{x}),
            \quad
            h_t \leftarrow \arg\min_{h} \sum_{n=1}^{N}
                \left[ -\frac{\partial \mathcal{L}(y_n, F_{t-1}(\mathbf{x}_n))}{\partial F_{t-1}(\mathbf{x}_n)} - h(\mathbf{x}_n) \right]^2
        \end{equation}

        \tcbitem[title={XGBoost and LightGBM}, raster multicolumn=6]
        XGBoost (Chen \& Guestrin, 2016) extends gradient boosting with a second-order Taylor expansion of the loss, L1/L2 regularization on tree weights, and efficient column subsampling. LightGBM (Ke et al., 2017) further accelerates training via Gradient-based One-Side Sampling (GOSS) and Exclusive Feature Bundling (EFB), enabling learning on very large datasets with millions of rows. Both consistently rank among the top performers on tabular-data benchmarks\textsuperscript{\cite[][p.590]{hanDataMiningConcepts2012}}.
        \tcblower
        \begin{tblr}{|Q[l,m,wd=2.6cm]|X|X|}
            \hline
            \textbf{Method}   & \textbf{Key innovation}                                  & \textbf{Typical use}           \\
            \hline
            Gradient Boosting & Fit residuals sequentially                               & General tabular regression/classification \\
            \hline
            XGBoost           & 2nd-order loss expansion, L1/L2 reg., column subsampling & Kaggle competitions, finance   \\
            \hline
            LightGBM          & GOSS + EFB, leaf-wise growth                             & Large-scale datasets           \\
            \hline
        \end{tblr}
    \end{tcbitemize}

    % ===========================================================================================
    \section{Nearest Neighbor Methods}

    % ---- 5.6.1 K-Nearest Neighbors -----------------------------------------------------------------
    \subsection{K-Nearest Neighbors}

    \begin{tcbitemize}[ skin=sectionraster ]
        \tcbitem[title={K-Nearest Neighbors Algorithm}, raster multicolumn=6]
        K-Nearest Neighbors (k-NN) is a non-parametric, instance-based learner: instead of fitting an explicit model, it stores the training data and at prediction time finds the $k$ closest training examples to the query point\textsuperscript{\cite[][pp.~396--400]{hanDataMiningConcepts2012}}. For classification, it returns the majority class among the $k$ neighbors; for regression, it returns their mean. There is no training phase, but prediction cost is $O(ND)$ per query without indexing.
        \tcblower
        \begin{equation}
            \hat{y}(\mathbf{x}) = \frac{1}{k}\sum_{i \in \mathcal{N}_k(\mathbf{x})} y_i
            \quad \text{(regression)}
            \qquad
            \hat{c}(\mathbf{x}) = \arg\max_{c} \sum_{i \in \mathcal{N}_k(\mathbf{x})} \mathbf{1}[y_i = c]
            \quad \text{(classification)}
        \end{equation}

        \tcbitem[title={Weighted Voting and Choosing k}, raster multicolumn=6]
        Distance-weighted k-NN gives closer neighbors more influence: the weight of neighbor $i$ is $w_i = 1/d(\mathbf{x}, \mathbf{x}_i)^2$\textsuperscript{\cite[][p.399]{hanDataMiningConcepts2012}}. The choice of $k$ is critical: $k=1$ is susceptible to noise (high variance); large $k$ smooths the boundary but may blur distinct clusters (high bias). Cross-validation is used to select the optimal $k$.
        \tcblower
        \begin{tblr}{|Q[c,m]|X|X|}
            \hline
            \textbf{$k$ value} & \textbf{Bias}    & \textbf{Variance}  \\
            \hline
            $k = 1$            & Low              & High (noise-sensitive)  \\
            \hline
            Moderate $k$       & Moderate         & Moderate (recommended)  \\
            \hline
            $k = N$            & High             & Very low (predicts overall majority) \\
            \hline
        \end{tblr}
    \end{tcbitemize}

    % ---- 5.6.2 Distance Metrics -------------------------------------------------------------------
    \subsection{Distance Metrics}

    \begin{tcbitemize}[ skin=sectionraster ]
        \tcbitem[title={Euclidean, Manhattan, and Minkowski Distances}, raster multicolumn=6]
        The choice of distance metric strongly affects k-NN behavior\textsuperscript{\cite[][p.397]{hanDataMiningConcepts2012}}. Euclidean distance ($p=2$) is the standard geometric distance but is sensitive to scale; feature normalization is essential. Manhattan distance ($p=1$) is more robust to outliers. For high-dimensional data, all distance metrics suffer from the curse of dimensionality (distances concentrate), and cosine similarity may be preferable.
        \tcblower
        \begin{equation}
            d_{\text{Minkowski}}(\mathbf{x}, \mathbf{z}) = \left(\sum_{j=1}^{D} |x_j - z_j|^p\right)^{1/p},
            \quad
            \begin{cases}
                p = 1: & \text{Manhattan} \\
                p = 2: & \text{Euclidean} \\
                p \to \infty: & \text{Chebyshev } (\max_j |x_j - z_j|)
            \end{cases}
        \end{equation}
    \end{tcbitemize}

    % ===========================================================================================
    \section{Genetic Algorithms}

    % ---- 5.7.1 Introduction to Genetic Algorithms --------------------------------------------------
    \subsection{Introduction to Genetic Algorithms}

    \begin{tcbitemize}[ skin=sectionraster ]
        \tcbitem[title={Terminology: Chromosomes, Genes, and Fitness}, raster multicolumn=6]
        A genetic algorithm (GA) maintains a \emph{population} of candidate solutions called \emph{chromosomes}\textsuperscript{\cite[][pp.~91--95]{hurbansGrokkingArtificialIntelligence2020}}. Each chromosome is a sequence of \emph{genes} (encoding one attribute each); the value stored in a gene is its \emph{allele}. A \emph{fitness function} assigns a scalar score to each chromosome, quantifying how well it solves the problem. GAs require no gradient information — only the ability to evaluate fitness.
        \tcblower
        \begin{tblr}{|Q[l,m,wd=2.4cm]|X|}
            \hline
            \textbf{Term}    & \textbf{Meaning}                                                        \\
            \hline
            Chromosome       & A complete candidate solution (e.g.\ a binary string $[1,0,1,1,0,\ldots]$) \\
            \hline
            Gene / Allele    & One position in the chromosome / the value stored there                 \\
            \hline
            Population       & Set of $N$ chromosomes evaluated in each generation                     \\
            \hline
            Fitness function & Maps chromosome $\to$ scalar score (higher = better solution)          \\
            \hline
            Genotype         & Encoded representation; \emph{phenotype} = the actual decoded solution  \\
            \hline
        \end{tblr}

        \tcbitem[title={The GA Life Cycle}, raster multicolumn=6]
        A GA iterates through a fixed life cycle until a stopping condition is met (maximum generations, fitness threshold, or stagnation)\textsuperscript{\cite[][pp.~95--110]{hurbansGrokkingArtificialIntelligence2020}}. Selection pressure drives exploitation of high-fitness regions; mutation and diverse initialization drive exploration. This balance prevents premature convergence to suboptimal solutions.
        \tcblower
        \begin{enumerate}
            \item \textbf{Encode} the solution space (binary, real-valued, permutation, or tree representation)
            \item \textbf{Initialize} a random population of $N$ chromosomes
            \item \textbf{Evaluate} fitness $f_i$ for each chromosome
            \item \textbf{Select} parents proportionally to fitness (roulette wheel: $P_i = f_i / \sum_j f_j$; or tournament)
            \item \textbf{Crossover}: combine two parents to produce offspring (single-point, two-point, or uniform)
            \item \textbf{Mutate}: randomly perturb genes with small probability $p_m$ to maintain diversity
            \item \textbf{Replace} the old population with the new generation (elitism: keep top solutions)
            \item \textbf{Repeat} steps 3--7 until the stopping condition is satisfied
        \end{enumerate}

        \tcbitem[title={Crossover and Mutation Operators}, raster multicolumn=6]
        Crossover (recombination) exchanges genetic material between two parent chromosomes to produce offspring, exploiting existing good partial solutions\textsuperscript{\cite[][pp.~100--115]{hurbansGrokkingArtificialIntelligence2020}}. Mutation randomly flips bits or perturbs values, reintroducing diversity lost through selection. The mutation rate $p_m$ is kept small (typically 0.001--0.01) to avoid turning the GA into a random search.
        \tcblower
        \begin{tblr}{|Q[l,m,wd=3.0cm]|X|}
            \hline
            \textbf{Operator}       & \textbf{Description}                                                                  \\
            \hline
            Single-point crossover  & One cut point; swap the tail segments of two parents                                 \\
            \hline
            Two-point crossover     & Two cut points; swap the middle segment                                              \\
            \hline
            Uniform crossover       & Each gene independently chosen from either parent via a random binary mask            \\
            \hline
            Bit-flip mutation       & Each gene flipped with probability $p_m$ (binary encoding)                           \\
            \hline
            Gaussian mutation       & Gene perturbed by $\mathcal{N}(0,\sigma^2)$ (real-valued encoding)                   \\
            \hline
        \end{tblr}
    \end{tcbitemize}

    % ---- 5.7.2 Applications of Genetic Algorithms --------------------------------------------------
    \subsection{Applications of Genetic Algorithms}

    \begin{tcbitemize}[ skin=sectionraster ]
        \tcbitem[title={Application Domains and Configurable Parameters}, raster multicolumn=6]
        Genetic algorithms excel in large, complex, or discontinuous search spaces where gradient methods fail\textsuperscript{\cite[][pp.~115--127]{hurbansGrokkingArtificialIntelligence2020}}. They are robust to noisy fitness functions and require no problem-specific gradient. For example, the Knapsack Problem with 26 items requires $2^{26} \approx 67$ million brute-force evaluations; a GA typically finds near-optimal solutions in 10\,000--100\,000 fitness evaluations. GAs provide no guarantee of global optimality.
        \tcblower
        \begin{tblr}{|Q[l,m,wd=3.5cm]|X|}
            \hline
            \textbf{Domain}             & \textbf{Example applications}                                              \\
            \hline
            Combinatorial optimization  & Travelling Salesman Problem, Knapsack, scheduling, bin packing              \\
            \hline
            Engineering design          & Structural optimization, antenna design, circuit layout                    \\
            \hline
            Machine learning            & Hyperparameter tuning, neural architecture search, feature selection       \\
            \hline
            Bioinformatics              & Protein folding, gene regulatory network inference                         \\
            \hline
            Finance \& game AI          & Portfolio optimization, trading strategy development, level generation     \\
            \hline
            \multicolumn{2}{|l|}{\textbf{Key configurable parameters:} population size $N$, mutation rate $p_m$, crossover rate $p_c$,} \\
            \multicolumn{2}{|l|}{selection pressure, chromosome encoding, stopping condition} \\
            \hline
        \end{tblr}
    \end{tcbitemize}
```
