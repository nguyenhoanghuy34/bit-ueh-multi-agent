from openai import OpenAI

from router.prompts import ROUTER_PROMPT


class AgentRouter:

    def __init__(self):
        self.client = OpenAI()

    def route(
        self,
        message
    ):
        response = self.client.responses.create(
            model="gpt-4.1-mini",
            input=[
                {
                    "role": "system",
                    "content": ROUTER_PROMPT
                },
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        return response.output_text.strip()