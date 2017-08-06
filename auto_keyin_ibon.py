
# coding: utf-8

# In[1]:


#coding:utf-8
import time
from selenium import webdriver
from bs4 import BeautifulSoup

class KeyinTheData:
    def __init__(self, name, phone, store):#收件人輸入
        self.name  = name
        self.phone = phone
        self.store = store

    def autoKeyin(self):
		options = webdriver.ChromeOptions()
		#options.add_argument("--disable-print-preview")

		path = r'C:\Users\dajun\Desktop\python3_work\pdf'
		prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': path}
		options.add_experimental_option('prefs', prefs) #下載時不彈跳視窗並指定路徑


		exe_path = r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe'
		driver = webdriver.Chrome(executable_path= exe_path , chrome_options= options) # 開起chrome瀏覽器
		time.sleep(3)
		driver.get('https://myship.sp88.tw/C2C/Page02') #輸入網址

		time.sleep(2)
		price = '1000' #包裹金額
		driver.find_element_by_name("orderAmount").send_keys(price)
		driver.find_element_by_id("nextStep").click()

		time.sleep(2)
		senderphone =  '0975393349' #寄件人資料
		sendername = '林達俊'

		driver.find_element_by_id("senderPhone").send_keys(senderphone)
		driver.find_element_by_id("senderName").send_keys(sendername)
		driver.find_element_by_id("nextStep").click()

		time.sleep(2)
		receiverphone = self.phone #收件人資料
		receivername = self.name

		driver.find_element_by_id("receiverPhone").send_keys(receiverphone)
		driver.find_element_by_id("receiverName").send_keys(receivername)
		driver.find_element_by_id("checkStore").click()
		receiverstore = self.store

		time.sleep(2)
		driver.switch_to_window(driver.window_handles[-1]) #網頁跳轉
		driver.find_element_by_id("byName").click() #點選門市名稱查詢
		driver.switch_to.frame("frmMain") #跳轉frame

		time.sleep(1)
		driver.find_element_by_name("storeNameKey").send_keys(receiverstore) #填入門市名稱
		driver.find_element_by_id("serach_name").click() 

		element = driver.find_element_by_id("storeByName")
			if len(element.find_elements_by_tag_name("option")) > 1  :
				for option in element.find_elements_by_tag_name("option"):
					#print(option.text)
					if option.text == receiverstore:
						option.click()
					break

		driver.switch_to.default_content()
		time.sleep(1)
		driver.find_element_by_id("sevenDataBtn").click() #確認門市
		#driver.find_elements_by_tag_name("input")

		driver.find_element_by_id("AcceptBtn").click()

		driver.find_element_by_id("submit_butn").click()

		driver.switch_to_window(driver.window_handles[0])

		driver.find_element_by_id("nextStep").click()


		# In[8]:


		driver.find_element_by_id("printOrder").click()


		# In[9]:


		time.sleep(1)
		code = driver.find_element_by_id("pinno").text


		# In[10]:


		driver.find_element_by_id("PrintOK").click()
		driver.switch_to_window(driver.window_handles[1]) #網頁跳轉
		#print(driver.page_source)


		# In[11]:



		#driver.execute_script("window.print();")
		#driver.switch_to_dialog()
		#a_check = lambda: pywinauto.findwindows.find_windows(title=u'列印', class_name='#32770')[0]
		#a_check.click()
		#print(a_check)
		#driver.quit()

		time.sleep(3)
		driver.set_window_size(400, 700)

		driver.save_screenshot(path+'/'+code+'.png')  # 保存截圖
		driver.close()
		driver.switch_to_window(driver.window_handles[0])
		driver.close()
		print ('Name : ' + receivername + ' , '+ 'Phone : ' + receiverphone + ' -> ' + code)
"""
def confirm_click():
    #print(n)
    driver.driver.find_elements_by_tag_name("td")[0].send_Keys(Keys.ENTER)
    
    
t = Thread(target = confirm_click(),args=(10,))
t.start()
time.sleep(3)
driver.execute_script("window.print()")
"""

