from google import genai

from backend.app.core.config import settings


class LLMService:

    def __init__(self):
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY
        )

    def generate_response(self, messages):

        prompt = ""

        for message in messages:

            if message["role"] == "user":
                prompt += f"User: {message['content']}\n"

            elif message["role"] == "assistant":
                prompt += f"Assistant: {message['content']}\n"

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text


llm_service = LLMService()