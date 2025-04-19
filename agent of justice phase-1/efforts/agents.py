from huggingface_hub import InferenceClient
import os
from dotenv import load_dotenv

load_dotenv()
HF_API_TOKEN = os.getenv("HF_API_TOKEN")

class LawyerAgent:
    def __init__(self, name, system_prompt, model="microsoft/Phi-3-mini-4k-instruct"):
        self.name = name
        self.system_prompt = system_prompt.strip()
        self.client = InferenceClient(model=model, token=HF_API_TOKEN)

    def respond(self, user_msg):
        prompt = f"{self.system_prompt}\n\n{user_msg}"
        response = self.client.text_generation(prompt, max_new_tokens=100)
        return response.strip()
