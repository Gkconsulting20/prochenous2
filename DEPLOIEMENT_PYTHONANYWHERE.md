# 🚀 Guide de Déploiement - PRO CHEZ NOUS sur PythonAnywhere

## 📋 Mise à Jour de Votre Application Existante

### Étape 1 : Pousser les Changements

#### Option A : Via Git (Recommandé)

Si vous utilisez Git :

1. **Sur votre ordinateur local** (ou Replit), committez et poussez vos changements :
   ```bash
   git add .
   git commit -m "Ajout intégrations FedaPay, SendGrid, Twilio et normalisation téléphone"
   git push origin main
   ```

2. **Sur PythonAnywhere**, ouvrez une console Bash :
   - Allez dans l'onglet **Consoles**
   - Cliquez sur **Bash**
   - Exécutez :
   ```bash
   cd ~/votre-projet-pro-chez-nous
   git pull origin main
   ```

#### Option B : Upload Manuel des Fichiers

Si vous n'utilisez pas Git :

1. Allez dans l'onglet **Files** sur PythonAnywhere
2. Naviguez vers votre dossier de projet
3. Uploadez les fichiers modifiés :
   - `app.py` ⭐ (IMPORTANT - contient les nouvelles routes)
   - `utils.py` (normalisation téléphone)
   - `fedapay_service.py` (nouveau)
   - `email_service.py` (nouveau)
   - `sms_service.py` (nouveau)
   - `templates/upgrade_premium.html` (nouveau)
   - `templates/payment_redirect.html` (nouveau)
   - Autres templates modifiés si nécessaire

### Étape 2 : Installer les Nouvelles Dépendances

Ouvrez une **console Bash** sur PythonAnywhere :

```bash
# Activez votre environnement virtuel
workon votre-env-name  # Remplacez par le nom de votre virtualenv

# Naviguez vers votre projet
cd ~/votre-projet-pro-chez-nous

# Installez les nouvelles dépendances
pip install requests  # Pour les appels API (FedaPay, SendGrid, Twilio)
```

Si vous avez un fichier `requirements.txt` à jour :
```bash
pip install -r requirements.txt
```

### Étape 3 : Configurer les Variables d'Environnement (Optionnel)

Pour activer les services en production, ajoutez les clés API :

1. Ouvrez une **console Bash**
2. Éditez votre fichier `.bashrc` :
   ```bash
   nano ~/.bashrc
   ```

3. Ajoutez ces lignes à la fin du fichier :
   ```bash
   # PRO CHEZ NOUS - Configuration
   export SECRET_KEY="votre-secret-key-flask"
   
   # FedaPay (Paiements T-Money/Flooz) - Optionnel pour démarrer
   export FEDAPAY_SECRET_KEY="sk_live_votre_cle"
   export FEDAPAY_PUBLIC_KEY="pk_live_votre_cle"
   export FEDAPAY_ENV="live"
   
   # SendGrid (Emails) - Optionnel pour démarrer
   export SENDGRID_API_KEY="SG.votre_cle"
   export FROM_EMAIL="[email protected]"
   export FROM_NAME="PRO CHEZ NOUS"
   
   # Twilio (SMS) - Optionnel pour démarrer
   export TWILIO_ACCOUNT_SID="ACxxxxxxxx"
   export TWILIO_AUTH_TOKEN="votre_token"
   export TWILIO_PHONE_NUMBER="+228XXXXXXXX"
   ```

4. Sauvegardez (`Ctrl+O`, `Enter`, puis `Ctrl+X`)
5. Rechargez la configuration :
   ```bash
   source ~/.bashrc
   ```

**Note importante** : Sans les clés API, l'application fonctionne en **mode démo** - toutes les fonctionnalités de base marchent, mais les paiements/emails/SMS ne sont pas réellement envoyés.

### Étape 4 : Mettre à Jour la Base de Données (Si Nécessaire)

Si vous avez une base de données existante **sans** la colonne `phone` :

1. Dans la console Bash :
   ```bash
   cd ~/votre-projet-pro-chez-nous
   python add_phone_column.py
   ```

