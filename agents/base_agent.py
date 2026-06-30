
class BaseAgent:
    def __init__(
        self,
        name,
        prompt
    ):

        self.name=name
        self.prompt=prompt
    def run(
        self,
        input_text,
        context
    ):
        raise NotImplementedError