from typing import TypedDict, List


class AgentState(TypedDict):

    session_id: str

    messages: List[str]

    current_agent: str

    user_input: str

    response: str