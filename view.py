from flask import render_template, url_for, request, jsonify
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


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/api/<sentence>', methods = ['GET'])
def get_styled(sentence):
    output = stylish(sentence)
    response = {
        'origin': sentence,
        'styled': output
    }
    return jsonify(response)