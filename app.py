import gradio as gr
from kani_tts import KaniTTS
import soundfile as sf
import numpy as np
import tempfile
import os

# Initialize the KaniTTS model
print("Loading KaniTTS model...")
model = KaniTTS('nineninesix/kani-tts-400m-en')
print("Model loaded successfully!")

def generate_speech(text):
    """Generate speech from text using KaniTTS model."""
    if not text or not text.strip():
        return None
    
    try:
        # Generate audio from text
        audio, _ = model(text)
        
        # Get sample rate from model (typically 22050Hz or 24000Hz)
        sample_rate = model.sample_rate
        
        # Save to temporary file
        temp_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
        sf.write(temp_file.name, audio, sample_rate)
        
        return temp_file.name
    except Exception as e:
        print(f"Error generating speech: {e}")
        return None

# Create Gradio interface
with gr.Blocks(title="KaniTTS Web App") as demo:
    gr.Markdown("# KaniTTS Web App")
    gr.Markdown("Enter text below and click Generate to convert it to speech.")
    
    with gr.Row():
        text_input = gr.Textbox(
            label="Text Input",
            placeholder="Enter text to convert to speech...",
            lines=3
        )
    
    generate_btn = gr.Button("Generate", variant="primary")
    
    audio_output = gr.Audio(label="Generated Audio", type="filepath")
    
    generate_btn.click(
        fn=generate_speech,
        inputs=text_input,
        outputs=audio_output
    )

if __name__ == "__main__":
    demo.launch(server_port=7860)
