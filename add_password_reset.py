import sqlite3

def add_password_reset_table():
    """Ajoute la table pour les tokens de réinitialisation de mot de passe"""
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    print("📋 Création de la table password_reset_tokens...")
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS password_reset_tokens (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            token TEXT UNIQUE NOT NULL,
            expiration TEXT NOT NULL,
            used INTEGER DEFAULT 0,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    ''')
    
    conn.commit()
    conn.close()
    
    print("✅ Table password_reset_tokens créée avec succès!")

if __name__ == '__main__':
    add_password_reset_table()
