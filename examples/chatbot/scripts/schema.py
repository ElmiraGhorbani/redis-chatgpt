from pydantic import BaseModel


class ChatBotRequest(BaseModel):
    user_input: str = ""
