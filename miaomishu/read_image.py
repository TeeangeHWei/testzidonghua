#coding=utf-8
import pytesseract
from PIL import Image
from ShowapiRequest import ShowapiRequest

r = ShowapiRequest("http://route.showapi.com/184-4","96323","46ac60839c024ffb8f0738023da6c9bc" )
r.addBodyPara("img_base64", "")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
# r.addBodyPara("needMorePrecise", "0")
r.addFilePara("image", r"E:\184.png") #文件上传时设置
res = r.post()
text = res.json()['showapi_res_body']['Result']
print(text) # 返回信息
