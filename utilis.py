import urllib.request, urllib.error, urllib.parse
from pathlib import Path


def create_directory_if_doesnt_exist(directory):
    Path(directory).mkdir(parents=True, exist_ok=True)


def get_site(url, filename, directory='sites'):
    create_directory_if_doesnt_exist(directory)
    response = urllib.request.urlopen(url)
    web_content = response.read()
    f = open(directory + "/" + filename + '.html', 'wb')
    f.write(web_content)
    f.close()
    print('DONE: ', url)
