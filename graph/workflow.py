from langgraph.graph import StateGraph

from core.state import AgentState

from router.agent_router import AgentRouter

from agents.crawl_data.agent import CrawlAgent

from agents.notification.agent import NotificationAgent



router = AgentRouter()


crawl_agent = CrawlAgent()

notification_agent = NotificationAgent()



def router_node(state):


    agent = router.route(
        state["user_input"]
    )


    state["current_agent"]=agent


    return state




def crawl_node(state):


    result = crawl_agent.run(

        state["user_input"],

        state["messages"]

    )


    state["response"]=result

    return state



def notification_node(state):


    result = notification_agent.run(

        state["user_input"],

        state["messages"]

    )


    state["response"]=result


    return state



graph = StateGraph(
    AgentState
)


graph.add_node(
    "router",
    router_node
)


graph.add_node(
    "crawl_data",
    crawl_node
)


graph.add_node(
    "notification",
    notification_node
)


graph.set_entry_point(
    "router"
)


graph.add_conditional_edges(

    "router",

    lambda x:x["current_agent"],

    {

        "crawl_data":
        "crawl_data",

        "notification":
        "notification"

    }

)



workflow = graph.compile()
