from datetime import datetime


def write_log(query, answer, escalated):
    with open("logs.txt", "a", encoding="utf-8") as file:
        file.write("\n===================================\n")
        file.write(f"Time: {datetime.now()}\n")
        file.write(f"Query: {query}\n")
        file.write(f"Response: {answer}\n")
        file.write(f"Escalated: {escalated}\n")
        file.write("===================================\n")