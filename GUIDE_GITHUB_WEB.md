# 📤 Guide : Mettre à Jour GitHub via l'Interface Web (Sans Shell)

## 🎯 Objectif
Pousser les changements vers GitHub sans utiliser la ligne de commande, directement via l'interface web.

---

## 📋 Liste des Fichiers à Mettre à Jour

Voici les fichiers qui ont été modifiés et doivent être mis à jour sur GitHub :

### ⭐ Fichiers Principaux (OBLIGATOIRES)
1. **`app.py`** - Fichier principal (ajout routes FedaPay, webhook, etc.)
2. **`utils.py`** - Normalisation des numéros de téléphone
3. **`fedapay_service.py`** - Service de paiement FedaPay (NOUVEAU)
4. **`email_service.py`** - Service d'envoi d'emails SendGrid (NOUVEAU)
5. **`sms_service.py`** - Service SMS Twilio (NOUVEAU)
6. **`add_phone_column.py`** - Script de migration base de données
7. **`requirements.txt`** - Dépendances

### 📄 Templates (OBLIGATOIRES)
8. **`templates/upgrade_premium.html`** - Page de paiement Premium (NOUVEAU)
9. **`templates/payment_redirect.html`** - Page de redirection paiement (NOUVEAU)

### 📖 Documentation (OPTIONNEL mais recommandé)
10. **`INTEGRATION_GUIDE.md`** - Guide d'intégration
11. **`SECURITY_NOTE.md`** - Notes de sécurité
12. **`.env.example`** - Exemple de configuration
13. **`COMPTES_TEST.md`** - Identifiants de test
14. **`DEPLOIEMENT_RAPIDE.md`** - Guide de déploiement rapide
15. **`replit.md`** - Documentation du projet

---

## 🌐 MÉTHODE 1 : Upload Fichier par Fichier (Recommandé)

### Pour CHAQUE fichier de la liste ci-dessus :

#### Étape 1 : Sur Replit - Copier le Contenu
1. Cliquez sur le fichier dans la barre de gauche (ex: `app.py`)
2. **Sélectionnez tout le contenu** : `Ctrl+A` (Windows) ou `Cmd+A` (Mac)
3. **Copiez** : `Ctrl+C` ou `Cmd+C`

#### Étape 2 : Sur GitHub - Mettre à Jour le Fichier

**Pour un fichier EXISTANT (ex: app.py)** :
1. Allez sur : https://github.com/Gkconsulting20/prochenous2
2. Cliquez sur le fichier à mettre à jour (ex: `app.py`)
3. Cliquez sur l'icône **crayon ✏️** ("Edit this file") en haut à droite
4. **Supprimez tout** le contenu actuel : `Ctrl+A` puis `Suppr`
5. **Collez** le nouveau contenu : `Ctrl+V`
6. En bas de la page :
   - **Commit message** : `Mise à jour app.py - Ajout intégrations`
   - Cliquez **"Commit changes"**

**Pour un fichier NOUVEAU (ex: fedapay_service.py)** :
1. Allez sur : https://github.com/Gkconsulting20/prochenous2
2. Cliquez sur **"Add file"** → **"Create new file"**
3. **Nom du fichier** : Tapez le nom exact (ex: `fedapay_service.py`)
4. **Collez** le contenu : `Ctrl+V`
5. En bas :
   - **Commit message** : `Ajout fedapay_service.py`
   - Cliquez **"Commit changes"**

