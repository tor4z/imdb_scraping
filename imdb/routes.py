from crabs.options import Method
from imdb.handlers import TitleHandler, NameHandler

routes = [
    (r"/title/.*", TitleHandler, Method.GET),
    (r"/name/.*", NameHandler, Method.GET),
]