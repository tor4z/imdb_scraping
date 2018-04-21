from crabs import Crabs
from imdb.routes import routes

if __name__ == "__main__":
    seed = ["http://www.imdb.com"]
    crabs = Crabs()
    crabs.set_max_depth(3)
    crabs.set_seeds(seed)
    crabs.set_routes(routes)
    crabs.set_allow_netloc(["www.imdb.com"])
    crabs.run()