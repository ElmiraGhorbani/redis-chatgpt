# Redis Chatgpt
This package is a useful tool specifically developed for effectively handling chat message history. This Python package's primary goal is to provide a reliable, efficient, and simple method to store chat logs in a Redis database.

redis_chatgpt makes use of Redis, a fast, efficient, and highly scalable in-memory data structure store. By organizing and preserving the chat message history in Redis, users can retrieve message history promptly and easily with the best performance.

This package is the perfect solution if you need to store and recover chat histories effortlessly from the Redis Database. With redis_chatgpt, you can streamline your chat log management tasks while becoming more productive and efficient with your resources.

# Getting started
```
pip install redis-chatgpt
```

To build a simple data store:
```
from redis_chatgpt.manager import RedisManager

redis_db = RedisManager(host="localhost", port=6379)
```

Set data
```
redis_key = "chat_key"
chat_memory = [
    {
      "role": "system",
      "content": "Assistant is a large language model trained by OpenAI."
    },
    {
      "role": "assistant",
      "content": "Hello! How can I assist you today?"
    },
    {
      "role": "user",
      "content": "hi"
    },
]
redis_db.set_data(redis_key, chat_memory)

```


Get data
```
chat_history = redis_db.get_data(redis_key)

```

Truncate history(conversation)
```
# You can choose whether to update the Redis database or 
# not by specifying the 'overwrite' parameter (boolean).

data = redis_db.truncate_conversation(redis_key, overwrite=True)

```

### Use with FastAPI Swagger
`cd examples/chatbot`
1. Get your `OpenAI` API key [here](https://platform.openai.com/overview).
2. Copy env.example .env (set fastapi webserver workers and openai api key)
    `cp env.example .env`
3. `docker-compose up -d`
4. check out : `http://0.0.0.0:8012/docs`
