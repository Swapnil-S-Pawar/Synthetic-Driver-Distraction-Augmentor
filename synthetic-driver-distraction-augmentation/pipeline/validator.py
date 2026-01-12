class CLIPValidator:
    def __init__(self, clip_model, clip_processor, threshold=0.5):
        self.clip_model = clip_model
        self.clip_processor = clip_processor
        self.threshold = threshold

    def validate_image(self, image, prompt):
        """Calculates similarity score to filter out 'hallucinations'."""
        inputs = self.clip_processor(text=[prompt], images=image, return_tensors="pt", padding=True).to(image.device)
        with torch.no_grad():
            outputs = self.clip_model(**inputs)
        score = outputs.logits_per_image.item() / 100  # Normalized score
        return score >= self.threshold

    def filter_images(self, images, prompts):
        """Filters a list of images based on their corresponding prompts."""
        valid_images = []
        for image, prompt in zip(images, prompts):
            if self.validate_image(image, prompt):
                valid_images.append(image)
        return valid_images