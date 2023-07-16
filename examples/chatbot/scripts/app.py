import logging

from fastapi import FastAPI, HTTPException

from redis_chatgpt.manager import RedisManager

from .openai_chatbot import ChatApp
from .schema import ChatBotRequest

redis_db = RedisManager(host="redis_chatgpt", port=6379)

chat_app = ChatApp()

tags_metadata = [
    {
        "name": "Chatbot",
        "description": "A wrapper for using OpenAI chatbot.",
    },

]

app = FastAPI(
    title="Chatbot",
    description="This API serves as a wrapper for utilizing OpenAI chatbot models.",
    version="0.1.0",
    openapi_tags=tags_metadata,

)

logging.basicConfig(level=logging.INFO)

chat_responses = {
    200: {
        "description": "Return OpenAI chatbot response",
        "content": {
            "application/json": {
                "example": {
                    "bot_response": "you're welcome!",
                    "chat_summary": "",
                    "data": {
                        "project_info": {
                        }
                    },
                    "bot": {
                        "bot_name": "gpt-4",
                        "bot_state": "chat_completion"
                    },
                }
            }
        }
    },
}


@app.post("/user/{user_id}/chatbot", tags=["Chatbot"], responses=chat_responses)
async def chatbot(user_id: str, request: ChatBotRequest):
    try:
        redis_key = user_id + '_chatbot_history'
        try:
            chat_history = redis_db.get_data(redis_key)
        except:
            chat_history = []

        chat_response = chat_app.chat(
            chat_data=request.user_input, chat_history=chat_history)
        chat_memory = chat_response['memory']
        redis_db.set_data(redis_key, chat_memory)
        return chat_response
    except Exception as e:
        logging.error(f'/chatbot HTTP:/500, {str(e)}')
        raise HTTPException(status_code=500, detail=f"{str(e)}")
