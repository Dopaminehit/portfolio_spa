# Copyright (c) 2023 Dopamine Inc.
# All rights reserved.  See https://{placeholder_for_url}.

"""Single Page Flask App."""

from flask import Flask,render_template, send_from_directory
from flask_cors import CORS
from pathlib import Path

app = Flask(__name__)
CORS(app)
content_file = Path(__file__).resolve().parent /"static/about.txt"


@app.route('/')
def home():
    return render_template('base.html')

@app.route('/about')
def about():
    with open(content_file, 'r') as file:
        content = file.read()
        print(content)
    return render_template('about.html', content=content)
    
@app.route('/resume')
def resume():
    return render_template('resume.html')
    
@app.route('/cover-letter')
def cover_letter():
    return render_template('cover_letter.html')

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5001, debug=True)
