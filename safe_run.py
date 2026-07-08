"""Safe runner that uses the local ChatAgent only.

This avoids importing or executing the potentially harmful `fraudGPT.py` logic.
"""
from agent import ChatAgent


def main() -> None:
    agent = ChatAgent()
    print("Safe Runner — local-only. Type 'exit' to quit.")
    while True:
        try:
            user_input = input("You: ").strip()
        except (KeyboardInterrupt, EOFError):
            print()
            break

        if user_input.lower() in {"exit", "quit"}:
            break

        response = agent.respond(user_input)
        print(f"Agent: {response}")


if __name__ == "__main__":
    main()
