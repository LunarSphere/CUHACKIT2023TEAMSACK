from langchain.memory import ChatMessageHistory
from langchain.chat_models import ChatOpenAI

class GptInterpreter:
    def __init__(self, openAIkey):
        self.myChat = ChatOpenAI(openai_api_key=openAIkey)
        self.memory = ChatMessageHistory()

    def sendUserMessage(self, prompt):
        self.memory.add_user_message(prompt)
        output = self.myChat(self.memory.messages)
        self.memory.add_ai_message(output.content)

        return output.content
    
    def setPersonality(self, personality):
        self.memory.add_user_message("Please respond to all of the following messages like like " + personality)

def main():
    interpreter = GptInterpreter("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")
    print(interpreter.sendUserMessage("What is the capitol of Thailand?"))

if __name__ == "__main__":
    main()