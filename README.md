# auto-music-video

auto-music-video uses generative AI tools to automatically generate music videos for a given song.
Currently, it consists of a proof-of-concept jupyter notebook which generates a music video for the song "Yesterday"
by The Beatles using Stable Diffusion v1.5 and prompts from GPT-3.5. One image is generated for each lyric from a lyrics file.

The particular Stable Diffusion model is a coreml model optimized for running on low memory apple devices
(i.e. images can be generated quickly on an 8gb M1 macbook air).
The image prompts stored in yesterday_prompts.txt were created by asking ChatGPT (GPT-3.5) the following:
```
"I want to create a sequence of images for the song "Yesterday" by the Beatles. I will provide the lyrics to you,
and want you to give one prompt for each image that can be given to a generative image model.
Output only the prompts as a numbered list. Here are the 16 lyrics: [lyrics pasted in from the .lrc file]"
```

<h2 align="center"> Demo: "Yesterday" by The Beatles </h2>

https://user-images.githubusercontent.com/11326277/232620425-cd77d5cd-81c6-46f9-a56a-25a05bdbf45c.mp4

## 📋 Requirements
- Python 3.9 or later
- A device compatible with Apple's coreml models (e.g. M1 Macbook air)

## 💾 Installation
1. Clone the repository:

    ```bash
    git clone https://github.com/johnephillips/auto-music-video.git
    ```

2. Navigate to the directory where the repository was downloaded

    ```bash
    cd auto-music-video
    ```

3. It is recommended to either use conda or a virtualenv. Then install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Download the Stable Diffusion coreml model "coreml-stable-diffusion-v1-5_split_einsum_packages" into
`./stable_diffusion_apple/models/coreml-stable-diffusion-v1-5_split_einsum_packages` (see https://huggingface.co/blog/diffusers-coreml for details)

5. Run the `sd.ipynb` notebook
    ```bash
    jupyter notebook
    ```
