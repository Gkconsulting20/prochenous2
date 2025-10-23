# 🚀 Guide Complet : Déployer PRO CHEZ NOUS via GitHub → PythonAnywhere

## Vue d'ensemble du Processus

```
Replit → GitHub → PythonAnywhere
  (1)      (2)         (3)
```

1. **Pousser le code de Replit vers GitHub**
2. **Tirer le code de GitHub vers PythonAnywhere**
3. **Installer les dépendances et recharger**

---

## 📦 ÉTAPE 1 : Pousser le Code depuis Replit vers GitHub

### Option A : Si vous avez déjà un dépôt GitHub

#### 1.1 Ouvrir la console Bash sur Replit
- Cliquez sur l'onglet **Shell** en bas de l'écran

#### 1.2 Vérifier votre configuration Git
```bash
git config --global user.name "Votre Nom"
git config --global user.email "[email protected]"
```

#### 1.3 Ajouter tous les nouveaux fichiers
```bash
git add .
```

#### 1.4 Créer un commit avec vos changements
```bash
git commit -m "Ajout intégrations FedaPay, SendGrid, Twilio et normalisation téléphone"
```

#### 1.5 Pousser vers GitHub
```bash
git push origin main
```

**Note** : Si vous avez des problèmes d'authentification, GitHub nécessite un Personal Access Token (pas de mot de passe). Voir Option B ci-dessous.

---

### Option B : Créer un nouveau dépôt GitHub (si vous n'en avez pas)

#### 1.1 Créer le dépôt sur GitHub.com
1. Allez sur https://github.com
2. Connectez-vous à votre compte
3. Cliquez sur le **+** en haut à droite → **New repository**
4. Nom du dépôt : `pro-chez-nous` (ou le nom de votre choix)
5. **NE COCHEZ PAS** "Initialize with README"
6. Cliquez **Create repository**

#### 1.2 Obtenir un Personal Access Token GitHub
1. Sur GitHub, allez dans **Settings** (icône profil en haut à droite)
2. Descendez et cliquez sur **Developer settings** (tout en bas)
3. Cliquez sur **Personal access tokens** → **Tokens (classic)**
4. Cliquez **Generate new token** → **Generate new token (classic)**
5. Nom : `Replit Deploy`
6. Cochez : **repo** (accès complet)
7. Cliquez **Generate token**
8. **⚠️ COPIEZ LE TOKEN** immédiatement (vous ne pourrez plus le voir !)

Exemple de token : `ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`

#### 1.3 Initialiser Git sur Replit (si ce n'est pas déjà fait)
```bash
# Ouvrir le Shell sur Replit
git init
git config --global user.name "Votre Nom"
git config --global user.email "[email protected]"
```

#### 1.4 Ajouter tous les fichiers
```bash
git add .
git commit -m "Version initiale avec intégrations FedaPay, SendGrid, Twilio"
```

#### 1.5 Lier votre dépôt GitHub
```bash
# Remplacez VOTRE-NOM-UTILISATEUR et VOTRE-DEPOT
git remote add origin https://github.com/VOTRE-NOM-UTILISATEUR/VOTRE-DEPOT.git
git branch -M main
```

#### 1.6 Pousser vers GitHub
```bash
git push -u origin main
```

**Quand demandé** :
- **Username** : Votre nom d'utilisateur GitHub
- **Password** : **COLLEZ VOTRE TOKEN** (pas votre mot de passe !)

---

## 📥 ÉTAPE 2 : Tirer le Code de GitHub vers PythonAnywhere

### 2.1 Se connecter à PythonAnywhere
1. Allez sur https://www.pythonanywhere.com
2. Connectez-vous à votre compte

### 2.2 Ouvrir une console Bash
1. Cliquez sur l'onglet **Consoles**
2. Cliquez sur **Bash** pour ouvrir une nouvelle console

### 2.3 Naviguer vers votre projet
```bash
cd ~/votre-nom-de-projet
# Exemple: cd ~/pro-chez-nous
```

**Si vous ne connaissez pas le nom** :
```bash
ls -la ~
# Cherchez le dossier de votre projet
```

### 2.4 Sauvegarder votre base de données actuelle (IMPORTANT)
```bash
# Sauvegarder database.db avant de mettre à jour
cp database.db database.db.backup
```

### 2.5 Tirer les changements depuis GitHub

