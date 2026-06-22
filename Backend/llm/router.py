from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPEN_ROUTER_API_KEY")
)

MODELS = [
    "google/gemini-2.5-flash",
    "meta-llama/llama-3.3-70b-instruct",
    "qwen/qwen3-32b",
    "deepseek/deepseek-chat-v3"
]

def generate(prompt):

    for model in MODELS:

        try:

            response = client.chat.completions.create(
                model=model,
                max_tokens=1000,
                messages=[
                    {
                        "role":"user",
                        "content":prompt
                    }
                ]
            )

            print(f"Using: {model}")

            return response.choices[0].message.content

        except Exception as e:

            print(f"{model} failed")
            print(e)

    return "All models unavailable."
