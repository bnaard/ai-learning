# Research Notes: Ch09 Computer Vision — Sections 1-2
## Agent: Research+Writer | Date: 2026-03-14

## Available Bibliography Keys for CV
- `jahneDigitalImageProcessing2005` — Jähne, Bernd (2005). Digital Image Processing (6th ed.). Springer.
- `howseLearningOpenCV42020` — Howse & Minichino (2020). Learning OpenCV 4 Computer Vision with Python 3. Packt.
- `fleuretLittleBookDeep` — Fleuret, François. The Little Book of Deep Learning.
- **New entries to add**: szeliski2022, gonzalezWoods2018, hartleyZisserman2004 (standard CV references from literature list in ch09 stub)

## Section 1: Image Processing and Low-Level Vision

### 1.1 Image Acquisition
**Human Visual System**
- Retina contains ~120M rods (low-light, achromatic) and ~6M cones (photopic, 3 types: L/M/S for RGB).
- Fovea: high-density cones for fine detail; peripheral vision dominated by rods.
- The brain does significant post-processing (lateral inhibition, contrast enhancement, invariance).
- Relevance to CV: motivates multi-scale representations, color spaces, HDR imaging.

**Camera Sensors**
- CCD (Charge-Coupled Device): each pixel read sequentially via shifting; high quality, higher power.
- CMOS (Complementary Metal-Oxide-Semiconductor): each pixel has own amplifier; lower power, faster, now dominant.
- Bayer mosaic: most sensors use one R, two G, one B filter per 2×2 pixel block; demosaicing recovers full color.
- Sensor noise: shot noise (Poisson), read noise (Gaussian), fixed-pattern noise.

**Digital Image as Matrix**
- Grayscale image: 2D matrix I[y,x] of intensity values (typically uint8: 0–255).
- Color image: 3D tensor H×W×3.
- Pixel spacing defines spatial resolution; bit depth defines intensity resolution.

### 1.2 Image Representation and Morphology
**Image Types**
- Binary (0/1), grayscale (0–255), color (RGB/HSV/LAB), depth/range images (float or uint16).
- Multispectral: >3 spectral channels (e.g., satellite, hyperspectral).

**Color Spaces**
- RGB: device-dependent, additive primaries.
- HSV (Hue, Saturation, Value): perceptually intuitive; hue is robust to illumination changes (used in skin detection, segmentation).
- CIE LAB: perceptually uniform; L* lightness, a* red-green, b* blue-yellow; device-independent.
- YCbCr: luma + chrominance; used in JPEG/video compression.

**Morphological Operations** (structuring element B applied to binary image A)
- Erosion: A ⊖ B — shrinks foreground; removes isolated pixels.
  Formula: (A ⊖ B)(x) = {p | B+p ⊆ A}
