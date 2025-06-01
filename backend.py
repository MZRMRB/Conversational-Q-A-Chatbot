import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class GeminiAPI:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables")
        
        self.api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={self.api_key}"
        self.headers = {
            "Content-Type": "application/json"
        }
        self.temperature = 0.7
        self.max_tokens = 1000

    def get_response(self, prompt, conversation_history=None):
        if conversation_history is None:
            conversation_history = []
        
        data = {
            "contents": [
                *conversation_history,
                {
                    "parts": [{"text": prompt}]
                }
            ],
            "generationConfig": {
                "temperature": self.temperature,
                "maxOutputTokens": self.max_tokens
            }
        }
        
        try:
            response = requests.post(self.api_url, headers=self.headers, json=data)
            response.raise_for_status()
            return response.json()["candidates"][0]["content"]["parts"][0]["text"]
        except requests.exceptions.RequestException as e:
            return f"Network error: Please check your internet connection"
        except KeyError as e:
            return f"API response format error: {str(e)}"
        except Exception as e:
            return f"Unexpected error: {str(e)}"
