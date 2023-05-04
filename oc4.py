from flask import Flask, render_template, request
import cv2
import pytesseract
import re

app = Flask(__name__)

# Define regular expressions for name and birthdate
name_regex = r"([A-Za-z]+\s[A-Za-z]+)"
birthdate_regex = r"DOB:\s+(\d{2}/\d{2}/\d{4})"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/results', methods=['POST'])
def results():
    if request.method == 'POST':
        # Get the uploaded image file
        image_file = request.files['image']

        # Read the image file using OpenCV
        img = cv2.imdecode(np.frombuffer(image_file.read(), np.uint8), cv2.IMREAD_COLOR)

        # Perform OCR on the image using pytesseract
        ocr_text = pytesseract.image_to_string(img)

        # Pass the OCR text to the results template
        return render_template('results.html', ocr_text=ocr_text)

@app.route('/filtered_results', methods=['POST'])
def filtered_results():
    # Get the OCR text from the form data
    ocr_text = request.form['ocr_text']

    # Search for name and birthdate in the OCR text
    name_match = re.search(name_regex, ocr_text)
    birthdate_match = re.search(birthdate_regex, ocr_text)

    # Extract the name and birthdate from the matches
    name = name_match.group(1) if name_match else None
    birthdate = birthdate_match.group(1) if birthdate_match else None

    # Pass the extracted name and birthdate to the filtered results template
    return render_template('filtered_results.html', name=name, birthdate=birthdate)

if __name__ == '__main__':
    app.run(debug=True)
