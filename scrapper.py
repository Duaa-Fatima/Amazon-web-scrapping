#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from bs4 import BeautifulSoup
import requests
import selenium
from selenium import webdriver
import pandas as pd
import json
from fuzzywuzzy import process
from selenium.webdriver.common.by import By
from tqdm import tqdm
index=10
import time
from bs4 import BeautifulSoup
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By


# In[3]:


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import random
import json
from urllib.parse import urlparse, parse_qs


def urls(driver):
    link = []
    anchor_tags = driver.find_elements(By.CSS_SELECTOR, 'a.a-link-normal.s-underline-text.s-underline-link-text.s-link-style.a-text-normal')

    for tag in anchor_tags:
        link_url = tag.get_attribute('href')
        normalized_url = normalize_url(link_url)
        if normalized_url not in product_links:
            # Check for duplicates
            link.append(normalized_url)
    return link

def normalize_url(url):
    parsed_url = urlparse(url)
    # Remove query parameters and fragments
    return parsed_url.scheme + '://' + parsed_url.netloc + parsed_url.path


# Load proxies from file
def load_proxies(filename):
    with open(filename) as f:
        proxies = f.read().splitlines()
    return proxies

# Function to set up Selenium WebDriver with a random proxy
def setup_driver_with_proxy(proxy_address):
    binary = FirefoxBinary(r"C:\Program Files\Mozilla Firefox\firefox.exe")
    options = FirefoxOptions()
    options.add_argument('--proxy-server=%s' % proxy_address)
    driver = webdriver.Firefox(firefox_binary=binary, options=options,
                               executable_path=r"C:\Users\fatim\Downloads\geckodriver-v0.34.0-win64\geckodriver.exe")
    return driver

# URL to scrape
url = "https://www.amazon.com/s?i=specialty-aps&bbn=16225019011&rh=n%3A7141123011%2Cn%3A16225019011%2Cn%3A1040658&ref=nav_em__nav_desktop_sa_intl_clothing_0_2_13_2"

# Load proxies from file
proxies = load_proxies(r"C:\Users\fatim\OneDrive\Desktop\valid_proxy.txt")

# Choose a random proxy
proxy_address = random.choice(proxies)

# Set up Selenium WebDriver with the chosen proxy
driver = setup_driver_with_proxy(proxy_address)

link = []
for _ in range(50):
    # Load the page
    driver.get(url)
    link.extend(urls(driver))
    next_page_link = driver.find_element(By.CSS_SELECTOR, 'a.s-pagination-item.s-pagination-next.s-pagination-button.s-pagination-separator')
    url = next_page_link.get_attribute('href')
    time.sleep(2)


with open('links.txt', 'w') as f:
    for l in link:
        f.write(l + '\n')



for links in link:
    print(links)

output_file = "product_info.json"

# # Extract product info
extract_clothes(driver, output_file)


# In[5]:


def read_links_from_file(filename):
    with open(filename, 'r') as f:
        links = f.readlines()
    unique_links = set()
    for link in links:
        link = link.strip()
        if 'https://www.amazon.com/sspa/click' not in link:
            unique_links.add(link)
    return list(unique_links)

def extract_clothes(driver, output_file):
    links = read_links_from_file('links.txt')
    try:
        # Initialize list to store product information
        all_products_info = []

        # Iterate over the provided links
        for link in links:
            # Go to the product page
            driver.get(link)

            # Get the page source
            page_source = driver.page_source
            soup = BeautifulSoup(page_source, 'html.parser')
            product_info = {}

            # Extract product information
            asin_span = soup.find('span', string='ASIN')
            product_info["asin"] = asin_span.find_next_sibling('span').text.strip() if asin_span else None

            product_title_span = soup.find('span', id='productTitle')
            product_info["Title"] = product_title_span.text.strip() if product_title_span else None

            price_span = soup.find('span', class_='a-price')
            price_text_span = price_span.find('span', class_='a-offscreen') if price_span else None
            product_info["price"] = price_text_span.text.strip() if price_text_span else None

            product_info["gender"] = 'male'

            product_description_div = soup.find('class', class_='a-row feature')
            product_info["description"] = product_description_div.span.text.strip() if product_description_div else None

            a_element = soup.find('span', class_='a-list-item').a
            product_info["sub-category"] = a_element.text.strip() if a_element else None

            manufacturer_span = soup.find('span', string='Manufacturer')
            product_info["brandName"] = manufacturer_span.find_next_sibling('span').text.strip() if manufacturer_span else None

            color_element = soup.find('span', class_='selection')
            product_info["color"] = color_element.text.strip() if color_element else None

            rating_span = soup.find('span', class_='a-size-medium a-color-base')
            rating_text = rating_span.get_text(strip=True) if rating_span else None
            product_info["rating"] = float(rating_text.split()[0]) if rating_text else None

            review_containers = soup.find_all('div', class_='a-expander-content')
            reviews = [review_container.find('span').text.strip() if review_container.find('span') else None for review_container in review_containers]
            product_info["review"] = reviews

            # Add product URL to product_info
            product_info["productURL"] = link

            # Add product information to the list
            all_products_info.append(product_info)

            # Save product_info to JSON file
            with open(output_file, 'a') as json_file:
                json.dump(product_info, json_file, indent=4)
                json_file.write('\n')  # Add a newline to separate product info

            print("Product Info saved to", output_file)

    except NoSuchElementException as e:
        print("Error: Element not found -", e)
    except TimeoutException as e:
        print("Error: Timeout waiting for element -", e)
    except Exception as e:
        print("Error occurred while extracting products:", e)


# In[6]:


output_file = "product_info.json"
extract_clothes(driver, output_file)


# In[100]:


link


# In[ ]:





# In[ ]:





# In[ ]:




