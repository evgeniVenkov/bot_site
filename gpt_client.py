import os
import openai
from dotenv import load_dotenv
from promt import get


load_dotenv()
api_key = os.getenv("KEY")
sys_promt = get()

class client:
    def __init__(self,count_history = 10, model = "gpt-3.5-turbo"):
        """Инициализация API клиента и загрузка ключа"""
        self.client = openai.OpenAI(api_key=api_key)
        self.history = []
        self.system_prompt = sys_promt
        self.first_request = True
        self.count_history = count_history
        self.model = model
    def chat(self, user_message):

        if not api_key:
            return " Ошибка: API-ключ OpenAI не найден."
        if len(self.history) >= self.count_history:
            self.history = []
            self.first_request = False


        if self.first_request:
            self.history.append({"role": "system", "content": self.system_prompt})
            self.first_request = False


        self.history.append({"role": "user", "content": user_message})

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=self.history,
                temperature=0.7,
                max_tokens=25
            )

            bot_reply = response.choices[0].message.content
            self.history.append({"role": "assistant", "content": bot_reply})


            return bot_reply
        except Exception as e:
            return f" Ошибка при обращении к GPT: {e}"



