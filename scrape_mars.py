#Import Dependencies
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from bs4 import BeautifulSoup
import time

# Create functions to import into Flask Server
    # MASTER
def scrape_all():
    # CHROME DRIVER
    executable_path = {'executable_path': './Missions_to_Mars/chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    news_title, news_p = news_data(browser)
    return{
        'news_title':news_title,
        'news_p':news_p,
        'featured_image_url':featured_image_url,
        'mars_weather':mars_weather,
        'hemisphere_image_urls':hemisphere_image_urls

    }

def news_data(browser):
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(2)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    slide_li = soup.find("li",class_="slide")
    news_title = slide_li.find("div",class_="content_title").text
    news_p = slide_li.find("div",class_="article_teaser_body").text
    return news_title, news_p

def featured_image_url(browser):
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    base_url = 'https://www.jpl.nasa.gov'
    browser.visit(url)
    time.sleep(2)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    img = soup.find("img",class_="main_image")["src"]
    featured_image_url = base_url + img
    return featured_image_url

def mars_weather(browser):
    url = 'https://twitter.com/marswxreport?lang=en'
    time.sleep(2)
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    mars_weather = soup.find("p",class_="tweet-text").text

def tables(browser):
    url = 'https://space-facts.com/mars/'
    time.sleep(2)
    tables = pd.read_html(url)[0]
    tables = tables.rename(columns={0:"Description",1:"Value"})
    tables = tables.to_html(classes = "table table-striped")
    tables

def hemisphere_image_urls(browser):
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    for i in range(4): 
        browser.find_by_tag('h3')[i].click()
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        my_dict = {
            "title": soup.find("h2",class_="title").text, 
            "img_url": soup.find("div",class_="downloads").find("a")["href"]
        }
        hemisphere_image_urls.append(my_dict)
        browser.back()
        return hemisphere_image_urls
    # Create function for each scrape