#!/bin/bash

python setup.py sdist bdist_wheel
pip install dist/redis_chatgpt-1.0.tar.gz
