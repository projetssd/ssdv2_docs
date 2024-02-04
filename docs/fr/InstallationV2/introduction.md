# Introduction

Bienvenue dans ce guide complet destiné à vous accompagner pas à pas dans l'installation et la configuration de votre serveur avec SSDV2. Que vous soyez un utilisateur non technique cherchant à comprendre les bases, ou un technicien aguerri à la recherche d'optimisations avancées, ce tutoriel est fait pour vous.

Notre objectif est de vous fournir toutes les connaissances nécessaires pour mettre en place un serveur sécurisé, performant et personnalisé, capable de gérer vos besoins en matière de streaming, de stockage et de gestion de fichiers multimédias. De la préparation initiale de votre environnement à l'installation des applications indispensables, en passant par la sécurisation de votre serveur, nous couvrirons chaque aspect essentiel pour vous assurer une expérience utilisateur optimale.

Ce guide est structuré pour faciliter sa compréhension et son suivi, indépendamment de votre niveau d'expertise. Ainsi, chaque section a été pensée pour construire progressivement vos connaissances et compétences, en veillant à ce que vous disposiez des fondations nécessaires avant de passer aux étapes plus complexes.

***

[![ScreenShot](https://user-images.githubusercontent.com/64525827/166642246-48c95b9e-c116-4d5b-b3e2-2e1305389f4f.png)](https://user-images.githubusercontent.com/64525827/166640750-3a9b032f-80b1-4aa0-8966-b7abd560f57d.mp4)


***

# Prérequis

Avant de commencer l'installation de votre serveur avec SSDV2, certains prérequis sont nécessaires pour assurer une configuration optimale et performante. Cette section vous guidera à travers le matériel et les logiciels requis, ainsi que des considérations budgétaires pour mener à bien votre projet.

## Serveur

- **Performances** : Pour une expérience fluide, en particulier pour le direct play, il est recommandé d'utiliser un VPS avec au minimum 4 vCores, 8 Go de RAM, et une bande passante illimitée de 1 Gb/s. Les options vont d'environ 150 € par an à des solutions gratuites comme Oracle Cloud Free Tier.
- **Pare-feu** : Ouvrir le port 32400 pour le fonctionnement de Plex.

## Compatibilité des processeurs et des systèmes d’exploitation

- **Systèmes d'exploitation** : Ce guide est conçu pour Ubuntu Server 20.04 (amd64) mais reste compatible avec Ubuntu Server 18.04 à 22.04 et Debian 9 à 12, aussi bien en architectures amd64 qu'arm64.

## Comptes et services

- **Real-Debrid** : Nécessaire pour héberger les différents contenus à streamer. Coût annuel approximatif : 32 €.
- **Nom de domaine** : Essentiel pour la création de sous-domaines facilitant l'accès aux divers panels et sites web. Coût annuel approximatif : 15 €.
- **Plex Pass** : Permet l'accès au contenu sur l'application mobile Plex, avec un coût annuel de 60 €. (optionnel)

## Coûts estimés

La mise en place de ce serveur entraînera des coûts mensuels d'environ 21.41 €, soit un total annuel d'environ 257 €.