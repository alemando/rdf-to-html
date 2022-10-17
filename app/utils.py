import os
import json
from dotenv import load_dotenv
from SPARQLWrapper import SPARQLWrapper2
import urllib.parse

load_dotenv()

LOCALPREFIX = os.getenv("LOCALPREFIX", "")
LOCALIRI = os.getenv("LOCALIRI", "")


async def getSparqlData(sparqlEndpoint, prefix, entity):
    sparqlEndpoint = sparqlEndpoint.replace("localhost", "host.docker.internal")
    sparqlEndpoint = sparqlEndpoint.replace("127.0.0.1", "host.docker.internal")
    response = {}
    sparql = SPARQLWrapper2(sparqlEndpoint)
    query = "PREFIX iri: <" + prefix + "> \n"
    query += (
        "SELECT ?property ?object \nWHERE { iri:" + entity + " ?property ?object. }"
    )
    sparql.setQuery(query)
    for result in sparql.query().bindings:
        resultProperty = result["property"].value
        resultObject = result["object"].value
        if resultProperty in response.keys():
            response[resultProperty].append(resultObject)
        else:
            response[resultProperty] = [resultObject]
    return response


async def getInverseSparqlData(sparqlEndpoint, prefix, entity):
    sparqlEndpoint = sparqlEndpoint.replace("localhost", "host.docker.internal")
    sparqlEndpoint = sparqlEndpoint.replace("127.0.0.1", "host.docker.internal")
    response = {}
    sparql = SPARQLWrapper2(sparqlEndpoint)
    query = "PREFIX iri: <" + prefix + "> \n"
    query += (
        "SELECT ?property ?subject \nWHERE { ?subject ?property iri:" + entity + ". }"
    )
    sparql.setQuery(query)
    for result in sparql.query().bindings:
        resultProperty = result["property"].value
        resultSubject = result["subject"].value
        if resultProperty in response.keys():
            response[resultProperty].append(resultSubject)
        else:
            response[resultProperty] = [resultSubject]
    return response


def prefixReplace(sparqlEndpoint, value):
    prefixes = loadPrefixes()
    for iri, prefix in prefixes.items():
        if iri in value:
            entity = value.replace(iri, "")
            return (
                "<a href=?sparqlendpoint="
                + urllib.parse.quote_plus(sparqlEndpoint)
                + "&iri="
                + urllib.parse.quote_plus(iri)
                + "&entity="
                + entity
                + ">"
                + value.replace(iri, prefix + ":")
                + "</a>"
            )
    return value


def loadPrefixes():
    f = open("./prefixes.json")
    prefixes = json.load(f)
    f.close()
    if LOCALPREFIX != "" and LOCALIRI != "":
        prefixes[LOCALIRI] = LOCALPREFIX
    return prefixes
