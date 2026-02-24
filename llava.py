import ollama

image_path = r"C:\Users\selin\Pictures\apple.jpg"

response = ollama.chat(
    model="llava",
    messages=[
        {
            "role": "user",
            "content": "Describe this image in one sentence.",
            "images": [image_path]
        }
    ]
)

print("\n=== MODEL OUTPUT ===")
print(response["message"]["content"])