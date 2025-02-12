import sys
import whisper
 
def transcribe_audio_to_text(audio_path):
    # Charger le modèle Whisper
    model = whisper.load_model("base")

    # Transcrire l'audio
    result = model.transcribe(audio_path)
    return result['text']

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python transcribe.py <path_to_audio_file>")
        sys.exit(1)

    audio_path = sys.argv[1]
    transcription = transcribe_audio_to_text(audio_path)
    print("Transcription :", transcription)
