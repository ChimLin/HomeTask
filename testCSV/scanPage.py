import urllib.request as test

str = test.urlopen('https://mail.ru').read()
print(str)