import pyttsx3
import keyboard
import pyaudio
import wave
import speech_recognition as sr
import langchain.memory

class SpeechRecognition: 

    def speechToText(self):
        r = sr.Recognizer()
        audio = False

        # access myrecording.wav
        with sr.AudioFile("myrecording.wav") as source:
            audio = r.record(source)
        # recognize audio 
        try:
            s = r.recognize_google(audio)
            #print("Text: "+s)
        # throws exeception if audio recongizition doesnt work
        except Exception as e:
            print("Exception: "+str(e))
            s = ""

        #print(".")
        #print(".")
        #print(".")

        return s

    def recordSpeech(self):    
        # Calls function 
        audio = pyaudio.PyAudio()
        # Gets read to set up audio 
        stream = audio.open(format = pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)
        frames = []

        pressed = keyboard.read_key()   # Reads user keypress
        if (str(pressed) == "space"):   # if key 'spacebar' is pressed 

            try:
                # Whlie there is no error, keep running the code
                while True:
                    data = stream.read(1024)
                    frames.append(data)
                # When keyboard interuupts code, exit and stop recording
            except KeyboardInterrupt:
                pass
            
            print("")
            # Exits the stream and audio
            stream.stop_stream()
            stream.close()
            audio.terminate()

            # Puts audio into myrecording.wav
            sound_file = wave.open("myrecording.wav", "wb")
            sound_file.setnchannels(1)
            sound_file.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
            sound_file.setframerate(44100)
            sound_file.writeframes(b''.join(frames))
            sound_file.close()
            
            #return true
            return True
        
        # if they press e then return false
        else:
            return False

    # Readings innputed parameter
    def speakFunction(self, text):
        engine = pyttsx3.init()                     # Calls pyttsx3 API
        voices = engine.getProperty('voices')       # gets list of voices 
        engine.setProperty('voice', voices[0].id)   # maeks voice id 0, male
        engine.say(text)                            # Say parameter
        engine.runAndWait()                         # run and wait

    def RunSpeechRecognition(self):
         # if user does not want to record speech then stop code
        condition = self.recordSpeech()
        # When codition is true 
        if(condition == True):
            s = self.speechToText() 
            #self.speakFunction(s)
            return s


def main():
     objectCall = SpeechRecognition()
     x = objectCall.RunSpeechRecognition()
     print(x)
     objectCall.speakFunction(x)

  
if __name__ == "__main__":
    main()