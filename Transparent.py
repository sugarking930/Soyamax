from PIL import Image
  
def convertImage(input_file: str):
    img = Image.open(input_file)
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
    img.save("/Users/taisho/Desktop/Soyamax/Res/"+ str(input_file) +".png", "PNG")
    print("Successful")

  