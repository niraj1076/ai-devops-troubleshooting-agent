#!/bin/bash

set -e

echo "======================================"
echo "   Remove Ollama + Qwen3"
echo "======================================"

echo
echo "[1/4] Stopping Ollama..."

sudo systemctl stop ollama 2>/dev/null || true
sudo systemctl stop snap.ollama.service 2>/dev/null || true

echo
echo "[2/4] Removing Ollama Snap package..."

if snap list ollama >/dev/null 2>&1; then
    sudo snap remove ollama --purge
else
    echo "Ollama Snap package is not installed."
fi

echo
echo "[3/4] Removing Ollama user data..."

rm -rf "$HOME/.ollama"

echo
echo "[4/4] Verifying removal..."

if snap list ollama >/dev/null 2>&1; then
    echo "WARNING: Ollama is still installed."
else
    echo "Ollama Snap successfully removed."
fi

if [ -d "$HOME/.ollama" ]; then
    echo "WARNING: ~/.ollama still exists."
else
    echo "Ollama model data removed."
fi

echo
echo "======================================"
echo "      Removal completed"
echo "======================================"

