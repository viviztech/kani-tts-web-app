# KaniTTS Web App

A text-to-speech web application using KaniTTS model with Gradio interface.

## Prerequisites

- Python 3.10 or higher
- PyTorch 2.8.0 or higher (requires Linux or Apple Silicon Mac)

> **Note**: This app requires PyTorch 2.8+. macOS x86_64 (Intel) only supports up to PyTorch 2.2.2. For Intel Macs, please use a cloud platform.

## Cloud Deployment

### Google Colab
1. Upload the files to Google Drive or clone from GitHub
2. Run: `!pip install -r requirements.txt`
3. Run: `!python app.py`

### Hugging Face Spaces
1. Create a new Space with Gradio SDK
2. Upload `app.py` and `requirements.txt`
3. The app will automatically deploy

### Replit
1. Create a new Python Repl
2. Upload the files
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `python app.py`

## Local Installation (Linux/Apple Silicon)

```bash
# Clone the repository
git clone <your-repo-url>
cd tts-app

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

## Usage

1. Open your browser and go to: `http://127.0.0.1:7860`
2. Enter the text you want to convert to speech
3. Click the "Generate" button
4. Listen to the generated audio

## Model Information

- **Model**: `nineninesix/kani-tts-400m-en`
- **Sample Rate**: 22050Hz (model default)
- **Language**: English

