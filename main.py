import subprocess

if __name__ == '__main__':
    print("Welcome to Robospeaker 1.1. Created by Jinal Rathod")
    user_input = input("Enter the text you want me to speak: ")

    # Construct the PowerShell command
    ps_command = f"Add-Type -AssemblyName System.Speech; $jinal = New-Object -TypeName System.Speech.Synthesis.SpeechSynthesizer; $jinal.Speak('{user_input}')"

    # Execute the PowerShell command
    subprocess.run(['C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe', '-command', ps_command],
                   shell=True)

    # os module not working in windows

# --------------------------

# import win32com.client as wincom
#
# def text_to_speech_win32(text):
#     speak = wincom.Dispatch("SAPI.SpVoice")
#     speak.Speak(text)
#
# if __name__ == "__main__":
#     input_text = input("Enter the text you want to convert to speech: ")
#     text_to_speech_win32(input_text)


# ---------------------------

# import pyttsx3
#
# def text_to_speech(text):
#     engine = pyttsx3.init()
#     engine.say(text)
#     engine.runAndWait()
#
# if __name__ == "__main__":
#     input_text = input("Enter the text you want to convert to speech: ")
#     text_to_speech(input_text)
