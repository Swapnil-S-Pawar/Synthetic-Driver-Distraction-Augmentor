# Synthetic Driver Distraction Augmentation

## Project Overview
The Synthetic Driver Distraction Augmentation project aims to create a synthetic dataset of driver distraction scenarios for research in automotive AI. By generating realistic in-cabin images depicting various distractions (such as eating or using a phone), this project supports the development of advanced activity recognition systems while ensuring privacy and compliance with data protection regulations.

## Key Features
- **Structural Fidelity**: Utilizes ControlNet with OpenPose to maintain anatomically correct joint positions of drivers, ensuring realistic pose estimation.
- **Metric-Guided Selection**: Implements a CLIP-based filtering mechanism to validate generated images, ensuring that only relevant distraction data is included in the training set.
- **Privacy-Safe**: The dataset is generated synthetically, eliminating the need for real human subjects and mitigating data privacy risks.

## Project Structure
```
synthetic-driver-distraction-augmentation
├── pipeline
│   ├── __init__.py
│   ├── generator.py
│   └── validator.py
├── main.py
├── Driver_Augmentation_Colab.ipynb
├── pyproject.toml
└── README.md
```

## Installation
To set up the project, you will need to install the required dependencies. You can do this by running the following command in your terminal or within a Google Colab notebook:

```bash
pip install -q diffusers transformers accelerate opencv-python controlnet_aux
```

## Usage
1. **Generate Synthetic Data**: Use the `SyntheticDriverAugmentor` class from `pipeline/generator.py` to generate images based on distraction prompts.
2. **Validate Generated Images**: The `validator.py` file contains methods to filter out images that do not meet the quality criteria based on cosine similarity scores.
3. **Run the Main Script**: Execute `main.py` to orchestrate the generation and validation process for a list of distraction scenarios.

## Evaluation Metrics (Metric-Guided Research)

This project treats synthetic data generation as a **measure → filter → log** loop. Below are practical metrics to quantify quality and make dataset creation reproducible.

### A) Text–Image Alignment (CLIP Cosine Similarity)
**What it measures:** how well the generated image matches the distraction prompt (e.g., “driver using a phone”).

- **Metric:** cosine similarity between CLIP image and text embeddings
- **Usage:** reject samples below a threshold (`clip_threshold`)
- **Report:** per-scenario mean/median similarity, and acceptance rate at the chosen threshold

### B) Acceptance Rate (Filtering Efficiency)
**What it measures:** how often the generator produces valid samples under your constraints.

- **Metric:** `accepted / attempted` (tracked per scenario)
- **Why:** helps tune prompts, negative prompts, inference steps, and thresholds

### C) Structural Fidelity Proxy (Pose / Keypoint Coverage)
**What it measures:** whether the driver anatomy remains plausible and detectable.

- **Metric (suggested):** run a pose detector on the **generated image** and compute:
  - `coverage = valid_keypoints / total_keypoints`
- **Usage:** reject samples with low pose coverage (often indicates artifacts / implausible limbs)
- **Why it matters:** improves downstream robustness for pose-driven activity recognition

### D) Diversity Heuristics (Optional)
**What it measures:** whether the dataset collapses to near-duplicates.

- **Metric (suggested):** embedding-based diversity (e.g., average pairwise distance in CLIP image embedding space per scenario)
- **Usage:** flag near-duplicates; enforce a minimum diversity threshold when exporting a training set

### Recommended Summary Table (per run)
At minimum, log:
- number of attempted samples
- number of accepted samples
- acceptance rate (%)
- CLIP similarity mean/median/std
- (optional) pose coverage mean/median

## Google Colab
A ready-to-run Google Colab notebook, `Driver_Augmentation_Colab.ipynb`, is provided to demonstrate the functionality of the project. This notebook includes all necessary setup steps and example usage.

## Conclusion
This project contributes to the field of automotive AI by providing a synthetic dataset that can be used for training and validating activity recognition models. By focusing on metric-guided research and ensuring privacy, it paves the way for safer and more effective in-cabin monitoring systems.
