# ⚠️ NOTES DE SÉCURITÉ - PRO CHEZ NOUS

## Configuration Requise pour la Production

### 🔒 FedaPay - Paiements

**IMPORTANT** : Le mode démo permet de tester l'interface mais **ne doit jamais être utilisé en production** sans configuration complète.

#### Configuration minimale requise :

1. **Clés API FedaPay valides** :
   ```bash
   FEDAPAY_SECRET_KEY=sk_live_votre_cle_secrete  # Pas sk_sandbox !
   FEDAPAY_PUBLIC_KEY=pk_live_votre_cle_publique
   FEDAPAY_ENV=live
   ```

2. **Webhook configuré dans le dashboard FedaPay** :
   - URL : `https://votre-domaine.com/fedapay/callback`
   - Événements : `transaction.approved`, `transaction.declined`, `transaction.canceled`

3. **HTTPS obligatoire** :
   - FedaPay exige HTTPS pour les webhooks en production
   - Utilisez un certificat SSL valide

#### Flux de paiement sécurisé :

1. Utilisateur clique sur "Passer au Premium"
2. Transaction créée via API FedaPay
3. Utilisateur redirigé vers checkout FedaPay
4. Utilisateur paie avec T-Money/Flooz/etc.
5. **FedaPay envoie un webhook signé** à `/fedapay/callback`
6. **Vérification de la signature HMAC** du webhook
7. **Vérification du statut** via API FedaPay
8. **SEULEMENT ALORS**, mise à jour du plan utilisateur

#### Mode démo vs Production :

| Aspect | Mode Démo | Production |
|--------|-----------|------------|
| Clés API | Non requises | **OBLIGATOIRES** |
| Vérification signature | ❌ Bypassée | ✅ Activée |
| Vraie transaction | ❌ Non | ✅ Oui (argent réel) |
| Sécurité | ⚠️ Faible | ✅ Complète |

### 📧 SendGrid - Emails

**Configuration requise en production** :

```bash
SENDGRID_API_KEY=SG.votre_cle_api_sendgrid
FROM_EMAIL=[email protected]  # Email vérifié !
FROM_NAME=PRO CHEZ NOUS
```

**Important** :
- Vérifiez votre domaine ou email dans SendGrid
- Sans configuration : liens affichés à l'écran (démo uniquement)
- Limite gratuite : 100 emails/jour

### 📱 Twilio - SMS

**Configuration requise** :

```bash
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=votre_token_auth
TWILIO_PHONE_NUMBER=+228XXXXXXXX  # Numéro Twilio vérifié
```

**Coûts** :
- ~1$/mois pour le numéro
- ~0.05$/SMS envoyé

## 🚨 Vulnérabilités du Mode Démo

### ⚠️ NE PAS UTILISER EN PRODUCTION SANS CONFIGURATION

Le mode démo permet de :
- Tester l'interface utilisateur
- Vérifier les flux de navigation
- Développer et déboguer localement

**MAIS** :
- ❌ Pas de vérification de paiement réelle
- ❌ Pas de signature webhook
- ❌ Vulnérable aux abus (upgrade gratuit)
- ❌ Ne doit **JAMAIS** être en production

## ✅ Checklist Avant Production

- [ ] Toutes les clés API configurées (FedaPay live, SendGrid, Twilio)
- [ ] Webhook FedaPay configuré dans le dashboard
- [ ] HTTPS activé avec certificat SSL valide
- [ ] Tests de paiement réels effectués en mode sandbox
- [ ] Vérification de signature activée (clés configurées)
- [ ] Email SendGrid vérifié et opérationnel
- [ ] Numéro Twilio acheté et vérifié
- [ ] Variables d'environnement sécurisées (pas dans le code)
- [ ] Logs de paiement activés pour audit
- [ ] Plan de sauvegarde de base de données

## 🔐 Bonnes Pratiques

1. **Secrets** :
   - Ne jamais committer de clés API
   - Utiliser des variables d'environnement
   - Rotation régulière des clés

2. **Webhooks** :
   - Toujours vérifier les signatures
   - Logger toutes les tentatives
   - Rejeter les requêtes non signées

3. **Paiements** :
   - Toujours vérifier le statut via API
   - Ne jamais faire confiance aux paramètres GET
   - Logger toutes les transactions

4. **Monitoring** :
   - Surveiller les paiements échoués
   - Alertes sur activités suspectes
   - Audits réguliers des upgrades

---

**Pour toute question de sécurité, consultez :**
- https://docs.fedapay.com/security
- https://docs.sendgrid.com/ui/account-and-settings/security
- https://www.twilio.com/docs/usage/security

---

**RAPPEL** : Le mode actuel est **DÉMO UNIQUEMENT**. 
Configurez toutes les clés API avant de mettre en production ! 🔒
