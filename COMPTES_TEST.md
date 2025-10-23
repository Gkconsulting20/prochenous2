# 🧪 COMPTES DE TEST - PRO CHEZ NOUS

## 🔑 Mot de passe pour TOUS les comptes : `test123`

---

## 👤 COMPTES CLIENTS

### 1. Alice Dupont (Client avec Email ET Téléphone)
- **Email** : `alice@example.com`
- **Téléphone** : `+228 90 88 11 11` ou `90881111`
- **Mot de passe** : `test123`
- **Rôle** : Client
- **Plan** : Gratuit
- **Utilisation** : Tester la connexion par email OU par téléphone

### 2. Bob Martin (Client avec Email ET Téléphone)
- **Email** : `bob@example.com`
- **Téléphone** : `+228 90 88 22 22` ou `90882222`
- **Mot de passe** : `test123`
- **Rôle** : Client
- **Plan** : Gratuit
- **Utilisation** : Second compte client pour tester

---

## 👨‍🔧 COMPTES PROFESSIONNELS

### 3. Jean Peinture (Pro GRATUIT) 
- **Email** : `jean.peintre@prochesnous.fr`
- **Téléphone** : `+228 90 88 33 33` ou `90883333`
- **Mot de passe** : `test123`
- **Rôle** : Professionnel
- **Plan** : Gratuit
- **Catégorie** : Peinture
- **Utilisation** : ⭐ Tester l'upgrade vers Premium (paiement FedaPay)

### 4. Marc Dupont (Pro PREMIUM) 
- **Email** : `marc.plombier@prochesnous.fr`
- **Téléphone** : `+228 90 88 44 44` ou `90884444`
- **Mot de passe** : `test123`
- **Rôle** : Professionnel
- **Plan** : Premium ⭐
- **Catégorie** : Plomberie
- **Utilisation** : Tester toutes les fonctionnalités Premium (messagerie, stats, géolocalisation)

---

## 🧪 SCÉNARIOS DE TEST

### Test 1 : Connexion par Email
1. Allez sur `/login`
2. Email : `[email protected]`
3. Mot de passe : `test123`
4. ✅ Vous devriez être connecté comme client

### Test 2 : Connexion par Téléphone ⭐ NOUVEAU
1. Allez sur `/login`
2. **Champ Email/Téléphone** : Tapez `90881111` (format court)
3. Mot de passe : `test123`
4. ✅ Le système normalise automatiquement en `+228 90 88 11 11` et vous connecte

**Formats acceptés** :
- `90881111` → normalisé en `+228 90 88 11 11`
- `90 88 11 11` → normalisé en `+228 90 88 11 11`
- `22890881111` → normalisé en `+228 90 88 11 11`
- `+228 90 88 11 11` → déjà au bon format

### Test 3 : Upgrade vers Premium (FedaPay)
1. Connectez-vous avec `jean.peintre@prochesnous.fr` (pro gratuit)
2. Allez dans **Tableau de bord** → Cliquez sur **"Passer au Premium"**
3. Page `/subscription` : Voir les avantages Premium
4. Cliquez **"Passer au Premium Maintenant"**
5. Page `/upgrade-premium` : Formulaire de paiement
6. Cliquez **"Procéder au paiement - 5000 FCFA"**
7. Redirection vers page de paiement (mode démo si FedaPay non configuré)
8. ✅ Tester le flux complet de paiement

### Test 4 : Mot de Passe Oublié (SendGrid/Email)
1. Sur `/login`, cliquez **"Mot de passe oublié ?"**
2. Entrez `alice@example.com` OU `90881111`
3. **Mode démo** : Le lien de réinitialisation s'affiche à l'écran
4. **Mode production** (avec SendGrid configuré) : Email envoyé automatiquement
5. Cliquez sur le lien
6. Créez un nouveau mot de passe
7. ✅ Reconnectez-vous avec le nouveau mot de passe

### Test 5 : Fonctionnalités Premium
1. Connectez-vous avec `marc.plombier@prochesnous.fr` (premium)
2. **Tableau de bord** : Voir les statistiques avancées 📊
3. **Messagerie** : Tester l'envoi de messages internes 💬
4. **Favoris** : Ajouter/retirer des pros favoris ⭐
5. **Profil enrichi** : Voir la galerie photos, tarifs détaillés
6. **Géolocalisation** : Activer pour voir les pros à proximité 📍

### Test 6 : Normalisation Téléphone Multi-Pays
Testez avec différents formats et pays :

**Togo (+228)** :
- `90123456` → `+228 90 12 34 56`
- `228 90 12 34 56` → `+228 90 12 34 56`

**Bénin (+229)** :
- `97654321` → `+229 97 65 43 21`

**Burkina Faso (+226)** :
- `70123456` → `+226 70 12 34 56`

---

## 📝 NOTES IMPORTANTES

### Mode Démo vs Production

**Mode Démo actuel** (sans clés API configurées) :
- ✅ Connexion email/téléphone fonctionne
- ✅ Normalisation téléphone active
- ✅ Interface de paiement visible
- ⚠️ Paiements non réels (mode sandbox)
- ⚠️ Emails affichés à l'écran (pas envoyés)
- ⚠️ SMS non envoyés

**Mode Production** (avec clés API) :
- ✅ Tout fonctionne
- ✅ Paiements réels via FedaPay (T-Money, Flooz)
- ✅ Emails envoyés via SendGrid
- ✅ SMS envoyés via Twilio

### Codes de Test FedaPay (Mode Sandbox)

Si FedaPay est configuré en mode **sandbox** :

**Numéros de test T-Money** :
- `+228 90 00 00 01` → Paiement approuvé
- `+228 90 00 00 02` → Paiement refusé
- `+228 90 00 00 03` → Paiement expiré

**Numéros de test Flooz** :
- `+228 96 00 00 01` → Paiement approuvé
- `+228 96 00 00 02` → Paiement refusé

---

## 🔐 Réinitialiser les Comptes de Test

Si vous voulez recommencer à zéro :

```bash
# Sur Replit ou PythonAnywhere
python3 << 'EOF'
import sqlite3
conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute("DELETE FROM users WHERE email LIKE '%test@%' OR phone LIKE '+228 91%'")
conn.commit()
conn.close()
print("Comptes de test supprimés!")
EOF
```

Puis recréez-les en relançant le script de création.

---

## ✅ Checklist de Test Complète

- [ ] Connexion avec email
- [ ] Connexion avec téléphone (format court)
- [ ] Connexion avec téléphone (format international)
- [ ] Inscription nouveau client avec téléphone
- [ ] Inscription nouveau pro avec téléphone
- [ ] Mot de passe oublié (email)
- [ ] Mot de passe oublié (téléphone)
- [ ] Navigation dashboard client
- [ ] Navigation dashboard pro gratuit
- [ ] Navigation dashboard pro premium
- [ ] Page "Passer au Premium"
- [ ] Flux de paiement FedaPay
- [ ] Recherche de professionnels
- [ ] Prise de rendez-vous
- [ ] Système de notation
- [ ] Messagerie (premium)
- [ ] Favoris (premium)
- [ ] Géolocalisation (premium)

---

**Bon test ! 🎉**

Tous les comptes utilisent le mot de passe : **`test123`**
