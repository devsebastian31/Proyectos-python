import urllib.request

url = "http://example.com/file.txt"
filename = "file.txt"

urllib.request.urlretrieve(url, filename)

