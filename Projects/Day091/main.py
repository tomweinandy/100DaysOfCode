"""
Day 91: Photo Color Extraction Website

Inspiration from http://www.coolphptools.com/color_extract#demo
"""
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import colorgram


# Convert rbg colors to hex
def rgb_to_hex(rgb):
    return '%02x%02x%02x' % rgb


# Extract colors from the jpg
def extract_colors(image, number_of_colors):
    color_list = []
    number_of_colors = int(number_of_colors)
    colors = colorgram.extract(image, number_of_colors)

    # Convert colors to a list of RGB values
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        hex = rgb_to_hex((r, g, b))
        proportion = round(color.proportion, 3)
        color_tuple = ((r, g, b), hex, proportion)
        color_list.append(color_tuple)

    return color_list


akira_colors = extract_colors('static/img/akira.jpg', 13)

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


# all Flask routes below
@app.route('/')
def home():
    return render_template("index.html", color_list=akira_colors, photo='akira.jpg')


# Display newly uploaded photo and color distribution
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['imgFile']
        filetype = file.filename.split('.')[1]
        new_filename = 'last_photo.' + filetype

        # Only saves most recently uploaded photo of that file type
        file.save(f'static/img/{new_filename}')

        n = request.form.get('num_results')
        color_list = extract_colors(file, n)
        return render_template("index.html", color_list=color_list, photo=new_filename)


if __name__ == '__main__':
    app.run(debug=True)
