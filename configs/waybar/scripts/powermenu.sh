#!/bin/bash
dir="$HOME/.config/waybar3/scripts"
theme='power'

uptime="$(uptime -p | sed -e 's/up //g')"
host="$(uname -n)"

shutdown='  Shutdown'
reboot='  Reboot'
lock=' Lock'
suspend='  Suspend'
logout='   Logout'

rofi_cmd() {
    rofi -dmenu \
        -p "$host" \
        -mesg "Uptime: $uptime" \
        -theme ${dir}/${theme}.rasi \
        -hover-select \
        -me-select-entry "" \
        -kb-cancel Escape \
        -layer overlay \
        -me-accept-entry MousePrimary
}

chosen="$(echo -e "$lock\n$suspend\n$logout\n$reboot\n$shutdown" | rofi_cmd)"

case ${chosen} in
    "$shutdown") systemctl poweroff ;;
    "$reboot") systemctl reboot ;;
    "$suspend") systemctl suspend ;;
    "$logout") pkill strata ;;
    "$lock") swaylock -f -c 000000 ;;
esac
