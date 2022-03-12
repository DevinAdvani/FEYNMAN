import os
import webbrowser

html = '<html>Hello World</html>'
path = os.path.abspath('sample.html')
url = 'file://' + path

with open(path, 'w') as f:
    f.write(html)
webbrowser.open(url)
