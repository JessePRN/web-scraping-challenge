import os
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager

mars_data = {}
def scrape_news():

    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # ## NASA Mars News

    mars_url = "https://redplanetscience.com/"
    browser.visit(mars_url)
    html = browser.html

    # start soup
    mars_soup = bs(html, 'html.parser')

    # get title
    news_title = mars_soup.find('div',class_='content_title').text
    # print(nasa_news_title)
    mars_data["nasa_news_title"] = nasa_news_title

    # get p text
    news_p = mars_soup.find('div',class_='article_teaser_body').text
    # print(news_p)
    mars_data["news_p"] = news_p
    return mars_data

def scrape_jpl():
    # ## JPL Mars Space Images—Featured Image
    jpl_url = "https://spaceimages-mars.com/"
    browser.visit(jpl_url)
    html = browser.html

    # start soup
    jpl_soup = bs(html, 'html.parser')
    jpl_content = jpl_soup.find('img',class_='headerimage')['src']
    featured_image_url = jpl_url + jpl_content
    mars_data["featured_image_url"] = featured_image_url
    return mars_data

def scrape_fact():
    # ## Mars Facts
    fact_url = "https://galaxyfacts-mars.com/"
    fact_scrape = pd.read_html(fact_url)
    fact_df = fact_scrape[0]
    fact_df.columns = ['Mars-Earth Comparison', 'Mars', 'Earth']
    html_table = fact_df.to_html()
    html_table
    mars_data["html_table"] = html_table
    return mars_data

def scrape_hemi():
    # ## Mars Hemispheres
    hemi_url = "https://marshemispheres.com/"
    browser.visit(hemi_url)
    html = browser.html
    hemi_soup = bs(html, 'html.parser')
    hemi_desc = soup.find_all('div', class_='description')
    hemisphere_image_urls = []
    for desc in hemi_desc:
        title = desc.find('h3').text
        url = desc.find('a')['href']
        hemi_imgur = hemi_url + url
    #     print(hemi_imgur)
        
        browser.visit(hemi_imgur)
        html = browser.html
        soup = bs(html, 'html.parser')
    #     print(soup)
    
        enhanced_div = soup.find('div', class_='downloads')
        hemi_imgur = enhanced_div.find('a')['href']

        hemi_dict = {'title': title,'img_url': hemi_url + hemi_imgur}
        hemisphere_image_urls.append(hemi_dict)
        
    mars_data["hemisphere_image_urls"] = hemisphere_image_urls
    return mars_data    # # Setup splinter
    # # browser = init_browser()
    # executable_path = {'executable_path': ChromeDriverManager().install()}
    # browser = Browser('chrome', **executable_path, headless=False)

    # # Set an empty dict for listings that we can save to Mongo
    # listings = {}

    # # The url we want to scrape
    # url = "https://webscraper.io/test-sites/e-commerce/allinone/phones/touch"
    
    # # Call visit on our browser and pass in the URL we want to scrape   
    # browser.visit(url)

    # # Let it sleep for 1 second
    # time.sleep(1)

    # # Return all the HTML on our page
    # html = browser.html
    
    # # Create a Beautiful Soup object, pass in our HTML, and call 'html.parser'
    # soup = BeautifulSoup(html, "html.parser")

    # # Build our dictionary for the headline, price, and neighborhood from our scraped data
    # listings["headline"] = soup.find("a", class_="title").get_text()
    # listings["price"] = soup.find("h4", class_="price").get_text()
    # listings["reviews"] = soup.find("p", class_="pull-right").get_text()

    # # Quit the browser
    # browser.quit()

    # # Return our dictionary
    # return listings
