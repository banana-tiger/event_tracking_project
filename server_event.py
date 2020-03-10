from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
    title = 'EVENT'
    return render_template('start_page.html', page_title=title)

if __name__ == '__main__':
    app.run(debug=True)