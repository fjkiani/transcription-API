Transcription API

Overview
The Transcription API is a Python-based application designed for transcribing audio files. It offers a simple yet effective way to convert speech in audio files into text

Repository: Transcription API
Installation
Clone the repository:
bash
Copy code
git clone https://github.com/fjkiani/transcription-api.git
Navigate to the project directory:
bash
Copy code
cd transcription-api
Follow any additional installation steps, such as setting up a virtual environment or installing dependencies.
Usage
Training
Run the training script:
Copy code
python train.py
Transcribing
To transcribe an audio file, use the bot.py script.
To download a transcript, use the download_transcript.py script.
Files and Directories
bot.py: Sets up a conversational bot utilizing OpenAI for natural language processing and Gradio for the user interface. View bot.py
download_transcript.py: Uses AssemblyAI to transcribe audio content and save it in a text file, organized by date. View download_transcript.py
train.py: Demonstrates setting up a document retrieval system using pre-trained embeddings and vector-based similarity searches. View train.py
secret_config.py: Manages loading of secrets like API keys for secure communication. View secret_config.py
transcript_folder/: Directory containing sample transcripts.
Contributing
If you're interested in contributing to the Transcription API project, please follow the provided guidelines.
