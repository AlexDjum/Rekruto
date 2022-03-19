from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def rekruto_page():
    name = request.args.get('name')
    message = request.args.get('message')
    return render_template('rekruto.html', name=name, message=message)

app.run(debug=True)
