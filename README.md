# Transcript
Réalisation de CDT à partir de fichier video / audio

docker-compose build

Exécuter le conteneur :
Vous pouvez modifier le chemin du fichier audio directement dans le fichier docker-compose.yml ou passer le chemin en paramètre lors de l'exécution.

    docker-compose run whisper-transcriber python transcribe.py /app/path/to/your/audiofile.wav

Ces fichiers vous permettent de créer un conteneur Docker avec whisper et de transcrire un fichier audio en texte en passant le chemin du fichier en paramètre
