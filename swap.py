#importing class modu;e
import cmpt120image as cm

#this is the orginial picture
Originalimg = cm.getImage("bird.png")
#reveals the original picture for initial user interface
cm.showImage(Originalimg)

#First filter where i swaps the red and gree
def swapRedGreen(img):
    #NOT EDITING ON THE ORIGINAL IMAGE THIS FILTER IS APPLIED TO A NEW IMAGE
    img = cm.getImage("bird.png")
    #per pixel
    for row in range(len(img)):
        for col in range(len(img[0])):
            pixel = img[row][col]
            #saying red pixel is equal to green pixel and vice versa
            pixel[0], pixel[1] = pixel[1], pixel[0]
    #saving image
    cm.saveImage(img, "birdR&G")
    return img

#Second filter for black and white
def blackWhite(img):
    #NOT EDITING ON THE ORIGINAL IMAGE THIS FILTER IS APPLIED TO A NEW IMAGE
    img = cm.getImage("bird.png")
    for row in range(len(img)):
        for col in range(len(img[0])):
            pixel = img[row][col]
            #each independant RGB value
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            #sum of RGB values in a pixel
            sum = int((r + g + b))
            #white
            if sum > 384:
                img[row][col] = [255,255,255]
            #black
            else:
                img[row][col] = [0,0,0]
    cm.saveImage(img, "birdB&W.png")
    return img

#third filter to birghten image
def brighten(img):
    #look at the function parameter when called it shows that it's
    #NOT being EDITING ON THE ORIGINAL IMAGE THIS FILTER IS APPLIED TO A NEW IMAGE
    for row in range(len(img)):
        for col in range(len(img[0])):
            pixel = img[row][col]
            r = pixel[0]
            g = pixel[1]
            b = pixel[2]
            if r < 229 and g < 229 and b < 229:
                r = r*1.1
                g = g*1.1
                b = b*1.1
                img[row][col] = [r,g,b]
    cm.saveImage(img, "birdBright.png")
    return img

def reflect(img):
    #NOT EDITING ON THE ORIGINAL IMAGE THIS FILTER IS APPLIED TO A NEW IMAGE
    img = cm.getImage("bird.png")
    height = len(img)
    width = len(img[0])
    midpoint = height // 2
    #This is operating on anew image it is a black one
    imgBlack = cm.getBlackImage(width, height)
#Up side at the top like the movie
    for row in range(midpoint):
         for col in range(width):
            imgBlack[row][col] = img[row][col]
#down side at the bottom no movie
    for row in range(midpoint, height):
        for col in range(width):
            imgBlack[row][col] = img[height-row][col]
    cm.saveImage(imgBlack, "birdFlipped")
    return imgBlack

def reload(img):
    #Calling original Image
    Originalimg = cm.getImage("bird.png")
    cm.saveImage(img, "birdOriginal.png")
    return img
