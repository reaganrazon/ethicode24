import reflex as rx
import os
from dotenv import load_dotenv
from openai import OpenAI
import httpx

load_dotenv(override=True)

client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],
)

class QState(rx.State):
    question: str
    chat_history: list[tuple[str, str]]

    async def answer(self):

        # async with httpx.AsyncClient() as client:
        #     # Send the user_input to the backend and wait for the response
        #     response = await client.post('http://localhost:8000/rag-answer', json={'question': self.question})
        #     answering = response.json()["answer"]
        #     print(answering, "answer")
        #     # async with self:
        #         # Update chat history with the response from the backend
        #     self.chat_history.append((self.question, answering))
        #     self.question = ""

        session = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": self.question}
            ],
            stop=None,
            temperature=0.7,
            stream=True,
        )

        # Add to the answer as the chatbot responds.
        answer = ""
        self.chat_history.append((self.question, answer))

        # Clear the question input.
        self.question = ""
        # Yield here to clear the frontend input before continuing.
        yield

        for item in session:
            if hasattr(item.choices[0].delta, "content"):
                if item.choices[0].delta.content is None:
                    # presence of 'None' indicates the end of the response
                    break
                answer += item.choices[0].delta.content
                self.chat_history[-1] = (self.chat_history[-1][0], answer)
                yield

# class QState(rx.State):
#     question: str

#     chat_history: list[tuple[str, str]]

#     async def answer(self):

#         # # Code to send the question to the backend API and wait for the response
#         # response = await call_to_backend_api(self.question)
#         # # Update chat history with the response from the backend
#         # self.chat_history.append((self.question, response))

#         # Send the user_input to the backend and wait for the response
#         response = await rx.api.post('/rag-answer', json={'question': self.question})
#         # Update the state with the response from the backend
#         self.response = response.json()['answer']

#         # session = client.chat.completions.create(
#         #     model="gpt-3.5-turbo",
#         #     messages=[
#         #         {"role": "user", "content": self.question}
#         #     ],
#         #     stop=None,
#         #     temperature=0.7,
#         #     stream=True,
#         # )

#         answer = ""
#         self.chat_history.append((self.question, answer))

#         self.question = ""
#         yield

#         for item in session:
#             if hasattr(item.choices[0].delta, "content"):
#                 if item.choices[0].delta.content is None:
#                     break
#                 answer += item.choices[0].delta.content
#                 self.chat_history[-1] = (self.chat_history[-1][0], answer)
#                 yield"