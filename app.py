from flask import Flask, render_template, request, redirect, url_for, session, flash
import sqlite3
import bcrypt
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

def get_db():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    categories = [
        '🔧 Plomberie', '⚡ Électricité', '🎨 Peinture', '🪚 Menuiserie', '🧱 Maçonnerie',
        '🏗️ Rénovation', '🪟 Vitrerie', '🔐 Serrurerie', '🏠 Toiture', '🪜 Couverture',
        '🌳 Jardinage', '🌱 Paysagiste', '🌿 Élagage', '💧 Piscine',
        '❄️ Climatisation', '🔥 Chauffage', '📡 Antenne/Parabole', '🚪 Portail/Clôture',
        '🧹 Nettoyage', '🧽 Ménage à domicile', '🪟 Lavage vitres', '🧼 Pressing/Repassage',
        '🚚 Déménagement', '📦 Livraison', '🚗 Transport', '🛵 Coursier',
        '🔨 Bricolage', '⚙️ Dépannage', '🔧 Réparation électroménager', '📱 Réparation téléphone',
        '💻 Informatique', '🖥️ Maintenance PC', '📶 Installation internet',
        '✂️ Coiffure à domicile', '💅 Manucure', '💆 Massage', '👗 Couture/Retouche',
        '🍳 Cuisinier à domicile', '🎂 Pâtisserie', '🍕 Traiteur', '☕ Barista',
        '👶 Garde d\'enfants', '🧓 Aide à domicile', '🐕 Garde animaux', '🚶 Promenade chiens',
        '🚗 Mécanicien auto', '🏍️ Mécanicien moto', '🔧 Carrosserie', '🚙 Lavage auto',
        '📚 Soutien scolaire', '🎓 Formation', '🎸 Cours de musique', '🎨 Cours d\'art',
        '📸 Photographe', '🎥 Vidéaste', '🎤 DJ/Sonorisation', '🎪 Animation événements',
        '👔 Repassage', '🧺 Blanchisserie', '🪡 Tapissier', '🛋️ Rénovation meuble',
        '🪴 Fleuriste', '🌺 Décoration florale', '🎀 Décoration événements',
        '🔒 Sécurité', '👮 Gardiennage', '📹 Installation alarme',
        '🏋️ Coach sportif', '🧘 Yoga/Pilates', '💪 Personal trainer',
        '🐝 Apiculture', '🐓 Élevage', '🌾 Agriculture', '🥕 Maraîchage',
        '🎪 Autres services'
    ]
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()
        role = request.form.get('role', '').strip()
        localisation = request.form.get('localisation', '').strip()
        categorie = request.form.get('categorie', '').strip() if role == 'pro' else None
        
        if not name or not email or not password or not role:
            flash('Tous les champs obligatoires doivent être remplis', 'error')
            return render_template('register.html', categories=categories)
        
        conn = get_db()
        existing_user = conn.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
        if existing_user:
            flash('Cette adresse email est déjà utilisée', 'error')
            return render_template('register.html', categories=categories)
        
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        conn.execute('INSERT INTO users (name, email, password, role, localisation, categorie) VALUES (?, ?, ?, ?, ?, ?)',
                     (name, email, hashed_password, role, localisation, categorie))
        conn.commit()
        flash('Inscription réussie! Vous pouvez maintenant vous connecter', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', categories=categories)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '').strip()
        
        if not email or not password:
            flash('Veuillez remplir tous les champs', 'error')
            return render_template('login.html')
        
        conn = get_db()
        user = conn.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
        
        if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
            session['user_id'] = user['id']
            session['role'] = user['role']
            flash(f'Bienvenue {user["name"]}!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Email ou mot de passe incorrect', 'error')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session: return redirect(url_for('login'))
    conn = get_db()
    user = conn.execute('SELECT * FROM users WHERE id = ?', (session['user_id'],)).fetchone()
    if user['role'] == 'pro':
        rdvs = conn.execute('''
            SELECT r.id, r.date, u.name as client FROM rendezvous r
            JOIN users u ON r.client_id = u.id WHERE r.pro_id = ?
            ORDER BY r.date DESC
        ''', (user['id'],)).fetchall()
        return render_template('dashboard_pro.html', user=user, rdvs=rdvs)
    else:
        rdvs = conn.execute('''
            SELECT r.id, r.date, u.name as pro_name FROM rendezvous r
            JOIN users u ON r.pro_id = u.id WHERE r.client_id = ?
            ORDER BY r.date DESC
        ''', (user['id'],)).fetchall()
        return render_template('dashboard_user.html', user=user, rdvs=rdvs)

@app.route('/professionals')
def view_professionals():
    conn = get_db()
    categories = [
        '🔧 Plomberie', '⚡ Électricité', '🎨 Peinture', '🪚 Menuiserie', '🧱 Maçonnerie',
        '🏗️ Rénovation', '🪟 Vitrerie', '🔐 Serrurerie', '🏠 Toiture', '🪜 Couverture',
        '🌳 Jardinage', '🌱 Paysagiste', '🌿 Élagage', '💧 Piscine',
        '❄️ Climatisation', '🔥 Chauffage', '📡 Antenne/Parabole', '🚪 Portail/Clôture',
        '🧹 Nettoyage', '🧽 Ménage à domicile', '🪟 Lavage vitres', '🧼 Pressing/Repassage',
        '🚚 Déménagement', '📦 Livraison', '🚗 Transport', '🛵 Coursier',
        '🔨 Bricolage', '⚙️ Dépannage', '🔧 Réparation électroménager', '📱 Réparation téléphone',
        '💻 Informatique', '🖥️ Maintenance PC', '📶 Installation internet',
        '✂️ Coiffure à domicile', '💅 Manucure', '💆 Massage', '👗 Couture/Retouche',
        '🍳 Cuisinier à domicile', '🎂 Pâtisserie', '🍕 Traiteur', '☕ Barista',
        '👶 Garde d\'enfants', '🧓 Aide à domicile', '🐕 Garde animaux', '🚶 Promenade chiens',
        '🚗 Mécanicien auto', '🏍️ Mécanicien moto', '🔧 Carrosserie', '🚙 Lavage auto',
        '📚 Soutien scolaire', '🎓 Formation', '🎸 Cours de musique', '🎨 Cours d\'art',
        '📸 Photographe', '🎥 Vidéaste', '🎤 DJ/Sonorisation', '🎪 Animation événements',
        '👔 Repassage', '🧺 Blanchisserie', '🪡 Tapissier', '🛋️ Rénovation meuble',
        '🪴 Fleuriste', '🌺 Décoration florale', '🎀 Décoration événements',
        '🔒 Sécurité', '👮 Gardiennage', '📹 Installation alarme',
        '🏋️ Coach sportif', '🧘 Yoga/Pilates', '💪 Personal trainer',
        '🐝 Apiculture', '🐓 Élevage', '🌾 Agriculture', '🥕 Maraîchage',
        '🎪 Autres services'
    ]
    
    search = request.args.get('search', '').strip()
    ville = request.args.get('ville', '').strip()
    note_min = request.args.get('note_min', '').strip()
    categorie = request.args.get('categorie', '').strip()
    
    query = '''
        SELECT u.id, u.name, u.localisation, u.categorie,
               COALESCE(AVG(a.note), 0) as note_moyenne,
               COUNT(a.id) as nb_avis
        FROM users u
        LEFT JOIN avis a ON u.id = a.pro_id
        WHERE u.role = 'pro'
    '''
    
    params = []
    
    if search:
        query += ' AND u.name LIKE ?'
        params.append(f'%{search}%')
    
    if ville:
        query += ' AND u.localisation LIKE ?'
        params.append(f'%{ville}%')
    
    if categorie:
        query += ' AND u.categorie = ?'
        params.append(categorie)
    
    query += ' GROUP BY u.id'
    
    if note_min:
        query += ' HAVING note_moyenne >= ?'
        params.append(float(note_min))
    
    query += ' ORDER BY note_moyenne DESC'
    
    pros = conn.execute(query, params).fetchall()
    return render_template('professionals.html', professionals=pros, categories=categories)

@app.route('/book/<int:pro_id>', methods=['GET', 'POST'])
def book(pro_id):
    if 'user_id' not in session: return redirect(url_for('login'))
    conn = get_db()
    if request.method == 'POST':
        slot_id = request.form['slot_id']
        conn.execute('INSERT INTO rendezvous (pro_id, client_id, date) SELECT pro_id, ?, date FROM slots WHERE id = ?',
                     (session['user_id'], slot_id))
        conn.execute('DELETE FROM slots WHERE id = ?', (slot_id,))
        conn.commit()
        flash('Rendez-vous réservé avec succès!', 'success')
        return redirect(url_for('dashboard'))
    pro = conn.execute('SELECT * FROM users WHERE id = ?', (pro_id,)).fetchone()
    slots = conn.execute('SELECT * FROM slots WHERE pro_id = ?', (pro_id,)).fetchall()
    return render_template('book.html', pro=pro, slots=slots)

@app.route('/add_slot', methods=['GET', 'POST'])
def add_slot():
    if 'user_id' not in session or session['role'] != 'pro':
        return redirect(url_for('login'))
    if request.method == 'POST':
        conn = get_db()
        conn.execute('INSERT INTO slots (pro_id, date) VALUES (?, ?)',
                     (session['user_id'], request.form['date']))
        conn.commit()
        return redirect(url_for('dashboard'))
    return render_template('add_slot.html')

@app.route('/rate/<int:pro_id>', methods=['GET', 'POST'])
def rate(pro_id):
    if 'user_id' not in session or session['role'] != 'user':
        return redirect(url_for('login'))
    conn = get_db()
    if request.method == 'POST':
        from datetime import datetime
        note = request.form['note']
        commentaire = request.form.get('commentaire', '')
        conn.execute('INSERT INTO avis (pro_id, client_id, note, commentaire, date) VALUES (?, ?, ?, ?, ?)',
                     (pro_id, session['user_id'], note, commentaire, datetime.now().strftime('%Y-%m-%d')))
        conn.commit()
        return redirect(url_for('view_professionals'))
    pro = conn.execute('SELECT * FROM users WHERE id = ?', (pro_id,)).fetchone()
    return render_template('rate.html', pro=pro)

@app.route('/cancel_rdv/<int:rdv_id>', methods=['POST'])
def cancel_rdv(rdv_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    conn = get_db()
    rdv = conn.execute('SELECT * FROM rendezvous WHERE id = ?', (rdv_id,)).fetchone()
    
    if rdv and (rdv['client_id'] == session['user_id'] or rdv['pro_id'] == session['user_id']):
        conn.execute('INSERT INTO slots (pro_id, date) VALUES (?, ?)', (rdv['pro_id'], rdv['date']))
        conn.execute('DELETE FROM rendezvous WHERE id = ?', (rdv_id,))
        conn.commit()
        flash('Rendez-vous annulé avec succès. Le créneau est à nouveau disponible.', 'success')
    else:
        flash('Impossible d\'annuler ce rendez-vous', 'error')
    
    return redirect(url_for('dashboard'))

@app.route('/subscription')
def subscription():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    conn = get_db()
    user = conn.execute('SELECT * FROM users WHERE id = ?', (session['user_id'],)).fetchone()
    return render_template('subscription.html', user=user)

@app.route('/upgrade_premium', methods=['POST'])
def upgrade_premium():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    conn = get_db()
    conn.execute('UPDATE users SET plan = ? WHERE id = ?', ('premium', session['user_id']))
    conn.commit()
    flash('Félicitations! Vous êtes maintenant membre Premium 🌟', 'success')
    return redirect(url_for('dashboard'))

@app.route('/profil/<int:pro_id>')
def profil(pro_id):
    conn = get_db()
    pro = conn.execute('SELECT * FROM users WHERE id = ? AND role = ?', (pro_id, 'pro')).fetchone()
    if not pro:
        flash('Professionnel introuvable', 'error')
        return redirect(url_for('view_professionals'))
    
    profil_enrichi = conn.execute('SELECT * FROM profils_pro WHERE pro_id = ?', (pro_id,)).fetchone()
    avis = conn.execute('''
        SELECT a.*, u.name as client_name FROM avis a
        JOIN users u ON a.client_id = u.id
        WHERE a.pro_id = ? ORDER BY a.date DESC
    ''', (pro_id,)).fetchall()
    
    note_moyenne = conn.execute('SELECT AVG(note) as moyenne FROM avis WHERE pro_id = ?', (pro_id,)).fetchone()
    
    is_favori = False
    if 'user_id' in session:
        favori = conn.execute('SELECT * FROM favoris WHERE client_id = ? AND pro_id = ?', 
                            (session['user_id'], pro_id)).fetchone()
        is_favori = favori is not None
    
    return render_template('profil.html', pro=pro, profil=profil_enrichi, avis=avis, 
                         note_moyenne=note_moyenne, is_favori=is_favori)

@app.route('/messages')
def messages():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    conn = get_db()
    user = conn.execute('SELECT * FROM users WHERE id = ?', (session['user_id'],)).fetchone()
    
    if user['plan'] != 'premium':
        flash('La messagerie est réservée aux membres Premium. Passez à Premium pour accéder à cette fonctionnalité!', 'error')
        return redirect(url_for('subscription'))
    
    received = conn.execute('''
        SELECT m.*, u.name as expediteur_name FROM messages m
        JOIN users u ON m.expediteur_id = u.id
        WHERE m.destinataire_id = ? ORDER BY m.date DESC
    ''', (session['user_id'],)).fetchall()
    
    sent = conn.execute('''
        SELECT m.*, u.name as destinataire_name FROM messages m
        JOIN users u ON m.destinataire_id = u.id
        WHERE m.expediteur_id = ? ORDER BY m.date DESC
    ''', (session['user_id'],)).fetchall()
    
    return render_template('messages.html', received=received, sent=sent)

@app.route('/send_message/<int:dest_id>', methods=['GET', 'POST'])
def send_message(dest_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    conn = get_db()
    user = conn.execute('SELECT * FROM users WHERE id = ?', (session['user_id'],)).fetchone()
    
    if user['plan'] != 'premium':
        flash('La messagerie est réservée aux membres Premium!', 'error')
        return redirect(url_for('subscription'))
    
    if request.method == 'POST':
        from datetime import datetime
        contenu = request.form.get('contenu', '').strip()
        if contenu:
            conn.execute('INSERT INTO messages (expediteur_id, destinataire_id, contenu, date) VALUES (?, ?, ?, ?)',
                       (session['user_id'], dest_id, contenu, datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
            conn.commit()
            flash('Message envoyé avec succès!', 'success')
            return redirect(url_for('messages'))
    
    destinataire = conn.execute('SELECT * FROM users WHERE id = ?', (dest_id,)).fetchone()
    return render_template('send_message.html', destinataire=destinataire)

@app.route('/favoris')
def favoris():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    conn = get_db()
    user = conn.execute('SELECT * FROM users WHERE id = ?', (session['user_id'],)).fetchone()
    
    if user['plan'] != 'premium':
        flash('Les favoris sont réservés aux membres Premium!', 'error')
        return redirect(url_for('subscription'))
    
    favs = conn.execute('''
        SELECT u.*, f.date_ajout,
               COALESCE(AVG(a.note), 0) as note_moyenne,
               COUNT(a.id) as nb_avis
        FROM favoris f
        JOIN users u ON f.pro_id = u.id
        LEFT JOIN avis a ON u.id = a.pro_id
        WHERE f.client_id = ?
        GROUP BY u.id
        ORDER BY f.date_ajout DESC
    ''', (session['user_id'],)).fetchall()
    
    return render_template('favoris.html', favoris=favs)

@app.route('/add_favori/<int:pro_id>', methods=['POST'])
def add_favori(pro_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    conn = get_db()
    user = conn.execute('SELECT * FROM users WHERE id = ?', (session['user_id'],)).fetchone()
    
    if user['plan'] != 'premium':
        flash('Les favoris sont réservés aux membres Premium!', 'error')
        return redirect(url_for('subscription'))
    
    from datetime import datetime
    existing = conn.execute('SELECT * FROM favoris WHERE client_id = ? AND pro_id = ?', 
                          (session['user_id'], pro_id)).fetchone()
    
    if existing:
        conn.execute('DELETE FROM favoris WHERE client_id = ? AND pro_id = ?', 
                   (session['user_id'], pro_id))
        flash('Retiré des favoris', 'info')
    else:
        conn.execute('INSERT INTO favoris (client_id, pro_id, date_ajout) VALUES (?, ?, ?)',
                   (session['user_id'], pro_id, datetime.now().strftime('%Y-%m-%d')))
        flash('Ajouté aux favoris! ⭐', 'success')
    
    conn.commit()
    return redirect(request.referrer or url_for('view_professionals'))

@app.route('/logout')
def logout():
    session.clear()
    flash('Vous êtes déconnecté', 'info')
    return redirect(url_for('index'))

def init_db():
    conn = get_db()
    conn.executescript('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT, email TEXT, password TEXT, role TEXT, localisation TEXT, categorie TEXT
    );
    CREATE TABLE IF NOT EXISTS slots (
        id INTEGER PRIMARY KEY,
        pro_id INTEGER, date TEXT
    );
    CREATE TABLE IF NOT EXISTS rendezvous (
        id INTEGER PRIMARY KEY,
        pro_id INTEGER, client_id INTEGER, date TEXT
    );
    CREATE TABLE IF NOT EXISTS avis (
        id INTEGER PRIMARY KEY,
        pro_id INTEGER,
        client_id INTEGER,
        note INTEGER,
        commentaire TEXT,
        date TEXT,
        FOREIGN KEY (pro_id) REFERENCES users(id),
        FOREIGN KEY (client_id) REFERENCES users(id)
    );
    ''')
    try:
        conn.execute('ALTER TABLE users ADD COLUMN localisation TEXT')
        conn.commit()
    except:
        pass
    try:
        conn.execute('ALTER TABLE users ADD COLUMN categorie TEXT')
        conn.commit()
    except:
        pass

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
