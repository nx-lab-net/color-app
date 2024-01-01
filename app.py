from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('color.html')

@app.route('/color', methods=['POST'])
def change_color():
    color = request.form['color']
    return render_template('color.html', color=color)

if __name__ == '__main__':
    app.run()

