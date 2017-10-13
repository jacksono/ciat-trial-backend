"""Module to run the API."""

from inm.user_routes import (Home)
from inm.result import GetAllResults, GetAllYearResults, GetAllCombinationResults
from app import api, app


# Create api endpoints
api.add_resource(Home, "/")
api.add_resource(GetAllResults, "/results/")
api.add_resource(GetAllYearResults, "/results/year/<year>")
api.add_resource(GetAllCombinationResults, "/results/combination")

if __name__ == "__main__":
    app.run()
