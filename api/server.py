from fastapi import FastAPI

from graph.workflow import workflow

from core.session import (
    get_session,
    update_session
)



app = FastAPI()



@app.post("/chat")
def chat(
    session_id:str,
    message:str
):


    state = get_session(
        session_id
    )


    state["user_input"]=message


    result = workflow.invoke(
        state
    )


    update_session(
        session_id,
        result
    )


    return {

        "session_id":
        session_id,

        "answer":
        result["response"]

    }
