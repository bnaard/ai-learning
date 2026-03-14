# Writing Output: Ch6 Deep Learning — Sections 1–3
**Date:** 2026-03-13
**Agent:** Coordinator (Opus) based on Research Agent findings
**Sections:** 1 (Introduction to NN & DL), 2 (Network Architectures), 3 (Neural Network Training)

---

```latex
% ==== Section 1: Introduction to Neural Networks and Deep Learning ===========================
\section{Introduction to Neural Networks and Deep Learning}

% ---- 6.1.1 The Biological Brain -------------------------------------------------------------
\subsection{The Biological Brain}

\begin{tcbitemize}[ skin=sectionraster ]
    \tcbitem[title={The Biological Neuron}, raster multicolumn=3]
    Artificial neural networks draw inspiration from the structure of biological neurons\textsuperscript{\cite[][pp.~27--35]{Kriesel2007NeuralNetworks}}.
    A biological neuron consists of:
    \begin{itemize}
        \item \textbf{Dendrites}: tree-like input branches that receive signals from other neurons
        \item \textbf{Soma} (cell body): integrates incoming signals
        \item \textbf{Axon}: long output fibre that transmits the signal onward
        \item \textbf{Synapses}: junctions between neurons; neurotransmitter release modulates connection strength
    \end{itemize}

    \tcbitem[title={From Biology to Computation}, raster multicolumn=3]
    The neuron's membrane rests at approximately $-70\,\text{mV}$.
    When excitatory inputs push the potential above a threshold ($\approx -55\,\text{mV}$), an \textbf{action potential} (spike) propagates down the axon\textsuperscript{\cite[][pp.~29--31]{Kriesel2007NeuralNetworks}}.
    Chemical synapses strengthen or weaken over time (\textbf{synaptic plasticity}), providing a biological basis for learning.
    \tcblower
    The \textbf{100-step rule}: the brain performs complex recognition in ${\sim}500\,\text{ms}$; neurons fire at ${\sim}100\,\text{Hz}$, allowing at most ${\sim}100$ sequential processing steps.
    This implies massive parallelism --- motivating parallel architectures in artificial networks.
\end{tcbitemize}

% ---- 6.1.2 Perceptron and Multi-Layer Perceptrons -------------------------------------------
\subsection{Perceptron and Multi-Layer Perceptrons}

\begin{tcbitemize}[ skin=sectionraster ]
    \tcbitem[title={The Perceptron}, raster multicolumn=3]
    The \textbf{perceptron} (Rosenblatt, 1957) is the simplest artificial neuron\textsuperscript{\cite[][pp.~57--62]{Kriesel2007NeuralNetworks}}.
    It computes a weighted sum of inputs and applies a binary threshold:
    \begin{equation}
        y = \begin{cases} 1 & \text{if } \mathbf{w}^\top \mathbf{x} + b \geq 0 \\ 0 & \text{otherwise} \end{cases}
    \end{equation}
    The \textbf{perceptron convergence theorem} guarantees that the learning rule will find a separating hyperplane if the data is linearly separable.

    \tcbitem[title={The XOR Problem and MLPs}, raster multicolumn=3]
    Minsky \& Papert (1969) proved that a single perceptron \emph{cannot} solve the XOR problem --- it can only represent linearly separable functions\textsuperscript{\cite[][pp.~63--65]{Kriesel2007NeuralNetworks}}.
    This limitation contributed to the first ``AI winter''.
    The solution is the \textbf{Multi-Layer Perceptron (MLP)}: stacking layers with nonlinear activation functions creates networks that can represent arbitrarily complex decision boundaries.
    \tcblower
    \begin{center}
    \begin{tikzpicture}[
        node distance=0.8cm and 1.2cm,
        neuron/.style={circle, draw, minimum size=0.6cm, font=\scriptsize, inner sep=1pt},
        arr/.style={-{Stealth[length=1.5mm]}, thick}
    ]
        % Input layer
        \node[neuron, fill=blue!15] (i1) {$x_1$};
        \node[neuron, fill=blue!15, below=of i1] (i2) {$x_2$};
        % Hidden layer
        \node[neuron, fill=orange!20, right=of i1, yshift=-0.4cm] (h1) {$h_1$};
        \node[neuron, fill=orange!20, below=of h1] (h2) {$h_2$};
        % Output
        \node[neuron, fill=green!20, right=of h1, yshift=-0.4cm] (o) {$y$};

        \foreach \i in {i1,i2} \foreach \h in {h1,h2} \draw[arr] (\i) -- (\h);
        \foreach \h in {h1,h2} \draw[arr] (\h) -- (o);

        \node[below=0.15cm of i2, font=\sffamily\tiny] {Input};
        \node[below=0.15cm of h2, font=\sffamily\tiny] {Hidden};
        \node[below=0.55cm of o, font=\sffamily\tiny] {Output};
    \end{tikzpicture}
    \end{center}

    \tcbitem[title={From Perceptrons to Deep Learning}, raster multicolumn=6]
    The transition from single perceptrons to deep networks involved three key advances\textsuperscript{\cite[][pp.~1--3]{fleuretLittleBookDeep}}:
    \begin{itemize}
        \item \textbf{Hebbian learning} $\to$ \textbf{error-correction rules} $\to$ \textbf{backpropagation} (Rumelhart, Hinton \& Williams, 1986): enabled training of multi-layer networks by propagating gradients backward through layers
        \item \textbf{Nonlinear activations}: sigmoid, tanh, and later ReLU allow hidden layers to learn complex feature hierarchies
        \item \textbf{Hardware and data}: GPUs and large datasets made training deep networks practical from $\sim$2012 onward
    \end{itemize}
    \textbf{Deep learning} refers to neural networks with many hidden layers that learn hierarchical representations --- from low-level features (edges, textures) to high-level concepts (objects, semantics).
\end{tcbitemize}

% ---- 6.1.3 Activation Functions -------------------------------------------------------------
\subsection{Activation Functions}

\begin{tcbitemize}[ skin=sectionraster ]
    \tcbitem[title={Why Activation Functions Matter}, raster multicolumn=6]
    Without nonlinear activation functions, a multi-layer network collapses to a single linear transformation\textsuperscript{\cite[][p.~17]{fleuretLittleBookDeep}}.
    The choice of activation function affects gradient flow, training speed, and representational capacity.
    \tcblower
    \begin{tblr}{|Q[l,m]|X[l]|X[l]|X[l]|}
        \hline
        \textbf{Function} & \textbf{Formula} & \textbf{Range} & \textbf{Key Property} \\
        \hline
        Sigmoid & $\sigma(x) = \frac{1}{1+e^{-x}}$ & $(0, 1)$ & Vanishing gradients for $|x| \gg 0$ \\
        \hline
        Tanh & $\tanh(x)$ & $(-1, 1)$ & Zero-centred; still saturates \\
        \hline
        ReLU & $\max(0, x)$ & $[0, \infty)$ & Fast; can ``die'' (zero gradient for $x < 0$) \\
        \hline
        Leaky ReLU & $\max(\alpha x, x)$ & $(-\infty, \infty)$ & Prevents dying neurons ($\alpha \approx 0.01$) \\
        \hline
        GELU & $x \cdot \Phi(x)$ & $\approx (-0.17, \infty)$ & Smooth; used in Transformers \\
        \hline
        Softmax & $\frac{e^{x_i}}{\sum_j e^{x_j}}$ & $(0, 1)$, sums to 1 & Output layer for classification \\
        \hline
    \end{tblr}

    \tcbitem[title={ReLU: The Default Choice}, raster multicolumn=3]
    The \textbf{Rectified Linear Unit} $\mathrm{ReLU}(x) = \max(0, x)$ became the default activation after Glorot et al.\ (2011) showed it greatly improves training of deep networks\textsuperscript{\cite[][]{glorotUnderstandingDifficultyTraining}}.
    Its gradient is either $0$ or $1$ --- avoiding the vanishing gradient problem that plagues sigmoid and tanh in deep architectures.
    \tcblower
    The \textbf{dying ReLU problem}: if a neuron's pre-activation is always negative, its gradient is permanently zero and it stops learning.
    Leaky ReLU and parametric ReLU (PReLU) mitigate this by allowing a small gradient for negative inputs.

    \tcbitem[title={Softmax for Classification}, raster multicolumn=3]
    For multi-class classification, the \textbf{softmax} function converts a vector of raw scores (logits) into a probability distribution\textsuperscript{\cite[][p.~18]{fleuretLittleBookDeep}}:
    \begin{equation}
        \mathrm{softmax}(x_i) = \frac{e^{x_i}}{\sum_{j=1}^{K} e^{x_j}}
    \end{equation}
    All outputs are positive and sum to $1$.
    Combined with cross-entropy loss, softmax provides well-calibrated gradients for training classifiers.
\end{tcbitemize}


% ==== Section 2: Network Architectures =======================================================
\section{Network Architectures}

% ---- 6.2.1 Feed-Forward Networks ------------------------------------------------------------
\subsection{Feed-Forward Networks}

\begin{tcbitemize}[ skin=sectionraster ]
    \tcbitem[title={Dense Layers}, raster multicolumn=3]
    A \textbf{feed-forward network} (also called a \emph{fully connected} or \emph{dense} network) consists of layers where every neuron connects to all neurons in the next layer\textsuperscript{\cite[][pp.~15--17]{fleuretLittleBookDeep}}.
    Each layer computes:
    \begin{equation}
        Y = \sigma(WX + b)
    \end{equation}
    where $W$ is the weight matrix, $b$ the bias vector, and $\sigma$ a nonlinear activation.
    Information flows strictly forward --- there are no cycles or feedback connections.

    \tcbitem[title={Universal Approximation}, raster multicolumn=3]
    The \textbf{Universal Approximation Theorem} (Cybenko, 1989; Hornik, 1991) states that a feed-forward network with a single hidden layer containing sufficiently many neurons can approximate any continuous function on a compact set to arbitrary precision\textsuperscript{\cite[][p.~16]{fleuretLittleBookDeep}}.
    However, ``sufficiently many'' may be exponentially large.
    \textbf{Deeper networks} are exponentially more parameter-efficient than wider shallow ones for many function classes\textsuperscript{\cite[][pp.~8--12]{robertsPrinciplesDeepLearning2022}} --- this is the fundamental motivation for \emph{deep} learning.
\end{tcbitemize}

% ---- 6.2.2 Convolutional Networks -----------------------------------------------------------
\subsection{Convolutional Networks}

\begin{tcbitemize}[ skin=sectionraster ]
    \tcbitem[title={The Convolution Operation}, raster multicolumn=3]
    A \textbf{Convolutional Neural Network (CNN)} replaces dense matrix multiplications with convolution operations\textsuperscript{\cite[][pp.~43--48]{fleuretLittleBookDeep}}.
    Small learned \textbf{filters} (kernels) slide across the input, computing dot products at each position.
    Key properties:
    \begin{itemize}
        \item \textbf{Weight sharing}: the same filter is applied everywhere $\to$ translation equivariance
        \item \textbf{Local connectivity}: each output depends only on a small input region
        \item \textbf{Parameter efficiency}: far fewer parameters than a dense layer of the same input/output size
    \end{itemize}

    \tcbitem[title={Pooling and Feature Hierarchies}, raster multicolumn=3]
    \textbf{Pooling layers} (max or average) reduce spatial dimensions and provide a degree of translation invariance\textsuperscript{\cite[][pp.~49--50]{fleuretLittleBookDeep}}.
    Stacking convolution and pooling layers creates a \textbf{feature hierarchy}: early layers detect edges and textures; deeper layers detect parts and objects.
    The \textbf{receptive field} --- the input region that influences a single output unit --- grows with network depth.

    \tcbitem[title={Landmark CNN Architectures}, raster multicolumn=6]
    \tcblower
    \begin{tblr}{|Q[l,m]|Q[c,m]|X[l]|}
        \hline
        \textbf{Architecture} & \textbf{Year} & \textbf{Key Innovation} \\
        \hline
        LeNet-5 & 1998 & First successful CNN; handwritten digit recognition \\
        \hline
        AlexNet & 2012 & ReLU activation, dropout, GPU training; won ImageNet \\
        \hline
        VGG & 2014 & Uniform $3\times3$ filters; demonstrated depth matters \\
        \hline
        ResNet & 2015 & Skip connections; enabled training of 100+ layer networks \\
        \hline
    \end{tblr}
\end{tcbitemize}

% ---- 6.2.3 Recurrent Networks, Memory Cells and LSTMs --------------------------------------
\subsection{Recurrent Networks, Memory Cells and LSTMs}

\begin{tcbitemize}[ skin=sectionraster ]
    \tcbitem[title={Recurrent Neural Networks}, raster multicolumn=3]
    A \textbf{Recurrent Neural Network (RNN)} processes sequential data by maintaining a hidden state $h_t$ that is updated at each time step\textsuperscript{\cite[][pp.~55--58]{fleuretLittleBookDeep}}:
    \begin{equation}
        h_t = \sigma(W_h h_{t-1} + W_x x_t + b)
    \end{equation}
    Weight sharing across time steps means the same parameters handle sequences of any length.
    The \textbf{vanishing gradient problem} makes it difficult for standard RNNs to learn long-range dependencies: gradients are multiplied through many time steps and either vanish or explode.

    \tcbitem[title={LSTM: Long Short-Term Memory}, raster multicolumn=3]
    The \textbf{LSTM} (Hochreiter \& Schmidhuber, 1997) solves the vanishing gradient problem with a \textbf{cell state} $c_t$ and three multiplicative gates\textsuperscript{\cite[][pp.~59--61]{fleuretLittleBookDeep}}:
    \begin{itemize}
        \item \textbf{Forget gate} $f_t$: decides what to discard from cell state
        \item \textbf{Input gate} $i_t$: decides what new information to store
        \item \textbf{Output gate} $o_t$: decides what to output from cell state
    \end{itemize}
    \tcblower
    \begin{equation}
        c_t = f_t \odot c_{t-1} + i_t \odot \tilde{c}_t, \quad h_t = o_t \odot \tanh(c_t)
    \end{equation}
    The cell state provides a ``highway'' for gradients to flow through many time steps unimpeded.

    \tcbitem[title={GRU: Gated Recurrent Unit}, raster multicolumn=6]
    The \textbf{GRU} (Cho et al., 2014) simplifies the LSTM by merging the cell state and hidden state and using only two gates\textsuperscript{\cite[][p.~62]{fleuretLittleBookDeep}}:
    a \emph{reset gate} $r_t$ (controls how much past state to forget) and an \emph{update gate} $z_t$ (controls the mix of old state and new candidate).
    GRUs have fewer parameters than LSTMs and often achieve similar performance on many tasks.
    Both architectures have been largely superseded by Transformer-based models for most sequence tasks, but remain relevant for streaming and low-latency applications.
\end{tcbitemize}


% ==== Section 3: Neural Network Training =====================================================
\section{Neural Network Training}

% ---- 6.3.1 Forward Pass and Loss Functions --------------------------------------------------
\subsection{Forward Pass and Loss Functions}

\begin{tcbitemize}[ skin=sectionraster ]
    \tcbitem[title={The Forward Pass}, raster multicolumn=3]
    During the \textbf{forward pass}, input data propagates through the network layer by layer\textsuperscript{\cite[][pp.~20--22]{fleuretLittleBookDeep}}.
    Each layer applies its learned transformation (weights, bias, activation), producing intermediate representations.
    The final layer produces a prediction $\hat{y}$ that is compared to the true target $y$ using a \textbf{loss function} $\mathcal{L}(y, \hat{y})$.

    \tcbitem[title={Common Loss Functions}, raster multicolumn=3]
    \tcblower
    \begin{tblr}{|Q[l,m]|X[l]|Q[l,m]|}
        \hline
        \textbf{Loss} & \textbf{Formula} & \textbf{Task} \\
        \hline
        MSE & $\frac{1}{N}\sum(y_i - \hat{y}_i)^2$ & Regression \\
        \hline
        MAE & $\frac{1}{N}\sum|y_i - \hat{y}_i|$ & Regression (robust) \\
        \hline
        Cross-entropy & $-\sum y_i \log \hat{y}_i$ & Classification \\
        \hline
        Binary CE & $-[y\log\hat{y} + (1{-}y)\log(1{-}\hat{y})]$ & Binary classif. \\
        \hline
    \end{tblr}
\end{tcbitemize}

% ---- 6.3.2 Weight Initialization and Transfer Function --------------------------------------
\subsection{Weight Initialization and Transfer Function}

\begin{tcbitemize}[ skin=sectionraster ]
    \tcbitem[title={Why Initialization Matters}, raster multicolumn=3]
    Initializing all weights to zero causes a \textbf{symmetry problem}: all neurons in a layer compute the same output and receive the same gradient, so they never differentiate\textsuperscript{\cite[][pp.~8--10]{robertsPrinciplesDeepLearning2022}}.
    Too-large initial weights cause activations and gradients to explode; too-small weights cause them to vanish.
    Proper initialization keeps the variance of activations and gradients approximately constant across layers.

    \tcbitem[title={Xavier and He Initialization}, raster multicolumn=3]
    \textbf{Xavier/Glorot initialization}\textsuperscript{\cite[][]{glorotUnderstandingDifficultyTraining}} (for sigmoid/tanh):
    \begin{equation}
        W \sim \mathcal{N}\!\left(0,\; \frac{2}{n_{\mathrm{in}} + n_{\mathrm{out}}}\right)
    \end{equation}
    \textbf{He initialization} (for ReLU):
    \begin{equation}
        W \sim \mathcal{N}\!\left(0,\; \frac{2}{n_{\mathrm{in}}}\right)
    \end{equation}
    These schemes ensure that the expected variance of the output of each layer matches the variance of its input, preventing signal degradation in deep networks.
\end{tcbitemize}

% ---- 6.3.3 Backpropagation and Gradient Descent ---------------------------------------------
\subsection{Backpropagation and Gradient Descent}

\begin{tcbitemize}[ skin=sectionraster ]
    \tcbitem[title={Backpropagation}, raster multicolumn=3]
    \textbf{Backpropagation} computes the gradient of the loss with respect to every parameter by applying the chain rule layer by layer, from output back to input\textsuperscript{\cite[][pp.~1--4]{lecunTheoreticalFrameworkBack}}.
    For a network with layers $f_1, f_2, \ldots, f_L$:
    \begin{equation}
        \frac{\partial \mathcal{L}}{\partial W_l} = \frac{\partial \mathcal{L}}{\partial a_L} \cdot \frac{\partial a_L}{\partial a_{L-1}} \cdots \frac{\partial a_{l+1}}{\partial a_l} \cdot \frac{\partial a_l}{\partial W_l}
    \end{equation}
    Each layer's local Jacobian is computed once and reused --- making the algorithm $O(N)$ in the number of parameters.

    \tcbitem[title={Gradient Descent Variants}, raster multicolumn=3]
    Backpropagation computes gradients; an \textbf{optimiser} uses them to update weights\textsuperscript{\cite[][pp.~22--25]{fleuretLittleBookDeep}}.
    \tcblower
    \begin{tblr}{|Q[l,m]|X[l]|}
        \hline
        \textbf{Optimiser} & \textbf{Update Rule / Key Idea} \\
        \hline
        SGD & $\theta \leftarrow \theta - \eta \nabla\mathcal{L}$ \\
        \hline
        SGD + Momentum & Accumulates past gradients; smooths updates \\
        \hline
        RMSprop & Per-parameter adaptive learning rate \\
        \hline
        Adam & Momentum + RMSprop; default choice\textsuperscript{\cite[][]{kingmaAdamMethodStochastic2017}} \\
        \hline
    \end{tblr}

    \tcbitem[title={Mini-Batch Gradient Descent}, raster multicolumn=6]
    In practice, gradients are computed on \textbf{mini-batches} (subsets of the training data, typically 32--512 examples)\textsuperscript{\cite[][p.~23]{fleuretLittleBookDeep}}.
    This provides a compromise between full-batch gradient descent (low noise, expensive) and single-sample SGD (high noise, cheap).
    Mini-batch SGD introduces beneficial stochastic noise that helps escape shallow local minima and saddle points.
    The \textbf{learning rate} $\eta$ is the most important hyperparameter: too large $\to$ divergence; too small $\to$ slow convergence.
\end{tcbitemize}

% ---- 6.3.4 Training Loop -------------------------------------------------------------------
\subsection{Training Loop}

\begin{tcbitemize}[ skin=sectionraster ]
    \tcbitem[title={Epochs and Batches}, raster multicolumn=3]
    The training process iterates through the dataset in structured passes\textsuperscript{\cite[][pp.~24--26]{fleuretLittleBookDeep}}:
    \begin{itemize}
        \item \textbf{Epoch}: one complete pass through the entire training set
        \item \textbf{Iteration/step}: one parameter update using a single mini-batch
        \item \textbf{Batch size}: number of examples per mini-batch; affects gradient quality and memory usage
    \end{itemize}
    A typical training run uses tens to hundreds of epochs, with the dataset reshuffled between epochs.

    \tcbitem[title={Data Splits and Early Stopping}, raster multicolumn=3]
    The data is split into \textbf{training}, \textbf{validation}, and \textbf{test} sets (common split: 70/15/15 or 80/10/10)\textsuperscript{\cite[][p.~26]{fleuretLittleBookDeep}}.
    During training, the model is evaluated on the validation set after each epoch.
    \textbf{Early stopping}: if validation loss does not improve for a set number of epochs (``patience''), training halts and the model reverts to the best checkpoint.
    This is one of the most effective and simplest forms of regularisation.
    \tcblower
    \textbf{Learning rate scheduling} further improves training:
    \begin{itemize}
        \item \emph{Step decay}: reduce $\eta$ by a factor at fixed intervals
        \item \emph{Cosine annealing}: smoothly decrease $\eta$ following a cosine curve
        \item \emph{Warmup}: start with a very small $\eta$ and linearly increase it over the first few epochs
    \end{itemize}
\end{tcbitemize}

% ---- 6.3.5 Regularization and Overtraining --------------------------------------------------
\subsection{Regularization and Overtraining}

\begin{tcbitemize}[ skin=sectionraster ]
    \tcbitem[title={Overfitting}, raster multicolumn=6]
    A model \textbf{overfits} when it memorises the training data (low training loss) but generalises poorly to unseen data (high validation loss)\textsuperscript{\cite[][pp.~27--29]{fleuretLittleBookDeep}}.
    Deep networks with millions of parameters are particularly prone to overfitting when training data is limited.
    \textbf{Regularisation} techniques constrain the model's capacity to reduce overfitting.

    \tcbitem[title={Dropout}, raster multicolumn=3]
    During each training step, \textbf{dropout} randomly sets a fraction $p$ of neuron activations to zero\textsuperscript{\cite[][p.~28]{fleuretLittleBookDeep}}.
    This prevents co-adaptation: neurons cannot rely on specific other neurons being active, forcing redundant representations.
    At test time, dropout is turned off and activations are scaled by $(1 - p)$ to maintain expected values.

    \tcbitem[title={Weight Regularisation}, raster multicolumn=3]
    Adding a penalty term to the loss discourages large weights:
    \begin{itemize}
        \item \textbf{L2} (weight decay): $\mathcal{L}_{\mathrm{reg}} = \mathcal{L} + \lambda \sum w_i^2$ --- encourages small, distributed weights
        \item \textbf{L1}: $\mathcal{L}_{\mathrm{reg}} = \mathcal{L} + \lambda \sum |w_i|$ --- encourages sparsity (many weights exactly zero)
    \end{itemize}
    In practice, L2 regularisation (weight decay) is the most commonly used, often built directly into the optimiser.

    \tcbitem[title={Batch Normalization}, raster multicolumn=3]
    \textbf{Batch Normalization} (BN)\textsuperscript{\cite[][]{ioffeBatchNormalizationAccelerating2015}} normalises the activations of each layer across the mini-batch to have zero mean and unit variance, then applies learned scale $\gamma$ and shift $\beta$ parameters.
    Benefits: stabilises training, allows higher learning rates, and provides a mild regularisation effect.
    BN is applied between the linear transformation and the activation function.

    \tcbitem[title={Data Augmentation}, raster multicolumn=3]
    \textbf{Data augmentation} artificially expands the training set by applying label-preserving transformations\textsuperscript{\cite[][p.~29]{fleuretLittleBookDeep}}:
    random flips, rotations, crops, colour jitter, or more advanced techniques like mixup and cutout.
    This is particularly effective for image tasks and can reduce overfitting significantly without changing the model architecture.
\end{tcbitemize}
```
