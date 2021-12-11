
from fastapi import FastAPI, HTTPException, Request, Form, Query
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from app.api import router
from app.db import db
from app.settings import setting


template = Jinja2Templates('templates')

app = FastAPI(title='fastapi-url-shortener', version=1.0)

app.include_router(router)

HOST = setting.HOST

@app.get("/robots.txt")
async def robots_txt():
    return ''


@app.get("/")
async def short_link(request: Request):
    return template.TemplateResponse('index.html', context={'request': request, 'site': HOST})


@app.post("/")
async def add_link(request: Request, u: str = Form(...)):
    link = u.strip()
    link_check = db.fetch({'link': link})
    if link_check.items:
        return template.TemplateResponse('info.html', context={'request': request, 'site': HOST, 'link': link_check.items[0]})
    link = db.put({"link": link, 'views': 0})
    return template.TemplateResponse('info.html', context={'request': request, 'site': HOST, 'link': link})


@app.get("/views")
async def short_link_views(request: Request, u: str = Query(None)):
    if u:
        key = u.strip()[-12:]
        link = db.get(key=key)
        if link:
            return template.TemplateResponse('views.html', context={'request': request, 'link': link, 'site': HOST})
        else:
            raise HTTPException(status_code=404, detail='Key is Not Valid')
    return template.TemplateResponse('check.html', context={'request': request, 'site': HOST})


@app.get("/{key}")
async def short_link(key: str):
    link = db.get(key=key)
    if not link:
        raise HTTPException(status_code=404, detail='Key is Not Valid')
    db.update(updates={'views': link.get('views')+1}, key=key)
    return RedirectResponse(link.get('link'))


