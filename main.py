from PIL import Image
import numpy as np

def GenText(filename, mode = ""):

    if mode != "" and mode != "hd" and mode != "hdr":
        return "only mode hd, hdr and default are available"
    textimage = ""
    if mode == "hd":
        size = 16000
    else:
        size = 2000


    W = Image.open(f"image/{filename}").width
    H = Image.open(f"image/{filename}").height
    newW = 0
    newH = 0
    ratio = W/H
    while newW*newH <= size:
        W = newW
        H = newH
        newW += 1
        newH += ratio
    W -= W%2
    H -= H%4
    H = int(H)

    imageRaw = Image.open(f"image/{filename}").resize((W, H))
    image = np.asarray(imageRaw)



    def dark(color):
        if np.average(color) < 128:
            return True
        else:
            return False


    #work in progress
    if mode == "hd":
        i = 0
        while i < len(image):
            j = 0
            while j < len(image[0]):
                x = 0x2800
                if not dark(image[i][j]):
                    x += 0x1
                if not dark(image[i+1][j]):
                    x += 0x2
                if not dark(image[i+2][j]):
                    x += 0x4
                if not dark(image[i+3][j]):
                    x += 0x40
                if not dark(image[i][j+1]):
                    x += 0x8
                if not dark(image[i+1][j+1]):
                    x += 0x10
                if not dark(image[i+2][j+1]):
                    x += 0x20
                if not dark(image[i+3][j+1]):
                    x += 0x80
                if x == 0x2800:
                    for x in range(3):
                        textimage += chr(0x2005)
                else:
                    textimage += chr(x)
                j += 2
            textimage += "\n"
            i += 4
    else:
        for i in range(len(image)):
            for j in range(len(image[0])):
                pixelColor = np.average(image[i][j])
                if mode == "hdr":
                    if pixelColor < 28:
                        textimage += u"\u2800"
                    elif pixelColor < 56:
                        textimage += u"\u2802"
                    elif pixelColor < 84:
                        textimage += u"\u2842"
                    elif pixelColor < 112:
                        textimage += u"\u2826"
                    elif pixelColor < 140:
                        textimage += u"\u2866"
                    elif pixelColor < 168:
                        textimage += u"\u2867"
                    elif pixelColor < 196:
                        textimage += u"\u28e7"
                    elif pixelColor < 224:
                        textimage += u"\u28f7"
                    else:
                        textimage += u"\u28ff"
                else:
                    if dark(pixelColor):
                        textimage += "1"
                    else:
                        textimage += "0"
            textimage += "\n"
    return textimage


print(GenText("test.png", "hd"))
