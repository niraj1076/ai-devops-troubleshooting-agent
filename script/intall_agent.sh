#!/bin/bash

set -e

MODEL="qwen3:0.6b"

echo "======================================"
echo "   Ollama + Qwen3 Installation"
echo "======================================"

echo
echo "[1/4] Installing Ollama..."

if snap list ollama >/dev/null 2>&1; then
    echo "Ollama is already installed."
else
    sudo snap install ollama
fi

echo
echo "[2/4] Checking Ollama..."
ollama --version

echo
echo "[3/4] Downloading model: $MODEL"
ollama pull "$MODEL"

echo
echo "[4/4] Installed models:"
ollama list

echo
echo "======================================"
echo " Installation completed successfully"
echo "======================================"

echo
echo "To start Qwen3:"
echo "  ollama run $MODEL"
