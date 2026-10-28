# recovery

Adaptation de l'API conspiracy sous Docker et montée de version PHP/Symfony

Un petit jeu entre amis ou le but est d'accumuler le plus de Sinjes possible

Le système repose sur un cooldown collectif dont la durée reste cachée aux utilisateurs. Lorsqu'un certain délai s'est écoulé, un nouveau Sinje est disponible et les utilisateurs peuvent tenter de le récupérer en exécutant une commande avec un bot discord qui consomme l'API. Une fois qu'un Sinje est récupéré, le cooldown repart pour tout le monde. Premier arrivé, Premier servi !

L'API centralise la gestion de la disponibilité, le suivi du cooldown et les verifications pour associer les scores a de vrais comptes Discord. Le bot sert d'interface entre les utilisateurs et l'API, qui peut également être consommée par d'autres services comme par exemple la frontpage dans le repo pour simplement afficher les données.

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

## Installation API et déploiement

ajouter un token Bot discord en Env pour que l'API puisse faire des requêtes à l'API Discord pour les vérifications,
ajouter une URL webhook Discord pour les notifications du système de ticketing,
ajouter les creds en Env, puis :

- docker compose up -d --build
- docker compose exec -T php composer install
- docker compose exec -T php php bin/console doctrine:migrations:migrate --no-interaction

Le build Docker compile automatiquement le frontend avec vite et intègre les fichiers dans l'image donc pas besoin de build à la main pour la frontpage.

- accès à adminer par tunnel ssh une fois deployé