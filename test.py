from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
import uvicorn

from src.config import settings
from src.auth.router import userRouter
from fastapi.staticfiles import StaticFiles
from src.exceptions import AnsibleException
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)
from src.auth.exceptions import UserErrorMapping
from src.utils import resp_400_exception
import uvicorn
from service_test import test_raise_exception
app = FastAPI(docs_url=None, redoc_url=None)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
    )


@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()


@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title + " - ReDoc",
        redoc_js_url="/static/redoc.standalone.js",
    )


        

class ItemNotFoundException(Exception):
    def __init__(self, item_id: int):
        self.item_id = item_id

@app.exception_handler(ItemNotFoundException)
async def item_not_found_exception_handler(request: Request, exc: ItemNotFoundException):
    return JSONResponse(
        status_code=404,
        content={"message": f"Item with id {exc.item_id} not found"},
    )



@app.exception_handler(AnsibleException)
async def item_not_found_exception_handler(request: Request, ex: AnsibleException):
    print(ex)
    return resp_400_exception(errMapping=ex.errorMapping,data="hello")



@app.get("/items/{item_id}")
async def read_item(item_id: int):
    if item_id != 1:
        raise ItemNotFoundException(item_id=item_id)
    return {"item_id": item_id}

@app.get("/tests/{test_id}")
async def test1(test_id: int):
    if test_id != 1:
        test_raise_exception()
    return {"item_id": test_id}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=2223)