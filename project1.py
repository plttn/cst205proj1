for x in range(0, width):
	for y in range(0,height):

	# we have nine images
	for imageNumber in range(0,9)

	#JES getPixel function takes as input a picture object and coordinate pair

	pixel = getPixel(pictures[imageNumber], x, y)

	red = getRed(pixel)
	green = getGreen(pixel)
	blue = getBlue(pixel)

	redPixelList.append(red)
	greenPixelList.append(green)
	bluePixelList.append(blue)
