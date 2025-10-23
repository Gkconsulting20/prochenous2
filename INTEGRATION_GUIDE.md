# 🚀 Guide d'intégration des services PRO CHEZ NOUS

Ce guide vous explique comment configurer les 4 intégrations majeures de votre plateforme :

1. ✅ **Normalisation des numéros de téléphone** (déjà actif !)
2. 💳 **FedaPay** - Paiements T-Money/Flooz  
3. 📧 **SendGrid** - Envoi d'emails
4. 📱 **Twilio** - Vérification SMS

---

## ✅ Option 1 : Normalisation des numéros (ACTIF)

### ✨ Fonctionnalités
- ✅ Normalisation automatique au format international (+228...)
- ✅ Support de 10 pays d'Afrique de l'Ouest (Togo, Bénin, Burkina Faso, etc.)
- ✅ Validation des numéros
- ✅ Formats acceptés : `+228XX`, `228XX`, `00228XX`, `90XXXXXX`

### 📝 Utilisation
```python
from utils import normalize_phone_number, validate_phone_number

# Normaliser un numéro
phone = normalize_phone_number("90123456")  # Retourne "+22890123456"

# Valider un numéro
is_valid = validate_phone_number("+22890123456")  # True
```

**C'est déjà actif !** Tous les numéros sont automatiquement normalisés lors de l'inscription et de la connexion.

---

## 💳 Option 2 : FedaPay - Paiements T-Money/Flooz

### 🎯 Objectif
Accepter des paiements de 5000 FCFA/mois pour l'abonnement Premium via :
- 📱 T-Money (Togocel) - Togo
- 💸 Flooz (Moov Africa) - Togo, Bénin
- 📱 MTN Mobile Money
- 🍊 Orange Money
- 💳 Cartes bancaires (Visa/MasterCard)

### 📋 Étape 1 : Créer un compte FedaPay

1. **Inscription** : https://fedapay.com
2. **Accédez au dashboard** : https://dashboard.fedapay.com
3. **Mode Sandbox** (test) :
   - Récupérez votre `SECRET_KEY` (sk_sandbox_...)
   - Récupérez votre `PUBLIC_KEY` (pk_sandbox_...)

### ⚙️ Étape 2 : Configuration

Créez un fichier `.env` à la racine :

```bash
FEDAPAY_SECRET_KEY=sk_sandbox_votre_cle_secrete
FEDAPAY_PUBLIC_KEY=pk_sandbox_votre_cle_publique
FEDAPAY_ENV=sandbox
```

### 🧪 Étape 3 : Tests en mode Sandbox

```bash
python fedapay_service.py
```

Vous devriez voir :
```
🧪 Test du service FedaPay
Environnement: sandbox
Configuré: True
✅ Transaction créée!
ID: 12345
URL de paiement: https://sandbox-checkout.fedapay.com/...
```

### 🔄 Étape 4 : Tester un paiement

1. Allez sur `/subscription` quand vous êtes connecté
2. Cliquez sur "Passer au Premium"
3. Vous serez redirigé vers FedaPay
4. Testez avec les numéros de test (consultez la doc FedaPay)

### 🚀 Étape 5 : Passer en production

```bash
FEDAPAY_SECRET_KEY=sk_live_votre_cle_secrete
FEDAPAY_PUBLIC_KEY=pk_live_votre_cle_publique
FEDAPAY_ENV=live
```

**Frais FedaPay :** 4% par transaction (5000 FCFA = 200 FCFA de frais)

---

## 📧 Option 3 : SendGrid - Envoi d'emails

### 🎯 Objectif
Envoyer des emails de récupération de mot de passe automatiquement.

### 📋 Étape 1 : Créer un compte SendGrid

1. **Inscription** : https://signup.sendgrid.com
2. **Plan gratuit** : 100 emails/jour (amplement suffisant pour commencer)
3. **Créer une clé API** :
   - Settings > API Keys > Create API Key
   - Nom : "PRO CHEZ NOUS"
   - Permissions : "Full Access"
   - **Copiez la clé** (SG.xxx...)

### ⚙️ Étape 2 : Configuration

Ajoutez à votre `.env` :

```bash
SENDGRID_API_KEY=SG.votre_cle_api_sendgrid
FROM_EMAIL=[email protected]
FROM_NAME=PRO CHEZ NOUS
```

### ✅ Étape 3 : Vérifier votre domaine/email

