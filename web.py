# *******************************************************************
# Author - Harshit Prasad
# 18.12.2016
# Python program to download web images from a particular website.
# *******************************************************************

# Here we are going to use Python libraries. These are most common libraries used in web development
from urllib import request
from random import randrange # generates a random number

def download_web_image(url):
    name = randrange(1,100) # It will pick up any random number between 1 to 100
    full_name = str(name) + ".jpg" # converts the name into a string
    request.urlretrieve(url, full_name)

# Complete link of the web-image
download_web_image("https://s3.amazonaws.com/codechef_shared/sites/default/files/uploads/pictures/1418a84beff3a4ddcd96e54fc6224aa8.png")
# Make sure the url should be copied in double brackets.
# You can paste any link of your choice, but make sure it should be a web-image.

