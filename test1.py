
from transformers import pipeline
whisper = pipeline("automatic-speech-recognition",
                   model="openai/whisper-base")


p = whisper("audio/audio.mp3")

print(p)
