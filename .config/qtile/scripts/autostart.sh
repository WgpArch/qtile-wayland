#!/usr/bin/env bash

# wallpaper
swaybg -m fill -i ~/.config/qtile/wallpapers/TurquoiseTechnics.jpg &
waybar -c ~/.config/waybar3/config.jsonc -s ~/.config/waybar3/style.css &
nm-applet --indicator &
swaync &
