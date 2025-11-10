import os
from flask import Flask, render_template, request
import task

app = Flask(__name__)

@app.route("/")
def hello():
    name = request.args.get('name', 'John doe')
    result = task.hello.delay(name)
    result.wait()
    return render_template('index.html', celery=result)