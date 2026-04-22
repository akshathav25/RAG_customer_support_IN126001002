from graph import graph
from utils.helper import write_log

def main():
    print("===================================")
    print(" Customer Support RAG Assistant ")
    print("===================================")

    while True:
        query = input("\nAsk your question (or type 'exit'): ")

        if query.lower() == "exit":
            print("\nExiting assistant...")
            break

        result = graph.invoke({
            "query": query,
            "context": "",
            "answer": "",
            "needs_human": False
        })

        print("\n===================================")
        print(" FINAL RESPONSE ")
        print("-------------------------------------")
        print(result["answer"])
        print("===================================")

        write_log(
    query=query,
    answer=result["answer"],
    escalated=result["needs_human"]
    )


if __name__ == "__main__":
    main()