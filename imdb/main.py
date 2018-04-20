from crabs import Crabs
from imdb.routes import routes

if __name__ == "__main__":
    seed = ["http://www.imdb.com"]
    crabs = Crabs()
    crabs.set_seeds(seed)
    crabs.set_routes(routes)
    crabs.run()