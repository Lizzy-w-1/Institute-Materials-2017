from flask import Flask
from flask import render_template
from flask import request

defaults = { 'title': 'dynamic request header index.html' ,
             'header': 'Default "header" is used. Give request parameter header with a value to change it.',
             'paragraph': 'This is index.html with dynamic contents in response to a request for / (ROOT) in flask-request.py'
}

app = Flask(__name__)
@app.route("/")
def get_my_index():
    header = get_request_value_with_fallback('header')
    values = {
        'title': defaults['title'],
        'header': header,
        'paragraph': defaults['paragraph'] 
    }
    return render_template("index-dyn-dict.html", dict=values)

@app.route("/resource/<resource_name>")
def get_local_resource(resource_name = ''):
    return render_template("resource.html", resource_name=resource_name)

@app.route("/resource/<resource_name>/value/<value>")
def get_local_resource_with_value(resource_name = '', value = ''):
    return render_template("resource.html", resource_name=resource_name, value=value)

@app.route("/play/<play_code>")
def get_play(play_code = ''):
    return render_template("play.html", play_code=play_code)

#@app.route("/play/<play_code>/character/<character>")
#def get_play_char(play_code = '', character = ''):  #these are default values, ie empty
#	return ("abc")
#   return render_template("resource.html", resource_name=resource_name, value=value)

def get_request_value_with_fallback(key):
    if request.args.get(key):
        return request.args.get(key)
    return defaults[key]

if __name__ == '__main__':
    app.run(port=5000, debug=True)
