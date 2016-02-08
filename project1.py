folder = "/Users/jack/Github/cst205proj1/images/"

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

width = getWidth(image1)
height = getHeight(image1)

newImage = makeEmptyPicture(width, height)

redPixelList = []
greenPixelList = []
bluePixelList = []


def median(list): #https://stackoverflow.com/questions/24101524/finding-median-of-list-in-python
    sortedList = sorted(list)
    listLength = len(list)
    indexMedian = (listLength - 1) // 2

    if (listLength % 2):
        return sortedList[indexMedian]
    else:
        return (sortedList[indexMedian] + sortedList[indexMedian+1]) / 2.0


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

        # calculate median pixel
        medianRed = median(redPixelList)
        medianGreen = median(greenPixelList)
        medianBlue = median(bluePixelList)

        #this is the median pixel now
        medianColor = makeColor(medianRed, medianGreen, medianBlue)

        #get pixel from empty image
        currentNewPixel = getPixel(newImage, x, y)

        #set color of pixel
        setColor(currentNewPixel, medianColor)
        del redPixelList[:]
        del greenPixelList[:]
        del bluePixelList[:]

writePictureTo(newImage, folder+"output.png")
