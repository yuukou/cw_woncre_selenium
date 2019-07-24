# coding:utf-8
from time import sleep

def add(browser):

    # アラートボタン押下
    browser.find_element_by_xpath("/html/body/nav/ul/li[1]/a").click()

    # 画面遷移のため1秒間停止
    sleep(1)

    # 新しいアラートの作成を押下
    browser.find_element_by_xpath("/html/body/div[1]/div/button").click()

    # 画面遷移のため1秒間停止
    sleep(1)

    # 実際のデータ挿入処理
    import insert_data
    insert_data.insert(browser)