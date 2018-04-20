from crabs import Client, HTMLParser, StrParser, Set
import re

if __name__ == "__main__":
    domain = "http://www.imdb.com"
    client = Client()
    client.get(domain)
    parser = HTMLParser(client.page, "lxml")
    links = parser.find_all_links()

    for link in links:
        print(link)