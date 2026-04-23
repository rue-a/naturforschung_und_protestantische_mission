#!/usr/bin/env bash
# Serve the project locally at http://localhost:8080
# Required because fetch() cannot load local files over file:// protocol.
python -m http.server 8080
