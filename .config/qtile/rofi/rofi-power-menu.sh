#!/bin/bash

# Qtile Power Menu - Cayan Theme
LOCK="hyprlock"             
POWEROFF="systemctl poweroff"
REBOOT="systemctl reboot"
SUSPEND="systemctl suspend"
LOGOUT="qtile cmd-obj -o cmd -f shutdown"  

options="⏻ Shutdown\n🔄 Reboot\n🔒 Lock\n😴 Suspend\n🚪 Logout"

# Show rofi menu with inline theme
choice=$(echo -e "$options" | rofi -dmenu -p "Power" -i \
    -theme-str 'window {width: 450px; border: 2px; border-color: #00ffff; background-color: #000000;}' \
    -theme-str 'listview {lines: 5; background-color: #000000;}' \
    -theme-str 'element {background-color: #000000; text-color: #00ffff ; padding: 12px;}' \
    -theme-str 'element selected {background-color: #ffffff; text-color: #00ffff;}' \
    -theme-str 'element-text {font: "Z003 Nerd Font 12";}' \
    -theme-str 'prompt {background-color: #000000; text-color: #00ffff;}' \
    -theme-str 'entry {background-color: #000000; text-color: #00ffff;}' \
    -theme-str '* {font: "Z003 Nerd Font 12"; background: #000000; text-color: #00ffff;}')

case $choice in
    *"Shutdown"*) $POWEROFF ;;
    *"Reboot"*) $REBOOT ;;
    *"Lock"*) $LOCK ;;
    *"Suspend"*) $SUSPEND ;;
    *"Logout"*) $LOGOUT ;;
esac
