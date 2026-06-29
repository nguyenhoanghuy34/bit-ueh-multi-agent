from router.prompts import ROUTER_PROMPT



class AgentRouter:


    def route(
        self,
        message
    ):


        text = message.lower()


        if (
            "crawl" in text
            or "data" in text
        ):

            return "crawl_data"


        if (
            "notification" in text
            or "thông báo" in text
        ):

            return "notification"


        return "crawl_data"