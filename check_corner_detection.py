import cv2 as cv

# For a 7x5 chessboard
internalCornersX = 6
internalCornersY = 4

jpgImgPath = '/home/pi/Mau/calibration/captured_images/captured_image_1.jpg'

imgBGR = cv.imread(jpgImgPath)
imgGray = cv.cvtColor(imgBGR, cv.COLOR_BGR2GRAY)
cornersFound, cornersOrg = cv.findChessboardCorners(imgGray, (internalCornersY, internalCornersX), None)
if cornersFound:
    print("Corners found!")
    cv.drawChessboardCorners(imgBGR, (internalCornersY, internalCornersX), cornersOrg, cornersFound)
    cv.imshow('Chessboard', imgBGR)
    cv.waitKey(0)  # Press any key to close
else:
    print("Corners not found.")
