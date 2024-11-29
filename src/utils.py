from fastapi import status
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from typing import Generic,TypeVar,Optional
from src.errorMapping import ErrorMapping
from typing import Any

T = TypeVar('T')
class ResponseModel(BaseModel,Generic[T]):
    code: int
    message: str
    data: Optional[T]

def resp_200(*,data: Optional[T]) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder(ResponseModel(code=200,message="success",data=data))
    )


def resp_400_exception(*,data: Any | None , errMapping: ErrorMapping) -> JSONResponse:
    print(f"==============================data:{data} =========================")
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder(ResponseModel(code=errMapping.code,message=errMapping.message,data=data))
    )



