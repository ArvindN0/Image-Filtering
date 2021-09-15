import matplotlib.pyplot as plt
import time
import copy
from skimage import io


def brighten(image, val):
    x, y, _ = image.shape
    for i in range(x):
        for j in range(y):
            image[i][j][0] = min(image[i][j][0] * val / 100, 255)
            image[i][j][1] = min(image[i][j][1] * val / 100, 255)
            image[i][j][2] = min(image[i][j][2] * val / 100, 255)


def tintTwds(image, r, g, b):
    x, y, _ = image.shape
    for i in range(x):
        for j in range(y):
            image[i][j][0] = (image[i][j][0] + r)/2
            image[i][j][1] = (image[i][j][0] + g)/2
            image[i][j][2] = (image[i][j][0] + b)/2


def blkWht(image):
    x, y, _ = image.shape
    if len(image[0][0]) == 3:
        for i in range(x):
            for j in range(y):
                r, g, b = image[i][j]
                r, g, b = (int(r) + int(g) + int(b)) / 3, \
                          (int(r) + int(g) + int(b)) / 3, \
                          (int(r) + int(g) + int(b)) / 3
                image[i][j] = r, g, b
    else:
        for i in range(x):
            for j in range(y):
                r, g, b, _ = image[i][j]
                r, g, b, _ = (int(r) + int(g) + int(b)) / 3, \
                          (int(r) + int(g) + int(b)) / 3, \
                          (int(r) + int(g) + int(b)) / 3, 255
                image[i][j] = r, g, b, 255


def contrast(image):
    x, y, _ = image.shape
    if len(image[0][0]) == 3:
        for i in range(x):
            for j in range(y):
                r, g, b = image[i][j]
                r, g, b = r**3, g**3, b**3
                image[i][j] = r/65025, g/65025, b/65025
    else:
        for i in range(x):
            for j in range(y):
                r, g, b, _ = image[i][j]
                r, g, b, _ = r**3, g**3, b**3, _
                image[i][j] = r/65025, g/65025, b/65025, 255


def blur(image):
    x, y, _ = image.shape
    if len(image[0][0]) == 3:
        for k in range (0, 3):
            imgCpy = copy.deepcopy(image)
            for a in range(1, x-1):
                for c in range(1, y-1):
                    rsum = bsum = gsum = 0
                    for i in range(a-1, a+2):
                        for j in range(c-1, c+2):
                            rsum += int(imgCpy[i, j][0])
                            gsum += int(imgCpy[i, j][1])
                            bsum += int(imgCpy[i, j][2])
                    image[a,c] = rsum/9, gsum/9, bsum/9
    else:
        for k in range (0, 3):
            imgCpy = copy.deepcopy(image)
            for a in range(1, x-1):
                for c in range(1, y-1):
                    rsum = bsum = gsum = 0
                    for i in range(a-1, a+2):
                        for j in range(c-1, c+2):
                            rsum += int(imgCpy[i, j][0])
                            gsum += int(imgCpy[i, j][1])
                            bsum += int(imgCpy[i, j][2])
                    image[a,c] = rsum/9, gsum/9, bsum/9, 255


def sharpen(image):
    imgCpy = copy.deepcopy(image)
    blur(imgCpy)
    x, y, _ = image.shape
    for i in range(x):
        for j in range(y):
            imgCpy[i, j] = image[i, j] - imgCpy[i,j]
    for i in range(x):
        for j in range(y):
            image[i, j] += imgCpy[i, j] * 2


def main():
    image = io.imread('shadesOfRed.png')
    print("Welcome to the image filter!")
    val = input("Type 'demo' for a walkthrough of our features \n")
    if (val == "demo"):
        image = io.imread('garfield.jpeg')
        print("This is our original image")
        plt.imshow(image)
        plt.show()

        contrast(image)
        print("And this is the same image with increased contrast")
        plt.imshow(image)
        plt.show()

        image = io.imread('garfield.jpeg')
        brighten(image, 150)
        print("And here with increased brightness")
        plt.imshow(image)
        plt.show()

        image = io.imread('garfield.jpeg')
        blur(image)
        print("This is the image blurred!")
        plt.imshow(image)
        plt.show()
        time.sleep(5)

        print("Let's switch to another picture to check out the sharpen effect")
        time.sleep(2)
        image = io.imread('woman.png')
        print("This is the original image:")
        plt.imshow(image)
        plt.show()

        sharpen(image)
        print("And this is the sharpened image:")
        plt.imshow(image)
        plt.show()
        time.sleep(5)

        print("Let's look at one more picture")
        image = io.imread('classroom.png')
        print("This is the original image:")
        plt.imshow(image)
        plt.show()
        time.sleep(3)

        blkWht(image)
        print("And this is the image in black and white image:")
        plt.imshow(image)
        plt.show()
        time.sleep(3)


        print("We can tint this image to different colors using our desired RGB values")
        image = io.imread('classroom.png')
        time.sleep(3)
        tintTwds(image, 255, 50, 50)
        print("This is the result of tinting the image towards the RGB value 255, 50, 50")
        plt.imshow(image)
        plt.show()

        time.sleep(5)
        print("\n\nYou can now use any of these filters in any order! \nTo access the commands, type 'help' and to exit the program type 'quit'\n")

    while True:
        val = input("Enter your command:\n")
        if val == "quit":
            break
        elif val == "sharpen":
            sharpen(image)
            plt.imshow(image)
            plt.show()
        elif val == "blur":
            blur(image)
            plt.imshow(image)
            plt.show()
        elif val == "contrast":
            contrast(image)
            plt.imshow(image)
            plt.show()
        elif val == "bw":
            blkWht(image)
            plt.imshow(image)
            plt.show()
        elif val == "brighten":
            br = int(input("Enter your desired brightness on a scale from 0-100\n"))
            brighten(image, 100 + br)
            plt.imshow(image)
            plt.show()
        elif val == "tint":
            R = int(input("Enter the Red value of the color you wish to tint your image towards\n"))
            G = int(input("Enter the Green value of the color you wish to tint your image towards\n"))
            B = int(input("Enter the Blue value of the color you wish to tint your image towards\n"))
            tintTwds(image, R, G, B)
            plt.imshow(image)
            plt.show()
        elif val == "print":
            plt.imshow(image)
            plt.show()
        elif val == "help":
            print("Valid commands: brighten, print, tint, bw, contrast, blur, sharpen, quit")
        else:
            print("Unrecognized command")
            print("Valid commands: brighten, print, tint, bw, contrast, blur, sharpen, quit")

main()