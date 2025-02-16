# Image Caption Generator

## Overview
The **Image Caption Generator** is a simple and efficient tool that generates a caption for an image using OpenAI's **CLIP model**. It works offline and can quickly recognize objects and scenes in an image.

## Features
- Uses OpenAI's **CLIP** model for image understanding.
- Works **offline** without requiring an internet connection.
- Simple and lightweight, runs on both **CPU and GPU**.
- Displays the image with its generated caption.

## Installation
To run this project, make sure you have Python installed. Then, install the required dependencies:

```sh
pip install torch torchvision torchaudio ftfy regex tqdm git+https://github.com/openai/CLIP.git matplotlib opencv-python numpy pillow
```

## Usage
Run the script in your terminal:

```sh
python Offline_Caption_Generator.py
```

## How It Works
1. **Loads** the CLIP model.
2. **Preprocesses** the input image.
3. **Compares** the image against predefined text labels.
4. **Generates** the best matching caption.
5. **Displays** the image with the caption.

## Example Output
```sh
Generated Caption: A photo of a cat
```

The script will also open a window displaying the image with the generated caption.

## Customization
- Modify the `texts` list in the `generate_caption()` function to add more possible captions.
- Change the `image_path` variable to use your own image.

## License
This project is **open-source** and free to use.

