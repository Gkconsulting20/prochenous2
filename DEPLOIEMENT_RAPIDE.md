# ⚡ Déploiement Rapide : Replit → GitHub → PythonAnywhere

## 🎯 Votre Configuration Actuelle

✅ **Dépôt GitHub** : https://github.com/Gkconsulting20/prochenous2
✅ **Git déjà configuré** sur Replit
✅ **Fichiers prêts** pour le déploiement

---

## 📤 PARTIE 1 : Pousser depuis Replit vers GitHub (3 commandes)

### Ouvrez le Shell sur Replit et tapez :

```bash
# 1. Ajouter tous les nouveaux fichiers
git add .

# 2. Créer un commit avec message descriptif
git commit -m "Ajout FedaPay, SendGrid, Twilio et normalisation téléphone"

# 3. Pousser vers GitHub
git push origin main
```

**Si demandé** :
- Username : `Gkconsulting20`
- Password : **Votre Personal Access Token GitHub** (pas votre mot de passe)

**Vous n'avez pas de token ?** Créez-en un :
1. https://github.com/settings/tokens
2. "Generate new token (classic)"
3. Cochez "repo"
4. Copiez le token (commence par `ghp_...`)

---

## 📥 PARTIE 2 : Tirer sur PythonAnywhere (4 étapes)

### 1️⃣ Ouvrir Console Bash sur PythonAnywhere

- Allez sur https://www.pythonanywhere.com
- Onglet **Consoles** → Cliquez **Bash**

### 2️⃣ Naviguer vers votre projet et tirer les changements

```bash
# Aller dans votre projet (remplacez par votre nom de dossier)
cd ~/pro-chez-nous

# Sauvegarder votre base de données actuelle
cp database.db database.db.backup

# Tirer les changements depuis GitHub
git pull origin main
```

### 3️⃣ Installer les nouvelles dépendances

```bash
# Activer votre environnement virtuel
workon votre-virtualenv-name

# Installer requests (requis pour les nouveaux services)
pip install requests
```

**Trouver le nom de votre virtualenv** :
```bash
lsvirtualenv
```

### 4️⃣ Mettre à jour la base de données

```bash
# Ajouter la colonne phone (si pas déjà fait)
python add_phone_column.py
```

---

## 🔄 PARTIE 3 : Recharger l'Application

### Sur PythonAnywhere :

1. Allez dans l'onglet **Web**
2. Cliquez sur le gros bouton vert **"Reload votre-nom.pythonanywhere.com"**
3. Attendez 5-10 secondes

---

## ✅ PARTIE 4 : Vérifier que Tout Fonctionne

Visitez votre site : `https://votre-nom.pythonanywhere.com`

**Test rapide** :
1. Allez sur `/login`
2. Tapez : `90881111` (format téléphone court)
3. Password : `test123`
4. ✅ Si ça marche → **Déploiement réussi !** 🎉

---

## 🎁 Résumé Ultra-Court

### Sur Replit Shell :
```bash
git add .
git commit -m "Mise à jour"
git push origin main
```

### Sur PythonAnywhere Console Bash :
```bash
cd ~/pro-chez-nous
git pull origin main
workon votre-env
pip install requests
python add_phone_column.py
```

### Sur PythonAnywhere Web :
- Cliquer bouton vert **"Reload"**

---

## 🆘 Problèmes Fréquents

### ❌ "git push" demande un mot de passe qui ne marche pas

**Solution** : GitHub nécessite un Personal Access Token
- Créez-le ici : https://github.com/settings/tokens
- Utilisez-le comme "password"

### ❌ "ModuleNotFoundError: requests"

**Solution** :
```bash
workon votre-env
pip install requests
```
Puis rechargez l'app.

### ❌ "no such column: phone"

**Solution** :
```bash
python add_phone_column.py
```
Puis rechargez l'app.

### ❌ Les changements ne s'affichent pas

**Solution** :
1. Vérifiez que `git pull` a fonctionné
2. Rechargez l'application (bouton vert)
3. Videz le cache navigateur (`Ctrl+Shift+R`)

---

## 📋 Nouveautés Déployées

Après ce déploiement, votre site aura :

✅ **Connexion par téléphone** (ex: `90881111`)
✅ **Normalisation automatique** (+228, +229, +226, etc.)
✅ **Paiement FedaPay** (T-Money/Flooz - 5000 FCFA)
✅ **Emails SendGrid** (récupération mot de passe)
✅ **SMS Twilio** (vérification)

**Mode actuel** : Démo (testable sans clés API)

---

## 📖 Documentation Complète

Pour les détails :
- `DEPLOIEMENT_GITHUB_PYTHONANYWHERE.md` - Guide complet étape par étape
- `COMPTES_TEST.md` - Identifiants pour tester
- `INTEGRATION_GUIDE.md` - Configuration des API
- `SECURITY_NOTE.md` - Notes de sécurité

---

**C'est tout ! Bon déploiement ! 🚀**
