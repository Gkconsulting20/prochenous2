from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'secret'

def get_db():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        conn = get_db()
        conn.execute('INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)',
                     (request.form['name'], request.form['email'], request.form['password'], request.form['role']))
        conn.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        conn = get_db()
        user = conn.execute('SELECT * FROM users WHERE email = ? AND password = ?',
                            (request.form['email'], request.form['password'])).fetchone()
        if user:
            session['user_id'] = user['id']
            session['role'] = user['role']
            return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session: return redirect(url_for('login'))
    conn = get_db()
    user = conn.execute('SELECT * FROM users WHERE id = ?', (session['user_id'],)).fetchone()
    if user['role'] == 'pro':
        rdvs = conn.execute('''
            SELECT r.date, u.name as client FROM rendezvous r
            JOIN users u ON r.client_id = u.id WHERE r.pro_id = ?
        ''', (user['id'],)).fetchall()
        return render_template('dashboard_pro.html', user=user, rdvs=rdvs)
    return render_template('dashboard_user.html', user=user)

@app.route('/professionals')
def view_professionals():
    conn = get_db()
    pros = conn.execute("SELECT * FROM users WHERE role = 'pro'").fetchall()
    return render_template('professionals.html', professionals=pros)

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

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

def init_db():
    conn = get_db()
    conn.executescript('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT, email TEXT, password TEXT, role TEXT
    );
    CREATE TABLE IF NOT EXISTS slots (
        id INTEGER PRIMARY KEY,
        pro_id INTEGER, date TEXT
    );
    CREATE TABLE IF NOT EXISTS rendezvous (
        id INTEGER PRIMARY KEY,
        pro_id INTEGER, client_id INTEGER, date TEXT
    );
    ''')
    conn.commit()

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
