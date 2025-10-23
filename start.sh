#!/bin/bash
# Script de démarrage pour Render.com

echo "🚀 Démarrage de PRO CHEZ NOUS..."

# Créer les dossiers nécessaires
echo "📁 Création des dossiers requis..."
mkdir -p static/documents_verification
mkdir -p __pycache__

# Initialiser la base de données si elle n'existe pas
if [ ! -f database.db ]; then
    echo "🗄️ Initialisation de la base de données..."
    python3 init_data.py
else
    echo "✅ Base de données existante détectée"
fi

# Vérifier les permissions
chmod 755 static/documents_verification

echo "✅ Configuration terminée!"
echo "🌐 Démarrage du serveur Gunicorn..."

# Démarrer Gunicorn
exec gunicorn --bind=0.0.0.0:$PORT --reuse-port --workers=2 app:app
