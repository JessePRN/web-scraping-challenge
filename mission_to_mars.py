#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install flask_pymongo')
get_ipython().system('pip install webdriver-manager')
get_ipython().system('pip install selenium')


# In[5]:


# libraries
import os
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from splinter import Browser
from webdriver_manager.chrome import ChromeDriverManager


# In[6]:


# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ## NASA Mars News

# In[24]:


mars_url = "https://redplanetscience.com/"
browser.visit(mars_url)
html = browser.html


# In[14]:


# start soup
mars_soup = bs(html, 'html.parser')


# In[21]:


# get title
news_title = mars_soup.find('div',class_='content_title').text
print(nasa_news_title)


# In[23]:


# get p text
news_p = mars_soup.find('div',class_='article_teaser_body').text
print(news_p)


# In[ ]:





# ## JPL Mars Space Images—Featured Image

# In[32]:


jpl_url = "https://spaceimages-mars.com/"
browser.visit(jpl_url)
html = browser.html
html


# In[33]:


# start soup
jpl_soup = bs(html, 'html.parser')


# In[34]:


# Example:
jpl_content = jpl_soup.find('img',class_='headerimage')['src']
# url_prefix = "https://spaceimages-mars.com/"
featured_image_url = jpl_url + jpl_content
featured_image_url


# In[ ]:





# ## Mars Facts

# In[36]:


fact_url = "https://galaxyfacts-mars.com/"


# In[37]:


fact_scrape = pd.read_html(fact_url)
fact_scrape


# In[39]:


fact_df = fact_scrape[0]


# In[40]:


# clean up and convert to html table
fact_df.columns = ['Mars-Earth Comparison', 'Mars', 'Earth']
html_table = fact_df.to_html()
html_table


# In[ ]:





# ## Mars Hemispheres

# In[42]:


hemi_url = "https://marshemispheres.com/"


# In[44]:


browser.visit(hemi_url)
html = browser.html
hemi_soup = bs(html, 'html.parser')
hemi_soup


# In[46]:


hemi_desc = soup.find_all('div', class_='description')
hemi_desc


# In[53]:


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


hemisphere_image_urls





# Example:
# hemisphere_image_urls = [
#     {"title": "Valles Marineris Hemisphere", "img_url": "..."},
#     {"title": "Cerberus Hemisphere", "img_url": "..."},
#     {"title": "Schiaparelli Hemisphere", "img_url": "..."},
#     {"title": "Syrtis Major Hemisphere", "img_url": "..."},


# In[ ]:


titles=[]
hemisphere_img_urls=[] 

