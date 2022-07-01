import cv2
import numpy as np

# Read image
path_name = '/Users/taisho/Desktop/Soyamax/'
file_name = '101.jpg'
img = cv2.imread(path_name + file_name)
cv2.imshow("image", img)
hh,ww = img.shape[:2]

# threshold on white
# Define lower and uppper limits
lower = np.array([90, 90, 90])
upper = np.array([255, 255, 255])

# Create mask to only select black
thresh = cv2.inRange(img, lower, upper)

# apply morphology
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (1,1))
morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# invert morp image
mask = 255 - morph

# apply mask to image
result = cv2.bitwise_and(img, img, mask=mask)



# save results
cv2.imshow("img", img)
cv2.imwrite(('/Users/taisho/Desktop/Soyamax/'+ str(file_name) +'thresh.png'), thresh)
cv2.imwrite(('/Users/taisho/Desktop/Soyamax/' + file_name+'pills_morph.png'), morph)
cv2.imwrite('/Users/taisho/Desktop/Soyamax/pills_mask.png', mask)
cv2.imwrite('/Users/taisho/Desktop/Soyamax/pills_result.png', result)
print("???")

cv2.imshow('thresh', thresh)
cv2.imshow('morph', morph)
cv2.imshow('mask', mask)
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
