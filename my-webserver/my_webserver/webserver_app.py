from pathlib import Path
import os
import logging

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

logging.basicConfig(level=logging.ERROR)


hostname = os.getenv("HOSTNAME", "test")
try:
    color = os.environ["COLOR"]
except Exception:
    logging.error("Oooops! Something went wrong :(")
    logging.error("Please set the 'COLOR' environment variable")
    logging.error(
        "'COLOR' = hex code of a color (including the #-sign example: '#00ff00')"
    )
    raise SystemExit(1)

app = FastAPI()

templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse(
        "page.html", {"request": request, "hostname": hostname, "color": color}
    )
