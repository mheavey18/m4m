from bs4 import BeautifulSoup as soup
from urllib2 import urlopen
from selenium import webdriver

browser = webdriver.Chrome('/Users/martyheavey/Downloads/chromedriver')
browser.get('https://www.netflix.com/browse')

login_email = browser.find_element_by_css_selector('#email')
login_pass = browser.find_element_by_css_selector('#password')
submit = browser.find_element_by_css_selector('#appMountPoint > div > div.login-body > div > div > form:nth-child(2) > button')

# login_email.send_keys('chrisheavey@cox.net')
# login_pass.send_keys('heavecat')
# submit.click()

marty_user = browser.find_element_by_css_selector('#appMountPoint > div > div > div.profiles-gate-container > div > div > ul > li:nth-child(3) > div > a > div > div')
marty_user.click()

# myurl = 'https://www.netflix.com/originals'


# uclient = urlopen(myurl)
# page_html = uclient.read()
# uclient.close()
# page_soup = soup(page_html, "html.parser")
# items = page_soup.findAll("div", {"class": "original-title"})
# # item = items[0].text
# for item in items:
# 	print item.text
	
# for item in items:
# 	title = item.a.div["original-title"]
# 	print title



