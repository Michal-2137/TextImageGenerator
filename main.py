from PIL import Image
import numpy as np

def GenText(mode = ""):

    if mode != "" and mode != "hd" and mode != "hdr":
        return "only mode hd, hdr and default are available"

    textimage = ""
    image = np.asarray(Image.open("image/test.png"))

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
                if dark(image[i][j]):
                    x += 0x1
                if dark(image[i+1][j]):
                    x += 0x2
                if dark(image[i+2][j]):
                    x += 0x4
                if dark(image[i+3][j]):
                    x += 0x40
                if dark(image[i][j+1]):
                    x += 0x8
                if dark(image[i+1][j+1]):
                    x += 0x10
                if dark(image[i+2][j+1]):
                    x += 0x20
                if dark(image[i+3][j+1]):
                    x += 0x80
                print(chr(x))
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


print(GenText("hd"))