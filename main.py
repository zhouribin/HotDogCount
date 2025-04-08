from fastapi import FastAPI
from opencv import getHotDogCount
from pydantic import BaseModel, HttpUrl
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


class HotDogRequest(BaseModel):
    image_url: HttpUrl  # 确保是合法的 URL


@app.post("/getHotDogCount")
async def count_hotdog(request: HotDogRequest):
    eggsCount = getHotDogCount(str(request.image_url))  # HttpUrl 需转字符串
    return {"HotDogCount": eggsCount}

if __name__ == "__main__":
    import uvicorn
    # 启动服务
    uvicorn.run(app, host="0.0.0.0", port=8000)
