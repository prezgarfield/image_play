#note: PIL is no longer maintained.  You need to load the Pillow library, forked from the original PIL.
import os, numpy, PIL, cv2
from PIL import Image
from pathlib import Path

def amIrunning():
    print("Starting Program")

def getVidCap(fname):
    # Playing video from file:
    cap = cv2.VideoCapture(fname)

    try:
        if not os.path.exists('data'):
            os.makedirs('data')
    except OSError:
        print('Error: Creating directory of data')

    currentFrame = 0

    while (True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            break

        # Saves image of the current frame in jpg file
        name = './data/frame' + str(currentFrame) + '.jpg'
        print('Creating...' + name)
        cv2.imwrite(name, frame)

        # To stop duplicate images
        currentFrame += 1

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

def MedianPixels3(pth, slice):
    #allfiles = os.listdir(os.getcwd())
    allfiles = os.listdir(pth)
    #print(pth)
    #print(allfiles)
    imlist = [filename for filename in allfiles if filename[-4:] in [".jpg"]]
    numSlices = int(len(imlist) / slice)
    # only process if we have enough images
    if not numSlices:
        return
    i = 0
    slices = []
    images = []
    while i < numSlices:
        print(i)
        for fname in imlist[i*numSlices:(i*numSlices)+numSlices-1]:
            images.append(numpy.array(Image.open(str(pth) + '/'+fname)))
        arr = numpy.array(numpy.median(images, axis=(0)), dtype=numpy.uint8)
        out = Image.fromarray(arr)
        try:
            if not os.path.exists('data/medianstaging'):
                os.makedirs('data/medianstaging')
        except OSError:
            print('Error: Creating directory of data')

        out.save('data/medianstaging/image'+ str(i)+'.jpg')
        images=[]
        #out.show()
        i = i+1

def MeanPixels3(pth, slice):
    #allfiles = os.listdir(os.getcwd())
    allfiles = os.listdir(pth)
    #print(pth)
    #print(allfiles)
    imlist = [filename for filename in allfiles if filename[-4:] in [".jpg"]]
    numSlices = int(len(imlist) / slice)
    # only process if we have enough images
    if not numSlices:
        return
    i = 0
    slices = []
    images = []
    while i < numSlices:
        print(i)
        for fname in imlist[i*numSlices:(i*numSlices)+numSlices-1]:
            images.append(numpy.array(Image.open(str(pth) + '/'+fname)))
        arr = numpy.array(numpy.mean(images, axis=(0)), dtype=numpy.uint8)
        out = Image.fromarray(arr)
        try:
            if not os.path.exists('data/meanstaging'):
                os.makedirs('data/meanstaging')
        except OSError:
            print('Error: Creating directory of data')

        out.save('data/meanstaging/image'+ str(i)+'.jpg')
        images=[]
        #out.show()
        i = i+1


def medianComplete():
    newpath = setpath('data/medianstaging')
    allfiles = os.listdir(newpath)
    print(newpath)
    imlist = [filename for filename in allfiles if filename[-4:] in [".jpg"]]
    images = numpy.array([numpy.array(Image.open(str(newpath) + '/' + fname)) for fname in imlist])
    arr = numpy.array(numpy.median(images, axis=(0)), dtype=numpy.uint8)
    out = Image.fromarray(arr)
    out.save("median.jpg")
    out.show()

def meanComplete():
    newpath = setpath('data/meanstaging')
    allfiles = os.listdir(newpath)
    print(newpath)
    imlist = [filename for filename in allfiles if filename[-4:] in [".jpg"]]
    images = numpy.array([numpy.array(Image.open(str(newpath) + '/' + fname)) for fname in imlist])
    arr = numpy.array(numpy.mean(images, axis=(0)), dtype=numpy.uint8)
    out = Image.fromarray(arr)
    out.save("mean.jpg")
    out.show()

def AveragePixels2(pth):
    #allfiles = os.listdir(os.getcwd())
    allfiles = os.listdir(pth)
    print(allfiles)
    imlist = [filename for filename in allfiles if filename[-4:] in [".jpg"]]

    # Alternative method using numpy mean function
    images = numpy.array([numpy.array(Image.open(str(pth) + '/' + fname)) for fname in imlist])
    arr = numpy.array(numpy.mean(images, axis=(0)), dtype=numpy.uint8)
    out = Image.fromarray(arr)
    out.save("mean.jpg")
    out.show()

def AveragePixels(pth):
    # Access all jpg files in directory
    #pth = Path('data')

    allfiles=os.listdir(pth)
    print(allfiles)
    imlist=[filename for filename in allfiles if filename[-4:] in [".jpg"]]

    #AveragePixels2(imlist)

    avg = Image.open('data/'+ imlist[0])
    N = len(imlist)
    for i in range(1, N):
        img = Image.open('data/'+ imlist[i])
        avg = Image.blend(avg, img, 1.0 / float(i + 1))
    avg.save("Blend.jpg")
    avg.show()

def imageBlend():
    im1 = Image.open("3.jpg")
    im2 = Image.open("5.jpg")
    out = Image.blend(im1,im2,0.5)
    out.save("blend.jpg")
    out.show()


def setpath(pth):
    mypath = Path(pth)
    return mypath

if __name__ == '__main__':
    amIrunning()
    #getVidCap('OKGo1.mp4')
    #MeanPixels3(setpath('data'), 80)
    #MedianPixels3(setpath('data'), 80)
    medianComplete()
    meanComplete()
    #AveragePixels(setpath('data'))
    #imageBlend()
    exit()
