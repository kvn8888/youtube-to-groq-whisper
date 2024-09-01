import os
from groq import Groq

client = Groq()
filename = "tmp/output.mp3"

with open(filename, "rb") as file:
    transcription = client.audio.transcriptions.create(
      file=(filename, file.read()),
      model="whisper-large-v3",
      temperature=0.0  # Optional
    )