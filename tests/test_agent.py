import unittest

from agent import ChatAgent


class ChatAgentTests(unittest.TestCase):
    def test_fallback_greeting(self):
        agent = ChatAgent(api_key=None)
        reply = agent.respond("hello")
        self.assertIn("Hello", reply)

    def test_fallback_help(self):
        agent = ChatAgent(api_key=None)
        reply = agent.respond("help")
        self.assertIn("help", reply.lower())

    def test_command_help(self):
        agent = ChatAgent(api_key=None)
        reply = agent.respond("/help")
        self.assertIn("commands", reply.lower())


if __name__ == "__main__":
    unittest.main()
