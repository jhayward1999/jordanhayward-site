from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

TOOLS: list[dict] = []

@app.get("/", response_class=HTMLResponse)
def homepage(request: Request) -> str:
    return templates.TemplateResponse(
        request,
        "home.html",
        {"request": request, "name": "Jordan Hayward", "tools": TOOLS},
    )
