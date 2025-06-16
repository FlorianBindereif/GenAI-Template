from typing import Annotated

from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException

from app.api.schemas.greetings import GreetingRequest, GreetingResponse
from app.core.greetings_service import GreetingsService, get_greetings_service

router = APIRouter()


@router.post(
    "/greet",
    status_code=status.HTTP_200_OK,
    summary="Generate a custom greeting",
    description="This endpoint generates a greeting with a specific tone for a given user.",
    tags=["greetings"],
)
def generate_greeting(
    request: GreetingRequest,
    # pyright flags Annotated as not assignable to type GreetingsService- this however is best-practice for FastApi.
    # in cases like these we can use # ignore make pyright ignore this specific line
    service: GreetingsService = Annotated[GreetingsService, Depends(get_greetings_service)],  # type: ignore[reportArgumentType]
) -> GreetingResponse:
    """
    Generates a greeting based on the provided username and tone.
    - **username**: The name of the user to greet.
    - **tone**: The desired tone for the greeting.
    """
    try:
        greeting: str = service.generate_greeting(tone=request.tone, user_name=request.username)
        return GreetingResponse(greeting=greeting)
    except FileNotFoundError as err:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"The template '{service.template_name}' was not found.",
        ) from err
