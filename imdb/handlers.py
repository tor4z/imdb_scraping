from crabs import Handler
from crabs import HTMLParser

class NameHandler(Handler):
    def get(self):
        print("get name")


class TitleHandler(Handler):
    def get(self):
        print("get title")