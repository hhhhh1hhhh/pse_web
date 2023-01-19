from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI()  # fastAPI에는 app을 싱글톤 패턴을 사용해서 하나 찍어냄
templates = Jinja2Templates(
    directory=BASE_DIR / "templates"
)  # templates에는 해당하는 html 파일의 위치를 지정함

app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "static"),
    name="static",
)


"""
app.get은 하나의 라우터
여기서 라우터는 요청을 받고 해당하는 logic을 따라서 응답을 해주는 것
response_class=HTMLResponse: response를 해줬을 때 response 타입을 htmlResponse로 지정한 것
"""


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    """
    templeates 폴더 안에 TemplateResponse 클래스가 있는데, 클래스를 사용해서 리턴함
    첫 번째 인자는 index.html, 두 번째 인자는 보내고 싶은 데이터
    """
    return templates.TemplateResponse(
        "./start.html",
        {"request": request, "title": "Python is So Easy"},
    )


@app.get("/login", response_class=HTMLResponse)
async def login(request: Request):

    return templates.TemplateResponse(
        "/login.html",
        {"request": request, "title": "Python is So Easy"},
    )


@app.get("/home", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        "/home.html",
        {"request": request, "title": "Python is So Easy"},
    )


@app.get("/comm", response_class=HTMLResponse)
async def community(request: Request):

    return templates.TemplateResponse(
        "/comm.html",
        {"request": request, "title": "Python is So Easy"},
    )
