import asyncio
import time
from gpt_client import client

gpt = client()
class MessageHandler:

    def __init__(self, time_sleep = 7):
        self.time_sleep = time_sleep
        self.messages = []
        self.last_time = None

    async def add_message(self, message):
        self.last_time = time.time()
        self.messages.append(message)

    async def check_messages(self):
        while True:
            await asyncio.sleep(1)
            current_time = time.time()

            if self.last_time is not None and (current_time - self.last_time) > self.time_sleep:
                if self.messages:
                    all_messages = " ".join(self.messages)
                    print("Все сообщения, которые вы отправили:", all_messages)
                    response_gpt(all_messages)
                    self.messages = []
                    self.last_time = None

def response_gpt(text):
    print_speed = 0.05
    response = gpt.chat(text)
    letter_count = len(response)
    print(f"печатает ... со скоростью {print_speed * 100} символов в секунду")
    time.sleep(letter_count * print_speed)
    print(response)

async def input_handler(handler):
    while True:
        user_input = await asyncio.to_thread(input, "Введите сообщение: ")
        await handler.add_message(user_input)


async def main():
    handler = MessageHandler()

    await asyncio.gather(
        input_handler(handler),
        handler.check_messages()
    )


asyncio.run(main())
