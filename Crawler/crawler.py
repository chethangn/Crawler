import ast
import requests
import urllib

def crawl(keyword, num):
	c = []
	ijn = 0
	start = 0
	crawled_count = 0
	while crawled_count<num:
		url = "https://www.google.co.in/search?q=" + str(keyword) + "&ijn=" + str(ijn) + "&start=" + str(start) + "&asearch=ichunk"
		resp = requests.get(url)
		ss = ast.literal_eval(resp.text)
		url_unparsed = ss[1][1]
		a = url_unparsed.split('imgurl=')[1:]
		for b in a:
			d = b.split('\\u0026amp;imgrefurl=')[0]
			d = d.replace('\\', '')
			d = d.replace('%25', '%')
			if crawled_count == num:
				break
			c.append(str(d) + '\n')
			crawled_count += 1
		ijn += 1
	return c

search_string = raw_input('Search string: ')
folder = "/home/chethan/AI/Crawler/images/images.txt"
num_images = 10
ans = crawl(search_string, num_images)
f = open(folder + "temp_links.txt","w")
b = 0
for a in ans:
	url_ = str(a)
	f.write(url_)
	urllib.urlretrieve(url_, folder + str(b) + '.jpg')
	b += 1
f.close()
print "Done"
