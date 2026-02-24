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
