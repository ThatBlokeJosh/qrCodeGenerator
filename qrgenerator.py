import qrcode # Import the qrcode library


print("Welcome to QR Code Generator")

qr_name = input("Enter a valid URL: ") 

img = qrcode.make(qr_name) # Make a qr code from the qr_name variable

type(img)

image_name = input("Enter a name for the image: ")

valid_formats = ['png', 'jpg', 'jpeg', 'bmp', 'gif']

format = input("Enter a valid format: ").lower()

if format in valid_formats:
    img.save(f"{image_name}.{format}") # Create the image
else:
    print("Invalid format")
