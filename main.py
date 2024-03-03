from fastapi import FastAPI
from routers.SF6 import sf6_endpoints

app = FastAPI()

# Routers

@app.get("/")

def welcome():
    return '''Welcome to the Fighting Game API! Please visit our documentation: (GH documentation) or url/docs for information about the endpoints of the API.'''

app.include_router(sf6_endpoints.sf6_router)