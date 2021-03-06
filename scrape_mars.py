import os
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from splinter import Browser
import time
from webdriver_manager.chrome import ChromeDriverManager

mars_data = {}
def scrape_mars():

    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # ## NASA Mars News

    mars_url = "https://redplanetscience.com/"
    browser.visit(mars_url)

    time.sleep(1)

    html = browser.html
    # print(html)

    # start soup
    mars_soup = bs(html, 'html.parser')

    # get title
    news_title_div = mars_soup.find('div', class_='content_title')
    # print(news_title_div)
    news_title = news_title_div.text
    # print(news_title)
    mars_data["nasa_news_title"] = news_title

    # get p text
    news_p_div = mars_soup.find('div', class_='article_teaser_body')
    news_p = news_p_div.text
    # print(news_p)
    mars_data["news_p"] = news_p

#     return mars_data
# def scrape_jpl():
    # ## JPL Mars Space Images—Featured Image
    jpl_url = "https://spaceimages-mars.com/"
    browser.visit(jpl_url)
    time.sleep(1)
    html = browser.html

    # start soup
    jpl_soup = bs(html, 'html.parser')
    jpl_content = jpl_soup.find('img',class_='headerimage')['src']
    featured_image_url = jpl_url + jpl_content
    mars_data["featured_image_url"] = featured_image_url

#     return mars_data
# def scrape_fact():

    # ## Mars Facts
    fact_url = "https://galaxyfacts-mars.com/"
    fact_scrape = pd.read_html(fact_url)
    #table cleaning
    fact_df = fact_scrape[0]
    fact_df = fact_df.drop(0)
    fact_df.columns = ['Mars-Earth Comparison', 'Mars', 'Earth']
    fact_df = fact_df.set_index('Mars-Earth Comparison')

    html_table = fact_df.to_html()
    mars_data["html_table"] = html_table

    # return mars_data
# def scrape_hemi():

    # ## Mars Hemispheres
    hemi_url = "https://marshemispheres.com/"
    hemisphere_image_urls = []

    browser.visit(hemi_url)
    time.sleep(1)
    html = browser.html
    hemi_soup = bs(html, 'html.parser')
    hemi_desc = hemi_soup.find_all('div', class_='description')
    
    for desc in hemi_desc:
        title = desc.find('h3').text
        # print("OUR TITLE IS: " + title)
        url = desc.find('a')['href']
        hemi_imgur = hemi_url + url
        # print("HEMIIMGUR is: " + hemi_imgur)
        
        browser.visit(hemi_imgur)
        time.sleep(1)
        html = browser.html
        soup = bs(html, 'html.parser')
        # print("#######BELOW THIS IS OUR SOUP: ")
        # print(soup)
        # print("#######above THIS IS OUR SOUP: ")

        enhanced_div = soup.find('div', class_='downloads')
        hemi_imgur = enhanced_div.find('a')['href']

        hemi_dict = {'title': title,'img_url': hemi_url + hemi_imgur}
        hemisphere_image_urls.append(hemi_dict)
        
    mars_data["hemisphere_image_urls"] = hemisphere_image_urls
    # Quit the browser
    browser.quit()
    # Return our dictionary
    return mars_data    
    



    
