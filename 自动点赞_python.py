# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get('http://i.qq.com/')
driver.switch_to.frame('login_frame')
driver.find_element_by_id('switcher_plogin').click()




driver.execute_script("document.getElementById('u').value='XXXX';")
driver.execute_script("document.getElementById('p').value='XXXX';")
time.sleep(3)
driver.execute_script("document.getElementById('login_button').parentNode.hidefocus=false;")
time.sleep(3)

driver.execute_script("document.getElementById('login_button').click();")
time.sleep(3)
driver.execute_script("document.getElementById('login_button').click();")
#driver.find_element_by_id('u').clear()
#driver.find_element_by_name('u').send_keys('1171067930')
#driver.find_element_by_id('p').clear()
#driver.find_element_by_name('p').send_keys('zxc1171067930.')

#driver.find_element_by_id('login_button').click()
time.sleep(5)
print driver.current_url
#driver.get(driver.current_url)

time.sleep(5)
#driver.execute_script('function clickGood(){var li = jQuery("ul#feed_friend_list").find("li");var a = jQuery(li[1]).find(".qz_like_btn_v3");if(jQuery(a).attr("data-clicklog")=="like"){let i = jQuery(a).find(".fui-icon");i.click();}}clickGood();function myrefresh(){document.getElementById("feed_friend_refresh").click();setTimeout(function(){ clickGood();   },2000);  setTimeout(function(){myrefresh();},30000);  }  myrefresh();  ')

#driver.execute_script('document.getElementsByClassName("qz-main").click();')
#while (1) :
#    time.sleep(10)
#    driver.execute_script('var li = jQuery("ul#feed_friend_list").find("li");var a = jQuery(li[1]).find(".qz_like_btn_v3");if(jQuery(a).attr("data-clicklog")=="like"){var i = jQuery(a).find(".fui-icon");i.click();}')
#    time.sleep(5)
#    driver.execute_script('document.getElementById("feed_friend_refresh").click();')
i = 0   
while (1) :
    time.sleep(10)
    driver.execute_script('var li = jQuery("ul#feed_friend_list").find("li");var a = jQuery(li[1]).find(".qz_like_btn_v3");if(jQuery(a).attr("data-clicklog")=="like"){var i = jQuery(a).find(".fui-icon");i.click();}')
    time.sleep(5)
    i = i+1
    if i == 2:
        break;
    driver.execute_script('document.getElementById("feed_friend_refresh").click();')

driver.quit() 