**Pour les fichiers dans templates/** :
1. Sur GitHub, entrez dans le dossier `templates/`
2. Cliquez **"Add file"** → **"Create new file"**
3. Le nom sera automatiquement `templates/votre-fichier.html`
4. Collez le contenu et committez

---

## 🚀 MÉTHODE 2 : Upload Multiple Fichiers (Plus Rapide)

Si GitHub permet l'upload de fichiers (interface récente) :

1. Allez sur : https://github.com/Gkconsulting20/prochenous2
2. Cliquez **"Add file"** → **"Upload files"**
3. **Glissez-déposez** tous les fichiers modifiés
4. **Commit message** : `Mise à jour complète - Intégrations FedaPay, SendGrid, Twilio`
5. Cliquez **"Commit changes"**

**Note** : Pour cette méthode, vous devez d'abord télécharger les fichiers depuis Replit vers votre ordinateur.

---

## 📥 Une Fois sur GitHub : Tirer sur PythonAnywhere

### Étape 1 : Ouvrir Console Bash sur PythonAnywhere
1. https://www.pythonanywhere.com
2. Onglet **Consoles**
3. Cliquez **Bash**

### Étape 2 : Tirer les Changements
```bash
# Aller dans votre projet
cd ~/pro-chez-nous

# Sauvegarder la base de données
cp database.db database.db.backup

# Tirer les changements depuis GitHub
git pull origin main
```

### Étape 3 : Installer les Dépendances
```bash
# Activer l'environnement virtuel
workon votre-env-name

# Installer requests
pip install requests
```

### Étape 4 : Mettre à Jour la Base de Données
```bash
# Ajouter la colonne phone
python add_phone_column.py
```

### Étape 5 : Recharger l'Application
1. Onglet **Web**
2. Bouton vert **"Reload"**

---

## ✅ Ordre Recommandé pour Upload GitHub

Pour éviter les erreurs, uploadez dans cet ordre :

### 1️⃣ D'ABORD : Les nouveaux services
- `fedapay_service.py`
- `email_service.py`
- `sms_service.py`
- `utils.py`
- `add_phone_column.py`

### 2️⃣ ENSUITE : Le fichier principal
- `app.py`

### 3️⃣ PUIS : Les templates
- `templates/upgrade_premium.html`
- `templates/payment_redirect.html`

### 4️⃣ ENSUITE : Les dépendances
- `requirements.txt`

### 5️⃣ ENFIN : La documentation (optionnel)
- Tous les fichiers `.md`

---

## 🎯 Checklist Complète

**Sur GitHub (via interface web)** :
- [ ] `fedapay_service.py` uploadé
- [ ] `email_service.py` uploadé
- [ ] `sms_service.py` uploadé
- [ ] `utils.py` uploadé
- [ ] `add_phone_column.py` uploadé
- [ ] `app.py` mis à jour
- [ ] `templates/upgrade_premium.html` uploadé
- [ ] `templates/payment_redirect.html` uploadé
- [ ] `requirements.txt` mis à jour

**Sur PythonAnywhere (console Bash)** :
- [ ] `git pull origin main` exécuté
- [ ] `pip install requests` exécuté
- [ ] `python add_phone_column.py` exécuté
- [ ] Application rechargée (bouton vert Web)

**Test final** :
- [ ] Site visité : `https://votre-nom.pythonanywhere.com`
- [ ] Connexion testée avec téléphone : `90881111`
- [ ] ✅ Ça marche !

---

## 💡 Astuce : Télécharger les Fichiers depuis Replit

Si vous voulez télécharger un fichier depuis Replit :
1. Cliquez sur le fichier dans la barre de gauche
2. Cliquez sur les **3 points** à côté du nom du fichier
3. Sélectionnez **"Download"**

Ou sélectionnez plusieurs fichiers, clic droit → **"Download"**

---

## 🆘 Problèmes Courants

### ❌ "Couldn't find file on GitHub"
**Solution** : Vous essayez de modifier un fichier qui n'existe pas. Utilisez "Create new file" au lieu de "Edit".

### ❌ "Merge conflict"
**Solution** : Sur PythonAnywhere, faites :
```bash
git reset --hard origin/main
git pull origin main
```

### ❌ "Permission denied"
**Solution** : Vérifiez que vous êtes connecté avec le bon compte GitHub (Gkconsulting20).

---

**Vous êtes prêt ! 🚀**

Commencez par uploader `fedapay_service.py` sur GitHub pour vous familiariser avec le processus.
