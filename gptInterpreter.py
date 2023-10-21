from langchain.memory import ChatMessageHistory
from langchain.chat_models import ChatOpenAI

class GptInterpreter:
    def __init__(self, openAIkey, inModel):
        self.myChat = ChatOpenAI(openai_api_key=openAIkey)
        self.model = inModel
        self.memory = ChatMessageHistory()

    def runInterpretation(self, userInput):
        isAgentCommand = self.checkForCommand(userInput)
        print(isAgentCommand)

        if isAgentCommand:
            print("It is an agent command!")
        elif isAgentCommand == False:
            messageResponse = self.sendUserMessage("Increase my computer's volume")
            print(messageResponse)


    def sendUserMessage(self, prompt):
        self.memory.add_user_message(prompt)
        output = chat(memory.messages)
        self.memory.add_ai_message(output)

        return output
    
    def checkForCommand(self, inString):
        isCommand = False

        prePromptString = "Is the following statement a command for you to change the computer's volume, search the internet for something, or adjust the screen's brightness? (Answer with YES or NO): "
        response = self.sendUserMessage(prePromptString + inString)
        print(response)

        if response == "YES":
            isCommand = True
        elif response == "NO":
            isCommand = False

        return isCommand
    

def main():
    interpreter = GptInterpreter("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", "gpt-4")

    #interpreter.runInterpretation("Increase my computer's volume")
    print(interpreter.sendUserMessage("What is the capitol of Thailand?"))


if __name__ == "__main__":
    main()