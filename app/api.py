
from fastapi import HTTPException, APIRouter

from app import schemas
from app.db import db

router = APIRouter(prefix='/api',tags=['Api'])

@router.get("/")
async def getList():
    return db.fetch()

@router.post("/", response_model=schemas.ResponseLink)
async def addLink(link: schemas.CreateLink):
    result = db.put({"link": link.link.strip(), 'views': 0})
    return result

@router.put("/{key}", response_model=schemas.ResponseLink)
async def updateLink(updatelink: schemas.UpdateLink, key: str):
    link = db.get(key=key)
    if link:
        db.update({"link": updatelink.link.strip()}, key=key)
        return db.get(key=key)
    else:
        raise HTTPException(status_code=404, detail='Key is Not Valid')


@router.delete("/{key}")
async def deleteLink(key: str):
    link = db.get(key=key)
    if link:
        return db.delete(key=key)
    else:
        raise HTTPException(status_code=404, detail='Key is Not Valid')


@router.get("/{key}", )  # response_model=schemas.ResponseLink)
async def shortLink(key: str):
    link = db.get(key=key)
    if link:
        return link
    else:
        raise HTTPException(status_code=404, detail='Key is Not Valid')
