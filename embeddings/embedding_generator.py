import httpx

def generate_embedding(text):
    url = "http://localhost:11434/api/generate"
    prompt = f"Return a JSON-style vector embedding for: {text}"

    payload = {
        "model": "mistral",
        "prompt": prompt,
        "stream": False
    }

    response = httpx.post(url, json=payload)
    return response.json()["response"]
