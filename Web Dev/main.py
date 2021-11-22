from flask import Flask, render_template, send_file, redirect, url_for

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
    return render_template('index.html')


# @app.route('/css/<file>')
# def css_route(file):
#     return render_template('css/%s' % file)
# # Done wrong way


@app.route('/images/<file>')
def images_route(file):
    return send_file('static/images/%s' % file)


@app.route('/js/<file>')
def js_route(file):
    return render_template('/js/%s' % file)
# # Done Wrong way


@app.route('/bat/<file>')
def bat_route(file):
    return render_template('bat/%s' % file)


@app.route('/index.html')
def index_route():
    return render_template('index.html')


@app.route('/index-1.html')
def index1_route():
    return render_template('index-1.html')


@app.route('/index-2.html')
def index2_route():
    return render_template('index-2.html')


@app.route('/index-3.html')
def index3_route():
    return render_template('index-3.html')


@app.route('/index-4.html')
def index4_route():
    return render_template('index-4.html')


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
