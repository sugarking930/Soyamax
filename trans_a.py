from PIL import Image
  
def convertImage():
    img = Image.open("/Users/taisho/Desktop/Soyamax/Res/thresh.png")
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
    img.save("/Users/taisho/Desktop/Soyamax/Res/New.png", "PNG")
    print("Successful")

convertImage()
  