from setuptools import find_packages, setup

setup(
    name='redis_chatgpt',
    version='0.1.0',
    author='Elmira Ghorbani',
    description='A user-friendly package designed to save chat history conversation and truncate conversation if user exceeds max token when using OpenAI chat completion.',
    packages=find_packages(),
    install_requires=[
        'redis>=4.6.0'
    ],
)
