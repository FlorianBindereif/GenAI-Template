from fastapi import Depends
from jinja2 import Environment, Template

from app.models.greetings import Tone
from app.utils.jinja_utils import get_jinja_env


class GreetingsService:
    def __init__(self, jinja_env: Environment = Depends(get_jinja_env)) -> None:
        self.jinja_env = jinja_env
        self.template_name = "greeting_template.j2"

    def generate_greeting(self, tone: Tone, user_name: str) -> str:
        """
        Generates a tone-based message
        """
        template: Template = self.jinja_env.get_template(self.template_name)
        # This is an example service. This is where your GenAI logic would go.
        return template.render(tone=tone.value, username=user_name)
