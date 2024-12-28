from flask import Flask, render_template, request
from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return 'No file part'
    image_file = request.files['image']
    if image_file.filename == '':
        return 'No selected file'
    if image_file:
        # Save the uploaded image to a temporary file
        image_path = 'temp_image.jpg'  # You can choose your file extension here
        image_file.save(image_path)
        
        # Process the uploaded image using your trained model
        result = process_image(image_path)
        
        # Optionally, remove the temporary image file
        # os.remove(image_path)
        
        # Redirect to a new page with the result
        return redirect(url_for('result', result=result))

@app.route('/result')
def result():
    result = request.args.get('result')
    return render_template('result.html', result=result)

def process_image(image_path):
    # Here, you would load the trained model and perform inference on the uploaded image
    # Replace this with your actual code to load the model and make predictions
    # For example:
    model = load_model('model.h5')
    result = model.predict(image_path)
    return result
    return 'Placeholder result'

if __name__ == '__main__':
    app.run(debug=True)
