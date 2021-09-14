#!/usr/bin/env bash
mkdir ~/.config/Max
cp -r . ~/.config/Max
sudo cp -r assets/ /bin/
sudo cp max /bin/
sudo chmod +x /bin/max
sudo cp max_gui /bin/
sudo chmod +x /bin/max_gui
