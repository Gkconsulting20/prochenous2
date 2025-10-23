# 🚀 Guide de déploiement sur Render.com

## Configuration Render

### 1. Créer un nouveau Web Service
- Allez sur https://render.com
- Cliquez sur "New +" → "Web Service"
- Connectez votre dépôt Git (GitHub/GitLab)

### 2. Paramètres de configuration

**Build & Deploy:**
- **Name:** `pro-chez-nous` (ou votre choix)
- **Region:** Europe (Frankfurt) ou proche de votre cible
- **Branch:** `main` (ou votre branche principale)
- **Runtime:** `Python 3`
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `bash start.sh`

### 3. Variables d'environnement (IMPORTANT!)

Ajoutez ces variables dans l'onglet "Environment" :

```
SECRET_KEY=votre-cle-secrete-tres-longue-et-aleatoire-changez-moi-en-production-123456789
PORT=10000
```

⚠️ **Générez une SECRET_KEY sécurisée** (au moins 50 caractères aléatoires)

### 4. Plan
- **Free Plan:** Gratuit, mais se met en veille après 15 min d'inactivité
- **Starter Plan:** 7$/mois, toujours actif

### 5. Déploiement automatique
✅ Activez "Auto-Deploy" pour déployer à chaque push Git

---

## ⚠️ IMPORTANT : Base de données SQLite

**Problème:** Render utilise un système de fichiers **éphémère**. 
Cela signifie que votre `database.db` sera **supprimée à chaque redémarrage**.

### Solutions :

#### Option A : PostgreSQL (Recommandé pour production)
1. Créez une base PostgreSQL gratuite sur Render
2. Modifiez votre code pour utiliser PostgreSQL au lieu de SQLite
3. Vous aurez des données persistantes

#### Option B : SQLite (Pour test uniquement)
- La base sera réinitialisée à chaque déploiement
- Utile uniquement pour démonstration/test
- Le script `start.sh` recrée automatiquement la base

---

## 📋 Checklist avant déploiement

- [ ] Code poussé sur Git (GitHub/GitLab)
- [ ] Variables d'environnement configurées dans Render
- [ ] Build Command: `pip install -r requirements.txt`
- [ ] Start Command: `bash start.sh`
- [ ] Region sélectionnée (Europe recommandé)

---

## 🔍 Debug des erreurs

### Où voir les logs d'erreur ?

1. **Dans Render Dashboard:**
   - Ouvrez votre service
   - Onglet "Logs"
   - Vous verrez les logs en temps réel

2. **Erreurs communes:**

**Erreur: "Module not found"**
```
Solution: Vérifiez requirements.txt
```

**Erreur: "Permission denied"**
```
Solution: Vérifiez que start.sh est exécutable (chmod +x start.sh)
```

**Erreur: "Port already in use"**
```
Solution: Utilisez $PORT dans start.sh (déjà configuré)
```

**Erreur: "Database locked"**
```
Solution: Problème de concurrence SQLite. Passez à PostgreSQL.
```

---

## 🌐 Accès à votre application

Une fois déployé, votre URL sera :
```
https://pro-chez-nous.onrender.com
```
(ou le nom que vous avez choisi)

---

## 🔄 Mise à jour

Pour mettre à jour votre application :
1. Poussez vos modifications sur Git
2. Render redéploiera automatiquement

---

## 💡 Conseils

1. **Première fois:** Le déploiement peut prendre 5-10 minutes
2. **Free Plan:** L'app se met en veille après 15 min → premier chargement lent (30s)
3. **Logs:** Surveillez les logs pour diagnostiquer les problèmes
4. **PostgreSQL:** Migrez vers PostgreSQL pour la production réelle

---

## 📞 Support

Si le déploiement échoue, vérifiez les logs Render et partagez le message d'erreur complet.
