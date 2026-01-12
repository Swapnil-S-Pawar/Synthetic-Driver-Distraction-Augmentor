import torch
from pipeline.generator import SyntheticDriverAugmentor

def main():
    # Initialize the augmentor
    augmentor = SyntheticDriverAugmentor()
    
    # List of distraction scenarios
    distraction_scenarios = [
        "driver eating",
        "driver using phone",
        "driver adjusting radio",
        "driver drinking coffee",
        "driver talking to passenger"
    ]
    
    # Generate and validate images for each scenario
    for scenario in distraction_scenarios:
        # Generate image based on the scenario
        pose_map = None  # Placeholder for actual pose data
        image = augmentor.generate(prompt=scenario, pose=pose_map)
        
        # Validate the generated image
        score = augmentor.validate_image(image, scenario)
        
        # Check if the score meets the threshold
        if score >= 0.5:  # Example threshold
            print(f"Valid image generated for: {scenario} with score: {score}")
            # Save or process the valid image as needed
        else:
            print(f"Discarded image for: {scenario} with score: {score}")

if __name__ == "__main__":
    main()