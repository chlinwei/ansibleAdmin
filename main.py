from fastapi import FastAPI
from src.auth.router import userRouter
from fastapi.staticfiles import StaticFiles
from src.exceptions import AnsibleException,AnsibleAdminExceptionHandler
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)
import sys
from loguru import logger
from src.config import settings
import uvicorn

app = FastAPI(docs_url=None, redoc_url=None)

#日志配置
logger.add(settings.loggerSetting.LOG_DIR)
logger.add(sys.stderr, format="{time} {level} {message}",  level=settings.loggerSetting.LOG_LEVEL)

#全局异常
app.add_exception_handler(AnsibleException,AnsibleAdminExceptionHandler)

#静态资源
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

app.include_router(router=userRouter)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=2223)