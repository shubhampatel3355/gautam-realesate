import urllib.request, urllib.error
try:
    req = urllib.request.Request('http://127.0.0.1:8000/visitors/')
    print(urllib.request.urlopen(req).read().decode('utf-8'))
except urllib.error.HTTPError as e:
    print(e.read().decode('utf-8'))
