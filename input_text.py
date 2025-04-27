import asyncio
import time
from gpt_client import client

gpt = client()
class MessageHandler:

    def __init__(self):
        self.messages = []
        self.last_time = None

    async def add_message(self, message):
        self.last_time = time.time()
        self.messages.append(message)

    async def check_messages(self):
        while True:
            await asyncio.sleep(1)
            current_time = time.time()

            if self.last_time is not None and (current_time - self.last_time) > 7:
                if self.messages:
                    all_messages = " ".join(self.messages)
                    print("Все сообщения, которые вы отправили:", all_messages)
                    response_gpt(all_messages)
                    self.messages = []
                    self.last_time = None

def response_gpt(text):
    response = gpt.chat(text)
    letter_count = len(response)
    print(f"печатает ... со скоростью 10 символов в секунду")
    time.sleep(letter_count*0.1)
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
