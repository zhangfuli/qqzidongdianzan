# -*- coding: utf-8 -*-
"""
Created on Sun May 21 22:44:16 2017

@author: zfl
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from selenium import webdriver
import time
from pyvirtualdisplay import Display
display = Display(visible = 0,size=(800,600))
display.start()

i = 0
while (1):   
    driver = webdriver.Firefox() 
    print "open browser success"
    driver.get('http://i.qq.com/')
    print "open url success"
    driver.switch_to.frame('login_frame')
    print "find frame"
    driver.find_element_by_id('switcher_plogin').click()
    print "passwordway"
    time.sleep(3)
    driver.execute_script("document.getElementById('u').value='XXXX';")
    driver.execute_script("document.getElementById('p').value='XXXX';")
    time.sleep(3)
    print "name&password filled"
    driver.execute_script("document.getElementById('login_button').parentNode.hidefocus=false;")
    time.sleep(3)
    driver.execute_script("document.getElementById('login_button').click();")
    driver.execute_script("document.getElementById('login_button').click();")
    print driver.current_url
    time.sleep(10)
    print driver.current_url
    time.sleep(10)
    print driver.current_url
    #driver.switchTo().defaultContent();
    driver.get(driver.current_url)
#driver.execute_script('function clickGood(){var li = jQuery("ul#feed_friend_list").find("li");var a = jQuery(li[1]).find(".qz_like_btn_v3");if(jQuery(a).attr("data-clicklog")=="like"){let i = jQuery(a).find(".fui-icon");i.click();}}clickGood();function myrefresh(){document.getElementById("feed_friend_refresh").click();setTimeout(function(){ clickGood();   },2000);  setTimeout(function(){myrefresh();},30000);  }  myrefresh();  ')
    while (1) :
        time.sleep(5)
        driver.execute_script('var li = jQuery("ul#feed_friend_list").find("li");var a = jQuery(li[1]).find(".qz_like_btn_v3");if(jQuery(a).attr("data-clicklog")=="like"){var i = jQuery(a).find(".fui-icon");i.click();}')
        time.sleep(5)
        i = i+1
        if i == 900:
            break;
        driver.execute_script('document.getElementById("feed_friend_refresh").click();')    
    i = 0
    driver.quit()
    

    	
  
    
   


