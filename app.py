from flask import Flask, render_template, request, send_from_directory
import os
import tempvalues

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

picFolder = os.path.join('static', 'images')
print(picFolder)
app.config['UPLOAD_FOLDER'] = picFolder
pic1 = os.path.join(app.config['UPLOAD_FOLDER'], 'leaf.png')
pic2 = os.path.join(app.config['UPLOAD_FOLDER'], 'leaf.png')

@app.route("/")
def index():
    return render_template('index.html', leaf_image=pic1, disease_image=pic2)

@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)

    for file in request.files.getlist("file"):
        print(file)
        print("{} is the file name".format(file.filename))
        filename = file.filename
        destination = "/".join([target, filename])
        print ("Accept incoming file:", filename)
        print ("Save it to:", destination)
        file.save(destination)

    return render_template("index.html", image_name=filename, identity=images.name, disease=images.disease, leaf_image=pic1, disease_image=pic2)

@app.route('/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)

app.run(debug=True)