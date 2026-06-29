from agents.base_agent import BaseAgent
from .prompt import CRAWL_PROMPT
from .tools import crawl_mock



class CrawlAgent(
    BaseAgent
):


    def __init__(self):

        super().__init__(
            "crawl_data",
            CRAWL_PROMPT
        )



    def run(
        self,
        input_text,
        context
    ):


        data = crawl_mock(
            input_text
        )


        return {

            "agent":
            self.name,

            "result":
            data

        }
