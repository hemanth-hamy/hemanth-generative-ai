#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Start the backend server in the background
uvicorn app:app --host 0.0.0.0 --port 8000 &

# Start the frontend server in the foreground
streamlit run ui.py --server.port 10000
