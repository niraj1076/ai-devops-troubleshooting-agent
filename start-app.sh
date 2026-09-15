#!/bin/bash

set -e

echo "=========================================="
echo "        JARVIS STARTUP SCRIPT"
echo "=========================================="

echo ""
echo "[1/4] Activating Python environment..."

source venv/bin/activate

echo "Python:"
python --version
echo "Location:"
which python


echo ""
echo "[2/4] Installing Python requirements..."

pip install -r requirements.txt


echo ""
echo "[3/4] Setting up Ollama..."

chmod +x script/intall_agent.sh

./script/intall_agent.sh


echo ""
echo "Starting Ollama..."

if curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then

    echo "Ollama is already running."

else

    echo "Starting Ollama server..."

    nohup ollama serve > /tmp/ollama.log 2>&1 &

    echo "Waiting for Ollama..."

    for i in {1..30}; do

        if curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then
            echo "Ollama started successfully."
            break
        fi

        sleep 1

    done

fi


echo ""
echo "=========================================="
echo "           STARTING JARVIS"
echo "=========================================="

cd app

python main.py
