import requests

url = "http://data.pr4e.org/intro-short.txt"
response = requests.head(url)

print("Last-Modified:", response.headers.get("Last-Modified"))
print("Etag:", response.headers.get("Etag"))
print("Content-Length:", response.headers.get("Content-Length"))