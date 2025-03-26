import sys
from moviepy import VideoFileClip
import whisper
import os
from langchain_mistralai import ChatMistralAI

os.environ["MISTRAL_API_KEY"]="4S819Bz6jMYsoZHL4pF8ou9kj8bkZjTb"


def extract_audio_from_video(video_path, audio_path):
    # Charger le fichier vidéo
    video = VideoFileClip(video_path)
    # Extraire l'audio et le sauvegarder
    video.audio.write_audiofile(audio_path)

def transcribe_audio_to_text(audio_path):
    # Charger le modèle Whisper
    model = whisper.load_model("base")  # Vous pouvez choisir d'autres modèles comme "small", "medium", etc.

    # Transcrire l'audio
    result = model.transcribe(audio_path, fp16=False, language='french')
    return result['text']

def generate_test_cases(transcription):
    # Charger le modèle Mistral Instruct
    llm = ChatMistralAI(model='mistral-large-latest', temperature=0)
    
    character = "ton profil pour cette conversation est celui d'un consultant expert dans la rédaction de test. Ton role est de rédiger un cas de test à partir d'une description d'un cas metier"
    messages = [    ("system",character,    ),    ("human", transcription)]         
    ai_msg = llm.invoke(messages)
    
    return str(ai_msg.content)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python transcribe.py <path_to_video_file> <path_to_audio_file>")
        sys.exit(1)

# Chemins des fichiers
video_path = sys.argv[1]
audio_path = "extract.wav"
txt_path = "cdt.txt"

# Extraire l'audio
extract_audio_from_video(video_path, audio_path)

# Transcrire l'audio en texte
transcription = transcribe_audio_to_text(audio_path)
print("Transcription :", transcription)

# Générer des cas de test
test_cases = generate_test_cases(transcription)
print("Cas de test :", test_cases)
with open(txt_path, "w") as fichier:
    fichier.write(test_cases)
