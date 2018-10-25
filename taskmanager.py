from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route("/")
def show_hi():
    return "hi"

    
    
    

if __name__ == "__main__":
        app.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)