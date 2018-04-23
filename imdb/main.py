from crabs import Crabs
from imdb.routes import routes
import logging

if __name__ == "__main__":
    seed = ["http://www.imdb.com"]
    crabs = Crabs()
    crabs.set_max_depth(3)
    crabs.set_seeds(seed)
    crabs.set_log_level(logging.WARNING)
    crabs.set_client_max_redirects(5)
    crabs.update_routes(routes)
    crabs.set_allow_netloc(["www.imdb.com"])
    crabs.set_disallow_path(["/offsite/*"])
    crabs.run()