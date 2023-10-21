from SpeechRecognition import *
from GPTInterpreter import *
from Agents import *

def main():

    interpreter = GptInterpreter("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")
    speech = SpeechRecognition()
    agents = Agents()

    print("Welcome the FriendGPT!")
    speech.speakFunction("Welcome the FriendGPT!")
    print("FriendGPT is a program that allows you to verbally speak to a ChatGPT model with a custom personality!")
    speech.speakFunction("FriendGPT is a program that allows you to verbally speak to a ChatGPT model with a custom personality!")
    print("Please say the name of the person / character you would like to use for the personality.")
    speech.speakFunction("Please say the name of the person / character you would like to use for the personality.")
    print("Press the space bar to begin recording and ctrl+c to stop")
    speech.speakFunction("Press the space bar to begin recording and ctrl+c to stop")
    speech.recordSpeech()
    personality = speech.speechToText()
    print("You selected: " + personality)
    speech.speakFunction("You selected" + personality)
    interpreter.setPersonality(personality)

    print('')

    programRunning = True
    # While the condition equal true 
    while(programRunning == True):
        if(programRunning == True):
            # If user lets speech to be record, condition is allowd to be true
            # Saves speech to (myrecording.wav)
            print("Press the space bar to speak to " + personality + " and press ctrl+c when you are done speaking")
            speech.speakFunction("Press the space bar to speak to " + personality + " and press ctrl+c when you are done speaking")
            programRunning = speech.recordSpeech()
            # If condition remains to be true
            if(programRunning == True):
                # Converts the audio file to text
                # Stores that text into userString
                userString = speech.speechToText() 
                print("User: ")
                print("\t", userString)  

                if (userString.split()[0] == "image"):
                    output = agents.dalle(userString)
                    print(output)
                else:
                    print(personality + ": ")
                    aiString = interpreter.sendUserMessage(userString)
                    print("\t", aiString)
                    speech.speakFunction(aiString)
            # Otherwise return false 
            else:
                programRunning = False
        print("")


if __name__ == "__main__":
    main()


