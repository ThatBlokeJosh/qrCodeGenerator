import qrcode


print("Welcome to QR Code Generator")

qr_name = input("Enter a valid URL: ")

img = qrcode.make(qr_name)

type(img)

image_name = input("Enter a name for the image: ")

valid_formats = ['png', 'jpg', 'jpeg', 'bmp', 'gif']

format = input("Enter a valid format: ").lower()

if format in valid_formats:
    img.save(f"{image_name}.{format}")
else:
    print("Invalid format")
