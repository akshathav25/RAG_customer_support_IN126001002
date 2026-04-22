def escalate_to_human(query):
    print("\n===================================")
    print(" ESCALATED TO HUMAN SUPPORT ")
    print("===================================")

    print(f"Customer Query: {query}")
    print("Reason: Low confidence or sensitive issue detected")
    print("Action Required: Manual review by support agent\n")

    human_response = input(
        "Support Agent Final Response: "
    )

    return human_response