import cv2
from PIL import Image
  
#Function to convert image to trasnparent
def convertImage(img):
    img = Image.open(img)
    img = img.convert("RGBA")
  
    datas = img.getdata()
  
    newData = []
  
    for item in datas:
        # print(item)
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
            # print(item)
  
    img.putdata(newData)
    img.save("./New.png", "PNG")
    print("Successful")
  


# Input image
input = cv2.imread('/Users/taisho/Desktop/Soyamax/TW_FN200/IMG_8095.png')

# Get input size
height, width = input.shape[:2]

# Desired "pixelated" size
w, h = (80, 80)

# Resize input to "pixelated" size
temp = cv2.resize(input, (w, h), interpolation=cv2.INTER_LINEAR)

# Initialize output image
output = cv2.resize(temp, (width, height), interpolation=cv2.INTER_NEAREST)



cv2.imshow('Input', input)
cv2.imshow('Output', output)
cv2.imwrite('/Users/taisho/Desktop/Soyamax/cheng.png', output)
img = '/Users/taisho/Desktop/Soyamax/cheng.png'
convertImage(img)
cv2.waitKey(0)