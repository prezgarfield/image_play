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
    while (currentFrame < 350):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Saves image of the current frame in jpg file
        name = './data/frame' + str(currentFrame) + '.jpg'
        print('Creating...' + name)
        cv2.imwrite(name, frame)

        # To stop duplicate images
        currentFrame += 1

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

def MedianPixels3(pth):

    allfiles = os.listdir(os.getcwd())
    #allfiles = os.listdir(pth)
    print(allfiles)
    imlist = [filename for filename in allfiles if filename[-4:] in [".jpg"]]

    # Alternative method using numpy mean function
    images = numpy.array([numpy.array(Image.open(fname)) for fname in imlist])
    arr = numpy.array(numpy.median(images, axis=(0)), dtype=numpy.uint8)
    out = Image.fromarray(arr)
    out.save("median.jpg")
    out.show()

def AveragePixels2(pth):
    allfiles = os.listdir(os.getcwd())
    print(allfiles)
    imlist = [filename for filename in allfiles if filename[-4:] in [".jpg"]]

    # Alternative method using numpy mean function
    images = numpy.array([numpy.array(Image.open(fname)) for fname in imlist])
    arr = numpy.array(numpy.mean(images, axis=(0)), dtype=numpy.uint8)
    out = Image.fromarray(arr)
    out.save("mean.jpg")
    out.show()

def AveragePixels(pth):
    # Access all jpg files in directory
    pth = Path('data')

    allfiles=os.listdir(os.getcwd())
    print(allfiles)
    imlist=[filename for filename in allfiles if filename[-4:] in [".jpg"]]

    AveragePixels2(imlist)

    avg = Image.open(imlist[0])
    N = len(imlist)
    for i in range(1, N):
        img = Image.open(imlist[i])
        avg = Image.blend(avg, img, 1.0 / float(i + 1))
    avg.save("Blend.png")
    avg.show()

def setpath(pth):
    mypath = Path(pth)
    return mypath

if __name__ == '__main__':
    amIrunning()
    AveragePixels2(setpath('data'))
    #MedianPixels3(setpath('data'))
    #getVidCap('driveclip1.mp4')
    exit()