#### Si c'est votre premier pull depuis GitHub :
```bash
# Configurer Git (si ce n'est pas déjà fait)
git config --global user.name "Votre Nom"
git config --global user.email "[email protected]"

# Si le dépôt n'existe pas encore, clonez-le :
cd ~
git clone https://github.com/VOTRE-NOM-UTILISATEUR/VOTRE-DEPOT.git
```

#### Si le projet existe déjà :
```bash
# Naviguer vers le projet
cd ~/votre-nom-de-projet

# Vérifier l'état
git status

# Tirer les changements
git pull origin main
```

**Si vous avez des conflits** :
```bash
# Option 1 : Garder les changements de GitHub (recommandé)
git reset --hard origin/main

# Option 2 : Garder vos changements locaux
git stash
git pull origin main
```

---

## 🔧 ÉTAPE 3 : Installer les Dépendances et Configurer

### 3.1 Activer votre environnement virtuel
```bash
# Remplacez "mon-env" par le nom de votre virtualenv
workon mon-env
```

**Si vous ne connaissez pas le nom** :
```bash
# Lister tous vos virtualenvs
lsvirtualenv

# Ou regarder dans :
ls ~/.virtualenvs/
```

### 3.2 Installer les nouvelles dépendances
```bash
# S'assurer d'être dans le bon dossier
cd ~/votre-nom-de-projet

# Installer requests (requis pour FedaPay, SendGrid, Twilio)
pip install requests

# Si vous avez un requirements.txt à jour :
pip install -r requirements.txt
```

### 3.3 Mettre à jour la base de données (ajouter la colonne phone)

```bash
# Exécuter le script de migration
python add_phone_column.py
```

**Vérification** :
```bash
python << EOF
import sqlite3
conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute("PRAGMA table_info(users)")
columns = [col[1] for col in cursor.fetchall()]
print("Colonne 'phone' présente :" if 'phone' in columns else "⚠️ Colonne 'phone' MANQUANTE")
conn.close()
EOF
```

### 3.4 Configurer les variables d'environnement (Optionnel)

Si vous voulez activer les services en production :

```bash
# Éditer .bashrc
nano ~/.bashrc
```

**Ajouter à la fin du fichier** :
```bash
# PRO CHEZ NOUS - Configuration Production
export SECRET_KEY="votre-secret-key-flask-super-securisee"

# FedaPay (Optionnel - laisser vide pour mode démo)
export FEDAPAY_SECRET_KEY="sk_live_votre_cle_fedapay"
export FEDAPAY_PUBLIC_KEY="pk_live_votre_cle_fedapay"
export FEDAPAY_ENV="live"

# SendGrid (Optionnel - laisser vide pour mode démo)
export SENDGRID_API_KEY="SG.votre_cle_sendgrid"
export FROM_EMAIL="[email protected]"
export FROM_NAME="PRO CHEZ NOUS"

# Twilio (Optionnel - laisser vide pour mode démo)
export TWILIO_ACCOUNT_SID="ACxxxxxxxxxxxxxxxxx"
export TWILIO_AUTH_TOKEN="votre_token_twilio"
export TWILIO_PHONE_NUMBER="+228XXXXXXXX"
```

**Sauvegarder** : `Ctrl+O`, `Enter`, puis `Ctrl+X`

**Recharger** :
```bash
source ~/.bashrc
```

**⚠️ Note** : Sans ces clés API, l'application fonctionne en **mode démo** :
- ✅ Connexion email/téléphone fonctionne
- ✅ Interface de paiement visible
- ⚠️ Paiements non réels
- ⚠️ Emails affichés à l'écran (pas envoyés)
- ⚠️ SMS non envoyés

---

## 🔄 ÉTAPE 4 : Recharger l'Application PythonAnywhere

### 4.1 Aller dans l'onglet Web
1. Cliquez sur l'onglet **Web** en haut
2. Vous verrez votre application : `votre-nom.pythonanywhere.com`

### 4.2 Vérifier la configuration WSGI (Important !)

Cliquez sur le lien **WSGI configuration file** et vérifiez :

```python
import sys

# Chemin vers votre projet
path = '/home/votre-nom/votre-nom-de-projet'
if path not in sys.path:
    sys.path.insert(0, path)

# Importer votre application Flask
from app import app as application
```