Si c'est une nouvelle base de données, elle se créera automatiquement au premier lancement.

### Étape 5 : Recharger l'Application ⭐ IMPORTANT

1. Allez dans l'onglet **Web** sur PythonAnywhere
2. Cliquez sur le gros bouton vert **"Reload votre-app.pythonanywhere.com"**
3. Attendez quelques secondes

### Étape 6 : Vérifier que Tout Fonctionne

1. Visitez votre site : `https://votre-nom.pythonanywhere.com`
2. Testez :
   - ✅ Connexion avec email
   - ✅ Connexion avec numéro de téléphone (format accepté : 90123456 ou +228 90 12 34 56)
   - ✅ Page "Passer au Premium" (`/subscription`)
   - ✅ Mot de passe oublié (affichera le lien si SendGrid non configuré)

## 🎯 Résumé des Fonctionnalités Ajoutées

### ✅ Actives Immédiatement (Sans Configuration)

1. **Normalisation des numéros de téléphone**
   - Support de 10 pays africains
   - Formats multiples acceptés

2. **Interface de paiement Premium**
   - Page d'upgrade disponible
   - Mode démo fonctionnel

3. **Système de récupération de mot de passe**
   - Génération de liens sécurisés
   - Mode démo (lien affiché à l'écran)

### 🔧 À Activer avec Clés API (Production)

1. **FedaPay** - Paiements réels T-Money/Flooz (5000 FCFA/mois)
2. **SendGrid** - Envoi d'emails automatiques
3. **Twilio** - Vérification par SMS

Consultez `INTEGRATION_GUIDE.md` et `SECURITY_NOTE.md` pour obtenir les clés API.

## 📁 Structure des Fichiers Importants

```
/home/votre-nom/votre-projet/
├── app.py                          ⭐ Fichier principal (MODIFIÉ)
├── utils.py                        ⭐ Normalisation téléphone (NOUVEAU)
├── fedapay_service.py              ⭐ Service FedaPay (NOUVEAU)
├── email_service.py                ⭐ Service SendGrid (NOUVEAU)
├── sms_service.py                  ⭐ Service Twilio (NOUVEAU)
├── database.db                     Base de données SQLite
├── templates/
│   ├── upgrade_premium.html        ⭐ (NOUVEAU)
│   ├── payment_redirect.html       ⭐ (NOUVEAU)
│   └── ... autres templates
└── static/
    └── ... fichiers CSS/JS
```

## ❓ Problèmes Courants

### Erreur 502 / 504 après reload

**Cause** : Erreur dans le code Python

**Solution** :
1. Consultez les logs d'erreur :
   - Onglet **Web** → Section **Log files**
   - Cliquez sur **Error log**
2. Corrigez l'erreur mentionnée
3. Rechargez l'application

### "Module not found: requests"

**Cause** : Dépendances non installées

**Solution** :
```bash
workon votre-env-name
pip install requests
```
Puis rechargez l'application.

### Les numéros de téléphone ne fonctionnent pas

**Cause** : Format incorrect ou base de données non mise à jour

**Solution** :
1. Exécutez `python add_phone_column.py` pour ajouter la colonne phone
2. Testez avec le format : `90123456` (Togo) ou `+228 90 12 34 56`

### Le site ne recharge pas mes changements

**Cause** : Cache ou reload non effectué

**Solution** :
1. Cliquez sur le bouton **Reload** dans l'onglet Web
2. Videz le cache de votre navigateur (`Ctrl+Shift+R`)

## 🎉 C'est Terminé !

Votre application PRO CHEZ NOUS est maintenant à jour avec :
- ✅ Authentification email ET téléphone
- ✅ Normalisation automatique des numéros africains
- ✅ Interface de paiement Premium (FedaPay)
- ✅ Système d'emails (SendGrid)
- ✅ Vérification par SMS (Twilio)

**Mode démo actif** : Testez l'interface sans configurer les API

**Pour la production** : Ajoutez les clés API dans `~/.bashrc` (Étape 3)

---

📧 **Support** : Consultez les fichiers `INTEGRATION_GUIDE.md` et `SECURITY_NOTE.md` pour plus de détails.
