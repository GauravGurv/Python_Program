from PIL import Image,ImageFilter

path1="D:\STUDY\@Practice\Study\DS\DATA SCIENCE\pythonProject\Tiny Visual Program\Make_Watermark\\001.jpg"
path2="D:\STUDY\@Practice\Study\DS\DATA SCIENCE\pythonProject\Tiny Visual Program\Make_Watermark\\005.jpg"

img1=Image.open(path1,mode='r')
img2=Image.open(path2,mode='r')
# img2=img2.filter(ImageFilter.CONTOUR)
img1.paste(img2,(100,500))
img1.show()
# img3=Image.open(path3,mode='r')
