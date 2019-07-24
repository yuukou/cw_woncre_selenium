# coding:utf-8
from time import sleep

def insert(browser):
    # キーワード
    browser.find_element_by_id("inputKwAll").send_keys(unicode("あいうえお", 'utf-8'))

    # 除外キーワード１
    browser.find_element_by_id("inputKwe1").send_keys(unicode("かきくけこ", 'utf-8'))

    # 対象サービス

    # 下限値段
    browser.find_element_by_id("inputPmin").send_keys("222")

    # 上限値段
    browser.find_element_by_id("inputPmax").send_keys("2222")

    # アラート名
    # browser.find_element_by_id("inputNameAuto").send_keys("トリプルエス")

    # アラートのプレビュー押下
    browser.find_element_by_xpath("/html/body/div[1]/div/form/button").click()

    # 画面遷移のため1秒間停止
    sleep(1)

    # これでOKを押下
    browser.find_element_by_xpath("/html/body/div[1]/div/div[2]/button").click()

    # 画面遷移のため5秒間停止（登録処理が走るので少し長めに設定）
    sleep(5)