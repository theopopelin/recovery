# recovery

Adaptation de l'API conspiracy sous Docker et montée de version PHP/Symfony

## Stack

- PHP 8.4 Symfony 8.1
- Doctrine PostgreSQL 
- Docker Compose

## API

- API consommée par un bot Discord.py
- Gestion de systèmes de cooldowns communs ou individuels sur les commandes du Bot
- Enregistrement et comptage des activations par user

## Installation

docker compose up -d --build