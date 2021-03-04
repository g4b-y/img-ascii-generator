import sys, random, argparse, math
import numpy as np
# import PIL as pillow
from PIL import Image
# from Pillow import Image

# Set grayscale values - 70 levels
gscale1 = '$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`.'
# gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "

# Set grayscale values - 10 levels
gscale2 = 'MX@%8#/*+=-:. '
# gscale2 = 'MXCI+\:-,.  '

"""
Given PIL Image, return average value of grayscale value
"""
def getAverageL(image):
    im = np.array(image) # get image as numpy array
    w, h = im.shape  # get shape
    return np.average(im.reshape(w * h)) # get average

"""
Given Image and dimensions (rows, cols) returns an m*n list of Images
"""
def covertImageToAscii(fileName, cols, scale, moreLevels):
    global gscale1, gscale2 # declare globals

    image = Image.open(fileName).convert('L') # open image and convert to grayscale
    W, H = image.size[0], image.size[1]  # store dimensions
    print("input image dims: %d x %d" % (W, H))

""" 
Given Image and dimensions (rows, cols) returns an m*n list of Images  
""" 
def convertImageToAscii(fileName, cols, scale, moreLevels): 
    global gscale1, gscale2 # declare globals 
  
    image = Image.open(fileName).convert('L') # open image and convert to grayscale 
    W, H = image.size[0], image.size[1]  # store dimensions 
    print("input image dims: %d x %d" % (W, H)) 
    
    w = W / cols # calculate tile width
    h = w / scale # calculate tile height based on aspect ratio and scale
    rows = int(H / h) # calculate number of rows

    print("cols: %d, rows: %d" % (cols, rows))
    print("tile dims: %d x %d" % (w, h))

    # check if image size is too small
    if cols > W or rows > H:
        print("Image too small for specified cols!")
        exit(0)

    aimg = [] # ascii image is a list of character strings

    # generate list of dimensions
    for j in range(rows):
        y1 = int(j * h)
        y2 = int((j + 1) * h)

        if j == rows-1: # Correct last tile
            y2 = H

        aimg.append("") # Append an empty string

        for i in range(cols):
            x1 = int(i * w) # Crop image to tile
            x2 = int((i + 1) * w)

            if i == cols-1: # Correct last tile
                x2 = W

            img = image.crop((x1, y1, x2, y2)) # Crop image to extract tile
            avg = int(getAverageL(img)) # Get average luminance

            # Look up ascii char
            if moreLevels:
                gsval = gscale1[int((avg*69)/255)]
            else:
                gsval = gscale2[int((avg*9)/255)]

            aimg[j] += gsval # Append ascii char to string

    return aimg # Return txt image

# Parse arguments and set variables
def parseArgs():
    args = parser.parse_args()
    imgFile = args.imgFile

    outFile = 'out.txt' # Set output file
    if args.outFile:
        outFile = args.outFile

    scale = 0.5 # Set scale default as 0.5
    if args.scale:
        scale = float(args.scale)

    cols = 80 # Set cols
    if args.cols: 
        cols = int(args.cols) 
  
    print('Generating ASCII art...') 
    # Convert image to ascii txt 
    aimg = convertImageToAscii(imgFile, cols, scale, args.moreLevels) 
  
    # Open file 
    f = open(outFile, 'w') 
  
    # Write to file 
    for row in aimg: 
        f.write(row + '\n') 
  
    # End process 
    f.close() 
    print("ASCII art written to %s" % outFile) 
  
    print('Generating ASCII art...')

    # Convert image to ascii txt
    aimg = covertImageToAscii(imgFile, cols, scale, args.moreLevels)

    # Open file
    f = open(outFile, 'w')

    # Write to file
    for row in aimg:
        f.write(row + '\n')

    # End process
    f.close()
    print("ASCII art written to %s" % outFile)


if __name__ == '__main__':
    main()
