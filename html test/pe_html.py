from bs4 import BeautifulSoup
import requests
import os
import sys

root_path = os.path.abspath(os.path.join(os.path.dirname(sys.argv[0])))

# get content from url
url = "https://www.amebaiot.com/en/amebad-arduino-ws2812b-basics/"
html_content = requests.get(url).text

# parse the html content
soup = BeautifulSoup(html_content, 'lxml')
model_content = soup.find_all("div", {"class": "elementor-element elementor-element-c33a755 elementor-widget elementor-widget-text-editor"})
model_content = BeautifulSoup(str(model_content), 'html.parser').prettify()

# save result
with open(root_path +"\\output_example.html", "w", encoding='utf-8') as file:
    file.write(str(model_content))
file.close()
print("Files in '%s': %s" % (root_path, os.listdir(root_path)))