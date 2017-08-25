'''
install time, urllib2 (urllib in python3), splinter
'''
import time, urllib2
from splinter import Browser
start = time.time()
result = False
username = ['list', 'of', 'usernames']
browser = Browser()

def internet_on():
    try:
        response=urllib2.urlopen('http://www.google.com',timeout=10)
        return True
    except urllib2.URLError as err: pass
    return False

def finish():
    browser.quit()
    print 'time : ', time.time() - start, 'secs'

def login(user):
    browser.visit('link to the login page')
    browser.fill('username textbox', user)
    browser.find_by_name('tick box').first.click()
    browser.fill('password link', 'password')
    browser.find_by_value("Login button").first.click()
    return internet_on()

for x in username:
    if result:
        break
    else:
        result = login(x)
finish()