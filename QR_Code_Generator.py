import qrcode as qr
img= qr.make("https://youtu.be/sCOw5y1RQpY")
img.save("YouTube_QR.png")          #It autmatacally create a qr code in your existing path after run this

