from crabs import Handler

class NameHandler(Handler):
    _PATTERN = r".*name/(\w*)/?"


class TitleHandler(Handler):
    _PATTERN = r".*title/(\w*)/?"

    def init(self):
        pass

    def new_url(self):
        pass

    def put_link(self, links):
        if not isinstance(links, list):
            links = [links]
        self._crabs.put_links(links)

