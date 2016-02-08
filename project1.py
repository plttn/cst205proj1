folder = "/images/"

pictures = []

image1 = makePicture(folder+"1.png")
pictures.append(image1)
image2 = makePicture(folder+"2.png")
pictures.append(image2)
image3 = makePicture(folder+"3.png")
pictures.append(image3)
image4 = makePicture(folder+"4.png")
pictures.append(image4)
image5 = makePicture(folder+"5.png")
pictures.append(image5)
image6 = makePicture(folder+"6.png")
pictures.append(image6)
image7 = makePicture(folder+"7.png")
pictures.append(image7)
image8 = makePicture(folder+"8.png")
pictures.append(image8)
image9 = makePicture(folder+"9.png")
pictures.append(image9)

for x in range(0, width):
    for y in range(0,height):

        # we have nine images
        for imageNumber in range(0,9):

            #JES getPixel function takes as input a picture object and coordinate pair

            pixel = getPixel(pictures[imageNumber], x, y)

            red = getRed(pixel)
            green = getGreen(pixel)
            blue = getBlue(pixel)

            redPixelList.append(red)
            greenPixelList.append(green)
            bluePixelList.append(blue)
