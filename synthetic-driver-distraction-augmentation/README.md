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

## Google Colab
A ready-to-run Google Colab notebook, `Driver_Augmentation_Colab.ipynb`, is provided to demonstrate the functionality of the project. This notebook includes all necessary setup steps and example usage.

## Conclusion
This project contributes to the field of automotive AI by providing a synthetic dataset that can be used for training and validating activity recognition models. By focusing on metric-guided research and ensuring privacy, it paves the way for safer and more effective in-cabin monitoring systems.