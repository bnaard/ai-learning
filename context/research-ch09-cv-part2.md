# Research Notes: Ch09 Computer Vision — Sections 3–6

**Agent:** Research+Writer (Sonnet)
**Date:** 2026-03-14
**Scope:** Sections 3 (CV for Autonomous Systems), 4 (Cognitive CV), 5 (Challenges in CV), 6 (Further Reading)

---

## Section 3: Computer Vision for Autonomous Systems

### 3.1 Image Formation & Acquisition

**Light and the Electromagnetic Spectrum**
- Visible light: 380–700 nm. Cameras sample a 3D scene projected onto a 2D sensor.
- Radiometry: describes light transport (irradiance, radiance, BRDF). Photometry: human perception weighting.
- Key equation: image irradiance E proportional to scene radiance L: E = (pi/(4N^2)) * L * cos^4(theta)
- N = f-number = focal_length / aperture_diameter

**Color Models**
- RGB: device-dependent additive color; sRGB standard for display.
- HSV/HSL: perceptually intuitive (hue, saturation, value/lightness). Good for segmentation by color.
- LAB (CIE L*a*b*): perceptually uniform; L = lightness, a = green-red, b = blue-yellow. Used for white balance and color consistency.
- YCbCr: separates luminance (Y) from chrominance; used in video compression (JPEG, H.264).
- White balance: compensate for scene illumination color temperature (daylight ~5500K, tungsten ~3200K). Methods: gray-world assumption, white patch, learning-based.

**Perspective Camera Model (Pinhole)**
- Projects 3D point (X,Y,Z) to 2D image (x,y):
  - x = f*X/Z, y = f*Y/Z  (f = focal length)
- Homogeneous coordinates: [u,v,w]^T = K * [R|t] * [X,Y,Z,1]^T
- K = camera intrinsic matrix: [[fx, s, cx], [0, fy, cy], [0, 0, 1]]
  - fx, fy: focal lengths in pixels; cx, cy: principal point; s: skew (approx 0)
- [R|t]: extrinsic matrix (rotation + translation, world to camera)

**Camera Calibration — Zhang's Method**
- Estimate K, R, t from multiple views of a planar checkerboard (Zhang 2000).
- Each view gives 2 constraints on K; >=3 views needed.
- Also estimates radial/tangential lens distortion: r(x) = x*(1 + k1*r^2 + k2*r^4 + ...)
- Implemented in OpenCV: cv2.calibrateCamera()

### 3.2 Sensors for Autonomous Systems

**Cameras**
- Monocular: single image; depth ambiguous. Cheap, widely deployed.
- Stereo: two calibrated cameras; depth from disparity d = fB/Z (B = baseline).
- Event cameras (Dynamic Vision Sensors): log changes in log-illuminance asynchronously per pixel. Microsecond latency, high dynamic range, no motion blur.
- Night vision: near-infrared (NIR) illumination + NIR-sensitive sensor, or thermal (LWIR, 8-14 micrometer).
- Rolling vs global shutter: rolling shutter causes distortion with fast motion.

**LiDAR**
- Time-of-Flight (ToF): measures round-trip time of laser pulses -> range d = c*t/2.
- Rotating LiDAR (Velodyne): 360 degree scan; 16-128 beams. Point cloud at 10 Hz.
- Solid-state LiDAR (MEMS/OPA/Flash): no moving parts; cheaper; lower FoV but higher reliability.
- Range: 50-300 m. Resolution: ~0.1 deg. Outputs sparse 3D point cloud.

**Radar**
- FMCW radar: frequency-modulated continuous wave -> simultaneous range + velocity (Doppler).
- 77 GHz automotive radar. All-weather capability. Sparse, but velocity directly measured.

**Sensor Fusion**
- Complementary strengths: camera (rich texture/color), LiDAR (accurate 3D), radar (velocity, weather).
- Early fusion: combine raw data. Late fusion: combine detections. Middle fusion: intermediate feature fusion.
- Kalman filter: optimal linear state estimator; extended/unscented KF for nonlinear systems.

### 3.3 Object Detection and Tracking

**Classical Detection**
- Sliding window: evaluate classifier at multiple positions/scales.
- HOG (Histogram of Oriented Gradients): cell-wise gradient histograms + SVM. Dalal & Triggs (2005).
- Viola-Jones (2001): Haar features + AdaBoost + cascade; real-time face detection.

**Deep Detection Architectures**
- Faster R-CNN (Ren et al. 2015): two-stage. Region Proposal Network (RPN) + ROI pooling + classification.
- SSD (Liu et al. 2015): single-stage. Multi-scale feature maps; predicts class + offset for anchor boxes. 59 fps at 300x300. (Fleuret p.105-109)
- YOLO (Redmon et al. 2016): single forward pass; S×S grid; each cell predicts B boxes + C classes. v8/v9: SOTA real-time.
- DETR (Carion et al. 2020): Transformer encoder-decoder; bipartite matching; no anchors, no NMS.
- Key concepts: anchor boxes, NMS (Non-Maximum Suppression), IoU, mAP.

**Tracking**
- SORT: Kalman filter prediction + Hungarian algorithm association.
- DeepSORT: SORT + appearance feature (deep ReID) for re-identification.
- MOT metrics: MOTA, MOTP, ID switches.
- ByteTrack (2022): uses low-confidence detections; SOTA on MOT17.

### 3.4 Segmentation

