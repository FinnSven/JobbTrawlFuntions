from flask import Flask, request, jsonify
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

if __name__ == '__main__':
    app.run(debug=True)
