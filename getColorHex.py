# coding: UTF-8

# https://qiita.com/Azunyan1111/items/9b3d16428d2bcc7c9406

import urllib2
from bs4 import BeautifulSoup
import csv
import time


r = open("color.txt", "r")
f = open("color.csv", "w")
writer = csv.writer(f, lineterminator="\n")

for biomeColor in r:

	time.sleep(1)

	csv_list = []
	targetDiv = ""

	url = "http://www.color-hex.com/color/" + biomeColor[1:]
	print biomeColor
	html = urllib2.urlopen(url)

	soup = BeautifulSoup(html, "html.parser")

	divs = soup.find_all("div", "fullrow")

	for div in divs:
		try:
			h3s = div.find_all("h3")
			for h3 in h3s:
				if h3.string.find("Shades of") >= 0:
					targetDiv = div
		except:
			pass

	for div in targetDiv.find_all("div", "colordvconline"):
		print div.a.get_text().strip()
		csv_list.append(div.a.get_text().strip())

	writer.writerow(csv_list)


f.close()
r.close()