**Semantic Segmentation** (Fleuret p.110-112)
- Goal: assign a class label to every pixel.
- FCN (Long et al. 2015): fully convolutional; transposed convolutions for upsampling.
- U-Net (Ronneberger et al. 2015): encoder-decoder with skip connections. Standard in medical imaging.
- DeepLab v3+ (Chen et al. 2018): dilated convolutions + ASPP (Atrous Spatial Pyramid Pooling).
- PSPNet: pyramid pooling for multi-scale context. (Fleuret Figure 6.3)

**Instance & Panoptic Segmentation**
- Mask R-CNN (He et al. 2017): Faster R-CNN + mask branch; ROI Align.
- Panoptic: stuff (semantic) + things (instance) unified. Every pixel gets class + instance ID.
- MOTS: Multi-Object Tracking and Segmentation — per-frame masks + tracking IDs.

---

## Section 4: Cognitive Computer Vision

### 4.1 Image Classification (Fleuret p.104)
- Task: assign class label(s) to an image from finite predefined set.
- Standard models: ResNets (see Ch6), ViT (attention-based). Cross-entropy training.
- Data augmentation: cropping, scaling, mirroring, color changes.
- Transfer Learning: pre-train on ImageNet -> fine-tune on target. Reduces labeled data needs.
- Image Retrieval: CNN embedding + nearest-neighbor search (FAISS); cosine similarity.

### 4.2 Recognition
- Face Recognition pipeline: detection -> alignment -> feature extraction -> comparison.
- Eigenfaces (Turk & Pentland 1991): PCA-based global appearance representation.
- FaceNet (Schroff et al. 2015): triplet loss -> 128-d embedding; L2 distance.
- ArcFace (Deng et al. 2019): additive angular margin loss; SOTA on LFW, MegaFace.
- Verification (same person?) vs Identification (who is this?) — different threat models.

### 4.3 Image Synthesis
- Super-Resolution: SRCNN (Dong et al. 2014) first DL approach. ESRGAN (Wang et al. 2018): GAN-based perceptual loss.
- Style Transfer: Gatys et al. (2015): content loss + Gram matrix style loss; iterative optimization.
- Image-to-Image Translation:
  - pix2pix (Isola et al. 2017): cGAN, paired data.
  - CycleGAN (Zhu et al. 2017): cycle-consistency loss; unpaired domain translation.

### 4.4 Vision and Language (Fleuret p.115-117)
- CLIP (Radford et al. 2021): contrastive training of image encoder + text encoder on 400M pairs.
  - Similarity l_{m,n} = f(i_m)^T g(t_n); enables zero-shot classification.
- Image Captioning: CNN encoder + LSTM/Transformer decoder.
- VQA: image features + question text -> answer classification.
- Text-to-Image:
  - DALL-E (Ramesh et al. 2021): discrete VAE + autoregressive Transformer.
  - Stable Diffusion (Rombach et al. 2022): latent diffusion; denoising in latent space; text conditioning via CLIP.
  - Diffusion process (Fleuret p.121-123): forward process adds noise; model learns to reverse.

---

## Section 5: Challenges in Computer Vision

### 5.1 Fairness and Explainability
- Bias: face recognition error rates vary significantly by demographic (Gender Shades study: Buolamwini & Gebru 2018).
- Grad-CAM (Selvaraju et al. 2017): gradient of class score w.r.t. feature maps -> localization heatmap.
- Saliency maps: backprop class score to input pixels.
- LIME: model-agnostic local perturbation-based explanations.

### 5.2 Self-Supervised and Contrastive Learning
- SimCLR (Chen et al. 2020): two augmented views + NT-Xent contrastive loss. Large batch needed.
- BYOL (Grill et al. 2020): online + target networks; stop-gradient on target; no negatives needed.
- DINO (Caron et al. 2021): ViT + self-distillation; student on local, teacher on global views.
- MAE (He et al. 2021): mask 75% patches -> reconstruct; efficient scalable pre-training.

### 5.3 Robust Computer Vision
- Adversarial examples (Szegedy 2013, Goodfellow 2015): imperceptible perturbation causes misclassification.
  - FGSM: x_adv = x + eps * sign(grad_x L)
- Domain shift: distribution mismatch between training and deployment; domain adaptation via adversarial alignment.
- OOD Detection: detect inputs outside training distribution; energy-based scoring, maximum softmax.

---

## Available BibTeX Keys (confirmed in references.bib)
- `fleuretLittleBookDeep` — Fleuret (2023), Little Book of Deep Learning
- `howseLearningOpenCV42020` — Howse & Minichino (2020), Learning OpenCV 4
- `jahneDigitalImageProcessing2005` — Jähne (2005)
- `elsayedAdversarialReprogrammingNeural2018` — adversarial examples
- `raschkaPythonMachineLearning2015` — Raschka (2015)
- `fischerMaschinellesLernenFuer2024` — Fischer (2024)
- `hurbansGrokkingArtificialIntelligence2020` — Hurbans (2020)
- `ioffeBatchNormalizationAccelerating2015`
- `vaswaniAttentionAllYou2023`
- `devlinBERTPretrainingDeep2019`
- `dhamaniIntroductionGenerativeAI2024`

Keys NOT confirmed (will not cite page numbers for missing keys):
- szeliski, gonzalez, forsyth, klette, davies — not found in bib

## Card Count Plan
- Section 3 (Autonomous Systems): 12 cards
- Section 4 (Cognitive CV): 10 cards
- Section 5 (Challenges): 6 cards
- Section 6 (Further Reading): 1 card
Total: ~29 cards
