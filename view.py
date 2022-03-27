from flask import render_template, url_for, request, jsonify, session, redirect
from app import app
from external_scripts.jap import stylish

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        history = session.get('history')
        return render_template('index.html', history=history)
    elif request.method == 'POST':
        raw = request.form.get('raw_text')
        output = stylish(raw)
        if session.get('history') is not None:
            history = session['history']
            history.append((raw, output))
            session['history'] = history
        else:
            session['history'] = [(raw, output)]
            history = session['history']
        return render_template('index.html', output=output, history=history)

@app.route('/clear')
def clear_session():
    del session['history']
    return redirect(url_for('index'))


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
    