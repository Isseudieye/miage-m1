# Étape 1 : Utiliser une image Python légère
FROM python:3.10-slim

# Étape 2 : Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Étape 3 : Copier les fichiers nécessaires
COPY requirements.txt requirements.txt

# Étape 4 : Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Étape 5 : Exposer le port pour FastAPI
EXPOSE 8000

# Étape 6 : Lancer le serveur Uvicorn
CMD ["uvicorn", "simple-api:app", "--host", "0.0.0.0", "--port", "8000"]
