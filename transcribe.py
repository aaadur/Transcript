import sys
import moviepy.editor as mp
import whisper

def extract_audio_from_video(video_path, audio_path):
    # Charger le fichier vidéo
    video = mp.VideoFileClip(video_path)
    # Extraire l'audio et le sauvegarder
    video.audio.write_audiofile(audio_path)


def transcribe_audio_to_text(audio_path):
    # Charger le modèle Whisper
    model = whisper.load_model("base")

    # Transcrire l'audio
    result = model.transcribe(audio_path)
    return result['text']

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python transcribe.py <path_to_video_file> <path_to_audio_file>")
        sys.exit(1)

    video_path = sys.argv[1]
    audio_path = sys.argv[2]

    # Extraire l'audio
    extract_audio_from_video(video_path, audio_path)

    # Transcrire l'audio en texte
    transcription = transcribe_audio_to_text(audio_path)
    print("Transcription :", transcription)
