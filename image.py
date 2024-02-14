import requests
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from webdriver_manager.chrome import ChromeDriverManager
import time

chrom_options = Options()
chrom_options.add_experimental_option("detach", True)

chrom_options.add_experimental_option("excludeSwitches", ["enable-logging"])

service = Service(executable_path=ChromeDriverManager().install())
browser = webdriver.Chrome(service=service, options=chrom_options)

browser.get("https://www.naver.com/")
browser.implicitly_wait(10)  # 로딩이 끝날 때까지 10초까지는 기다려줌

search = browser.find_element(By.CSS_SELECTOR,"#query")
search.click()

search.send_keys("아이폰 13")
search.send_keys(Keys.ENTER)

browser.find_element(By.CSS_SELECTOR, "#lnb > div.lnb_group > div > div.lnb_nav_area._nav_area_root > div > div.api_flicking_wrap._conveyer_root > div:nth-child(1) > a").click()
time.sleep(5)
browser.find_element(By.CSS_SELECTOR, ".btn_option._search_option_open_btn").click()
browser.find_element(By.CSS_SELECTOR, "#snb > div.mod_group_option_sort._search_option_detail_wrap > ul > li.bx.ccl > div > div > a:nth-child(3)").click()

img_element = browser.find_element(By.CSS_SELECTOR, "#main_pack > section.sc_new.sp_nimage._fe_image_viewer_prepend_target > div.api_subject_bx._fe_image_tab_list_root.ani_fadein > div > div > div.image_tile._fe_image_tab_grid > div:nth-child(1) > div > div > div > img")

img_url = img_element.get_attribute("src")

response = requests.get(img_url, stream=True)

if response.status_code == 200:
    with open('image.jpg', 'wb') as f:
        response.raw.decode_content = True
        shutil.copyfileobj(response.raw, f)

browser.quit()