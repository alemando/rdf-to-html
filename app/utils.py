import json
from SPARQLWrapper import SPARQLWrapper2

async def getSparqlData(sparqlEndpoint, prefix, entity):
    response = {}
    sparql = SPARQLWrapper2(sparqlEndpoint)
    query = "PREFIX iri: <"+ prefix +"> \n"
    query += "SELECT ?property ?object \n WHERE { iri:"+ entity +" ?property ?object. }"
    sparql.setQuery(query)
    for result in sparql.query().bindings:
        resultProperty = result['property'].value
        resultObject = result['object'].value
        if resultProperty in response.keys():
            response[resultProperty].append(resultObject) 
        else:
            response[resultProperty] = [resultObject]
    return response

def prefixReplace(sparqlEndpoint, value):
    prefixes = loadPrefixes()
    for iri, prefix in prefixes.items():
        if (iri in value):
            entity = value.replace(iri, "")
            return "<a href=?sparqlendpoint="+sparqlEndpoint+"&iri="+iri+"&entity="+entity+">"+value.replace(iri, prefix + ":")+"</a>"
    return value

def loadPrefixes():
    f = open('../prefixes.json')
    prefixes = json.load(f)
    f.close()
    return prefixes