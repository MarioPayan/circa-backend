from fastapi import APIRouter
from fastapi import HTTPException
from fastapi.responses import HTMLResponse
from typing import List
from models import Coffee, Variety
from vars import base_url
from data import data

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def get_endpoints():
    links = []
    for route in router.routes:
        if hasattr(route, "methods"):
            full_path = f"{base_url}{route.path}"
            link = f'<a href="{full_path}">{full_path}</a><br>'
            links.append(link)
    html_content = "<h2>Clickable Endpoints:</h2>" + "".join(links)
    return HTMLResponse(content=html_content)


@router.get("/coffee/", response_model=List[Coffee])
async def get_coffees():
    return data.get_coffees()


@router.get("/coffee/{slug}", response_model=Coffee)
async def get_coffee(slug: str):
    coffee = data.get_coffee_by_slug(slug)
    if not coffee:
        raise HTTPException(status_code=404, detail="Coffee not found")
    return coffee


@router.get("/variety/", response_model=List[Variety])
async def get_varieties():
    return data.get_varieties()


@router.get("/variety/{slug}", response_model=Variety)
async def get_variety(slug: str):
    variety = data.get_variety_by_slug(slug)
    if not variety:
        raise HTTPException(status_code=404, detail="Variety not found")
    return variety
