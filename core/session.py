from typing import Dict
from core.state import AgentState


SESSION_STORE: Dict[str, AgentState] = {}


def get_session(session_id):

    if session_id not in SESSION_STORE:

        SESSION_STORE[session_id] = {

            "session_id": session_id,

            "messages": [],

            "current_agent": "",

            "user_input": "",

            "response": ""
        }


    return SESSION_STORE[session_id]


def update_session(
        session_id,
        state
):

    SESSION_STORE[session_id] = state


def clear_session(session_id):

    SESSION_STORE.pop(
        session_id,
        None
    )