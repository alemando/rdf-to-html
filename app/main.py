import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

load_dotenv()

DEFAULT_SPARQL_ENDPOINT = os.getenv("DEFAULT_SPARQL_ENDPOINT")
DEFAULT_IRI_NAMESPACE = os.getenv("DEFAULT_IRI_NAMESPACE")
DEFAULT_ENTITY = os.getenv("DEFAULT_ENTITY")

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get(
    "/",
    responses={
        404: {"description": "Entity not found"},
    },
    response_class=HTMLResponse,
)
async def root(request: Request, iri: str = DEFAULT_IRI_NAMESPACE, entity: str = None):
    if entity:
        return templates.TemplateResponse(
            "resource.html",
            {
                "request": request,
                "iri": iri,
                "entity": entity,
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
        # raise HTTPException(status_code=404, detail="Entity not found")
