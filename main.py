import uvicorn
from fastapi import FastAPI

from posts import router as posts_router

app = FastAPI(title="Emilia EMM Backend")
app.include_router(posts_router)


if __name__ == "__main__":
    uvicorn.run("main:app", workers=1, host="0.0.0.0", port=8000, reload=True)
