import urllib.request

print(urllib.request.urlopen("http://kmla.woobi.co.kr").read().decode('utf-8'))
