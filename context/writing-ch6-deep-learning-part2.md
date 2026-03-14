# Writing Output: Ch6 Deep Learning — Sections 4–6
**Date:** 2026-03-13
**Agent:** Writer (Sonnet)
**Sections:** 4 (Alternative Training Methods), 5 (Further Network Architectures), 6 (Further Reading)

---

```latex
% ==== Section 4: Alternative Training Methods ================================================
\section{Alternative Training Methods}

% ---- 6.4.1 Attention -----------------------------------------------------------------------
\subsection{Attention}

\begin{tcbitemize}[ skin=sectionraster ]
    \tcbitem[title={Attention: Why It Matters}, raster multicolumn=3]
    Fully connected layers cannot handle variable-length inputs; convolutional layers propagate information only locally.
    \textbf{Attention layers} address this by computing, for every component of the output, a weighted average over the \emph{entire} input tensor --- regardless of distance\textsuperscript{\cite[][p.~73]{fleuretLittleBookDeep}}.
    This makes them the key building block for Transformers and modern large language models.

    \tcbitem[title={Query, Key, Value}, raster multicolumn=3]
    The \textbf{attention operator} att$(Q, K, V)$ takes three tensors\textsuperscript{\cite[][pp.~74--76]{fleuretLittleBookDeep}}:
    \begin{itemize}
        \item $Q \in \mathbb{R}^{N^q \times D^{qk}}$ --- \emph{Queries}
        \item $K \in \mathbb{R}^{N^{kv} \times D^{qk}}$ --- \emph{Keys}
        \item $V \in \mathbb{R}^{N^{kv} \times D^v}$ --- \emph{Values}
    \end{itemize}
    For each query $Q_n$, attention scores $A_{n,m}$ measure how well $Q_n$ matches each key $K_m$.
    The retrieved value $Y_n = \sum_m A_{n,m} V_m$ is a weighted average of all values.

    \tcbitem[title={Scaled Dot-Product Attention}, raster multicolumn=6]
    Attention scores are computed as a scaled softmax of dot-products between queries and keys\textsuperscript{\cite[][p.~3]{vaswaniAttentionAllYou2023}}.
    The scaling factor $1/\!\sqrt{D^{qk}}$ keeps the dot products in a range where softmax has useful gradients.
    \tcblower
    \begin{equation}
        \mathrm{Attention}(Q, K, V)
        = \mathrm{softmax}\!\left(\frac{QK^{\!\top}}{\sqrt{D^{qk}}}\right) V
    \end{equation}

    \tcbitem[title={Self- and Cross-Attention}, raster multicolumn=3]
    In a \textbf{self-attention} block, the three input sequences $X^q$, $X^k$, $X^v$ are identical\textsuperscript{\cite[][p.~79]{fleuretLittleBookDeep}}.
    Every position can gather information from every other position in the same sequence --- enabling global context.

    In a \textbf{cross-attention} block, $X^k$ and $X^v$ come from a different sequence (e.g., the encoder representation), while $X^q$ comes from the current sequence (e.g., the decoder).

    \tcbitem[title={Multi-Head Attention}, raster multicolumn=3]
    A single attention head averages over all value positions and cannot attend to multiple subspaces simultaneously.
    \textbf{Multi-Head Attention}\textsuperscript{\cite[][pp.~4--5]{vaswaniAttentionAllYou2023}} runs $H$ attention heads in parallel, each with its own learned projections $W^q_h, W^k_h, W^v_h$, then concatenates and projects:
    \begin{equation}
        \mathrm{MultiHead}(Q,K,V) = \mathrm{Concat}(\mathrm{head}_1,\ldots,\mathrm{head}_H)\,W^O
    \end{equation}
    Each head can learn to attend to a different type of relationship (syntactic, semantic, positional).
\end{tcbitemize}

% ---- 6.4.2 Transformer Architecture ---------------------------------------------------------
\subsection{Transformer Architecture}

\begin{tcbitemize}[ skin=sectionraster ]
    \tcbitem[title={Why Transformers Replaced RNNs}, raster multicolumn=3]
    Recurrent networks process sequences step-by-step, requiring $O(n)$ sequential operations --- preventing parallelism and making long-range dependencies hard to learn\textsuperscript{\cite[][p.~6]{vaswaniAttentionAllYou2023}}.
    Self-attention layers connect all positions with $O(1)$ sequential operations and constant path length between any two positions.
    Transformers train significantly faster on modern hardware and scale to billions of parameters\textsuperscript{\cite[][p.~93]{fleuretLittleBookDeep}}.

    \tcbitem[title={Encoder--Decoder Structure}, raster multicolumn=3]
    The original Transformer\textsuperscript{\cite[][p.~2]{vaswaniAttentionAllYou2023}} is designed for sequence-to-sequence tasks (e.g., translation):
    \begin{itemize}
        \item \textbf{Encoder:} $N$ identical layers, each with (1) multi-head self-attention and (2) position-wise feed-forward network (FFN); residual connections and layer normalisation around each sub-layer
        \item \textbf{Decoder:} $N$ layers with (1) masked causal self-attention, (2) cross-attention over encoder output, and (3) FFN; causal masking prevents attending to future tokens
    \end{itemize}

    \tcbitem[title={Transformer Block Diagram}, raster multicolumn=6]
    The encoder processes the full input in parallel; the decoder generates output tokens autoregressively.
    \tcblower
    \begin{center}
    \begin{tikzpicture}[
        node distance=0.25cm and 0.7cm,
        box/.style={draw, rounded corners=2pt, minimum width=2.8cm, minimum height=0.55cm,
                    font=\sffamily\scriptsize, align=center, fill=blue!10},
        addnorm/.style={draw, rounded corners=2pt, minimum width=2.8cm, minimum height=0.45cm,
                    font=\sffamily\scriptsize, align=center, fill=orange!15},
        lbl/.style={font=\sffamily\scriptsize, text=gray},
        arr/.style={-{Stealth[length=2mm]}, thick},
        brace/.style={decorate, decoration={brace, amplitude=4pt}}
    ]
        % ---- ENCODER (left column) ----
        \node[box] (emb_e)                          {Embedding};
        \node[box, above=of emb_e] (pe_e)            {+ Pos.\ Encoding};
        \node[addnorm, above=of pe_e] (an1_e)       {Add \& Norm};
        \node[box, above=of an1_e] (mha_e)          {Multi-Head\\Self-Attention};
        \node[addnorm, above=of mha_e] (an2_e)      {Add \& Norm};
        \node[box, above=of an2_e] (ffn_e)          {Feed Forward};
        \node[addnorm, above=of ffn_e] (an3_e)      {Add \& Norm};
        \node[lbl, left=0.15cm of mha_e] {$\times N$};

        % ---- DECODER (right column) ----
        \node[box, right=2.5cm of emb_e] (emb_d)         {Embedding};
        \node[box, above=of emb_d] (pe_d)           {+ Pos.\ Encoding};
        \node[addnorm, above=of pe_d] (an1_d)      {Add \& Norm};
        \node[box, above=of an1_d] (cmha_d)        {Masked\\Self-Attention};
        \node[addnorm, above=of cmha_d] (an2_d)    {Add \& Norm};
        \node[box, above=of an2_d] (xatt_d)        {Cross-Attention};
        \node[addnorm, above=of xatt_d] (an3_d)    {Add \& Norm};
        \node[box, above=of an3_d] (ffn_d)         {Feed Forward};
        \node[addnorm, above=of ffn_d] (an4_d)     {Add \& Norm};
        \node[lbl, right=0.15cm of cmha_d] {$\times N$};

        % Output
        \node[box, above=0.3cm of an4_d, fill=green!15] (out) {Linear + Softmax};

        % Encoder arrows
        \draw[arr] (emb_e) -- (pe_e);
        \draw[arr] (pe_e) -- (an1_e);
        \draw[arr] (an1_e) -- (mha_e);
        \draw[arr] (mha_e) -- (an2_e);
        \draw[arr] (an2_e) -- (ffn_e);
        \draw[arr] (ffn_e) -- (an3_e);

        % Decoder arrows
        \draw[arr] (emb_d) -- (pe_d);
        \draw[arr] (pe_d) -- (an1_d);
        \draw[arr] (an1_d) -- (cmha_d);
        \draw[arr] (cmha_d) -- (an2_d);
        \draw[arr] (an2_d) -- (xatt_d);
        \draw[arr] (xatt_d) -- (an3_d);
        \draw[arr] (an3_d) -- (ffn_d);
        \draw[arr] (ffn_d) -- (an4_d);
        \draw[arr] (an4_d) -- (out);

        % Cross-attention connection from encoder
        \draw[arr, dashed, gray] (an3_e.east) .. controls +(0.4,0.8) and +(-0.4,0) .. (xatt_d.west)
            node[midway, above, font=\sffamily\tiny, gray] {K, V};

        % Input labels
        \node[lbl, below=0.1cm of emb_e] {Source tokens};
        \node[lbl, below=0.1cm of emb_d] {Target tokens (shifted)};
        \node[lbl, above=0.1cm of out] {Output probs};
    \end{tikzpicture}
    \end{center}

    \tcbitem[title={Positional Encoding}, raster multicolumn=3]
    Attention is permutation-invariant --- it has no notion of sequence order.
    Position information is injected by adding a \textbf{positional encoding} to the input embeddings\textsuperscript{\cite[][pp.~81--82]{fleuretLittleBookDeep}}.
    The original Transformer uses sinusoidal encoding:
    \begin{equation}
        \mathrm{PE}_{t,2i} = \sin\!\left(\frac{t}{10^{4 \cdot 2i/D}}\right),
        \quad
        \mathrm{PE}_{t,2i+1} = \cos\!\left(\frac{t}{10^{4(2i-1)/D}}\right)
    \end{equation}
    This allows the model to extrapolate to sequences longer than seen during training. Learned positional embeddings perform similarly\textsuperscript{\cite[][p.~6]{vaswaniAttentionAllYou2023}}.

    \tcbitem[title={GPT and BERT: Decoder- and Encoder-Only}, raster multicolumn=3]
    Modern large language models are typically \emph{decoder-only} or \emph{encoder-only}\textsuperscript{\cite[][pp.~97--99]{fleuretLittleBookDeep}}:
    \begin{itemize}
        \item \textbf{GPT} (Radford et al.\ 2018): decoder-only; stacked causal self-attention blocks; trained autoregressively on next-token prediction; scales to hundreds of billions of parameters
        \item \textbf{BERT}\textsuperscript{\cite[][]{devlinBERTPretrainingDeep2019}} (Devlin et al.\ 2019): encoder-only; bidirectional; trained on masked language modeling and next-sentence prediction
    \end{itemize}
\end{tcbitemize}

% ---- 6.4.3 Feedback Alignment ---------------------------------------------------------------
\subsection{Feedback Alignment}

\begin{tcbitemize}[ skin=sectionraster ]
    \tcbitem[title={The Weight Transport Problem}, raster multicolumn=3]
    Standard backpropagation transmits error signals using the \emph{transpose} of the forward weight matrix $W^\top$\textsuperscript{\cite[][p.~3]{fischerVorlesungGrundlagenNeuronale2024}}.
    This requires the backward path to have exact knowledge of every forward weight --- a condition with no known biological mechanism, called the \textbf{weight transport problem}.

    \tcbitem[title={Feedback Alignment}, raster multicolumn=3]
    Lillicrap et al.\ (2016) showed that replacing $W^\top$ with a \textbf{fixed random feedback matrix} $B$ still produces learning.
    The forward weights $W$ gradually align with $B$ during training --- the network effectively ``shapes itself'' to match the random feedback.
    \textbf{Direct Feedback Alignment} (N{\o}kland, 2016) extends this further: each layer receives error signals \emph{directly} from the output layer via separate random matrices, bypassing the chain entirely.
\end{tcbitemize}

% ---- 6.4.4 Synthetic Gradients --------------------------------------------------------------
\subsection{Synthetic Gradients}

\begin{tcbitemize}[ skin=sectionraster ]
    \tcbitem[title=Decoupled Neural Interfaces, raster multicolumn=6]
    In standard backpropagation, no layer can update until the full forward and backward passes complete --- a constraint called \textbf{update locking}.
    Jaderberg et al.\ (2017) introduced \textbf{Decoupled Neural Interfaces (DNI)}: a small auxiliary network $M_i$ attached to each layer that \emph{predicts} the gradient $\partial\mathcal{L}/\partial h_i$ without waiting for it to arrive.
    The layer updates immediately using this synthetic gradient; $M_i$ is itself trained by the true gradient when it eventually arrives.
    This enables asynchronous, modular training of deep networks --- each layer acts as an independent learning module with a local objective.
    \tcblower
    \begin{center}
    \begin{tikzpicture}[
        node distance=0.35cm and 0.5cm,
        lay/.style={draw, rounded corners, minimum width=1.8cm, minimum height=0.6cm,
                    font=\sffamily\scriptsize, fill=blue!10},
        dni/.style={draw, rounded corners, minimum width=1.4cm, minimum height=0.5cm,
                    font=\sffamily\scriptsize, fill=orange!20},
        arr/.style={-{Stealth[length=2mm]}, thick},
        darr/.style={-{Stealth[length=2mm]}, dashed, gray}
    ]
        \node[lay] (L1) {Layer 1};
        \node[lay, right=of L1] (L2) {Layer 2};
        \node[lay, right=of L2] (L3) {Layer 3};
        \node[lay, right=of L3] (loss) {Loss};

        \node[dni, below=of L1] (M1) {DNI $M_1$};
        \node[dni, below=of L2] (M2) {DNI $M_2$};

        \draw[arr] (L1) -- (L2) node[midway, above, font=\sffamily\tiny] {$h_1$};
        \draw[arr] (L2) -- (L3) node[midway, above, font=\sffamily\tiny] {$h_2$};
        \draw[arr] (L3) -- (loss);

        \draw[arr] (L1) -- (M1);
        \draw[arr] (L2) -- (M2);

        \draw[darr] (M1) -- (L1) node[midway, right, font=\sffamily\tiny, gray] {$\tilde{\delta}_1$};
        \draw[darr] (M2) -- (L2) node[midway, right, font=\sffamily\tiny, gray] {$\tilde{\delta}_2$};
    \end{tikzpicture}
    \end{center}
\end{tcbitemize}

% ---- 6.4.5 Decoupled Network Interfaces -----------------------------------------------------
\subsection{Decoupled Network Interfaces}

\begin{tcbitemize}[ skin=sectionraster ]
    \tcbitem[title={Local Learning Signals}, raster multicolumn=6]
    The full Decoupled Neural Interface framework removes both \emph{update locking} (no backward pass needed) and \emph{forward locking} (synthetic activations can substitute for real forward signals).
    Each module then has a \textbf{local learning signal} and can train asynchronously.
    This is more aligned with how biological neural circuits are thought to operate --- local Hebbian-like updates rather than a global error signal broadcast through the entire network\textsuperscript{\cite[][p.~2]{fischerVorlesungGrundlagenNeuronale2024}}.
    In practice, synthetic gradients are primarily a research contribution; standard backpropagation remains the dominant approach.
\end{tcbitemize}


% ==== Section 5: Further Network Architectures ===============================================
\section{Further Network Architectures}

% ---- 6.5.1 GANs -----------------------------------------------------------------------------
\subsection{Generative Adversarial Networks}

\begin{tcbitemize}[ skin=sectionraster ]
    \tcbitem[title={Generator and Discriminator}, raster multicolumn=3]
    A \textbf{Generative Adversarial Network (GAN)} introduced by Goodfellow et al.\ (2014) pits two networks against each other\textsuperscript{\cite[][p.~125]{fleuretLittleBookDeep}}:
    \begin{itemize}
        \item \textbf{Generator} $G(z)$: takes random noise $z \sim p(z)$ and produces a structured output (e.g., an image) that mimics real data
        \item \textbf{Discriminator} $D(x)$: takes either a real sample or $G(z)$; outputs probability that the input is real
    \end{itemize}
    At equilibrium, $G$ produces samples indistinguishable from real data and $D$ outputs $0.5$ everywhere.

    \tcbitem[title={The Minimax Objective}, raster multicolumn=3]
    Training is formulated as a two-player minimax game\textsuperscript{\cite[][p.~125]{fleuretLittleBookDeep}}: $D$ maximises its ability to distinguish real from fake; $G$ minimises the probability that $D$ identifies its outputs as fake.
    \tcblower
    \begin{equation}
        \min_G \max_D \;\bigl[\,\mathbb{E}[\log D(x)] + \mathbb{E}[\log(1 - D(G(z)))]\,\bigr]
    \end{equation}

    \tcbitem[title={Training Dynamics and Mode Collapse}, raster multicolumn=6]
    GAN training is notoriously unstable.
    When the discriminator is too strong, gradients to the generator vanish; when it is too weak, the generator does not learn useful structure.
    A key failure mode is \textbf{mode collapse}: the generator learns to produce a small variety of outputs that fool the discriminator, ignoring most of the real data distribution.
    As gradients flow from $D$ back to $G$, the discriminator informs the generator about the cues it detects --- the generator then learns to eliminate those cues\textsuperscript{\cite[][p.~125]{fleuretLittleBookDeep}}.
    Variants such as Wasserstein GAN (WGAN) and spectral normalisation address training stability.
\end{tcbitemize}

% ---- 6.5.2 Autoencoders ---------------------------------------------------------------------
\subsection{Autoencoders}

\begin{tcbitemize}[ skin=sectionraster ]
    \tcbitem[title={Encoder--Bottleneck--Decoder}, raster multicolumn=3]
    An \textbf{autoencoder} consists of an \emph{encoder} $f_\phi$ and a \emph{decoder} $g_\theta$\textsuperscript{\cite[][p.~125]{fleuretLittleBookDeep}}.
    The encoder maps the high-dimensional input $x$ to a low-dimensional latent vector $z = f_\phi(x)$; the decoder reconstructs $\hat{x} = g_\theta(z)$.
    The bottleneck forces the network to learn a compact representation of the data manifold.
    \tcblower
    \begin{itemize}
        \item Loss: $\mathcal{L} = \|x - \hat{x}\|^2$ (MSE) or cross-entropy
        \item Applications: dimensionality reduction, denoising, anomaly detection, pre-training
        \item A \textbf{denoising autoencoder} receives corrupted $\tilde{x}$ as input but targets clean $x$, forcing more robust representations
    \end{itemize}

    \tcbitem[title={Variational Autoencoder (VAE)}, raster multicolumn=3]
    The \textbf{Variational Autoencoder} (Kingma \& Welling, 2013) imposes a prior distribution on the latent space\textsuperscript{\cite[][p.~125]{fleuretLittleBookDeep}}.
    The encoder outputs parameters $(\mu, \sigma)$ of a Gaussian; the \emph{reparameterisation trick} ($z = \mu + \sigma \odot \varepsilon$, $\varepsilon \sim \mathcal{N}(0,I)$) makes sampling differentiable.
    \tcblower
    \begin{equation}
        \mathcal{L}_{\mathrm{ELBO}} = \mathbb{E}_{q_\phi(z|x)}\bigl[\log p_\theta(x|z)\bigr]
        - \mathrm{KL}\bigl(q_\phi(z|x) \,\|\, p(z)\bigr)
    \end{equation}
    The KL term regularises the latent space towards $\mathcal{N}(0,I)$, enabling new samples to be drawn by sampling $z \sim \mathcal{N}(0,I)$ and decoding.
\end{tcbitemize}

% ---- 6.5.3 Restricted Boltzmann Machines ----------------------------------------------------
\subsection{Restricted Boltzmann Machines}

\begin{tcbitemize}[ skin=sectionraster ]
    \tcbitem[title={Energy-Based Generative Model}, raster multicolumn=3]
    A \textbf{Restricted Boltzmann Machine (RBM)} is a bipartite undirected graphical model with visible units $v$ and hidden units $h$, and no intra-layer connections.
    The joint probability is defined via an energy function:
    \begin{equation}
        E(v, h) = -v^\top W h - b^\top v - c^\top h
    \end{equation}
    with $P(v, h) \propto \exp(-E(v,h))$.
    The restriction to bipartite structure makes conditional distributions tractable: $P(h|v)$ and $P(v|h)$ are independent Bernoulli.

    \tcbitem[title={Contrastive Divergence Training}, raster multicolumn=3]
    Exact maximum-likelihood training requires computing the partition function (intractable).
    \textbf{Contrastive Divergence (CD-k)} approximates the gradient\textsuperscript{\cite[][]{Kriesel2007NeuralNetworks}}:
    \begin{itemize}
        \item \emph{Positive phase}: clamp real data $v$; sample $h \sim P(h|v)$
        \item \emph{Negative phase}: run $k$ steps of Gibbs sampling to get model sample $(\tilde{v},\tilde{h})$
        \item Update: $\Delta W \propto \langle vh \rangle_\mathrm{data} - \langle \tilde{v}\tilde{h} \rangle_\mathrm{model}$
    \end{itemize}
    RBMs were used for greedy layer-wise pre-training of deep belief networks (Hinton et al., 2006) but have been largely superseded by modern training methods.
\end{tcbitemize}

% ---- 6.5.4 Capsule Networks -----------------------------------------------------------------
\subsection{Capsule Networks}

\begin{tcbitemize}[ skin=sectionraster ]
    \tcbitem[title={Capsules and Dynamic Routing}, raster multicolumn=6]
    Proposed by Sabour, Frosst \& Hinton (2017) to address a fundamental limitation of CNNs: pooling operations are viewpoint-invariant but discard spatial and pose information.
    A \textbf{capsule} is a group of neurons whose \emph{activity vector} encodes both the presence (vector length) and instantiation parameters such as pose, scale, and orientation (vector direction) of an entity.
    Lower-level capsules send \textbf{votes} to candidate higher-level capsules; an iterative \textbf{dynamic routing} algorithm (3 iterations) selects the higher-level capsule whose pose best agrees with the votes.
    This enables \textbf{equivariance}: as viewpoint changes, the capsule representation changes predictably, preserving part-whole relationships\textsuperscript{\cite[][]{fleuretLittleBookDeep}}.
    \tcblower
    \begin{itemize}
        \item Advantage: encodes spatial hierarchies, more interpretable than CNNs
        \item Limitation: $O(n^2)$ routing cost; does not scale well to complex datasets such as ImageNet
    \end{itemize}
\end{tcbitemize}

% ---- 6.5.5 Spiking Networks -----------------------------------------------------------------
\subsection{Spiking Networks}

\begin{tcbitemize}[ skin=sectionraster ]
    \tcbitem[title={Third-Generation Neural Networks}, raster multicolumn=6]
    \textbf{Spiking Neural Networks (SNNs)}, introduced by Maass (1997), are described as the ``third generation'' of neural networks.
    Rather than communicating through continuous activations, neurons emit discrete \textbf{spike} events.
    The \textbf{Leaky Integrate-and-Fire (LIF)} neuron model accumulates input in a membrane potential $V(t)$; when $V$ exceeds a threshold $\theta$, a spike is emitted and $V$ resets.
    Information can be encoded in spike rates or precise spike timing.
    \tcblower
    \begin{itemize}
        \item \textbf{Energy efficiency}: sparse spike events map naturally onto neuromorphic hardware (Intel Loihi, IBM TrueNorth) with orders-of-magnitude lower power than GPU-based ANNs
        \item \textbf{Biological plausibility}: closer to cortical computation than rate-coded networks
        \item \textbf{Training challenge}: the spike function is non-differentiable; \emph{surrogate gradients} (smooth approximations) enable gradient-based training
        \item \textbf{Current status}: promising for edge and embedded AI; not yet competitive with ANNs on standard benchmarks
    \end{itemize}
\end{tcbitemize}


% ==== Section 6: Further Reading =============================================================
\section{Further Reading}
\subsection{Recommended Literature}

\begin{tcbitemize}[ skin=sectionraster ]
    \tcbitem[title={Core Textbooks and Papers}, raster multicolumn=6]
    \begin{itemize}
        \item \fullcite{fleuretLittleBookDeep}
        \item \fullcite{robertsPrinciplesDeepLearning2022}
        \item \fullcite{Kriesel2007NeuralNetworks}
        \item \fullcite{vaswaniAttentionAllYou2023}
        \item \fullcite{devlinBERTPretrainingDeep2019}
        \item \fullcite{fischerVorlesungGrundlagenNeuronale2024}
        \item \fullcite{dhamaniIntroductionGenerativeAI2024}
        \item \fullcite{farrisHowLargeLanguage2025}
    \end{itemize}
\end{tcbitemize}
```
