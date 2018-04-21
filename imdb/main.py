from crabs import Crabs
from crabs.utils import ClientHeaders
from imdb.routes import routes

if __name__ == "__main__":
    seed = ["http://www.imdb.com"]
    crabs = Crabs()
    crabs.set_max_depth(3)
    crabs.set_seeds(seed)
    crabs.set_routes(routes)
    crabs.set_client_headers(ClientHeaders)
    crabs.set_allow_netloc(["www.imdb.com"])
    crabs.run()