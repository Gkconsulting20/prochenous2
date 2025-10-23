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
            categorie TEXT,
            plan TEXT DEFAULT 'gratuit',
            statut_verification TEXT DEFAULT 'non_verifie'
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
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS profils_pro (
            id INTEGER PRIMARY KEY,
            pro_id INTEGER UNIQUE,
            description TEXT,
            tarif_horaire TEXT,
            experience TEXT,
            certifications TEXT,
            photo_url TEXT,
            FOREIGN KEY(pro_id) REFERENCES users(id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY,
            expediteur_id INTEGER,
            destinataire_id INTEGER,
            contenu TEXT,
            date TEXT,
            lu INTEGER DEFAULT 0,
            FOREIGN KEY(expediteur_id) REFERENCES users(id),
            FOREIGN KEY(destinataire_id) REFERENCES users(id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS favoris (
            id INTEGER PRIMARY KEY,
            client_id INTEGER,
            pro_id INTEGER,
            date_ajout TEXT,
            FOREIGN KEY(client_id) REFERENCES users(id),
            FOREIGN KEY(pro_id) REFERENCES users(id)
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS documents_verification (
            id INTEGER PRIMARY KEY,
            pro_id INTEGER,
            type_document TEXT,
            nom_fichier TEXT,
            chemin_fichier TEXT,
            date_upload TEXT,
            statut TEXT DEFAULT 'en_attente',
            FOREIGN KEY(pro_id) REFERENCES users(id)
        )
    ''')
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
    
    print("🗑️  Nettoyage de la base de données...")
    cursor.execute('DELETE FROM documents_verification')
    cursor.execute('DELETE FROM favoris')
    cursor.execute('DELETE FROM messages')
    cursor.execute('DELETE FROM profils_pro')
    cursor.execute('DELETE FROM avis')
    cursor.execute('DELETE FROM rendezvous')
    cursor.execute('DELETE FROM slots')
    cursor.execute('DELETE FROM users')
    conn.commit()
    
    print("👥 Création des professionnels PRO CHEZ NOUS...")
    # Format: (nom, email, mot_de_passe, role, localisation, catégorie, plan)
    professionals = [
        ('Marc Dupont', 'marc.plombier@prochesnous.fr', 'demo123', 'pro', 'Paris 15e', 'Plomberie', 'premium'),
        ('Sophie Électric', 'sophie.elec@prochesnous.fr', 'demo123', 'pro', 'Lyon 3e', 'Électricité', 'premium'),
        ('Jean Peinture', 'jean.peintre@prochesnous.fr', 'demo123', 'pro', 'Marseille', 'Peinture', 'gratuit'),
        ('Marie Bois', 'marie.menuisiere@prochesnous.fr', 'demo123', 'pro', 'Toulouse', 'Menuiserie', 'premium'),
        ('Pierre Maçon', 'pierre.macon@prochesnous.fr', 'demo123', 'pro', 'Nice', 'Maçonnerie', 'gratuit'),
        ('Claire Rénov', 'claire.renov@prochesnous.fr', 'demo123', 'pro', 'Nantes', 'Rénovation', 'premium'),
        ('Lucas Vitrier', 'lucas.vitrier@prochesnous.fr', 'demo123', 'pro', 'Bordeaux', 'Vitrerie', 'gratuit'),
        ('Emma Jardin', 'emma.jardin@prochesnous.fr', 'demo123', 'pro', 'Strasbourg', 'Jardinage', 'premium'),
        ('Hugo Serrure', 'hugo.serrurier@prochesnous.fr', 'demo123', 'pro', 'Lille', 'Serrurerie', 'gratuit'),
        ('Léa Toiture', 'lea.couvreur@prochesnous.fr', 'demo123', 'pro', 'Rennes', 'Toiture', 'premium'),
        ('Thomas Chauffage', 'thomas.chauffage@prochesnous.fr', 'demo123', 'pro', 'Paris 11e', 'Autre', 'gratuit'),
        ('Nadia Nettoyage', 'nadia.nettoyage@prochesnous.fr', 'demo123', 'pro', 'Lyon 7e', 'Autre', 'gratuit')
    ]
    
    for pro in professionals:
        hashed_pwd = hash_password(pro[2])
        cursor.execute('INSERT INTO users (name, email, password, role, localisation, categorie, plan) VALUES (?, ?, ?, ?, ?, ?, ?)', 
                      (pro[0], pro[1], hashed_pwd, pro[3], pro[4], pro[5], pro[6]))
    
    print("👤 Création des clients...")
    # Format: (nom, email, mot_de_passe, role, localisation, catégorie, plan)
    clients = [
        ('Client Demo', 'client@example.com', 'demo123', 'user', None, None, 'premium'),
        ('Alice Dupont', 'alice@example.com', 'demo123', 'user', None, None, 'gratuit'),
        ('Bob Martin', 'bob@example.com', 'demo123', 'user', None, None, 'gratuit')
    ]
    
    for client in clients:
        hashed_pwd = hash_password(client[2])
        cursor.execute('INSERT INTO users (name, email, password, role, localisation, categorie, plan) VALUES (?, ?, ?, ?, ?, ?, ?)', 
                      (client[0], client[1], hashed_pwd, client[3], client[4], client[5], client[6]))
    
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
    
    print("💎 Ajout des profils enrichis pour les professionnels premium...")
    profils_premium = [
        (1, 'Plombier expérimenté spécialisé dans les installations sanitaires modernes. Interventions rapides et soignées.', '45€/h', '15 ans', 'Certification Qualibat, Assurance décennale'),
        (2, 'Électricienne diplômée, spécialiste en domotique et systèmes électriques intelligents.', '50€/h', '10 ans', 'Certification Qualifelec, Habilitation électrique'),
        (4, 'Menuisière passionnée, créations sur mesure en bois massif. Travail artisanal de qualité.', '42€/h', '12 ans', 'CAP Menuiserie, Artisan d\'Art'),
        (6, 'Experte en rénovation complète d\'appartements et maisons. Coordination de tous les corps de métier.', '55€/h', '18 ans', 'Certification RGE, Assurance tous risques'),
        (8, 'Paysagiste et jardinière professionnelle. Création et entretien d\'espaces verts.', '38€/h', '8 ans', 'Diplôme d\'État Paysagiste'),
        (10, 'Couvreur expert en toiture traditionnelle et isolation. Garantie décennale.', '48€/h', '20 ans', 'Certification Qualibat, Expert ardoise et tuile')
    ]
    
    for profil in profils_premium:
        cursor.execute('INSERT INTO profils_pro (pro_id, description, tarif_horaire, experience, certifications) VALUES (?, ?, ?, ?, ?)', 
                      profil)
    
    conn.commit()
    conn.close()
    
    print("\n✅ Base de données initialisée avec succès!")
    print("\n📋 Informations de connexion:")
    print("   Client: client@example.com / demo123")
    print("   Pro: sophie.martin@example.com / demo123")

if __name__ == '__main__':
    init_default_data()
