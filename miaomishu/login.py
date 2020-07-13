#coding=utf-8
from selenium import webdriver
import time
from PIL import Image
from ShowapiRequest import ShowapiRequest
driver = webdriver.Chrome()
#初始化
def driver_init():
    driver.get("https://www.ganjinsheng.com/loginByPwd")
    # driver.maximize_window()
    time.sleep(5)
#获取元素信息
def get_element(xpath):
    element = driver.find_element_by_xpath(xpath)
    return element

def get_code_image(file_name):
    driver.save_screenshot(file_name)
    code_element = driver.find_element_by_class_name("photoCode")
    left = code_element.location['x']
    top = code_element.location['y']
    right = code_element.size['width'] + left
    height = code_element.size['height'] + top
    im = Image.open(file_name)
    img = im.crop((left, top, right, height))

    img.save(file_name)
#解析图片获取验证码
def code_online(file_name):
    r = ShowapiRequest("http://route.showapi.com/184-4", "96323", "46ac60839c024ffb8f0738023da6c9bc")
    r.addBodyPara("img_base64", "")
    r.addBodyPara("typeId", "35")
    r.addBodyPara("convert_to_jpg", "0")
    # r.addBodyPara("needMorePrecise", "0")
    r.addFilePara("image", file_name)  # 文件上传时设置
    res = r.post()
    text = res.json()['showapi_res_body']['Result']
    print("验证码：",text)
    return text

#运行主程序
def run_main():
    driver_init()
    file_name = "G:/testzidonghua/miaomishu/test01.png"
    get_element("//*[@id='loginByPwd']/div[1]/div/div[3]/input").send_keys("13590926268")
    get_code_image(file_name)
    text = code_online(file_name)
    get_element("//*[@id='loginByPwd']/div[1]/div/div[4]/input").send_keys(text)
    get_element("//*[@id='loginByPwd']/div[1]/div/div[5]/input").send_keys("123456")
    get_element("//*[@id='submit']").click()
    time.sleep(10)
    driver.close()

run_main()