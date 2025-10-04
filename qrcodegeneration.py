# since we are creating qr code we need to install qrcode and PIL
#pip install qrcode[pil]


import qrcode
from PIL import Image

data=input("Enter the data for QR code:")
qr=qrcode.QRCode(version=3,box_size=10,border=4)
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill='black',back_color='white')
img.save('qrcode.png')
img.show()
print("QR code generated successfully")