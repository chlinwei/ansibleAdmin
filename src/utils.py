from fastapi import status
from fastapi.responses import JSONResponse,Response
from typing import Union
from src.exceptions import BaseException

def resp_200(*,data: Union[list,dict,str]) -> Response:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'code': 200,
            'message': "Success",
            'data': data,
        }
    )


def resp_400_exception(*,data: Union[list,dict,str] = None, baseException: BaseException) -> Response:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            'code': baseException.code,
            'message': baseException.message,
            'data': data,
        }
    )

