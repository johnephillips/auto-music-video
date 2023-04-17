from diffusers import DiffusionPipeline
from PIL import Image
import logging
import numpy as np
from python_coreml_stable_diffusion.pipeline import get_coreml_pipe
from diffusers import StableDiffusionPipeline


# Boilerplate diffuser code for running the original SD model on m1 mac
# pipe = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
# pipe = pipe.to("mps")

# # Recommended if your computer has < 64 GB of RAM
# pipe.enable_attention_slicing()

# prompt = "a photo of an astronaut riding a horse on mars"

# # First-time "warmup" pass if PyTorch version is 1.13 (see explanation above)
# # _ = pipe(prompt, num_inference_steps=1)

# # Results match those from the CPU device after the warmup pass.
# image = pipe(prompt, num_inference_steps=20).images[0]

# # Convert the numpy array to an Image object
# img = Image.fromarray(image)

# # Show the image
# img.show()


def get_model(
    model_version, i, compute_unit, prompt, num_inference_steps, guidance_scale
):
    logger.info("Initializing PyTorch pipe for reference configuration")

    pytorch_pipe = StableDiffusionPipeline.from_pretrained(
        model_version, use_auth_token=True
    )

    user_specified_scheduler = None
    # if args.scheduler is not None:
    #     user_specified_scheduler = SCHEDULER_MAP[args.scheduler].from_config(
    #         pytorch_pipe.scheduler.config
    #     )

    coreml_pipe = get_coreml_pipe(
        pytorch_pipe=pytorch_pipe,
        mlpackages_dir=i,
        model_version=model_version,
        compute_unit=compute_unit,
        scheduler_override=user_specified_scheduler,
    )

    return coreml_pipe


def generate_image(model, prompt, num_inference_steps, guidance_scale, out_path):
    logger.info("Beginning image generation.")
    image = model(
        prompt=prompt,
        height=model.height,
        width=model.width,
        num_inference_steps=num_inference_steps,
        guidance_scale=guidance_scale,
    )
    logger.info(f"Saving generated image to {out_path}")
    image["images"][0].save(out_path)


def init(seed):
    logger.info(f"Setting random seed to {seed}")
    np.random.seed(seed)


if __name__ == "__main__":
    # Init logging
    logging.basicConfig()
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    # Constants
    seed = 93
    model_version = "runwayml/stable-diffusion-v1-5"
    i = "stable_diffusion_apple/models/coreml-stable-diffusion-v1-5_split_einsum_packages"
    compute_unit = "ALL"
    prompt = "a photo of an astronaut riding a horse on mars"
    num_inference_steps = 20
    guidance_scale = 7.5
    out_path = "./img.png"

    init(seed)

    # Initializing the coreml model is unfortunately very slow
    model = get_model(
        model_version, i, compute_unit, prompt, num_inference_steps, guidance_scale
    )

    generate_image(model, prompt, num_inference_steps, guidance_scale, out_path)
