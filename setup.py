from setuptools import find_packages, setup

project_urls = {
  'Github': 'https://github.com/ElmiraGhorbani/redis-chatgpt',
}

setup(
    name='redis_chatgpt',
    version='0.1.0',
    author='Elmira Ghorbani',
    description='A user-friendly package designed to save chat history conversation and truncate conversation if user exceeds max token when using OpenAI chat completion.',
    packages=find_packages(),
    install_requires=[
        'redis>=4.6.0'
    ],
    project_urls=project_urls
)
