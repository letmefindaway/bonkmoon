from flask import Flask, render_template
import random

app = Flask(__name__)

# Sample list of memes related to "bonk"
memes = [
    "https://example.com/bonk1.jpg",
    "https://example.com/bonk2.jpg",
    "https://example.com/bonk3.jpg",
    "https://example.com/bonk4.jpg",
    "https://example.com/bonk5.jpg",
    "https://example.com/bonk6.jpg",
    "https://example.com/bonk7.jpg",
    "https://example.com/bonk8.jpg",
    "https://example.com/bonk9.jpg",
    "https://example.com/bonk10.jpg",
    "https://example.com/bonk11.jpg",
    "https://example.com/bonk12.jpg",
    "https://example.com/bonk13.jpg",
    "https://example.com/bonk14.jpg",
    "https://example.com/bonk15.jpg"
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/memes')
def memes_page():
    random_memes = random.sample(memes, 10)  # Select 10 random memes
    return render_template('memes.html', memes=random_memes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

