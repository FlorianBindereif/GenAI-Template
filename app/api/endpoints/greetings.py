from fastapi import APIRouter, Depends, status
from fastapi.exceptions import HTTPException

from app.api.schemas.greetings import GreetingRequest, GreetingResponse
from app.core.greetings_service import GreetingsService, get_greetings_service

router = APIRouter()


@router.post(
    "/greet",
    response_model=GreetingResponse,
    status_code=status.HTTP_200_OK,
    summary="Generate a custom greeting",
    description="This endpoint generates a greeting with a specific tone for a given user.",
    tags=["greetings"],
)
def generate_greeting(
    request: GreetingRequest,
    # ruff flags a function call as an argument default - this however is the traditional FastApi way.
    # in cases like these we can use the noqa argument to make the code check ignore it
    service: GreetingsService = Depends(get_greetings_service), # noqa: B008
) -> GreetingResponse:
    """
    Generates a greeting based on the provided username and tone.
    - **username**: The name of the user to greet.
    - **tone**: The desired tone for the greeting.
    """
    try:
        greeting: str = service.generate_greeting(tone=request.tone, user_name=request.username)
        return GreetingResponse(greeting=greeting)
    except FileNotFoundError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"The template '{service.template_name}' was not found.",
        )
