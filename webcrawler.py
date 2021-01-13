from utilis import get_site
from threading import Thread

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
