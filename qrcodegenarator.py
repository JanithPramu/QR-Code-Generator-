import qrcode  # Only import the necessary library

# Create an instance of QRCode
qr = qrcode.QRCode(
    version=15,  # QR code version
    box_size=10,  # Size of each box in the QR code grid
    border=5  # Thickness of the border (minimum is 4)
)

# Data to be encoded in the QR code
data = "https://github.com/JanithPramu"

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)  # Make the QR code fit the data

# Create the image for the QR code
img = qr.make_image(fill="black", back_color="white")

# Save the QR code image
img.save("test.png")
