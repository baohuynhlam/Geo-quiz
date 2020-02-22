from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test_page():
    return render_template('test-page.html')

if __name__ == "__main__":
    app.run(debug=True, port=3000)