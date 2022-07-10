from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import os
import glob
from pathlib import Path
import argparse


def prepare():
    home = str(Path.home())
    for file in glob.glob('%s/Downloads/data_*.csv' % (home)):
        ans = input('정상 수행을 위해 "%s" 파일을 삭제 해야 합니다. (y/n) ' % (file))
        if ans == 'y' or ans == 'Y':
            os.remove(file)
        else:
            exit(1)


def convert(dst):
    home = str(Path.home())
    for file in glob.glob('%s/Downloads/data_*.csv' % (home)):
        with open(file, 'rb') as src_file:
            with open(dst, 'w+b') as dst_file:
                contents = src_file.read()
                dst_file.write(contents.decode('cp949').encode('utf-8'))
        os.remove(file)


def download(driver, url, dst_file):
    wait_delay = 1.5
    driver.get(url)
    time.sleep(wait_delay)
    button = driver.find_element(
        by=By.XPATH, value='/html/body/div[2]/section[2]/section/section/div/div/form/div[2]/div/p[2]/button[2]')
    button.click()
    time.sleep(wait_delay)
    csv_button = driver.find_element(
        by=By.XPATH,  value='/html/body/div[2]/section[2]/section/section/div/div/form/div[2]/div[2]/div[2]/div/div[2]/a')
    csv_button.click()
    time.sleep(wait_delay)
    convert(dst_file)


def main():
    parser = argparse.ArgumentParser(description="Download Korean Stock List")
    parser.add_argument('--out', '-o', dest='out', default=".",
                        help='destination (default: current directory)')
    args = parser.parse_args()
    print(args.out)

    prepare()

    webdriver_options = webdriver.ChromeOptions()
    webdriver_options.add_argument("--no-sandbox")
    webdriver_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=webdriver_options)

    stock_url = 'http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201020201'
    etf_url = 'http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201030104'
    etn_url = 'http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201030204'

    download(driver, stock_url, '%s/kr-stock.csv' % (args.out))
    download(driver, etf_url, '%s/kr-etf.csv' % (args.out))
    download(driver, etn_url, '%s/kr-etn.csv' % (args.out))

    driver.close()


if __name__ == '__main__':
    main()