**⚠️ Assurez-vous que** :
- Le `path` pointe vers le bon dossier
- `from app import app as application` correspond à votre fichier (c'est bien `app.py`)

### 4.3 Recharger l'Application ⭐ CRITIQUE

**Cliquez sur le gros bouton vert** : **"Reload votre-nom.pythonanywhere.com"**

### 4.4 Vérifier les Logs en Cas d'Erreur

Si vous voyez "502 Bad Gateway" ou une erreur :

1. **Error log** (lien en bas de la page Web) :
   - Cherchez les erreurs Python récentes
   - Notez le message d'erreur

2. **Server log** :
   - Vérifiez que le serveur démarre correctement

**Erreurs courantes** :
- `ModuleNotFoundError: No module named 'requests'` → Retournez à l'étape 3.2
- `no such column: phone` → Exécutez `add_phone_column.py` (étape 3.3)
- Erreur d'import → Vérifiez le WSGI config (étape 4.2)

---

## ✅ ÉTAPE 5 : Tester Votre Application

### 5.1 Visiter votre site
```
https://votre-nom.pythonanywhere.com
```

### 5.2 Tester les nouvelles fonctionnalités

**Test rapide** :
1. Allez sur `/login`
2. Essayez de vous connecter avec un téléphone : `90881111`
3. Password : `test123`
4. ✅ Si ça marche, les changements sont déployés !

**Tests complets** (voir `COMPTES_TEST.md`) :
- ✅ Connexion par téléphone (formats multiples)
- ✅ Connexion par email
- ✅ Page "Passer au Premium" (`/subscription`)
- ✅ Flux de paiement FedaPay
- ✅ Mot de passe oublié (email ou téléphone)
- ✅ Dashboard pro premium (stats, messagerie)

---

## 🔁 Workflow pour les Prochaines Mises à Jour

À chaque fois que vous faites des changements sur Replit :

### Sur Replit (Shell) :
```bash
git add .
git commit -m "Description des changements"
git push origin main
```

### Sur PythonAnywhere (Console Bash) :
```bash
cd ~/votre-nom-de-projet
git pull origin main
workon mon-env
pip install -r requirements.txt  # Si nouvelles dépendances
# Puis recharger l'app via l'onglet Web
```

---

## 📋 Checklist Complète

- [ ] **Étape 1** : Code poussé vers GitHub depuis Replit
- [ ] **Étape 2** : Code tiré de GitHub vers PythonAnywhere
- [ ] **Étape 3a** : Environnement virtuel activé
- [ ] **Étape 3b** : Dépendances installées (`requests`)
- [ ] **Étape 3c** : Base de données mise à jour (colonne `phone`)
- [ ] **Étape 3d** : Variables d'environnement configurées (optionnel)
- [ ] **Étape 4** : Application rechargée (bouton vert)
- [ ] **Étape 5** : Application testée et fonctionnelle

---

## 🆘 Dépannage

### Problème : "git push" demande un mot de passe qui ne fonctionne pas

**Solution** : GitHub n'accepte plus les mots de passe. Utilisez un Personal Access Token (voir Étape 1.2)

### Problème : "Permission denied (publickey)" sur git pull

**Solution** : Utilisez HTTPS au lieu de SSH :
```bash
git remote set-url origin https://github.com/VOTRE-NOM/VOTRE-DEPOT.git
```

### Problème : "502 Bad Gateway" après reload

**Solution** :
1. Consultez l'Error log (onglet Web)
2. Vérifiez que toutes les dépendances sont installées
3. Vérifiez le WSGI config

### Problème : "ModuleNotFoundError: No module named 'requests'"

**Solution** :
```bash
workon mon-env
pip install requests
```
Puis rechargez l'app.

### Problème : Les changements ne s'affichent pas

**Solution** :
1. Vérifiez que `git pull` a bien fonctionné
2. Rechargez l'application (bouton vert)
3. Videz le cache du navigateur (`Ctrl+Shift+R`)

---

## 🎉 Félicitations !

Vos changements sont maintenant déployés sur PythonAnywhere ! 

Votre application **PRO CHEZ NOUS** est maintenant équipée de :
- ✅ Connexion par email OU téléphone
- ✅ Normalisation automatique des numéros (10 pays africains)
- ✅ Système de paiement FedaPay (T-Money/Flooz)
- ✅ Emails automatiques (SendGrid)
- ✅ Vérification par SMS (Twilio)

**Mode actuel** : Démo (sans clés API) ou Production (avec clés API configurées)

---

📖 **Documentation** :
- `COMPTES_TEST.md` - Identifiants de test
- `INTEGRATION_GUIDE.md` - Configuration des services
- `SECURITY_NOTE.md` - Notes de sécurité
