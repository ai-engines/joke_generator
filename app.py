import gradio as gr
from transformers import pipeline

# Load a pre-trained model
generator = pipeline('text-generation', model='gpt2')

def generate_text(prompt):
    return generator(prompt, max_length=50)[0]['generated_text']

# Create a Gradio interface
iface = gr.Interface(
    fn=generate_text,
    inputs="text",
    outputs="text",
    title="Joke Generator 🤖",
    description="Enter a topic, and I'll generate a joke!"
)

iface.launch()
