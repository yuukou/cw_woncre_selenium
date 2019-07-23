# coding:utf-8
from time import sleep
from selenium import webdriver


#Chromeを起動
browser = webdriver.Chrome()

#表示したいサイトを開く
browser.get("https://www.furimawatch.net/tool/#!/login")

#googleのログインボタンを押下
import google
google.googleLogin(browser)

#facebookのログインボタンを押下
#browser.find_element_by_xpath("/html/body/div[1]/div/button[2]").click()

#表示したサイトのスクリーンショットを撮る
browser.save_screenshot('screen.png')

#表示した瞬間消えちゃうから幅を持たせておく
sleep(5)

#ブラウザを閉じる
browser.close()