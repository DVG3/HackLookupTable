from urllib import request, parse

url = 'http://192.168.11.40:8000'
#!/usr/bin/python
with open("MATKHAU.INP","r") as f:
    value = f.read()
data = parse.urlencode({"message":value}).encode()
req =  request.Request(url, data=data) 
resp = request.urlopen(req)