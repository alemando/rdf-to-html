import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from utils import *

load_dotenv()

DEFAULT_SPARQL_ENDPOINT = os.getenv("DEFAULT_SPARQL_ENDPOINT", "")
DEFAULT_IRI_NAMESPACE = os.getenv("DEFAULT_IRI_NAMESPACE", "")
DEFAULT_ENTITY = os.getenv("DEFAULT_ENTITY", "")



app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")
templates.env.globals.update(prefixReplace=prefixReplace)

@app.get(
    "/",
    response_class=HTMLResponse,
)
async def root(request: Request, sparqlendpoint:str = DEFAULT_SPARQL_ENDPOINT, iri: str = DEFAULT_IRI_NAMESPACE, entity: str = None):
    if entity:
        response = await getSparqlData(sparqlendpoint, iri, entity)
        iri = f"<{iri}{entity}>"
        return templates.TemplateResponse(
            "resource.html",
            {
                "request": request,
                "sparqlEndpoint": sparqlendpoint,
                "iri": iri,
                "entity": entity,
                "properties": response,
            },
        )
    else:
        return templates.TemplateResponse(
            "index.html",
            {
                "request": request,
                "sparqlEndpoint": DEFAULT_SPARQL_ENDPOINT,
                "iri": DEFAULT_IRI_NAMESPACE,
                "entity": DEFAULT_ENTITY,
            },
        ) 