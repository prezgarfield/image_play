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
        for fname in imlist[i*numSlices:(i*numSlices)+numSlices]:
            images.append([numpy.array(Image.open(str(pth)+ '/'+fname))])
        i = i+1
    i = 0
    while i < numSlices:
        slices.append(images[i*numSlices:(i*numSlices)+numSlices])
        print(slices[i])
        i = i + 1
    # Alternative method using numpy median function
    #return
    #images = numpy.array([numpy.array(Image.open(str(pth) + '/' + fname)) for fname in imlist])

    imgSlices = []

    #     print(numSlices)
    # print(len(slices))
    # print(slices[numSlices-1])
    arr = []
    for slc in slices:
        arr = numpy.array(numpy.median(slc, axis=(0)), dtype=numpy.uint8)
        imgSlices.append(arr)
    out = Image.fromarray(arr)
    #out.save('test.jpg')
    out.show()
    return
    for slc in imgSlices:
        arr = numpy.array(numpy.median(slc, axis=(0)), dtype=numpy.uint8)
    out = Image.fromarray(arr)
    out.save("median.jpg")
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
    #getVidCap('driveclip1.mp4')
    #AveragePixels2(setpath('data'))
    MedianPixels3(setpath('data'), 25)
    exit()
