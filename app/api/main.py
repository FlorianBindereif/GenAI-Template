from fastapi import FastAPI
from app.api.endpoints import greetings
from app.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION
)
app.include_router(greetings.router, prefix=settings.API_PREFIX)

@app.get("/", tags=["Root"])
def read_root():
    """
    Root endpoint to confirm the API is running.
    Provides a simple welcome message.
    """
    return {"message": f"Welcome to the {settings.APP_NAME}!"}