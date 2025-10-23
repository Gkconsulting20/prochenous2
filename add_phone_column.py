import sqlite3

def add_phone_column():
    """Ajoute la colonne phone à la table users"""
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    print("📱 Ajout de la colonne phone à la table users...")
    
    try:
        cursor.execute('ALTER TABLE users ADD COLUMN phone TEXT')
        conn.commit()
        print("✅ Colonne phone ajoutée avec succès!")
    except sqlite3.OperationalError as e:
        if "duplicate column name" in str(e).lower():
            print("ℹ️  La colonne phone existe déjà")
        else:
            print(f"❌ Erreur: {e}")
    
    # Créer un index pour les recherches rapides par téléphone
    try:
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_users_phone ON users(phone)')
        conn.commit()
        print("✅ Index créé pour les numéros de téléphone")
    except Exception as e:
        print(f"⚠️  Index: {e}")
    
    conn.close()
    print("✅ Migration terminée!")

if __name__ == '__main__':
    add_phone_column()
