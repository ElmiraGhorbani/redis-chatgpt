import json

import redis


class RedisManager:
    """
    this class is used to manage the redis connection 
    """

    def __init__(self, host, port):
        self.host = host
        self.port = port
        try:
            self.redis_con = redis.StrictRedis(
                host=self.host, port=self.port
            )
        except Exception as e:
            raise Exception('could not create redis connection: {e}')

    def get_data(self, key):
        """
        this function is used to get the data from redis
        :param key: the redis key
        :return: the data
        """
        data = self.redis_con.get(key)
        data = json.loads(data)
        return data

    def set_data(self, key, data):
        """
        this function is used to set the data to redis
        :param key: the redis key
        :param data: the data
        :return:None
        """
        self.redis_con.set(
            key,
            json.dumps(data).encode('utf-8'),
        )

    def truncate_conversation(self, key, overwrite=True):
        """
        Truncate the conversation in order to handle Max Tokens issue in case you are saving chat history.
        :param key: the redis key
        :param overwrite: user can choose whether overwrite the redis value, or not
        :return: redis value
        """
        # Don't remove the first message because it contains system prompt
        data = self.get_data(key)
        data.pop(1)
        if overwrite:
            self.set_data(key, data)
        return data
