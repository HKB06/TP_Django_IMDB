# TP Django - Minigallery

Application Django de galerie d'images avec intégration d'API externe ImgBB.

## 🎯 Objectif

Créer une application Django qui :
- Permet d'ajouter des images via une URL
- Permet d'uploader des images vers ImgBB
- Affiche les images dans une galerie
- Stocke les URLs d'images hébergées dans une base de données

## 📋 Étapes réalisées

### Étape 1 - Mise en place du projet
- ✅ Projet Django `minigallery`
- ✅ App `gallery`
- ✅ Configuration SQLite

### Étape 2 - Modèle de données
- ✅ Modèle `Image` avec `title`, `url`, `created_at`
- ✅ Enregistrement dans l'admin Django

### Étape 3 - Vue et template d'affichage
- ✅ Vue `gallery_list` avec boucle `{% for image in images %}`
- ✅ Route `/` configurée

### Étape 4 - Formulaire de création
- ✅ Formulaire `ImageForm` pour ajouter manuellement une URL
- ✅ Vue `add_image` avec GET/POST et redirection
- ✅ Lien "Ajouter une image" sur la page principale

### Étape 5 - Intégration API externe
- ✅ Formulaire d'upload avec `FileField`
- ✅ Utilisation de `requests` pour envoyer l'image à l'API ImgBB
- ✅ Récupération de l'URL hébergée depuis la réponse JSON
- ✅ Stockage de l'URL dans le modèle `Image`
- ✅ Affichage des images hébergées dans la galerie

## 🚀 Installation

```bash
# Activer l'environnement virtuel
.\venv\Scripts\Activate.ps1

# Installer les dépendances
pip install -r requirements.txt

# Appliquer les migrations
python manage.py migrate

# Créer un superutilisateur (optionnel)
python manage.py createsuperuser
```

## 📖 Utilisation

```bash
# Lancer le serveur de développement
python manage.py runserver
```

Puis accéder à :
- **Galerie** : http://127.0.0.1:8000/
- **Upload vers ImgBB** : http://127.0.0.1:8000/upload/
- **Ajouter une URL** : http://127.0.0.1:8000/add/
- **Admin** : http://127.0.0.1:8000/admin/

## 🎨 Fonctionnalités

- **Deux façons d'ajouter des images** :
  1. Uploader un fichier local → envoyé vers ImgBB → URL stockée
  2. Ajouter manuellement une URL d'image

- **Affichage** :
  - Grille responsive avec cartes d'images
  - Titre et date de création affichés
  - Effet hover sur les cartes

## 📦 Dépendances

- Django
- requests

## 🔑 Configuration ImgBB

La clé API ImgBB est configurée dans `minigallery/settings.py` :
```python
IMGBB_API_KEY = 'votre_cle'
```

## 🤔 Questions de réflexion

**Pourquoi ne pas stocker les fichiers directement dans la base ?**
- Limite de taille de la base de données
- Performance dégradée
- Nécessité d'un système de fichiers

**Avantages d'une API d'hébergement externe :**
- ✅ CDN (Content Delivery Network) pour des images rapides
- ✅ Pas de stockage local
- ✅ Infrastructure gérée par un tiers
- ✅ Scalabilité

## 👤 Auteur

HKB06

