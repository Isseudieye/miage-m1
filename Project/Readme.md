# Analyse de l'inflation mondiale

Ce projet explore les données d’inflation par pays et par année, en utilisant un environnement Docker avec PostgreSQL, MinIO et Jupyter Notebook.

1. Si vous êtes sur la racine du projet lancer la commande
   ```bash
   cd Project
   ```
   
2. Build les images Docker
   ```bash
   docker compose -f docker/docker-compose.yaml build
   ```
   
3. Lancer les containers
   ```bash
    docker compose -f docker/docker-compose.yaml up -d
    ```
4. Aller sur l'interface de minio puis explorer les fonctionnalités de minio.
   ```bash
    http://localhost:9001
    ```
5. Aller sur l'interface de Jupyter puis commencer le Projet.
   ```bash
    http://localhost:8888
    ```
6. Résultats générés
Les moyennes d’inflation sont exportées dans MinIO :
- inflation_annuelle.csv
- inflation_par_pays.csv
Ces fichiers sont accessibles via l’interface MinIO (http://localhost:9001) dans le bucket big-data-bucket.

7. Si vous voulez arrêter les containers, vous pouvez lancer la commande suivante :
   ```bash
   docker compose -f docker/docker-compose.yaml down -v
   ```
