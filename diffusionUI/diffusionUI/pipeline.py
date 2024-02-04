from diffusers import DiffusionPipeline
import torch

class DiffusionModel:
    pipeline = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16)
    pipeline.to("cuda")

    def __init__(self):
        if (self.pipeline is None):
            self.pipeline = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16)
            self.pipeline.to("cuda")

    def generate_image(self, positive_prompt):
        print(positive_prompt)
        image = self.pipeline(prompt=positive_prompt).images[0]
        print(image)
        return image
