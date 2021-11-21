from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    '''
    Flask automatically converts it to html for us to render it on browser.
    '''
    return 'Hello World!'


@app.route('/blog')
def blog():
    return "This is an area to write blog!!"


@app.route('/cafe')
def cafe():
    return render_template('index-1.html')


@app.route('/css/<file>')
def css_route(file):
    return render_template('css/%s' % file)


@app.route('/images/<file>')
def images_route(file):
    return render_template('images/%s' % file)


@app.route('/js/<file>')
def js_route(file):
    return render_template('js/%s' % file)


@app.route('/bat/<file>')
def bat_route(file):
    return render_template('bat/%s' % file)


if '__name__' == '__main__':
    app.run(debug=True)
