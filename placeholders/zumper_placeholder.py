#-*- coding: utf-8 -*-
import requests
import bs4
import csv

# NOTE: For this class, I am providing the urls for the pages we will scrape.
# Step 1: Identify page to scrape. 
url = "https://www.zumper.com/blog/2015/07/the-10-most-luxurious-apartments-for-rent-in-nyc-right-now/"


# Step 2: Determine what data you'll be retrieving.
    #rank, location, info, price

# Step 3: Inspect and analyze the website's structure to learn how to get the data.
# Step 4: Think about how you want to structure your data.
# Step 5: request for the page’s content with Python Requests and store the content in a variable.
# Step 6: Create a beautiful soup object by passing the variable into the beautiful soup
# Step 7: Parse/Find your desired content with Beautiful Soup methods.
# Step 8: Transform and Store the data in dictionary format.
# Step 9: Use Python’s CSV module to write a CSV file with the web page’s content.
