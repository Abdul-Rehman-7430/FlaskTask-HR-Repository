
from flask import Flask, redirect, url_for, request, render_template,make_response, send_file,jsonify
import nltk
import spacy

app = Flask(__name__)
@app.route('/')
def index():
    return ("--Hello word--")



if __name__ == '__main__':
    app.run()
