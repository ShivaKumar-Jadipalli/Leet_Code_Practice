from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize Chrome WebDriver
driver = webdriver.Edge()

# URL of the YouTube playlist
url = 'https://www.youtube.com/playlist?list=PLKnIA16_RmvYuZauWaPlRTC54KxSNLtNn'

# Open the URL in the browser
driver.get(url)

# Find all the playlist names
playlist_names = driver.find_elements(By.CSS_SELECTOR, 'a#video-title')

# Extract and print the names
with open("videos_names.txt",'w') as file:
    for playlist_name in playlist_names:
        file.write(playlist_name.text)
        file.write('\n')

# Close the WebDriver
driver.quit()
