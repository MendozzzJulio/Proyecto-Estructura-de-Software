import qrcode

url = "https://drive.google.com/file/d/1YHRvki6i10HaZBc3Pslm6SjGap9KFq5x/view?usp=sharing"

qr = qrcode.QRCode(
    version=1,
    box_size=25,
    border=4
)
qr.add_data(url)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="lightblue")
img.save("qrcode.png")

