import os
from typing import Optional


class ChatAgent:
    """A simple local chat agent that works without an API key."""

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.memory = []

    def respond(self, message: str) -> str:
        text = (message or "").strip()
        if not text:
            return "Hello! I’m ready to help."

        lowered = text.lower()
        self.memory.append(text)

        if lowered in {"/help", "help"}:
            return (
                "Available commands:\n"
                "- /help: show this menu\n"
                "- /clear: clear conversation memory\n"
                "- /status: show local mode status"
            )

        if lowered in {"/clear", "clear"}:
            self.memory.clear()
            return "Conversation memory cleared."

        if lowered in {"/status", "status"}:
            return "Local fallback mode is active. No API key is required for basic responses."

        if "hello" in lowered or "hi" in lowered:
            return "Hello! I’m your local assistant. What would you like help with?"

        if "name" in lowered and "your" in lowered:
            return "I’m a local assistant built for this workspace."

        if "joke" in lowered:
            return "Sure — why do programmers prefer dark mode? Because light attracts bugs."

        return (
            f"You said: {text}\n"
            "I’m running in local fallback mode. Add an API key to enable richer responses."
        )


def main() -> None:
    agent = ChatAgent()
    print("Local Agent Ready. Type 'exit' to quit.")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in {"exit", "quit"}:
            break
        print(f"Agent: {agent.respond(user_input)}")


if __name__ == "__main__":
    main()
