# recovery

Adaptation de l'API conspiracy sous Docker et montée de version PHP/Symfony

## Stack

- PHP 8.4 Symfony 8.1
- Doctrine PostgreSQL 
- Docker Compose

- Vue.js/Vite pour la frontpage (indépendante)

## API

- API consommée par des bots Discord.py
- Gestion de systèmes de cooldowns communs ou individuels sur les commandes du Bot
- Enregistrement et comptage des activations par user
- Sortie de données en json en piochant dans plusieurs tables
- Call vers l'API discord avec un token Bot pour récupérer les user data a partir des id user stockés dans l'API conspiracy

## Bots Discord.py

les fichiers python sont dans le repo mais sont indépendants du montage Docker

## Frontpage

- Une petite page qui consomme l'API Symfony, ne sert pas à grand-chose en soi

## Installation API

ajouter un token Bot discord en Env pour que l'api puisse faire des requêtes à l'api discord pour les user data
ajouter les creds en Env, puis :

- docker compose up -d --build
- docker compose exec -T php composer install
- docker compose exec -T php php bin/console doctrine:migrations:migrate --no-interaction
- docker compose run --rm node npm install
- docker compose run --rm node npm run build

- accès à adminer par tunnel ssh une fois deployé