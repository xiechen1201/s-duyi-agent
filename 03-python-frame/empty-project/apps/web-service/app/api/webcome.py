from fastapi import APIRouter

router = APIRouter()


# 定义路由
@router.get("/")
def read_root():
    return {"Hello": "World"}
