# Chatbot
Allows to save chat history of converation between human and assistant(like chatgpt) by using adaptive memory powered by Redis datastore.

# Getting Started
1. Get your `OpenAI` API key [here](https://platform.openai.com/overview).
2. Copy env.example .env (set fastapi webserver workers and openai api key)
    `cp env.example .env`
3. docker-compose up -d

# Testing
checkout fast api swagger.
http://0.0.0.0:8012/docs
