from utilis import get_site
from threading import Thread

"""
Title
-----
    Multi-threaded web crawler

Author
-------
    Jakub Kwiatkowski

Description
-----------
    Web crawler - A Web crawler, sometimes called a spider or spiderbot and often shortened
    to crawler, is an Internet bot that systematically browses the World Wide Web, typically
    for the purpose of Web indexing (web spidering). Web search engines and some other websites
    use Web crawling or spidering software to update their web content or indices of other
    sites' web content. Web crawlers copy pages for processing by a search engine, which indexes
    the downloaded pages so that users can search more efficiently. 

Sources
---------------------------
https://docs.python.org/3/library/threading.html
"""

url_list = [
    "https://piwolucja.pl/felietony/powrot-na-zachodnie-wybrzeze-olschool-ipa/",
    "https://piwolucja.pl/piwa-polecane/piwo-z-cbd-hemp-brew-browar-tarnobrzeg/",
    "https://piwolucja.pl/felietony/7-piw-bezalkoholowych-po-ktore-siegam-najczesciej/",
    "https://blog.kopyra.com/index.php/2021/01/13/jak-warzyc-piwo-johna-j-palmera-po-polsku/",
    "https://blog.kopyra.com/index.php/2021/01/13/ten-rzad-nienawidzi-przedsiebiorcow-ja-to-widze-inaczej/",
    "https://blog.kopyra.com/index.php/2021/01/05/italo-pilsco-czyli-ritmo-pils-vs-italiano-vero/",
    "https://blog.kopyra.com/index.php/2021/01/04/1-live-w-2021/",
    "https://blog.kopyra.com/index.php/2021/01/04/zascianki-supraskie-partyzana-rapier-i-pilum/",
    "https://blog.kopyra.com/index.php/2020/12/31/kormoran-vs-bocian/",
    "https://blog.kopyra.com/index.php/2020/12/29/hempbrew-cbd-pale-ale/"
]

threads = []
for name, url in enumerate(url_list):
    thread = Thread(target=get_site, args=(url, str(name), 'sites'))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
