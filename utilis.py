import urllib.request, urllib.error, urllib.parse
from pathlib import Path

"""
Title
-----
    Utilities for webcrawler part

Author
-------
    Jakub Kwiatkowski

Description
-----------
    The part of the project responsible for providing
    useful functions for webcrawler.py.

Sources
---------------------------
https://docs.python.org/3/library/pathlib.html
https://docs.python.org/3/library/urllib.html
"""


def create_directory_if_doesnt_exist(directory):
    """
    Function for creating directory if it does not exist

    Parameters
    ----------

        directory : String
            Name of directory

    Returns
    -------
        The function returns nothing
    """
    Path(directory).mkdir(parents=True, exist_ok=True)


def get_site(url, filename, directory='sites'):
    """
    Function for downloading website to directory

    Parameters
    ----------

        url : String
            Website url address

        filename : String
            Downloaded website filename

        directory : String
            Name of directory where websites will be located

    Returns
    -------
        The function returns nothing
    """
    create_directory_if_doesnt_exist(directory)
    response = urllib.request.urlopen(url)
    web_content = response.read()
    f = open(directory + "/" + filename + '.html', 'wb')
    f.write(web_content)
    f.close()
    print('DONE: ', url)
