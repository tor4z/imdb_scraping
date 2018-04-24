from crabs import Crabs
from imdb.routes import routes
import logging

if __name__ == "__main__":
    seed = ["http://www.acfun.cn"]
    crabs = Crabs()
    crabs.set_max_depth(2)
    crabs.set_seeds(seed)
    crabs.set_log_level(logging.INFO)
    crabs.set_client_max_redirects(5)
    crabs.update_routes(routes)
    crabs.set_allow_netloc(["www.acfun.cn"])
    crabs.set_disallow_path(["/reg/*", "/login/*", "/info/*"])
    crabs.run()