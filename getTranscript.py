import os
from groq import Groq

client = Groq()
client.api_key = os.environ["GROQ_API_KEY"]
filename = "tmp/output.mp3"

def transcribe_audio():
    with open(filename, "rb") as file:
        transcription = client.audio.transcriptions.create(
            file=(filename, file.read()),
            model="whisper-large-v3",
            temperature=0.0,  # Optional
            # response_format="json",  # Optional
            language="en",  # Optional 
        )

    with open("tmp/transcript.txt", "w") as file:
        file.write(transcription.text)

if __name__ == "__main__":
    print(transcribe_audio())