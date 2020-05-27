import urllib.request, urllib.parse, urllib.error
import webbrowser
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input('Enter link(type "exit" to exit): ')
    if url == 'exit':
        print('Exiting....')
        quit()
    try:
        html = urllib.request.urlopen(url, context=ctx).read()
    except:
        print('Bad URL')
        continue
    lst = re.findall('"(https:\/\/instagram.+?)"', str(html))
    print('Opening a new tab.....')
    webbrowser.open_new_tab(lst[0])
