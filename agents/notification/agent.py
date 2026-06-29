from agents.base_agent import BaseAgent

from .prompt import NOTIFICATION_PROMPT

from .tools import read_notification



class NotificationAgent(
    BaseAgent
):


    def __init__(self):

        super().__init__(
            "notification",
            NOTIFICATION_PROMPT
        )


    def run(
        self,
        input_text,
        context
    ):


        notifications = (
            read_notification()
        )


        return {

            "agent":
            self.name,

            "notifications":
            notifications

        }
