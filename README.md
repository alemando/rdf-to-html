# RDF TO HTML

RDF TO HTML is a python web application that offer to publish RDF data to HTML web pages.

## Installation

### Local Installatioon

First Execute in the root of the project

```
pip install -r requirements.txt
```

Then go to app folder

```
cd app
```

And execute

```
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Docker Installatioon

Just execute

```
docker compose up
```

Wait and connect to http://localhost:8000/

## Configuration

Configure the prefixes that your ontology uses in order to enable navigation, modify prefixes.json file and add your prefixes.
Optional: You can use env variables to put some default values, or copy the file .env.example and start using it.

## How to use it

Put an sparql endpoint url, a iri namespace and an entity to start browsing the data.
