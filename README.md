# Amazon-web-scrapping
# Overview
This project involves collecting, cleaning, and inserting data from Amazon product pages into a MySQL database. The data includes various product details such as ASIN, title, price, description, reviews, and more. This README provides an overview of the process, including data collection, cleaning, and insertion.

# Data Collection
# 1. Extracting Product Links
Process:
Product links are gathered and stored in a list.
Duplicate and irrelevant URLs are filtered out to ensure data quality.
# 2. Web Scraping
Tools: WebDriver and BeautifulSoup library.
Process:
Navigate to each product page using a WebDriver.
Extract relevant information such as ASIN, title, price, description, reviews, and image URLs.
Parse the HTML content of the product pages using BeautifulSoup to extract desired data.
# 3. Data Structure
Format: Dictionaries.
Attributes:
Directly extracted: ASIN, title, price, description.
Complex parsing: Reviews and image URLs.
# Data Cleaning
# 1. Handling Missing Values
Approach:
Assign default values or mark as null.
Example: Assign 'N/A' to fields like price or description if they are missing.
# 2. Text Processing
Techniques:
Remove special characters, punctuation, and irrelevant information.
Apply tokenization, removal of stop words, and lemmatization to standardize text data.
# 3. Data Transformation
Process:
Convert data types to ensure compatibility with MySQL database schema.
Example: Convert prices to decimal format, flatten reviews, and store them as strings.
Data Insertion
# 1. MySQL Database
Components:
Tables: products, categories, and reviews.
Constraints: Foreign key constraints to link tables appropriately.
# 2. Insertion Process
Tools: MySQL Connector library.
Process:
Establish a connection to the MySQL database.
Initialize a cursor for executing SQL queries.
Insert product data into the products table, with corresponding category IDs retrieved from the categories table.
Insert reviews into the reviews table, linked to their respective products via product IDs.
# 3. Error Handling
Mechanisms:
Handle duplicate entries, missing values, and other potential issues during insertion.
Identify and skip duplicate ASINs to avoid data redundancy.
# Requirements
Libraries
WebDriver
BeautifulSoup
MySQL Connector
NLTK (for text processing)
Database
MySQL database with tables: products, categories, and reviews.
# Usage
Extract Product Links:

Gather and store product links in a list.
Filter out duplicate and irrelevant URLs.
# Web Scraping:

Use the WebDriver to navigate to each product page.
Use BeautifulSoup to parse the HTML and extract product data.
# Data Cleaning:

Handle missing values.
Process text data to remove unwanted characters and standardize it.
Transform data types as needed.
# Data Insertion:

Connect to the MySQL database.
Insert cleaned and structured data into the appropriate tables.
Handle errors during the insertion process.
# Contact
For any questions or issues, please contact Duaa Fatima at fatimaduaa053@gmail.com.

