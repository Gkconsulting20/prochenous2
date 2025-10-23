# 🐍 Déploiement sur PythonAnywhere (RECOMMANDÉ pour l'Afrique)

## Pourquoi PythonAnywhere ?

- ✅ SQLite **PERSISTANT** - vos données ne seront jamais perdues
- ✅ Plan gratuit généreux
- ✅ Parfait pour Flask
- ✅ Simple et rapide à configurer
- ✅ Support technique disponible

---

## 📋 Guide de déploiement complet

### Étape 1 : Créer un compte

1. Allez sur https://www.pythonanywhere.com
2. Créez un compte **gratuit**
3. Confirmez votre email

### Étape 2 : Uploader vos fichiers

**Option A : Via Git (Recommandé)**

1. Dans PythonAnywhere, ouvrez un **Bash console**
2. Clonez votre dépôt :
```bash
git clone https://github.com/votre-username/pro-chez-nous.git
cd pro-chez-nous
```

**Option B : Upload manuel**

1. Allez dans l'onglet **Files**
2. Uploadez tous vos fichiers un par un
3. Organisez-les dans un dossier `pro-chez-nous`

### Étape 3 : Installer les dépendances

Dans le **Bash console** :

```bash
cd pro-chez-nous
pip3.10 install --user -r requirements.txt
```

### Étape 4 : Initialiser la base de données

```bash
python3.10 init_data.py
```

Vérifiez que `database.db` est créé :
```bash
ls -lh database.db
```

### Étape 5 : Configurer le Web App

1. Allez dans l'onglet **Web**
2. Cliquez sur **Add a new web app**
3. Choisissez **Manual configuration**
4. Sélectionnez **Python 3.10**

### Étape 6 : Configurer le WSGI

1. Dans la section **Code**, cliquez sur le fichier WSGI
2. **Supprimez tout** le contenu
3. Remplacez par ce code :

```python
import sys
import os

# Ajoutez le chemin de votre projet
path = '/home/VOTRE_USERNAME/pro-chez-nous'
if path not in sys.path:
    sys.path.insert(0, path)

# Importez votre application Flask
from app import app as application

# Configuration
application.secret_key = os.environ.get('SECRET_KEY', 'changez-moi-en-production-cle-tres-longue-et-aleatoire')
```

⚠️ Remplacez `VOTRE_USERNAME` par votre nom d'utilisateur PythonAnywhere

### Étape 7 : Configurer les fichiers statiques

Dans l'onglet **Web**, section **Static files** :

| URL | Directory |
|-----|-----------|
| `/static/` | `/home/VOTRE_USERNAME/pro-chez-nous/static` |

⚠️ Remplacez `VOTRE_USERNAME`

### Étape 8 : Créer le dossier d'uploads

Dans le **Bash console** :

```bash
cd /home/VOTRE_USERNAME/pro-chez-nous
mkdir -p static/documents_verification
chmod 755 static/documents_verification
```

### Étape 9 : Configurer les variables d'environnement

1. Ouvrez le fichier WSGI (étape 6)
2. Ajoutez AVANT `from app import app` :

```python
# Variables d'environnement
os.environ['SECRET_KEY'] = 'votre-cle-secrete-tres-longue-minimum-50-caracteres-aleatoires'
```

### Étape 10 : Recharger l'application

1. Dans l'onglet **Web**
2. Cliquez sur le gros bouton vert **Reload**
3. Votre URL sera : `https://VOTRE_USERNAME.pythonanywhere.com`

---

## 🎉 C'est fini !

Visitez : `https://VOTRE_USERNAME.pythonanywhere.com`

---

## 🔍 Debug des erreurs

### Erreur 502 / Site ne charge pas

1. Allez dans **Web** → **Error log**
2. Vérifiez le dernier message d'erreur
3. Corrigez le problème
4. Cliquez sur **Reload**

### Erreurs communes

**"ModuleNotFoundError: No module named 'flask'"**
```bash
cd pro-chez-nous
pip3.10 install --user -r requirements.txt
```

**"Database is locked"**
```bash
# Vérifiez les permissions
chmod 644 database.db
```

**"Static files not loading (logo.png missing)"**
- Vérifiez la configuration Static files (étape 7)
- Assurez-vous que le chemin est correct

---

## 📊 Limites du plan gratuit

- **Stockage** : 512 MB (suffisant pour votre projet)
- **Trafic** : Illimité
- **Uptime** : L'app s'endort après 3 mois d'inactivité (se réveille au premier accès)
- **Custom domain** : Non (besoin du plan payant à 5$/mois)

---

## 🔄 Mettre à jour votre application

### Via Git :

```bash
cd /home/VOTRE_USERNAME/pro-chez-nous
git pull origin main
```

Puis **Reload** dans l'onglet Web

### Via upload manuel :

1. Uploadez les nouveaux fichiers
2. **Reload** dans l'onglet Web

---

## 💡 Avantages pour l'Afrique

- ✅ **Base SQLite persistante** - Aucune perte de données
- ✅ **Gratuit pour commencer** - Pas de frais cachés
- ✅ **Simple** - Pas besoin de DevOps complexe
- ✅ **Fiable** - Utilisé par des milliers d'applications
- ✅ **Support** - Forums actifs et documentation complète

---

## 🚀 Passer au plan payant (optionnel)

Si votre business décolle :

**Plan Hacker** - 5$/mois
- Custom domain (pro-chez-nous.com)
- Plus de CPU
- Pas de publicité PythonAnywhere

---

## 📞 Support

- Forum : https://www.pythonanywhere.com/forums/
- Documentation : https://help.pythonanywhere.com/
- Email : support@pythonanywhere.com
