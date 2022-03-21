from flask import render_template, url_for, request
from app import app
from external_scripts.jap import stylish

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        raw = request.form.get('raw_text')
        output = stylish(raw)
        return render_template('index.html', output=output)
