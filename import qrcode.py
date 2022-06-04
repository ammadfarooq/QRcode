import qrcode
I = "https://www.youtube.com/watch?v=h_nukH6iPQU"
print("The QRcode is now saved ",I)


def generate(data, img_name="QRcode.png"):
    img = qrcode.make(data)
    img.save(img_name)
    return img

generate(I)

