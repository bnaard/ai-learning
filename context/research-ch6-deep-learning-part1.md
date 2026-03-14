# Research Notes: Ch6 Deep Learning — Sections 1–3
**Date:** 2026-03-13
**Sources:** Fleuret (Little Book of Deep Learning), Kriesel (Brief Intro to Neural Networks), LeCun (Theoretical Framework for Backprop), Daumé III (Course in ML), Roberts et al. (Principles of DL Theory)

---

## Section 1: Introduction to Neural Networks and Deep Learning

### 1.1 The Biological Brain (Kriesel ch.2)
- Neuron components: dendrites (input), soma (cell body, integration), axon (output), synapses (connections)
- Action potential: membrane potential at rest ~−70 mV; when excitation exceeds threshold → spike propagates down axon
- Chemical synapses: neurotransmitter release modulates connection strength → biological basis for "weights"
- 100-step rule: brain performs complex recognition in ~500ms; neurons fire at ~100Hz → at most ~100 sequential steps → massive parallelism
- ~86 billion neurons, ~10^14 synapses

### 1.2 Perceptron and Multi-Layer Perceptrons (Kriesel ch.3, Fleuret ch.1)
- Rosenblatt (1957): single-layer perceptron with binary threshold activation
- Perceptron convergence theorem: guaranteed to find separating hyperplane if data is linearly separable
- XOR problem: Minsky & Papert (1969) proved single perceptron cannot solve XOR → "AI winter"
- MLP: multiple layers with nonlinear activations solve XOR; hidden layers enable learning complex decision boundaries
- Hebbian learning → error-correction → backpropagation (Rumelhart, Hinton, Williams 1986)

### 1.3 Activation Functions (Fleuret §4.1, Roberts ch.1)
- Sigmoid: σ(x) = 1/(1+e^−x), output [0,1], suffers vanishing gradients
- Tanh: zero-centered [-1,1], still saturates
- ReLU: max(0,x), Glorot et al. 2011; most widely used; "dying ReLU" problem
- Leaky ReLU: max(αx, x) with small α; GELU: x·Φ(x)
- Softmax: exp(x_i)/Σexp(x_j), used for classification output layer

## Section 2: Network Architectures

### 2.1 Feed-Forward Networks (Fleuret §4.2)
- Dense/fully-connected layers: Y = σ(WX + b)
- Universal Approximation Theorem: single hidden layer with enough neurons can approximate any continuous function
- Depth vs width: deeper networks are exponentially more parameter-efficient than wider ones for many function classes

### 2.2 Convolutional Networks (Fleuret §5.1)
- Convolution operation: learned filters slide over input; weight sharing → translation equivariance
- Receptive field grows with depth
- Pooling: max or average; reduces spatial dimensions; provides some translation invariance
- Architecture progression: LeNet (1998) → AlexNet (2012, ReLU + dropout) → VGG (2014, 3×3 filters) → ResNet (2015, skip connections)

### 2.3 RNNs and LSTMs (Fleuret §5.2, Kriesel ch.7)
- RNN: h_t = σ(W_h h_{t-1} + W_x x_t + b); shares weights across time steps
- Vanishing/exploding gradient problem: gradients multiplied through many time steps
- LSTM (Hochreiter & Schmidhuber, 1997): cell state c_t + 3 gates (forget, input, output)
- GRU: simplified LSTM with 2 gates (reset, update); fewer parameters, similar performance

## Section 3: Neural Network Training

### 3.1 Forward Pass and Loss Functions (Fleuret §3.1-3.2)
- Forward pass: input propagated layer by layer; output compared to target via loss function
- MSE: (1/N)Σ(y - ŷ)², used for regression
- Cross-entropy: -Σ y_i log(ŷ_i), used for classification (with softmax output)
- MAE: (1/N)Σ|y - ŷ|, robust to outliers

### 3.2 Weight Initialization (Fleuret §4.4, Roberts §1.3)
- Zero init → all neurons learn same features (symmetry breaking problem)
- Xavier/Glorot: Var(W) = 2/(n_in + n_out), designed for sigmoid/tanh
- He initialization: Var(W) = 2/n_in, designed for ReLU
- Proper initialization keeps activations and gradients in reasonable range across layers

### 3.3 Backpropagation and Gradient Descent (LeCun, Fleuret §3.3)
- Chain rule applied layer by layer backward from loss
- SGD: θ ← θ − η∇L; mini-batch SGD reduces variance of gradient estimates
- Momentum: accumulates past gradients; helps escape shallow local minima
- Adam (Kingma & Ba, 2014): adaptive learning rates per parameter; combines momentum + RMSprop

### 3.4 Training Loop (Fleuret §3.4)
- Epoch: one full pass through training data
- Mini-batch: subset of training data; trade-off between gradient quality and computational cost
- Train/validation/test split: monitor validation loss to detect overfitting
- Learning rate scheduling: step decay, cosine annealing, warmup
- Early stopping: halt training when validation loss stops improving

### 3.5 Regularization and Overtraining (Fleuret §4.5-4.6)
- Dropout (Srivastava et al., 2014): randomly zero out activations with probability p during training; rescale at test time
- L1/L2 regularization: add penalty term λ||w|| to loss
- Batch normalization (Ioffe & Szegedy, 2015): normalize activations per mini-batch; stabilizes training, allows higher learning rates
- Data augmentation: artificially expand training set (flips, rotations, crops, color jitter)

## BibTeX Keys
- `fleuretLittleBookDeep` — primary source for most content
- `krieselBriefIntroductionNeural2007` — biological brain, perceptron history
- `lecunTheoreticalFrameworkBack` — backpropagation theory
- `iiiCourseMachineLearning` — ML/DL foundations
- `robertsPrinciplesDeepLearning2022` — initialization, depth theory
