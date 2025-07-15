from langchain.chat_models import init_chat_model
from langchain import hub
from langchain_core.documents import Document
from typing_extensions import List, TypedDict

from langgraph.graph import START, StateGraph


def build_qa_chain(vectorstore):

    prompt = hub.pull("rlm/rag-prompt")

    example_messages = prompt.invoke(
                                        {"context": "(context goes here)", "question": "(question goes here)"}
                                    ).to_messages()

    class State(TypedDict):
        question: str
        context: List[Document]
        answer: str

    def retrieve(state: State):
        retrieved_docs = vectorstore.similarity_search(state["question"])
        print('retrieved_docs ',retrieved_docs)
        return {"context": retrieved_docs}


    def generate(state: State):
        docs_content = "\n\n".join(doc.page_content for doc in state["context"])
        messages = prompt.invoke({"question": state["question"], "context": docs_content})
        response = llm.invoke(messages)
        return {"answer": response.content}

    # N.B. for non-US LangSmith endpoints, you may need to specify
    # api_url="https://api.smith.langchain.com" in hub.pull.

    graph_builder = StateGraph(State).add_sequence([retrieve, generate])
    graph_builder.add_edge(START, "retrieve")
    graph = graph_builder.compile()

    print('prompt ',prompt)


    llm = init_chat_model("gemini-2.0-flash", model_provider="google_genai")

    print('return ',graph)

    return graph

'''
    result = graph.invoke({"question": "can you provide the summary of the context?"})

    return {"answer":result["answer"]}

    graph_builder = StateGraph(State)
    graph_builder.add_node("retrieve", retrieve)
    graph_builder.add_node("generate", generate)
    graph_builder.add_edge(START, "retrieve")
    graph_builder.add_edge("retrieve", "generate")
    graph_builder.set_finish("generate")

    graph = graph_builder.compile()

    
'''



