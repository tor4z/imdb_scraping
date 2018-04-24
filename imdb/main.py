from crabs import Crabs
from crabs.options import Travel
from imdb.routes import routes
import logging

if __name__ == "__main__":
    seed = ["http://www.163.com"]
    crabs = Crabs()
    crabs.set_seeds(seed)
    crabs.set_logger(level=logging.DEBUG)
    crabs.set_http_client(max_redirects=5)
    crabs.set_routes(routes)

    crabs.set_url_filter(allow_netlocs = ["*.163.com"],
                        disallow_paths = [])
    crabs.set_scraper(depth = 2, travel_mod = Travel.BFS)

    crabs.set_executor(10)
    crabs.run()