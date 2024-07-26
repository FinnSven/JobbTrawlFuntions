from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Dummy user data
users = {
    "admin": generate_password_hash("password")
}
from webscraper import search_websites

app = Flask(__name__)

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    urls = data.get('urls')
    search_term = data.get('search_term')
    
    if not urls or not search_term:
        return jsonify({"error": "URLs and search term are required"}), 400

    try:
        results = search_websites(urls, search_term)
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users and check_password_hash(users[username], password):
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Invalid Credentials')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/')
def index():
    if 'username' in session:
        return app.send_static_file('index.html')
    return redirect(url_for('login'))
    app.run(debug=True, host='0.0.0.0')
