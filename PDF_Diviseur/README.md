# Diviseur de PDF - Application Web

Une application web permettant de diviser un fichier PDF en plusieurs documents individuels. L'utilisateur peut télécharger un fichier PDF et obtenir une archive contenant les fichiers divisés.

## Fonctionnalités

- **Téléchargement de fichier PDF :** L'utilisateur peut télécharger un fichier PDF depuis son ordinateur.
- **Division du PDF :** Le PDF téléchargé sera automatiquement divisé en plusieurs fichiers.
- **Téléchargement des fichiers divisés :** Après le traitement, l'utilisateur peut télécharger les fichiers séparés sous forme d'une archive `.zip`.
- **Interface conviviale :** Une interface simple et épurée avec des notifications de progression lors du traitement du fichier PDF.

## Technologies utilisées

- **Frontend :**
  - HTML5
  - CSS3 (Bootstrap 4)
  - JavaScript (pour la gestion de la progression et de l'interface utilisateur)
- **Backend :**
  - Python (utilisation d'un framework comme Flask ou Django pour le traitement)
  - Bibliothèque Python `PyPDF2` pour la manipulation des fichiers PDF
  - `zipfile` pour la génération d'archives ZIP des fichiers divisés

## Installation

### Prérequis

1. **Python 3.x** doit être installé sur votre machine.
2. Installez les dépendances nécessaires avec `pip` :
   ```bash
   pip install Flask
   pip install Flask PyPDF2
