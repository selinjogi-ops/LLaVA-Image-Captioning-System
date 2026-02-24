# LLaVA Image Captioning System

A lightweight image captioning system built using the LLaVA multimodal model running locally via Ollama.
This project demonstrates how to generate natural language descriptions from images using a Vision-Language Model (VLM) without relying on cloud APIs.

# Project Overview

This system:

* Accepts an image file from local storage

* Sends the image to a locally running LLaVA model

* Generates a concise one-sentence caption

* Runs entirely offline using Ollama

The implementation is intentionally minimal to focus on multimodal inference workflow.

# Model Details

**Model**: LLaVA (Large Language and Vision Assistant)

**Runtime**: Ollama

**Inference Mode**: Local execution

LLaVA combines:

* A vision encoder (extracts image features)

*A language model (generates text)

* Cross-modal alignment between visual and textual representations

The model processes both text and image inputs and produces contextual captions.

# System Architecture

<img width="227" height="180" alt="image" src="https://github.com/user-attachments/assets/2bfd5f5c-c019-4a79-8269-4f61b7f3f5bd" />

# Project Structure

LLaVA-Image-Captioning-System/

│

├── llava.py

├── requirements.txt

├── README.md

└── .gitignore

# Installation

**1.Install Ollama**

Download and install Ollama from the official website.

After installation, pull the LLaVA model:

ollama pull llava

**2️.Clone Repository**

git clone https://github.com/your-username/LLaVA-Image-Captioning-System.git

cd LLaVA-Image-Captioning-System

**3️.Install Python Dependency**

pip install -r requirements.txt

**requirements.txt**

ollama

**Usage**

Modify the image path in llava.py:

image_path = r"C:\Users\Pictures\apple.jpg"

Run the script:

python llava.py

Example prompt:

"Describe this image in one sentence."

# Hardware Requirements

Minimum:

* 8 GB RAM

* CPU-based inference supported

Recommended:

* 16 GB RAM

* GPU acceleration (if available)

Model size depends on the specific LLaVA variant downloaded via Ollama.

# Example Output

=== MODEL OUTPUT ===

A red apple placed on a wooden table under natural lighting.

# Applications

* Local multimodal AI experimentation

* Offline image captioning

* Educational AI demonstrations

* Prototyping vision-language workflows

# Future Improvements

* Batch image processing

* Live camera integration

* GUI interface

* Integration with other VLMs (BLIP, Moondream)

* Web API deployment

# Author

Selin Jogi Chittilappilly

B.Voc Mathematics & Artificial Intelligence

AI Intern
