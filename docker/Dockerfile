# Étape 1 : Choisir une image de base
FROM <base-image>:<tag>

# Étape 2 : Ajouter des métadonnées (optionnel)
LABEL maintainer="your-email@example.com"
LABEL version="1.0"
LABEL description="Description of the application."

# Étape 3 : Définir le répertoire de travail
WORKDIR /app

# Étape 4 : Copier les fichiers nécessaires dans l'image
COPY . /app

# Étape 5 : Installer les dépendances
RUN <install-commands>

# Étape 6 : Définir des variables d'environnement (optionnel)
ENV ENV_VARIABLE=value

# Étape 7 : Exposer un ou plusieurs ports
EXPOSE <port>

# Étape 8 : Nettoyage (optionnel, pour réduire la taille de l'image)
RUN rm -rf /var/lib/apt/lists/*

# Étape 9 : Définir la commande d’exécution
CMD ["<command>", "arg1", "arg2"]
