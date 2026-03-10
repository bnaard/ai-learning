# Writing Output: Chapter 5, Section 2 — Clustering

Target insertion: replaces lines 948–955 of `/workspace/ai and data analytics/ai-dataanalytics-cards.tex`

```latex
    \section{Clustering}

    % ---- 5.2.1 Introduction to Clustering ---------------------------------------------------------
    \subsection{Introduction to Clustering}

    \begin{tcbitemize}[ skin=sectionraster ]
        \tcbitem[title=What is Clustering?, raster multicolumn=6]
        Clustering is unsupervised learning that partitions data into groups (clusters) such that objects within a cluster are more similar to each other than to objects in other clusters\textsuperscript{\cite[][p.166]{iiiCourseMachineLearning}}. Unlike classification, there are no predefined class labels; the algorithm discovers structure from the data alone.
        \tcblower
        \begin{tblr}{|Q[c,m]|X|X|}
            \hline
            \textbf{Family}      & \textbf{Representative Algorithm} & \textbf{Key Idea}                          \\
            \hline
            Partitioning         & K-Means                           & Minimize within-cluster sum of squares     \\
            \hline
            Hierarchical         & Agglomerative / Divisive          & Build nested cluster tree (dendrogram)     \\
            \hline
            Density-based        & DBSCAN                            & Clusters as dense, connected regions       \\
            \hline
            Model-based          & GMM / EM                          & Mixture of Gaussian distributions          \\
            \hline
        \end{tblr}

        \tcbitem[title=Evaluating Cluster Quality, raster multicolumn=6]
        Because there are no labels, clustering quality must be assessed by internal criteria\textsuperscript{\cite[][pp.~443--445]{hanDataMiningConcepts2012}}. The silhouette coefficient $s(i)$ combines cohesion (average intra-cluster distance $a(i)$) and separation (average distance to the nearest other cluster $b(i)$) into a single score in $[-1, 1]$.
        \tcblower
        \begin{equation}
            s(i) = \frac{b(i) - a(i)}{\max\{a(i),\, b(i)\}}, \qquad s(i) \in [-1,\, 1]
        \end{equation}
    \end{tcbitemize}

    % ---- 5.2.2 K-Means -----------------------------------------------------------------------------
    \subsection{K-Means}

    \begin{tcbitemize}[ skin=sectionraster ]
        \tcbitem[title=K-Means Objective, raster multicolumn=6]
        K-means partitions $N$ data points into $K$ clusters by minimizing the within-cluster sum of squared distances to the cluster centroid\textsuperscript{\cite[][p.166]{iiiCourseMachineLearning}}. The algorithm alternates between assigning each point to its nearest centroid and recomputing each centroid as the mean of its assigned points.
        \tcblower
        \begin{equation}
            \mathcal{L}(\mathbf{z}, \boldsymbol{\mu}) = \sum_{k=1}^{K} \sum_{n:\, z_n = k} \|\mathbf{x}_n - \boldsymbol{\mu}_k\|^2
        \end{equation}

        \tcbitem[title=K-Means Algorithm, raster multicolumn=6]
        K-means is guaranteed to converge (the objective decreases monotonically at each step) but only to a local optimum\textsuperscript{\cite[][pp.~166--168]{iiiCourseMachineLearning}}. Initialization therefore strongly affects the solution quality.
        \tcblower
        \begin{enumerate}
            \item Initialize $K$ cluster centroids $\boldsymbol{\mu}_1, \ldots, \boldsymbol{\mu}_K$
            \item \textbf{Assign:} $z_n \leftarrow \arg\min_k \|\mathbf{x}_n - \boldsymbol{\mu}_k\|^2$ for every point $n$
            \item \textbf{Update:} $\boldsymbol{\mu}_k \leftarrow \dfrac{1}{|C_k|}\displaystyle\sum_{n \in C_k} \mathbf{x}_n$ for every cluster $k$
            \item Repeat steps 2--3 until convergence (no assignment changes)
        \end{enumerate}

        \tcbitem[title=K-Means++ Initialization, raster multicolumn=6]
        K-means++ improves the standard random initialization by spreading the initial centroids across the data\textsuperscript{\cite[][pp.~168--169]{iiiCourseMachineLearning}}. The first centroid is chosen uniformly at random; each subsequent centroid is chosen with probability proportional to $D(\mathbf{x})^2$, the squared distance to the nearest existing centroid. This yields the approximation guarantee below.
        \tcblower
        \begin{equation}
            \mathbb{E}\bigl[\hat{\mathcal{L}}\bigr] \leq 8(\log K + 2)\,\mathcal{L}^{(\mathrm{opt})}
        \end{equation}

        \tcbitem[title=Choosing K: Elbow Method and Information Criteria, raster multicolumn=6]
        There is no single best method for choosing $K$\textsuperscript{\cite[][p.169]{iiiCourseMachineLearning}}. The elbow method plots the within-cluster sum of squares (WCSS) against $K$ and selects the value at which improvement begins to plateau. Information criteria penalize model complexity explicitly.
        \tcblower
        \begin{equation}
            \text{BIC:}\; \arg\min_K \hat{\mathcal{L}}_K + K\log D
            \qquad
            \text{AIC:}\; \arg\min_K \hat{\mathcal{L}}_K + 2KD
        \end{equation}
    \end{tcbitemize}

    % ---- 5.2.3 Expectation Maximization ------------------------------------------------------------
    \subsection{Expectation Maximization}

    \begin{tcbitemize}[ skin=sectionraster ]
        \tcbitem[title=Gaussian Mixture Models (GMM), raster multicolumn=6]
        A Gaussian Mixture Model assumes data are generated from $K$ Gaussian components with mixing weights $\theta_k$, means $\boldsymbol{\mu}_k$, and covariances $\boldsymbol{\Sigma}_k$\textsuperscript{\cite[][p.175]{iiiCourseMachineLearning}}. Unlike K-means (hard, binary assignments), GMM fitting via EM produces \emph{soft} (probabilistic) memberships: each point belongs to every cluster to some degree.
        \tcblower
        \begin{equation}
            p(\mathbf{x}) = \sum_{k=1}^{K} \theta_k \,\mathcal{N}(\mathbf{x} \mid \boldsymbol{\mu}_k, \boldsymbol{\Sigma}_k), \qquad \sum_{k=1}^{K}\theta_k = 1
        \end{equation}

        \tcbitem[title=E-Step: Computing Responsibilities, raster multicolumn=6]
        In the Expectation step, the current parameters are held fixed and the posterior probability (responsibility) that component $k$ generated point $\mathbf{x}_n$ is computed\textsuperscript{\cite[][pp.~175--177]{iiiCourseMachineLearning}}. These soft assignments $z_{n,k}$ replace the hard assignments $z_n$ of K-means.
        \tcblower
        \begin{equation}
            z_{n,k} = \frac{\theta_k \,\mathcal{N}(\mathbf{x}_n \mid \boldsymbol{\mu}_k, \boldsymbol{\Sigma}_k)}
                           {\displaystyle\sum_{j=1}^{K} \theta_j \,\mathcal{N}(\mathbf{x}_n \mid \boldsymbol{\mu}_j, \boldsymbol{\Sigma}_j)}
        \end{equation}

        \tcbitem[title=M-Step: Re-estimating Parameters, raster multicolumn=6]
        In the Maximization step, the responsibilities are held fixed and the model parameters are updated to maximize the expected log-likelihood\textsuperscript{\cite[][pp.~177--178]{iiiCourseMachineLearning}}. Each iteration of EM is guaranteed to increase (or maintain) the log-likelihood.
        \tcblower
        \begin{equation}
            \theta_k = \frac{1}{N}\sum_{n=1}^{N} z_{n,k}, \qquad
            \boldsymbol{\mu}_k = \frac{\sum_n z_{n,k}\,\mathbf{x}_n}{\sum_n z_{n,k}}, \qquad
            \boldsymbol{\Sigma}_k = \frac{\sum_n z_{n,k}(\mathbf{x}_n - \boldsymbol{\mu}_k)(\mathbf{x}_n - \boldsymbol{\mu}_k)^\top}{\sum_n z_{n,k}}
        \end{equation}

        \tcbitem[title=EM as a Generalization of K-Means, raster multicolumn=6]
        K-means is a special case of EM\textsuperscript{\cite[][p.180]{iiiCourseMachineLearning}}. When all GMM covariances are fixed to $\sigma^2 \mathbf{I}$ and $\sigma \to 0$, the soft responsibilities $z_{n,k}$ collapse to hard indicator assignments and the EM update reduces exactly to the K-means update. EM thus trades the assumption of spherical, equal-size clusters for the ability to model elliptical clusters of varying shapes and sizes.
        \tcblower
        \begin{tblr}{|X|X|X|}
            \hline
                                    & \textbf{K-Means}          & \textbf{EM / GMM}                    \\
            \hline
            Assignments             & Hard (binary)             & Soft (probabilistic)                 \\
            \hline
            Cluster shape           & Spherical, equal-size     & Elliptical, varying size             \\
            \hline
            Parameters learned      & Centroids $\boldsymbol{\mu}_k$ & $\boldsymbol{\mu}_k$, $\boldsymbol{\Sigma}_k$, $\theta_k$ \\
            \hline
            Convergence guarantee   & Local optimum of WCSS     & Monotone increase of log-likelihood  \\
            \hline
        \end{tblr}
    \end{tcbitemize}

    % ---- 5.2.4 DBSCAN ------------------------------------------------------------------------------
    \subsection{DBSCAN}

    \begin{tcbitemize}[ skin=sectionraster, halign lower=center ]
        \tcbitem[title=Density-Based Clustering Concept, raster multicolumn=6]
        DBSCAN (Density-Based Spatial Clustering of Applications with Noise) identifies clusters as dense regions of points separated by sparser regions\textsuperscript{\cite[][p.471]{hanDataMiningConcepts2012}}. It requires two parameters: the neighborhood radius $\varepsilon$ and the minimum point count MinPts. Crucially, DBSCAN requires no preset number of clusters $K$ and naturally labels low-density points as noise (outliers).

        \tcbitem[title=Core, Border, and Noise Points, raster multicolumn=6]
        Every point in DBSCAN is classified as exactly one of three types based on the density of its $\varepsilon$-neighborhood $N_\varepsilon(p) = \{q \mid d(p,q) \leq \varepsilon\}$\textsuperscript{\cite[][pp.~472--474]{hanDataMiningConcepts2012}}. A cluster is the maximal set of density-connected core and border points.
        \tcblower
        \begin{tblr}{|Q[c,m]|X|}
            \hline
            \textbf{Point type} & \textbf{Definition}                                                          \\
            \hline
            Core point          & $|N_\varepsilon(p)| \geq \text{MinPts}$ — enough neighbors to start a cluster \\
            \hline
            Border point        & $|N_\varepsilon(p)| < \text{MinPts}$ but within $\varepsilon$ of a core point  \\
            \hline
            Noise point         & Neither core nor border — an outlier                                         \\
            \hline
        \end{tblr}

        \tcbitem[title=DBSCAN Point Types Illustrated, raster multicolumn=6]
        With MinPts $= 4$ and radius $\varepsilon$, core points have dense neighborhoods, border points are nearby but sparse, and noise points are isolated\textsuperscript{\cite[][p.473]{hanDataMiningConcepts2012}}.
        \tcblower
        \begin{tikzpicture}[scale=1.1]
            % -- colour definitions --------------------------------------------------
            \definecolor{corecolor}{RGB}{52,120,196}
            \definecolor{bordercolor}{RGB}{240,160,30}
            \definecolor{noisecolor}{RGB}{190,50,50}

            % -- epsilon circles around core points (light fill) ---------------------
            \foreach \cx/\cy in {0/0, 0.9/0.5, 0.4/0.9} {
                \draw[dashed, corecolor!50, fill=corecolor!8, thin]
                    (\cx,\cy) circle (0.75);
            }

            % -- cluster 1: core points ----------------------------------------------
            \foreach \px/\py in {0/0, 0.9/0.5, 0.4/0.9, 1.1/-0.2} {
                \filldraw[corecolor] (\px,\py) circle (3.5pt);
            }

            % -- cluster 1: border points -------------------------------------------
            \foreach \px/\py in {-0.65/0.4, 1.6/0.9, 1.4/-0.7} {
                \filldraw[bordercolor] (\px,\py) circle (3.5pt);
            }

            % -- cluster 2: two core points + border --------------------------------
            \foreach \cx/\cy in {3.4/0.3, 3.9/0.9} {
                \draw[dashed, corecolor!50, fill=corecolor!8, thin]
                    (\cx,\cy) circle (0.75);
            }
            \foreach \px/\py in {3.4/0.3, 3.9/0.9, 3.1/0.95, 4.3/0.4} {
                \filldraw[corecolor] (\px,\py) circle (3.5pt);
            }
            \foreach \px/\py in {3.0/-0.3, 4.55/1.3} {
                \filldraw[bordercolor] (\px,\py) circle (3.5pt);
            }

            % -- noise points --------------------------------------------------------
            \foreach \px/\py in {2.1/1.7, 2.5/-0.5, 5.1/0.1} {
                \filldraw[noisecolor] (\px,\py) circle (3.5pt);
            }

            % -- legend --------------------------------------------------------------
            \node[right] at (5.3, 1.1)  {\small\textbf{Legend}};
            \filldraw[corecolor]   (5.3, 0.65) circle (3.5pt);
            \node[right] at (5.5, 0.65) {\small Core point};
            \filldraw[bordercolor] (5.3, 0.25) circle (3.5pt);
            \node[right] at (5.5, 0.25) {\small Border point};
            \filldraw[noisecolor]  (5.3,-0.15) circle (3.5pt);
            \node[right] at (5.5,-0.15) {\small Noise point};
            \draw[dashed, corecolor!60, thin] (5.3,-0.52) circle (8pt);
            \node[right] at (5.5,-0.52) {\small $\varepsilon$-neighborhood};

            % -- cluster labels ------------------------------------------------------
            \node[corecolor!80!black] at (0.45,-1.0) {\small Cluster 1};
            \node[corecolor!80!black] at (3.65,-0.9) {\small Cluster 2};
        \end{tikzpicture}

        \tcbitem[title=DBSCAN Algorithm, raster multicolumn=6]
        DBSCAN visits each unvisited point, expands a new cluster if a core point is found, and marks isolated points as noise\textsuperscript{\cite[][pp.~474--477]{hanDataMiningConcepts2012}}. With a spatial index (e.g.\ R-tree), complexity is $O(n \log n)$; without indexing it degrades to $O(n^2)$.
        \tcblower
        \begin{enumerate}
            \item For each unvisited point $p$: compute $N_\varepsilon(p)$
            \item If $|N_\varepsilon(p)| \geq \text{MinPts}$: mark $p$ as a core point, start a new cluster $C$
            \item Expand $C$: add all points density-reachable from $p$ (recursively include core points found)
            \item If $|N_\varepsilon(p)| < \text{MinPts}$: mark $p$ as noise (may later become a border point of another cluster)
            \item Repeat until all points are visited
        \end{enumerate}
    \end{tcbitemize}

    % ---- 5.2.5 Hierarchical Clustering -------------------------------------------------------------
    \subsection{Hierarchical Clustering}

    \begin{tcbitemize}[ skin=sectionraster, halign lower=center ]
        \tcbitem[title=Agglomerative Hierarchical Clustering, raster multicolumn=6]
        Hierarchical clustering builds a tree-like decomposition of data called a dendrogram\textsuperscript{\cite[][p.457]{hanDataMiningConcepts2012}}. The agglomerative (bottom-up) approach starts with each data point as its own singleton cluster and iteratively merges the two closest clusters until only one remains. The number of clusters $K$ need not be specified in advance: it is determined by cutting the dendrogram at the desired height.
        \tcblower
        \begin{enumerate}
            \item Start: assign each of the $n$ points to its own cluster
            \item Compute the $n \times n$ pairwise distance matrix
            \item Merge the two clusters with the smallest inter-cluster distance
            \item Update the distance matrix (recompute distances to the merged cluster)
            \item Repeat steps 3--4 until one cluster remains
            \item Cut the dendrogram at the desired level to obtain $K$ clusters
        \end{enumerate}

        \tcbitem[title=Linkage Criteria, raster multicolumn=6]
        The choice of linkage criterion defines how the distance between two clusters $C_i$ and $C_j$ is measured and strongly affects the shape of the resulting clusters\textsuperscript{\cite[][pp.~460--463]{hanDataMiningConcepts2012}}.
        \tcblower
        \begin{tblr}{|Q[l,m,wd=2.6cm]|X|X|}
            \hline
            \textbf{Linkage}  & \textbf{Formula}                                                                                              & \textbf{Effect}                       \\
            \hline
            Single            & $\min_{p \in C_i,\, q \in C_j} d(p,q)$                                                                       & Chain-shaped, elongated clusters      \\
            \hline
            Complete          & $\max_{p \in C_i,\, q \in C_j} d(p,q)$                                                                       & Compact, spherical clusters           \\
            \hline
            Average (UPGMA)   & $\dfrac{1}{|C_i||C_j|}\displaystyle\sum_{p \in C_i}\sum_{q \in C_j} d(p,q)$                                  & Compromise between single and complete \\
            \hline
            Ward's method     & Merges pair minimizing increase in total within-cluster variance                                              & Compact, equal-size clusters          \\
            \hline
        \end{tblr}

        \tcbitem[title=Reading a Dendrogram, raster multicolumn=6]
        The height of each merge in the dendrogram encodes the inter-cluster distance at which two groups were joined\textsuperscript{\cite[][pp.~457--467]{hanDataMiningConcepts2012}}. A horizontal cut at height $h$ produces the clustering at that granularity: every connected subtree below the cut is one cluster. Large vertical gaps between merges indicate a natural number of clusters.
        \tcblower
        \begin{tikzpicture}[scale=1.0]
            % -- leaf labels (6 points: A..F) ----------------------------------------
            \foreach \lbl/\x in {A/0, B/1, C/2, D/3, E/4, F/5} {
                \node[font=\small\sffamily] at (\x, -0.3) {\lbl};
            }

            % -- merge 1: A+B at height 0.8 ------------------------------------------
            \draw[thick] (0, 0) -- (0, 0.8) -- (1, 0.8) -- (1, 0);
            \node[right, font=\tiny] at (1.05, 0.8) {};

            % -- merge 2: D+E at height 0.7 ------------------------------------------
            \draw[thick] (3, 0) -- (3, 0.7) -- (4, 0.7) -- (4, 0);

            % -- merge 3: (D+E)+F at height 1.3 --------------------------------------
            \draw[thick] (3.5, 0.7) -- (3.5, 1.3) -- (5, 1.3) -- (5, 0);

            % -- merge 4: (A+B)+C at height 1.5 --------------------------------------
            \draw[thick] (0.5, 0.8) -- (0.5, 1.5) -- (2, 1.5) -- (2, 0);

            % -- merge 5: cluster{A,B,C} + cluster{D,E,F} at height 2.5 -------------
            \draw[thick] (0.5, 1.5) -- (0.5, 2.5) -- (4.25, 2.5) -- (4.25, 1.3);

            % -- cut line at height 1.8 ----------------------------------------------
            \draw[red, dashed, thick] (-0.4, 1.8) -- (5.5, 1.8)
                node[right, font=\small, text=red] {cut $\Rightarrow K{=}2$};

            % -- y-axis label --------------------------------------------------------
            \draw[->] (-0.5, 0) -- (-0.5, 2.8) node[above, font=\small] {distance};
            \foreach \y/\lbl in {0/0, 0.8/0.8, 1.3/1.3, 1.5/1.5, 2.5/2.5} {
                \draw (-0.55,\y) -- (-0.45,\y);
                \node[left, font=\tiny] at (-0.55,\y) {\lbl};
            }
        \end{tikzpicture}
    \end{tcbitemize}
```
