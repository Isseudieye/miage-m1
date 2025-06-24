# TP 2 Datalake


Ce TP a pour but de vous faire découvrir les bases d'un datalake et de la gestion des données dans un stockage objet.

Comment démarrer ?

0. être sur la bonne branche du projet
   ```bash
   git checkout main && git pull && git checkout -b "your-branch-name"
   ```

1. Si vous êtes sur la racine du projet lancer la commande
   ```bash
   cd Tps/TP2
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
5. Aller sur l'interface de Jupyter puis commencer le TP.
   ```bash
    http://localhost:8888
    ```

6. Si vous voulez arrêter les containers, vous pouvez lancer la commande suivante :
   ```bash
   docker compose -f docker/docker-compose.yaml down -v
   ```
