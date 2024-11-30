from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
import os
from color_selector import get_color_percentages

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        return redirect(url_for('display_image', filename=file.filename))
    return redirect(request.url)


@app.route('/display/<filename>')
def display_image(filename):
    my_image = Image.open('static/uploads/' + filename)
    color_percentages = get_color_percentages(my_image, 10)
    return render_template('display.html',
                           filename=filename, color_percentages=color_percentages)


if __name__ == '__main__':
    app.run(debug=True)
