from pydantic import BaseModel
from typing import List, Union


class BaseLink(BaseModel):
    link: str
    expire: float = 0


class CreateLink(BaseLink):
    expired: bool = False


class UpdateLink(BaseModel):
    link: str = None


class ResponseLink(BaseLink):
    views: int
    key: str


class ListResponseLink(BaseLink):
    _count: int
    _last: Union[int, None]
    _items: List[ResponseLink]
