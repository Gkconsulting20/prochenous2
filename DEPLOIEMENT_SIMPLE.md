# 🚀 DÉPLOIEMENT SIMPLE - PRO CHEZ NOUS

## 📦 ÉTAPE 1 : Push vers GitHub (Sur Replit)

### Dans le Shell Replit, exécutez ces 3 commandes :

```bash
git add .
```

```bash
git commit -m "Fix: Tous les formats de téléphone fonctionnent maintenant"
```

```bash
git push origin main
```

**Si demande de login** :
- Username : `Gkconsulting20`
- Password : Votre Personal Access Token GitHub (pas votre mot de passe)

---

## 🌐 ÉTAPE 2 : Déployer sur PythonAnywhere

### Commande Unique (Copier-Coller dans Console Bash PythonAnywhere)

```bash
cd ~/pro-chez-nous && cp database.db database.db.backup && git pull origin main && source ~/.virtualenvs/*/bin/activate && pip install requests && python fix_phone_spaces.py && echo "✅ TERMINÉ ! Allez dans Web → Cliquez Reload"
```

### Explication de la commande :
1. `cd ~/pro-chez-nous` - Aller dans le dossier du projet
2. `cp database.db database.db.backup` - Sauvegarder la base de données
3. `git pull origin main` - Télécharger les nouveaux fichiers depuis GitHub
4. `source ~/.virtualenvs/*/bin/activate` - Activer l'environnement Python
5. `pip install requests` - Installer les dépendances
6. `python fix_phone_spaces.py` - Normaliser les numéros de téléphone dans la base
7. Message de confirmation

### Après la commande :
1. Allez dans l'onglet **Web** sur PythonAnywhere
2. Cliquez sur le bouton vert **"Reload votre-nom.pythonanywhere.com"**
3. ✅ Votre site est à jour !

---

## 🧪 ÉTAPE 3 : Tester le Site Déployé

Visitez : `https://votre-nom.pythonanywhere.com/login`

Testez la connexion avec :
- Téléphone : `90881111` (ou n'importe quel format)
- Email : `alice@example.com`
- Password : `test123`

**Tous les formats de téléphone fonctionnent** :
- `90881111` ✅
- `90 88 11 11` ✅  
- `+22890881111` ✅
- `+228 90 88 11 11` ✅

---

## ⚙️ Configuration Production (Optionnel)

Pour activer les paiements et emails en production, ajoutez ces variables d'environnement sur PythonAnywhere :

### Sur PythonAnywhere : Web → Variables d'environnement

```bash
# FedaPay (Paiements)
FEDAPAY_SECRET_KEY=votre_clé_secrète
FEDAPAY_PUBLIC_KEY=votre_clé_publique
FEDAPAY_ENV=live

# SendGrid (Emails)
SENDGRID_API_KEY=votre_clé_sendgrid
FROM_EMAIL=noreply@prochenous.com
FROM_NAME=PRO CHEZ NOUS

# Twilio (SMS - Optionnel)
TWILIO_ACCOUNT_SID=votre_account_sid
TWILIO_AUTH_TOKEN=votre_auth_token
TWILIO_PHONE_NUMBER=+228XXXXXXXX
```

Puis : **Web** → **Reload**

---

## 🔧 Dépannage

### Erreur : "no such file or directory"
→ Remplacez `pro-chez-nous` par le vrai nom de votre dossier
→ Vérifiez avec : `ls -la ~`

### Erreur : "virtualenv not found"
→ Trouvez le nom exact avec : `lsvirtualenv`
→ Remplacez `~/.virtualenvs/*/bin/activate` par le bon chemin

### Le site ne se met pas à jour
→ Vérifiez que `git pull` a bien téléchargé les fichiers
→ Assurez-vous d'avoir cliqué sur **Reload** dans l'onglet Web

### Les téléphones ne fonctionnent toujours pas
→ Vérifiez que `fix_phone_spaces.py` s'est bien exécuté
→ Testez : `python -c "import sqlite3; conn = sqlite3.connect('database.db'); print(conn.execute('SELECT phone FROM users LIMIT 1').fetchone())"`
→ Les numéros doivent être SANS espaces : `+22890881111`

---

**Déploiement complet en 3 étapes simples ! 🎉**
