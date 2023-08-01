#We start by importing the necessary libraries. assemblyai will be used for the transcription service, datetime to format the file name with the current date, and os to handle the file operations
import assemblyai as aai
from datetime import datetime
import os

# we define our file name and the directory where we'll store the transcriptions

file_name = "news.txt"
data_directory = "transcript_folder"

# we're setting our API key for AssemblyAI. This is essential for authenticating our requests to the service
aai.settings.api_key = "#"


# We initialize a Transcriber object and request a transcription of an online audio file. There's also a commented line that shows how to handle a local file.
transcriber = aai.Transcriber()
transcript = transcriber.transcribe("https://gtusieyatzvotohzvlfy.supabase.co/storage/v1/object/public/take-home/video1982379628.mp4?t=2023-05-01T16%3A31%3A40.958Z")
# transcript = transcriber.transcribe("./my-local-audio-file.wav")

# Retrieve the Transcription Text:
text = transcript.text


#We ensure our target directory exists, and then we write the transcribed text to a new file inside that directory."
current_date = datetime.now().strftime('%Y-%m-%d')

os.makedirs(data_directory, exist_ok=True)
with open(f"{data_directory}/{current_date}_{file_name}", 'w') as f:
    f.write(text)


# This code snippet leverages AssemblyAI to transcribe audio content and save it in a text file, neatly organized by date