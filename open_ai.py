import openai

class OpenAI:
    def __init__(self, key, model, temperature):
        openai.api_key = key
        self.model = model
        self.temperature = temperature

    def generate(self, system, user):
        messages = [
            {
                "role": "system",
                "content": system
            },
            {
                "role": "user",
                "content": user
            }
        ]
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
            max_tokens=512,
        )
        result = response.choices[0]['message']['content']
        return result