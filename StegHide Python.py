import cv2
import os

# Read the image
img = cv2.imread("target.jpg")  # Replace with the correct image path

# Get the secret message and passcode from the user
msg = input("Enter secret message:  ")
password = input("Enter a passcode:  ")

# Create dictionaries for mapping characters to integers and vice versa
d = {}
c = {}

# Populate the dictionaries
for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

# Variables for iterating through the image
m = 0
n = 0
z = 0

# Encrypt the secret message in the image
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

# Save the encrypted image
cv2.imwrite("encryptedImage.jpg", img)

# Open the encrypted image
os.system("start encryptedImage.jpg")  # Use 'start' to open the image on Windows

# Variables for decrypting the message from the image
message = ""
n = 0
m = 0
z = 0

# Get the passcode for decryption
pas = input("Enter passcode for Decryption:  ")

# Check if the passcode is correct
if password == pas:
    # Decrypt the message from the image
    for i in range(len(msg)):
        message = message + c[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    print("Decryption message:", message)
else:
    print("YOU ARE NOT auth")
