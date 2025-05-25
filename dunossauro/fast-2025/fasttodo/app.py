from fastapi import FastAPI, status
from fastapi.responses import HTMLResponse

from fasttodo.schemas import Message
from fasttodo.static.htmls import ENDPOINT_HEALTH

app = FastAPI()


@app.get(path='/', status_code=status.HTTP_200_OK, response_model=Message)
def read_root():
    return {'message': 'Hello World'}


@app.get(
    path='/health', status_code=status.HTTP_200_OK, response_class=HTMLResponse
)
def health():
    return ENDPOINT_HEALTH
