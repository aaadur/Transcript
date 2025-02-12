# Transcript
Réalisation de CDT à partir de fichier video / audio

docker build -t whisper-transcriber .
docker run --rm -v /chemin/vers/votre/dossier:/app whisper-transcriber python transcribe.py /app/votre_fichier_video.mp4 /app/audio_extrait.wav
