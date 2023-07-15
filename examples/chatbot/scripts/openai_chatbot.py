import os

import openai

from .error_handler import retry_on_openai_errors

openai.api_key = os.environ.get(
    "OPENAI_API_KEY", "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"
)


PROMPT = """Assistant is a large language model trained by OpenAI.

    Assistant is designed to be able to assist with a wide range of tasks, from answering simple questions to providing in-depth explanations and discussions on a wide range of topics. As a language model, Assistant is able to generate human-like text based on the input it receives, allowing it to engage in natural-sounding conversations and provide responses that are coherent and relevant to the topic at hand.

    Assistant is constantly learning and improving, and its capabilities are constantly evolving. It is able to process and understand large amounts of text, and can use this knowledge to provide accurate and informative responses to a wide range of questions. Additionally, Assistant is able to generate its own text based on the input it receives, allowing it to engage in discussions and provide explanations and descriptions on a wide range of topics.

    Overall, Assistant is a powerful tool that can help with a wide range of tasks and provide valuable insights and information on a wide range of topics. Whether you need help with a specific question or just want to have a conversation about a particular topic, Assistant is here to assist.

    Human: {}
    Assistant:"""

class ChatApp:
    """
    This class is a wrapper for the OpenAI API and returns the chatbot response
    """

    def __init__(
        self, model_name: str = "gpt-4", max_tokens: int = 1000,
            temperature: int = 0, top_p: int = 1, presence_penalty: int = 0, frequency_penalty: int = 0):
        """
        This function initializes the chatbot
        """
        self.prompt = PROMPT.strip()
        self.max_tokens = max_tokens
        self.model = model_name
        self.temperature = temperature
        self.top_p = top_p
        self.presence_penalty = presence_penalty
        self.frequency_penalty = frequency_penalty

        self.chatbot_response = {
            "bot_response": "",
            "data": {
                "project_info": {
                }
            },
            "bot": {
                "bot_name": "gpt-4",
                "bot_state": "chat_completion"
            },
        }

    @retry_on_openai_errors(max_retry=3)
    def chat(self, user_input, chat_history=[]):
        """
        This function is a wrapper for the OpenAI API and returns the chatbot response and the chat history with the user as a list of dictionaries
        :param user_input: the user's query
        :param chat_history: The chat history with the user as a list of dictionaries
        :return: The chatbot response and the chat history with the user as a list of dictionaries
        """

        if chat_history:
            messages = chat_history
        else:
            messages = [
                {"role": "system", "content": self.prompt.format(user_input)},
            ]

        messages.append({"role": "user", "content": ""})

        response = openai.ChatCompletion.create(
            model=self.model,
            messages=messages,
            max_tokens=self.max_tokens,
            temperature=self.temperature,
            top_p=self.top_p,
            presence_penalty=self.presence_penalty,
            frequency_penalty=self.frequency_penalty,
        )
        messages.append(
            {"role": "assistant", "content": response["choices"][0]["message"].content})

        bot_response = response["choices"][0]["message"].to_dict()

        # retun openai response and messages
        result = self.chatbot_response
        result["bot_response"] = bot_response["content"]
        result["memory"] = messages
        return result
