import sqlite3
from datetime import datetime, timedelta
import random
import bcrypt

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def init_default_data():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    print("📊 Création des tables si nécessaire...")
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT UNIQUE,
            password TEXT,
            role TEXT,
            localisation TEXT,
            categorie TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS slots (
            id INTEGER PRIMARY KEY,
            pro_id INTEGER,
            date TEXT,
            FOREIGN KEY(pro_id) REFERENCES users(id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS rendezvous (
            id INTEGER PRIMARY KEY,
            pro_id INTEGER,
            client_id INTEGER,
            date TEXT,
            FOREIGN KEY(pro_id) REFERENCES users(id),
            FOREIGN KEY(client_id) REFERENCES users(id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS avis (
            id INTEGER PRIMARY KEY,
            pro_id INTEGER,
            client_id INTEGER,
            note INTEGER,
            commentaire TEXT,
            date TEXT,
            FOREIGN KEY(pro_id) REFERENCES users(id),
            FOREIGN KEY(client_id) REFERENCES users(id)
        )
    ''')
    conn.commit()
    
    print("🗑️  Nettoyage de la base de données...")
    cursor.execute('DELETE FROM avis')
    cursor.execute('DELETE FROM rendezvous')
    cursor.execute('DELETE FROM slots')
    cursor.execute('DELETE FROM users')
    conn.commit()
    
    print("👥 Création des professionnels PRO CHEZ NOUS...")
    # Format: (nom, email, mot_de_passe, role, localisation, catégorie)
    professionals = [
        ('Marc Dupont', 'marc.plombier@prochesnous.fr', 'demo123', 'pro', 'Paris 15e', 'Plomberie'),
        ('Sophie Électric', 'sophie.elec@prochesnous.fr', 'demo123', 'pro', 'Lyon 3e', 'Électricité'),
        ('Jean Peinture', 'jean.peintre@prochesnous.fr', 'demo123', 'pro', 'Marseille', 'Peinture'),
        ('Marie Bois', 'marie.menuisiere@prochesnous.fr', 'demo123', 'pro', 'Toulouse', 'Menuiserie'),
        ('Pierre Maçon', 'pierre.macon@prochesnous.fr', 'demo123', 'pro', 'Nice', 'Maçonnerie'),
        ('Claire Rénov', 'claire.renov@prochesnous.fr', 'demo123', 'pro', 'Nantes', 'Rénovation'),
        ('Lucas Vitrier', 'lucas.vitrier@prochesnous.fr', 'demo123', 'pro', 'Bordeaux', 'Vitrerie'),
        ('Emma Jardin', 'emma.jardin@prochesnous.fr', 'demo123', 'pro', 'Strasbourg', 'Jardinage'),
        ('Hugo Serrure', 'hugo.serrurier@prochesnous.fr', 'demo123', 'pro', 'Lille', 'Serrurerie'),
        ('Léa Toiture', 'lea.couvreur@prochesnous.fr', 'demo123', 'pro', 'Rennes', 'Toiture'),
        ('Thomas Chauffage', 'thomas.chauffage@prochesnous.fr', 'demo123', 'pro', 'Paris 11e', 'Autre'),
        ('Nadia Nettoyage', 'nadia.nettoyage@prochesnous.fr', 'demo123', 'pro', 'Lyon 7e', 'Autre')
    ]
    
    for pro in professionals:
        hashed_pwd = hash_password(pro[2])
        cursor.execute('INSERT INTO users (name, email, password, role, localisation, categorie) VALUES (?, ?, ?, ?, ?, ?)', 
                      (pro[0], pro[1], hashed_pwd, pro[3], pro[4], pro[5]))
    
    print("👤 Création des clients...")
    clients = [
        ('Client Demo', 'client@example.com', 'demo123', 'user', None, None),
        ('Alice Dupont', 'alice@example.com', 'demo123', 'user', None, None),
        ('Bob Martin', 'bob@example.com', 'demo123', 'user', None, None)
    ]
    
    for client in clients:
        hashed_pwd = hash_password(client[2])
        cursor.execute('INSERT INTO users (name, email, password, role, localisation, categorie) VALUES (?, ?, ?, ?, ?, ?)', 
                      (client[0], client[1], hashed_pwd, client[3], client[4], client[5]))
    
    conn.commit()
    
    print("⭐ Ajout des avis...")
    reviews = [
        (1, 1, 5, 'Excellente professionnelle! Très à l\'écoute et efficace.'),
        (1, 2, 5, 'Service impeccable, je recommande vivement!'),
        (1, 3, 4, 'Très bon service, ponctuelle et professionnelle.'),
        (2, 1, 4, 'Bon professionnel, travail de qualité.'),
        (2, 2, 5, 'Parfait! Exactement ce que je cherchais.'),
        (3, 1, 5, 'Excellente prestation, très satisfait!'),
        (3, 3, 4, 'Bonne qualité de service.'),
        (4, 2, 3, 'Correct, mais peut mieux faire.'),
        (5, 1, 5, 'Incroyable! Je reviendrai sans hésiter.'),
        (5, 2, 5, 'Professionnalisme au top!'),
        (6, 3, 4, 'Très bien, bon rapport qualité/prix.'),
        (7, 1, 5, 'Excellent travail, recommandé!'),
        (8, 2, 4, 'Bon service dans l\'ensemble.'),
        (9, 1, 5, 'Parfait du début à la fin!')
    ]
    
    today = datetime.now()
    for review in reviews:
        date_review = (today - timedelta(days=random.randint(1, 60))).strftime('%Y-%m-%d')
        cursor.execute('INSERT INTO avis (pro_id, client_id, note, commentaire, date) VALUES (?, ?, ?, ?, ?)', 
                      (review[0], review[1], review[2], review[3], date_review))
    
    print("📅 Ajout des créneaux disponibles...")
    base_date = datetime.now() + timedelta(days=1)
    
    for pro_id in range(1, 11):
        for i in range(5):
            slot_date = (base_date + timedelta(days=i)).strftime('%Y-%m-%d')
            hours = ['09:00', '10:00', '11:00', '14:00', '15:00', '16:00', '17:00']
            for hour in random.sample(hours, 3):
                cursor.execute('INSERT INTO slots (pro_id, date) VALUES (?, ?)', 
                             (pro_id, f"{slot_date} {hour}"))
    
    print("📆 Ajout de quelques rendez-vous...")
    past_date = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d 10:00')
    cursor.execute('INSERT INTO rendezvous (pro_id, client_id, date) VALUES (?, ?, ?)', (1, 1, past_date))
    cursor.execute('INSERT INTO rendezvous (pro_id, client_id, date) VALUES (?, ?, ?)', (2, 2, past_date))
    
    conn.commit()
    conn.close()
    
    print("\n✅ Base de données initialisée avec succès!")
    print("\n📋 Informations de connexion:")
    print("   Client: client@example.com / demo123")
    print("   Pro: sophie.martin@example.com / demo123")

if __name__ == '__main__':
    init_default_data()
