from flask import Flask, request, render_template, request, abort
import requests
from urllib.parse import urlparse

app = Flask(__name__)

def filter_flag(url):
    urlp = urlparse(url)
    urlloc = urlp.netloc.lower()
    if (urlloc.startswith('localhost') or urlloc.startswith('127') or urlloc.startswith('0') or urlloc.startswith('213')):
        return False
    if(url.endswith('flag')):
        return False
    else:
        return True

@app.route('/',methods=['GET','POST'])
def index():
    return render_template("index.html")

@app.route('/visit', methods=['GET','POST'])
def visit():
    if request.method == "GET":
        return render_template("visit.html")
    elif request.method == "POST":
        url = request.form.get("url", "")
        if not url:
            return render_template("visit.html", res="URL is required")
        
        elif filter_flag(url):
            try:
                # Send a POST request to the specified URL
                response = requests.post(url)

                # Get the response content
                response_content = response.text

                return render_template("visit.html", res=response_content[0:200])
            except requests.RequestException as e:
                return render_template("visit.html", error=f"Error during request: {str(e)}")
        else:
            return render_template("visit.html", res="filtered")

@app.route('/flag',methods=['POST'])
def flag():
    # Check if the request is coming from localhost
    if request.remote_addr != '127.0.0.1':
        abort(404)  # Return a 404 error if not from localhost

    return render_template("flag.html")

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8000)