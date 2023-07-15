#!/bin/bash
echo ">> API Started <<" 
uvicorn --workers 1 --host 0.0.0.0 scripts.app:app