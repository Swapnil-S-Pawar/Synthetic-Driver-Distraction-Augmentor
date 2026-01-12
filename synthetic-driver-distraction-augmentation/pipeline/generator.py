import torch
from diffusers import StableDiffusionControlNetPipeline, ControlNetModel

class SyntheticDriverAugmentor:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        
        # Load ControlNet with OpenPose for maintaining structural driver anatomy
        controlnet = ControlNetModel.from_pretrained("lllyasviel/sd-controlnet-openpose", torch_dtype=torch.float16)
        self.pipe = StableDiffusionControlNetPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5", controlnet=controlnet, torch_dtype=torch.float16
        ).to(self.device)

    def generate(self, prompt, pose):
        """Generates an image based on the given prompt and pose."""
        image = self.pipe(prompt=prompt, controlnet_conditioning_image=pose).images[0]
        return image

    def generate_scenarios(self, scenarios, poses):
        """Generates a list of images for the given distraction scenarios and poses."""
        images = []
        for scenario, pose in zip(scenarios, poses):
            image = self.generate(prompt=scenario, pose=pose)
            images.append(image)
        return images