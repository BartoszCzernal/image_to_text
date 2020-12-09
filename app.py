import pytesseract
from PIL import Image
from flask import Flask, render_template, flash, request


app = Flask(__name__)
app.secret_key = 'dummy'


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "GET":
        return render_template('index.html')
    else:
        if 'myfile' not in request.files:
            flash('No file found')
            return render_template('index.html')
        file = request.files['myfile']
        if file.filename == '':
            flash('No selected file')
            return render_template('index.html')
        else:
            img = Image.open(file)
            text = pytesseract.image_to_string(img)
            return render_template('answer.html', params={'answer': text})


if __name__ == '__main__':

    app.config['SESSION_TYPE'] = 'filesystem'

    app.debug = True
    app.run()
