# AI Image Caption Generator

## Overview
The **AI Image Caption Generator** is a Python-based application that utilizes OpenAI's CLIP model to generate meaningful captions for images. This tool provides users with an easy-to-use graphical interface (GUI) for selecting images and obtaining captions, along with additional features such as text-to-speech, translation, history tracking, and more.

## Features
1. **AI-Powered Captions** – Uses the CLIP model to generate accurate image captions.
2. **Graphical User Interface (GUI)** – Simple and user-friendly UI using Tkinter.
3. **Image Preview** – Displays the selected image before generating a caption.
4. **Copy to Clipboard** – Easily copy captions for further use.
5. **Text-to-Speech** – Listen to the generated captions using a speech engine.
6. **Translation Support** – Translate captions into multiple languages.
7. **Caption History** – Stores generated captions for reference.
8. **Colorful Theme** – An elegant and visually appealing UI.
9. **Multi-Device Support** – Runs on both Windows and macOS.
10. **Lightweight & Fast** – Works efficiently without high system requirements.

## Installation
### Prerequisites
Ensure you have **Python 3.8+** installed on your system. Install the required dependencies using the command below:

```bash
pip install torch torchvision torchaudio clip-by-openai pillow pyperclip pyttsx3 googletrans==4.0.0-rc1 opencv-python-headless tkinter
```

### Running the Application
Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/Burhanali2211/Offline_Caption_Generator.git
cd Offline_Caption_Generator
```

Run the Python script:

```bash
python Offline_Caption_Generator.py
```

## Usage
1. Click **"Choose Image"** and select an image.
2. The AI generates a caption based on the image content.
3. You can **copy** the caption, **listen** to it, or **translate** it.
4. View **history** of previously generated captions.

## Technologies Used
- **Python** – Backend processing
- **OpenAI CLIP Model** – AI-powered captioning
- **Tkinter** – GUI interface
- **PyTTSX3** – Text-to-speech conversion
- **Google Translate API** – Language translation
- **Pyperclip** – Clipboard management


## License
This project is open-source and available under the **MIT License**.

## Contributions
Feel free to fork the repository and submit pull requests with improvements!


