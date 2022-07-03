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


    # work in progress
    # if mode == "hd":
    #     i = 0
    #     while i < len(image):
    #             j = 0
    #             while j < len(image[0]):
    #                 if dark(image[i][j]):


    if True:
        for i in range(len(image)):
            for j in range(len(image[0])):
                pixelColor = dark(image[i][j])
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
                    if pixelColor < 128:
                        textimage += "1"
                    else:
                        textimage += "0"
            textimage += "\n"
    return textimage
print(GenText("hd"))