import qrcode
phone_number=(input("enter you phone number and your name:"))
QR=qrcode.make(phone_number)
QR.save("frist-qrcode.png")