SendGrid exige une vérification :
- **Option 1** : Vérification d'email simple (Single Sender)
  - Settings > Sender Authentication > Single Sender Verification
  - Entrez votre email ([email protected])
  - Vérifiez votre boîte mail

- **Option 2** : Vérification de domaine (recommandé pour production)
  - Settings > Sender Authentication > Authenticate Your Domain
  - Suivez les instructions DNS

### 🧪 Étape 4 : Tests

```bash
python email_service.py
```

Pour tester l'envoi réel :
```python
from email_service import email_service

result = email_service.send_email(
    "[email protected]",
    "Test",
    "<h1>Hello!</h1>",
    "Hello!"
)
print(result)
```

### 🔄 Étape 5 : Utilisation dans l'app

Maintenant, quand un utilisateur oublie son mot de passe :
1. Il entre son email sur `/forgot_password`
2. **Si SendGrid est configuré** : Un email est automatiquement envoyé
3. **Si non configuré** : Le lien s'affiche à l'écran (mode démo actuel)

---

## 📱 Option 4 : Twilio - Vérification SMS

### 🎯 Objectif
Envoyer des codes de vérification par SMS (utile pour sécuriser les inscriptions par téléphone).

### 📋 Étape 1 : Créer un compte Twilio

1. **Inscription** : https://www.twilio.com/try-twilio
2. **Gratuit** : 15$ de crédit offerts
3. **Console** : https://console.twilio.com

### ⚙️ Étape 2 : Configuration

Récupérez vos identifiants :
- **Account SID** : ACxxxxxxx...
- **Auth Token** : votre token
- **Phone Number** : Achetez un numéro ou utilisez le numéro de test

Ajoutez à votre `.env` :

```bash
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=votre_token_auth
TWILIO_PHONE_NUMBER=+228XXXXXXXX
```

### 📞 Étape 3 : Acheter un numéro

- Buy a Number > Togo (+228) ou autre pays
- **Coût** : ~1$/mois
- **SMS** : ~0.05$/SMS

### 🧪 Étape 4 : Tests

```bash
python sms_service.py
```

Test d'envoi :
```python
from sms_service import sms_service

result = sms_service.send_verification_code("+22890123456")
if result['success']:
    print(f"Code envoyé : {result['code']}")
```

### 🔄 Étape 5 : Utilisation (à implémenter selon vos besoins)

Exemples d'usage :
```python
# Lors de l'inscription
code = sms_service.generate_verification_code()
sms_service.send_verification_code(phone, code)
sms_service.store_verification_code(phone, code)

# Lors de la vérification
if sms_service.verify_code(phone, code_saisi):
    # Code valide, activer le compte
    pass
```

---

## 📊 Résumé des coûts

| Service | Plan gratuit | Coût production |
|---------|--------------|-----------------|
| **FedaPay** | Tests illimités | 4% par transaction |
| **SendGrid** | 100 emails/jour | 15$/mois (40k emails) |
| **Twilio** | 15$ crédit | ~0.05$/SMS + 1$/mois (numéro) |

---

## 🔧 Vérifier la configuration

Créez un fichier `check_config.py` :

```python
from fedapay_service import fedapay_service
from email_service import email_service
from sms_service import sms_service

print("🔍 Vérification de la configuration\n")

print(f"💳 FedaPay: {'✅ Configuré' if fedapay_service.is_configured() else '❌ Non configuré'}")
print(f"📧 SendGrid: {'✅ Configuré' if email_service.is_configured() else '❌ Non configuré'}")
print(f"📱 Twilio: {'✅ Configuré' if sms_service.is_configured() else '❌ Non configuré'}")
```

Exécutez :
```bash
python check_config.py
```

---

## ⚠️ Sécurité en production

### PythonAnywhere

Définissez les variables d'environnement dans l'onglet **Files** :
1. Éditez le fichier `.env`
2. Ou ajoutez-les dans **Web > Environment variables**

### Replit

Utilisez **Secrets** :
- Tools > Secrets
- Ajoutez chaque variable

---

## 🎯 Prochaines étapes

1. **Aujourd'hui** : Testez FedaPay en mode sandbox
2. **Cette semaine** : Configurez SendGrid pour les emails
3. **Optionnel** : Ajoutez Twilio pour la vérification SMS
4. **Production** : Passez FedaPay en mode "live"

---

## 📞 Support

- **FedaPay** : https://docs.fedapay.com
- **SendGrid** : https://docs.sendgrid.com
- **Twilio** : https://www.twilio.com/docs

---

**Votre plateforme est maintenant prête pour le marché africain ! 🎉**
