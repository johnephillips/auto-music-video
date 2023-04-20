# auto-music-video

auto-music-video uses generative AI tools to automatically generate music videos for a given song. More precisely, the goal is: given an mp3 file for a song and a corresponding lyrics (.lrc) file, generate a music video with AI art generated for each lyric. There have been a number of incredibly popular YouTube music videos which do this manually, often with a great deal of manual prompt tuning, like [this great music video for Mr. Blue Sky](https://www.youtube.com/watch?v=nyD6g47DHQk). This project attempts to automate that a little further by having an LLM generate the image prompts and by automating all of the image generation and video editing. Currently, it consists of a proof-of-concept jupyter notebook which generates a music video for the song "Yesterday" by The Beatles using DALL·E 2 for remote generation (or Stable Diffusion v1.5 for local generation) and prompts from GPT-3.5 (or a file).

<h2 align="center"> Demo: "Yesterday" by The Beatles, with art from DALL·E 2 </h2>

https://user-images.githubusercontent.com/11326277/233494975-47d1aeac-c4fb-4dfb-811f-f1e6d9c6036e.mp4

The particular Stable Diffusion model is a coreml model optimized for running on low memory apple devices
(i.e. images can be generated quickly on an 8gb M1 macbook air).
The image prompts stored in yesterday_prompts.txt were created by asking ChatGPT (GPT-3.5) the following:
```
"I want to create a sequence of images for the song "Yesterday" by the Beatles. I will provide the lyrics to you,
and want you to give one prompt for each image that can be given to a generative image model.
Output only the prompts as a numbered list. Here are the 16 lyrics: [lyrics pasted in from the .lrc file]"
```

## 📋 Requirements
- Python 3.9 or later
- (Necessary only for local art generation) A device compatible with Apple's coreml models (e.g. M1 Macbook air)

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

5. If you wish to use remote generation for images or prompts, set your [OPENAI_API_KEY](https://help.openai.com/en/articles/5112595-best-practices-for-api-key-safety) by running something like:
    ```
    echo "export OPENAI_API_KEY='yourkey'" >> ~/.zshrc
    ```

5. Run the `sd.ipynb` notebook
    ```bash
    jupyter notebook
    ```
