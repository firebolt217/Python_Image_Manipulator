#Hasan Merchant
#March 24th 2021
#Image Processor

#Importing all six modules
import cmpt120image as cm
import swap
#this is the Original image
Originalimg = cm.getImage("bird.png")
cm.showImage(Originalimg)

#User interface
print("\n1: Swap red and green \
\n2: Convert to black and white\
\n3: Reflect\
\n4: Brighten\
\n5: Reload Image\
\n0: Quit")

#While loops so user interface persists
looping = True
while looping:
    continue_looping = True
    while (continue_looping):
        Iu = int(input("Enter 1 to 5, 0 to quit: "))
        if (Iu == 1 or Iu == 2 or Iu == 3 or Iu == 4 or Iu == 5 or Iu == 0 ):
            continue_looping = False
    #Calling from the other module: Swap that has all function parameter
    if Iu == 1:
        swap.swapRedGreen(Originalimg)
        #Using return Value
        cm.showImage(swap.swapRedGreen(Originalimg))#call the function
    if Iu == 2:
        swap.blackWhite(Originalimg)
        cm.showImage(swap.blackWhite(Originalimg))
        #call the functio1
    if Iu == 3:
        swap.reflect(Originalimg)
        cm.showImage(swap.reflect(Originalimg))
    if Iu == 4:
        swap.brighten(Originalimg)
        cm.showImage(swap.brighten(Originalimg))
    if Iu == 5:
        #ANOTHER Orignial PIC - I better not lose marks for not using orignal pic BECAUSE I HAVE
        OGpic = cm.getImage("bird.png")
        swap.reload(OGpic)
        cm.showImage(swap.reload(OGpic))
    if Iu == 0:
        looping = False




