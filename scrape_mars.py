# Importing dependencies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd
import requests
import os

# chromedriver 
executable_path = {'executable_path': 'C:\\Users\\maham\\Desktop\\bin\\chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless = False)

def scrape():
    url = requests.get('https://mars.nasa.gov/news/')
    browser.visit(url)
    html = browser.html
    soup = bs(page.content, 'html.parser')
    
    # Retrieve article  title and paragraph Text
    title = soup.find_all('div',class_='content_title')[0].text
    paragraph = soup.find_all('div',class_='rollover_description_inner')[0].text
    
    mars_data['title'] = title
    mars_data['paragraph'] = paragraph
    return mars_data

Find featured Mars image on JPL

def scrape_mars_image():
    try:
        
        url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars' 
        browser.visit(image_url)
        
        image_button = browser.find_by_id('full_image')[0] 
        image_button.click()
        
        browser.find_link_by_partial_text('more info') 
        more_info_button = browser.links.find_by_partial_text('more info') 
        more_info_button.click()
        
         
        html = browser.html
        soup = bs(html, 'html.parser')  #scrape page into soup
        
        
        image_url = soup.select_one("figure.lede a img").get("src")   #find image source
        featured_image_url = (f" https://www.jpl.nasa.gov{image_url}")
        featured_image_url
        
        mars_info['featured_image_url'] = featured_image_url

        return mars_info
    finally:
        browser.quit()

Mars Facts

def scrape_for_facts():
    mars_facts_url = 'http://space-facts.com/mars/'
    mars_facts = pd.read_html(mars_facts_url)

    mars_facts_df = mars_facts[0]
    mars_facts_df.columns = ['Description','Value']
    mars_facts_df.set_index('Description', inplace=True)
    mars_data = mars_facts_df.to_html()

    mars_info['mars_facts'] = mars_data # Dictionary for mars facts.

    return mars_info

Mars Hemispheres

def scrape_hemispheres():
    try: 
        hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(hemispheres_url)
        html = browser.html
        soup = bs(html, 'html.parser')
        items = soup.find_all('div', class_='item')

        hemisphere = [] #create empty list for hemisphere
        hemispheres_base_url = 'https://astrogeology.usgs.gov' 

        
        for i in items: 
            title = i.find('h3').text
            image_url = i.find('a', class_='itemLink product-item')['href']
            browser.visit(hemispheres_base_url + image_url)
            image_html = browser.html
            soup = bs( image_html, 'html.parser')
            img_url = hemispheres_base_url + soup.find('img', class_='wide-image')['src']
            
            
            hemisphere.append({"title" : title, "img_url" : img_url})

        mars_info['hemisphere'] = hemisphere
        return mars_info
    finally:
        browser.quit()