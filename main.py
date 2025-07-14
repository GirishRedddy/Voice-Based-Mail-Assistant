import os
import webbrowser
from voice_utils import speak, listen
from mail_utils import send_email

EMAIL = "your_email@gmail.com"
PASSWORD = "your_password"  # use App Passwords if 2FA enabled

def main():
    speak("Welcome to Voice Based Mail Assistant.")
    while True:
        speak("Please say a command.")
        command = listen()

        if "send mail" in command:
            speak("Who is the recipient?")
            to = listen()
            to_email = to.replace(" ", "") + "@gmail.com"  # simple mock

            speak("What is the subject?")
            subject = listen()

            speak("What is the message?")
            body = listen()

            success = send_email(to_email, subject, body, EMAIL, PASSWORD)
            if success:
                speak("Email sent successfully.")
            else:
                speak("Failed to send email.")

        elif "group mail" in command:
            recipients = ["example1@gmail.com", "example2@gmail.com"]
            send_email(", ".join(recipients), "Group Update", "This is a group message.", EMAIL, PASSWORD)
            speak("Group email sent.")

        elif "open youtube" in command:
            webbrowser.open("https://youtube.com")
            speak("Opening YouTube.")

        elif "open google" in command:
            webbrowser.open("https://google.com")
            speak("Opening Google.")

        elif "shutdown" in command:
            speak("Shutting down system.")
            # os.system("shutdown /s /t 1")  # Uncomment for actual shutdown

        elif "exit" in command or "stop" in command:
            speak("Goodbye!")
            break

        else:
            speak("Command not recognized.")

if __name__ == "__main__":
    main()
