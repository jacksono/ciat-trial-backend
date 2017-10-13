"""Module to define buckeltist endpoints."""

from flask_restful import Resource
from inm.models import Observation
from flask import request


def get_all_results():
    """Docstring."""
    results = Observation.query.all()
    all_results = []
    for result in results:
        output = {"plot_num": result.plot_num,
                  "combination": result.combination,
                  "Results2004": result._2004,
                  "Results2005": result._2005,
                  "Results2006": result._2006,
                  "Results2007": result._2007,
                  "Results2008": result._2008,
                  "Results2009": result._2009,
                  "Results2010": result._2010,
                  "Results2011": result._2011,
                  "Results2012": result._2012,
                  "Results2013": result._2013,
                  "Results2014": result._2014,
                  "Results2015": result._2015}
        all_results.append(output)
        output = []
    return all_results


class GetAllResults(Resource):
    """Shows all results. Route: /api/v1/results/ using GET."""

    def get(self):  # noqa
        """
           End point for returning all results
           ---
           parameters:
             - in: header
               name: token
               type: string
               description: Access token
               required: true
           responses:
             200:
               description: Returns all results.

            """
        return get_all_results()


class GetAllYearResults(Resource):
    """Shows all results for a year. Route: /api/v1/results/year using GET."""

    def get(self, year):  # noqa
        """
           End point for returning all results for a particular year
           ---
           parameters:
             - in: header
               name: token
               type: string
               description: Access token
               required: true
           responses:
             200:
               description: Returns all results.

            """
        yr = year + "_results"
        year_results = []
        for result in get_all_results():
            output = {"plot_num": result["plot_num"],
                      yr: result[yr]}
            year_results.append(output)
            output = []
        return year_results


class GetAllCombinationResults(Resource):
    """Shows all results for a year. Route: /api/v1/results/year using GET."""

    def get(self):  # noqa
        """
           End point for returning all results for a particular year
           ---
           parameters:
             - in: header
               name: token
               type: string
               description: Access token
               required: true
           responses:
             200:
               description: Returns all results.

            """
        args = request.args.to_dict()
        residues = args.get("res")
        manure = args.get("f")
        nitro = args.get("n")
        phos = args.get("p")
        rotation = args.get("rot")
        rep = args.get("rep")
        combination_results = []
        print("it", rep)
        for result in get_all_results():
            if (result["combination"]["RESIDUES"] == residues and
               result["combination"]["FYM"] == manure and
               result["combination"]["N"] == nitro and
               result["combination"]["ROTATION"] == rotation and
               result["combination"]["P"] == phos and
               result["combination"]["REP"] == int(rep)):
                    combination_results.append({"plot_num": result["plot_num"]})
                    combination_results.append({"combination": result["combination"]})
                    combination_results.append({"Results2004": result["Results2004"]})
                    combination_results.append({"Results2005": result["Results2005"]})
                    combination_results.append({"Results2006": result["Results2006"]})
                    combination_results.append({"Results2007": result["Results2007"]})
                    combination_results.append({"Results2008": result["Results2008"]})
                    combination_results.append({"Results2009": result["Results2009"]})
                    combination_results.append({"Results2010": result["Results2010"]})
                    combination_results.append({"Results2011": result["Results2011"]})
                    combination_results.append({"Results2012": result["Results2012"]})
                    combination_results.append({"Results2013": result["Results2013"]})
                    combination_results.append({"Results2014": result["Results2014"]})
                    combination_results.append({"Results2015": result["Results2015"]})

        return combination_results