- Dilation: A ⊕ B — expands foreground; fills small holes.
- Opening = Erosion then Dilation: removes small objects (structuring element doesn't fit).
- Closing = Dilation then Erosion: fills small holes, connects nearby objects.
- Grayscale morphology: uses min/max operations with flat structuring element.
- Hit-or-Miss: detects specific binary patterns.

### 1.3 Single and Multi-View Geometry
**Pinhole Camera Model**
- Idealized camera with single aperture point (center of projection).
- Perspective projection equation:
  [u, v, 1]^T ~ K [R | t] [X, Y, Z, 1]^T
  where K = intrinsic matrix [[f_x, 0, c_x], [0, f_y, c_y], [0, 0, 1]]
  f_x, f_y: focal lengths in pixels; c_x, c_y: principal point.
- Homogeneous coordinates handle projective geometry elegantly.
- Lens distortion (radial, tangential) corrected by calibration.

**Homography**
- Maps points between two planes (or two views of a planar scene).
- 3×3 matrix H (projective, 8 DOF). Estimated with RANSAC + DLT.
- Applications: panorama stitching, planar AR markers.

**Stereo Vision and Epipolar Geometry**
- Epipolar constraint: for a point p in left image, its correspondence lies on the epipolar line l' = Fp in the right image.
- F = fundamental matrix (3×3, rank 2, 7 DOF); E = essential matrix (for calibrated cameras).
- Stereo depth: disparity d = x_L − x_R; depth Z = f·B/d (baseline B, focal length f).

### 1.4 Filtering
**Spatial Domain Filtering**
- Convolution: (f * g)[x,y] = Σ_{i,j} f[i,j] · g[x−i, y−j]
  In practice: correlation (no flip) used in feature detection.
- Gaussian blur: G(x,y;σ) = (1/2πσ²) exp(−(x²+y²)/2σ²)
  Reduces high-frequency noise; σ controls smoothing amount.
- Sharpening: unsharp mask = I + α(I − Gaussian(I)); amplifies high frequencies.
- Median filter: non-linear; excellent for salt-and-pepper noise (preserves edges better than Gaussian).

**Frequency Domain (Fourier)**
- DFT: F(u,v) = Σ_{x,y} f(x,y) · e^{−j2π(ux/M + vy/N)}
- Convolution theorem: convolution in spatial domain = multiplication in frequency domain.
- Low-pass filter: attenuates high frequencies → blurring.
- High-pass filter: attenuates low frequencies → edge emphasis.
- Band-pass/stop filters for specific frequency selection.

### 1.5 Texture
**Classical Texture Descriptors**
- GLCM (Gray-Level Co-occurrence Matrix): captures spatial relationship between pixel intensities; features: contrast, correlation, energy, homogeneity.
- LBP (Local Binary Pattern): compare each pixel to its 8 neighbors; binary string → histogram. Rotation-invariant variants exist. Efficient, works on grayscale.
- Gabor filters: oriented sinusoidal wave modulated by Gaussian; captures frequency + orientation. Multi-scale, multi-orientation filter bank → texture features.

**Bag of Visual Words (BoVW)**
- Sample local descriptors (SIFT) from images.
- K-means cluster into visual vocabulary (codebook).
- Represent each image as histogram over codewords.
- Used for texture and image retrieval (TF-IDF weighting).

**CNN Features for Texture**
- Early CNN layers detect Gabor-like edges; middle layers capture textures.
- Gram matrix G = F^T F (features × features): captures style/texture statistics (used in neural style transfer).
- Deep features outperform hand-crafted descriptors on texture benchmarks.

---

## Section 2: Mid-Level Vision and Video

### 2.1 Edge and Feature Detection
**Edge Detection**
- Edges: locations of rapid intensity change; caused by depth discontinuity, surface orientation, reflectance.
- Sobel operator: 3×3 kernel approximates gradient (Gx, Gy); magnitude = √(Gx²+Gy²).
  Gx = [[-1,0,1],[-2,0,2],[-1,0,1]], Gy = transpose of Gx.
- Canny edge detector (1986): gold standard.
  Steps: (1) Gaussian smooth, (2) gradient magnitude & direction, (3) non-maximum suppression, (4) double threshold (high/low), (5) hysteresis linking.
  Output: thin, connected edge chains.

**Corner/Interest Point Detection**
- Harris corner detector: M = Σ w(x,y) [Ix², IxIy; IxIy, Iy²]; response R = det(M)−k·trace²(M).
  Corner: both eigenvalues large (R > threshold).
- FAST (Features from Accelerated Segment Test): test 16 pixels on circle; corner if ≥N contiguous are brighter/darker by threshold. Very fast for real-time use.
- SIFT (Scale-Invariant Feature Transform, Lowe 2004): LoG (Laplacian of Gaussian) blob detection at multiple scales via DoG (Difference of Gaussians); orientation from gradient histogram; 128-dim descriptor.
- SURF: approximation of SIFT with integral images; faster. ORB: binary descriptor, patent-free, fast.

**Feature Matching**
- Nearest-neighbor matching in descriptor space (L2 for SIFT, Hamming for ORB).
- Lowe's ratio test: match if d1/d2 < 0.8.
- RANSAC: random sample consensus to find geometric model (homography) from noisy matches.

### 2.2 Segmentation
**Thresholding**
- Global (Otsu): maximizes inter-class variance between foreground/background; optimal threshold computed analytically from histogram.
- Adaptive: threshold varies locally (e.g., mean/Gaussian of neighborhood window).

**Region-Based: Watershed**
- Treat gradient magnitude as topographic surface; water fills from seed points ("markers").
- Boundaries form at watershed lines.
- Over-segmentation mitigated by marker selection.

**Graph-Cut Segmentation**
- Represent image as graph: nodes=pixels, edges weighted by similarity.
- Min-cut: partition minimizes edge weights between segments.
- GrabCut (Rother et al. 2004): iterative; uses GMMs for foreground/background appearance models.

**Superpixels**
- Group pixels into perceptually uniform patches (SLIC, 2012: Simple Linear Iterative Clustering).
- Reduce computation in subsequent pipeline; preserve edges well.
- SLIC: k-means in [CIELAB, x, y] space with spatial constraint.

### 2.3 Motion and Optical Flow
**Optical Flow Equation**
- Brightness constancy assumption: I(x,y,t) = I(x+u, y+v, t+1)
- Taylor expansion → Lucas-Kanade constraint: I_x·u + I_y·v + I_t = 0
  (one equation, two unknowns: aperture problem)

**Lucas-Kanade (1981)**
- Assumes local patch has constant flow; overdetermined system solved by least squares.
- Works well for small displacements; fails for large motions or homogeneous regions.

**Horn-Schunck (1981)**
- Global method: adds smoothness regularization (penalizes large flow gradients).
- Variational formulation; solved iteratively.
- Dense flow field; sensitive to discontinuities.

**Deep Optical Flow: FlowNet (2015)**
- First CNN trained end-to-end for optical flow on synthetic data (Flying Chairs).
- FlowNet 2.0: stacked networks; near real-time.
- PWC-Net (2018): pyramid + warping + cost volume; state-of-the-art efficiency.
- RAFT (2020): iterative refinement with 4D cost volumes; current benchmark leader.

### 2.4 Tracking
**Kalman Filter**
- Two-step: Predict (state transition) + Update (measurement correction).
- Predict: x̂_{k|k-1} = F·x_{k-1|k-1} + B·u; P_{k|k-1} = F·P·F^T + Q
- Update: K = P·H^T·(H·P·H^T + R)^{-1}; x̂_{k|k} = x̂_{k|k-1} + K·(z_k − H·x̂)
- Assumes linear dynamics + Gaussian noise; optimal for these conditions.
- Extended Kalman Filter (EKF): linearizes nonlinear dynamics via Jacobians.

**Particle Filter**
- Sequential Monte Carlo: maintain set of weighted hypotheses ("particles").
- Non-linear, non-Gaussian tracking; handles multi-modal distributions.
- Steps: propagate particles through motion model → weight by likelihood → resample.
- Computationally expensive; scales poorly with state dimension.

**Deep Tracking**
- SORT (Simple Online and Realtime Tracking, 2016): Kalman filter + Hungarian algorithm for bounding box association; uses IoU as distance metric.
- DeepSORT (2017): adds appearance descriptor (deep ReID network); reduces ID switches.
- Modern: ByteTrack (2022), StrongSORT, OC-SORT — improve association with low-confidence detections.

### 2.5 Shape
**Shape from Shading**
- Reconstruct surface normals/depth from single image + known illumination.
- Lambertian model: I = ρ · (n · l), n=surface normal, l=light direction, ρ=albedo.
- Underdetermined without constraints (shape-albedo ambiguity).

**Stereo/SfM 3D Reconstruction**
- Shape from Stereo: dense disparity map → depth map via triangulation.
- Structure from Motion (SfM): multiple images → sparse 3D point cloud + camera poses.
  Pipeline: feature extraction → matching → RANSAC → bundle adjustment (non-linear refinement of all cameras + points simultaneously).
- Multi-View Stereo (MVS): dense reconstruction from calibrated images.

**Active Shape / Snakes**
- Active contours (Kass, Witkin, Terzopoulos 1988): energy-minimizing curve.
  E = ∫ [α|C'|² + β|C''|² + E_image(C)] ds
  Internal energy (smoothness) + external energy (image gradient).
- Level-set methods: implicit representation; handle topology changes.

---

## Key BibTeX References
Primary available keys:
- `jahneDigitalImageProcessing2005` — foundational image processing
- `howseLearningOpenCV42020` — practical implementations
- `fleuretLittleBookDeep` — CNN features context

**New keys to add to references.bib:**
- `szeliski2022` — Szeliski, R. (2022). Computer Vision: Algorithms and Applications (2nd ed.). Springer.
- `gonzalezWoods2018` — Gonzalez, R.C., Woods, R.E. (2018). Digital Image Processing (4th ed.). Pearson.
- `hartleyZisserman2004` — Hartley, R., Zisserman, A. (2004). Multiple View Geometry in Computer Vision (2nd ed.). Cambridge.
