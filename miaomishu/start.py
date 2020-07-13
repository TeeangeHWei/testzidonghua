from selenium import webdriver
import pytesseract
from PIL import Image
from ShowapiRequest import ShowapiRequest
import time

driver = webdriver.Chrome()
driver.get("https://www.miaomishuo.com/loginByPwd")
time.sleep(5)

driver.find_element_by_xpath("//*[@id='loginByPwd']/div[1]/div/div[3]/input").send_keys("13590926268")
driver.save_screenshot("G:/testzidonghua/miaomishu/184.png")
code_element = driver.find_element_by_class_name("photoCode")
print(code_element.location)
left = code_element.location['x']
top = code_element.location['y']
right = code_element.size['width']+left
height = code_element.size['height']+top
im = Image.open("G:/testzidonghua/miaomishu/184.png")
img = im.crop((left,top,right,height))
img.save("G:/testzidonghua/miaomishu/185.png")

r = ShowapiRequest("http://route.showapi.com/184-4","96323","46ac60839c024ffb8f0738023da6c9bc" )
r.addBodyPara("img_base64", "")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
# r.addBodyPara("needMorePrecise", "0")
r.addFilePara("image", r"G:/testzidonghua/miaomishu/185.png") #文件上传时设置
res = r.post()
text = res.json()['showapi_res_body']['Result']
print(text) # 返回信息
time.sleep(2)
driver.find_element_by_xpath("//*[@id='loginByPwd']/div[1]/div/div[4]/input").send_keys(text)

driver.find_element_by_xpath("//*[@id='loginByPwd']/div[1]/div/div[5]/input").send_keys("123456")
driver.find_element_by_id("submit").click()
