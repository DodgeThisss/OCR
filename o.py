import cv2
import pytesseract

# Load the image and convert it to grayscale
img = cv2.imread('paper.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding to the image
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# Apply dilation to the image
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2))
dilate = cv2.dilate(thresh, kernel, iterations=2)

# Apply OCR using pytesseract
text = pytesseract.image_to_string(dilate)

# Filter the results by name and DOB
name = "John Doe"
dob = "01/01/2000"
if name in text and dob in text:
    print("Name and DOB found in the text!")
else:
    print("Name and/or DOB not found in the text.")
