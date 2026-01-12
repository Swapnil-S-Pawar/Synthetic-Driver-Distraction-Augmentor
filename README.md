# Synthetic Driver Distraction Augmentor

## Overview
The Synthetic Driver Distraction Augmentor project aims to create a dataset of synthetic images depicting drivers engaged in various distracted actions, such as eating or checking their watch. By leveraging advanced techniques like Stable Diffusion, ControlNet, and CLIP, this project addresses the challenge of obtaining diverse and specific images that are often underrepresented in existing datasets.

## Project Structure
The project is organized into the following directories and files:

- **notebooks/**: Contains Jupyter notebooks for Google Colab.
  - `colab_synthetic_driver_augmentor.ipynb`: The main notebook for implementing the synthetic driver distraction augmentor.

- **src/**: Contains the source code for the project.
  - **diffusion/**: Functions for generating synthetic images.
    - `generate_images.py`: Code for image generation using the Hugging Face diffusers library.
  - **controlnet/**: Implements control mechanisms for image generation.
    - `canny_control.py`: Canny edge detection for perspective control.
    - `pose_control.py`: Pose estimation for driver positioning.
  - **clip_filter/**: Functions for filtering images based on relevance.
    - `filter_images.py`: Utilizes CLIP to filter out irrelevant images.
  - **utils/**: Utility functions for dataset management.
    - `dataset_utils.py`: Functions for saving, loading, and preprocessing images.
  - `app.ts`: Main entry point for coordinating the application.

- **requirements.txt**: Lists Python dependencies required for the project.

- **package.json**: Configuration file for npm, listing JavaScript dependencies.

- **tsconfig.json**: TypeScript configuration file specifying compiler options.

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd synthetic-driver-distraction-augmentor
   ```

2. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Install JavaScript dependencies:
   ```
   npm install
   ```

4. Open the Jupyter notebook in Google Colab:
   - Upload `colab_synthetic_driver_augmentor.ipynb` to your Google Drive or open it directly in Colab.

## Usage Guidelines
- Use the provided Jupyter notebook to generate synthetic images by specifying the desired distracted actions.
- The generated images will be filtered and saved using the utility functions provided in the `src/utils/dataset_utils.py` file.
- Ensure that the necessary libraries are installed and configured correctly to avoid any runtime issues.

## Contributing
Contributions to enhance the project are welcome. Please submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
