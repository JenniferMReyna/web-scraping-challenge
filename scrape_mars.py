from bs4 import BeautifulSoup
from splinter import Browser
import os
import pandas as pd
import time
from webdriver_manager.chrome import ChromeDriverManager
import pprint


# # NASA Mars News

# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# Setup splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# URLs of pages to be scraped
news_url = 'https://redplanetscience.com/'
browser.visit(news_url) #you are typing in the link
myhtml = browser.html  #you are retrieving the html of that link

# Create BeautifulSoup object; parse with 'html.parser'
soup = BeautifulSoup(myhtml, 'html.parser')



# Examine the results, then determine element that contains sought info
#pprint.pprint(soup)


# In[9]:


# Scrape the Mars News Site and collect the latest News Title and Paragraph Text. 
# Assign the text to variables that you can reference later.

# #Latest News Title
news_title = soup.find('div', class_="list_text")


#Loop through returned results
for news in news_title:
    list_date = soup.find('div', class_='list_date')
    latest_title = soup.find('div', class_ ='content_title')
    latest_parag = soup.find('div', class_ = 'article_teaser_body')

print(list_date.text)
print(latest_title.text)
print(latest_parag.text)


# # JPL Mars Space Images - Featured Image

# In[10]:


#Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[11]:


#Visit URL for the feartures image
image_url = "https://spaceimages-mars.com/"
browser.visit(image_url) 
myhtml_2 = browser.html  
soup2 = BeautifulSoup(myhtml_2, 'html.parser')
#pprint.pprint(soup2)


# In[12]:


#Retrieve URL for featured image
feat_image = soup2.find('img', class_="headerimage fade-in")

featured_image_url = "https://spaceimages-mars.com/" + feat_image['src']
print(featured_image_url)


# # Mars Facts

# In[13]:


#Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[14]:


#Setting URLs to variables
facts_url = "https://galaxyfacts-mars.com/"
browser.visit(facts_url) 
myhtml_4 = browser.html  
soup4 = BeautifulSoup(myhtml_4, 'html.parser')


# In[15]:


facts_table = pd.read_html(facts_url)
print(facts_table)


# In[16]:


mars_df = facts_table[0]
mars_df.columns = ['Mars - Earth Comparison', 'Mars', 'Earth']
mars_df.head(7)


# # Mars Hemispheres

# In[17]:


#Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[18]:


#Setting URLs to variables
hemis_url = "https://marshemispheres.com/"
browser.visit(hemis_url) 
myhtml_3 = browser.html  
soup3 = BeautifulSoup(myhtml_3, 'html.parser')
#pprint.pprint(soup3)


# In[19]:


mars_hemis = soup3.find_all('div', class_="item")

for mars in mars_hemis:
    hemis_links = mars.a['href']
    hemis_urls = "https://marshemispheres.com/" + hemis_links
    
    browser.visit(hemis_urls)
    soup_for_image = BeautifulSoup(browser.html, 'html.parser')
    hemis_image = soup_for_image.find('div', class_ = 'downloads')
    hemis_image_url = hemis_image.find('li').a['href']
    print(hemis_urls + hemis_image_url) 
    


# In[20]:


# #Cerberus Hemisphere
# cer_hemis = soup3.find('div', class_ = 'description')
# cer_title = cer_hemis.h3.text
# cer_link = soup3.a['href']
# print(cer_title)


# In[21]:


#Schiaparelli Hemisphere


# In[22]:


#Syrtis Major Hemisphere


# In[23]:


#Valles Marineris Hemisphere


# In[24]:


# # Example:
# hemisphere_image_urls = [
#     {"title": "Valles Marineris Hemisphere", "img_url": "..."},
#     {"title": "Cerberus Hemisphere", "img_url": "..."},
#     {"title": "Schiaparelli Hemisphere", "img_url": "..."},
#     {"title": "Syrtis Major Hemisphere", "img_url": "..."},
# ]

