#!/bin/bash
read -p "Name the task: " choice

cd tasks/ && touch "$choice.sh"

echo "Edit the file as you need in 3s"
sleep 3

nano "$choice.sh"