#!/bin/bash

echo "Setting up Python environment..."

python3 -m venv .venv

./.venv/bin/pip install --upgrade pip

./.venv/bin/pip install -r requirements.txt

echo "Setup complete!"
echo "----- run -----"
echo "source .venv/bin/activate"