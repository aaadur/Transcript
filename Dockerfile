# Utiliser une image de base officielle Python
FROM python:3.11-slim

# Mettre à jour les paquets et installer les dépendances nécessaires
RUN apt-get update && apt-get install -y \
    git \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires dans le conteneur
COPY requirements.txt requirements.txt

# Installer derniere version de PIP
RUN pip install --upgrade pip

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier le script Python dans le conteneur
COPY transcribe.py transcribe.py

# Définir la commande par défaut à exécuter
ENTRYPOINT ["python", "transcribe.py", "/mnt/azurefile/cdt.mp4"]
