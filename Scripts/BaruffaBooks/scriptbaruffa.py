"""
Script per scaricare libri da flylib in formato html.

Il programma prende in ingresso il codice del libro.

Usage:
::
    python scriptbaruffa.py -b 2.405.1
"""

__author__ = 'davide.cacciavillani@energee3.com'
__reviewer__ = 'alessandro.cucci@energee3.com'

from lxml import html
import requests
import argparse
from itertools import count


def main(book):
    index = 1
    template = 'http://flylib.com/books/en/{0}.{1}/1/'
    book_content = []
    main_page = requests.get(template.format(book, index))
    tree = html.fromstring(main_page.text)
    title = html.tostring(tree.xpath('/html/head/title')[0])[7:-9].replace('.', "")

    for index in count():
        if index == 0:
            continue  # Si parte da pagina 1
        print "Processing page", index
        page = requests.get(template.format(book, index))

        tree = html.fromstring(page.text)
        page_body = tree.xpath('//*[@id="content"]')

        if page_body:
            page_body = page_body[0]
            skip = False
            for old_page in book_content:
                if html.tostring(old_page) == html.tostring(page_body):
                    skip = True
                    break
            if not skip:
                book_content.append(page_body)

        finished = "First page" in html.tostring(tree.xpath('//*[@id="maincontent"]/div/div[2]/div[1]/div[1]/div[2]/div[3]/a')[0])
        if finished:
            break  # se troviamo il link alla prima pagina, vuol dire che questa e' l'ultima, e posso uscire

    with open('books/' + title + '.html', "w") as f:  # Attenzione, assicurarsi che esista la cartella books
        for elem in book_content:
            f.write(html.tostring(elem))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--book', '-b', help='Codice libro di flylib')

    args = parser.parse_args()
    if args.book:
        main(args.book)
    else:
        print "Devi dirmi il codice del libro (es 2.405.1)"



