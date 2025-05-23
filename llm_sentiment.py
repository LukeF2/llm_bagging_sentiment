import requests
from collections import Counter

def query_llm_sentiment(text, api_key, model_name, prompt_style):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    prompt = f"{prompt_style}\nClassify the following text: {text}"

    data = {
        "model": model_name,
        "messages": [
            {
                "role": "system",
                "content": "You are a sentiment classifier that answers only with 'POS' or 'NEG'."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content'].strip()
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")

