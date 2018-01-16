#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Yee_172'
__date__ = '2017/12/29'


from Func import *


DRIVER_OPTION = 1
SOURCE = 'https://pan.baidu.com/share/init?surl=miwy4YW'
WRONG_INPUT = '0000'
TARGET_NUMBER = 200


def main():
    global INDEX
    if DRIVER_OPTION is 1:
        driver = webdriver.Safari()
        driver.maximize_window()
    if DRIVER_OPTION is 2:
        driver = webdriver.PhantomJS()
    driver.get(SOURCE)
    driver.find_element_by_css_selector('[class=clearfix]').send_keys(WRONG_INPUT)
    button = driver.find_element_by_css_selector('[title=提取文件]')
    while 1:
        button.click()
        info_content = driver.find_element_by_css_selector('[class=verify-form]').text
        if info_content.find('请输入验证码') > 0:
            break
        sleep(0.2)
    while 1:
        if INDEX > TARGET_NUMBER:
            break
        change_button = driver.find_element_by_css_selector('[class=change-code]')
        try:
            element = driver.find_element_by_css_selector('[verify=verify]')
            img_url = element.get_attribute('src')
            data = request.urlopen(img_url).read()
            sys.stdout.write('Collecting on %d\r' % INDEX)
            sys.stdout.flush()
            filename = '%07d.png' % INDEX
            with open(PATH + '/Captchas/' + filename, 'wb') as f:
                f.write(data)
            INDEX = update_setting()
            change_button.click()
        except:
            change_button.click()


os.system('clear')
print('YOUR TARGET NUMBER:')
TARGET_NUMBER = int(input())
main()
sys.stdout.write(''.center(50) + '\r')
print('DONE!')
