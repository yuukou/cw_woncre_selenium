# coding:utf-8
from time import sleep

def googleLogin(browser):

    # Click GMail login
    browser.find_element_by_xpath("/html/body/div[1]/div/button[1]").click()

    # ウィンドウ移動のため1秒間停止
    sleep(1)

    # ウィンドウハンドルを取得する
    handle_array = browser.window_handles

    # seleniumで操作可能なdriverを切り替える
    browser.switch_to.window(handle_array[1])

    # type email
    browser.find_element_by_name("identifier").send_keys("yuukou.triplejump0219@gmail.com")

    # click next
    browser.find_element_by_id("identifierNext").click()

    # 画面遷移のため1秒間停止
    sleep(1)

    # type password
    browser.find_element_by_name("password").send_keys("yuukou0219")

    # click signin
    element = browser.find_element_by_id('passwordNext')
    browser.execute_script("arguments[0].click();", element)

    # ウィンドウ移動のため5秒間停止（google認証のリダイレクト処理も走るので少し長めに設定）
    sleep(5)

    # ウィンドウハンドルを取得する
    handle_array = browser.window_handles

    # seleniumで操作可能なdriverを切り替える
    browser.switch_to.window(handle_array[0])

    # ブラウザを返す
    return browser