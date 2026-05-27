# 📊 Waybar Integration

Using Waybar with Qtile on Wayland is notoriously difficult because Waybar does not natively support Qtile's workspace API. This setup uses a custom Python bridge to make them communicate perfectly.

## The Bridge Mechanism

Inside `config.py`, there is a custom hook subscribed to focus changes, window creation, and window deletion:

    @hook.subscribe.focus_change
    @hook.subscribe.client_killed
    @hook.subscribe.client_managed
    def update_groups_waybar(*_args):

**How it works:**
1. When a window is focused, created, or destroyed, the hook fires.
2. It queries Qtile for all groups and their window counts.
3. It formats the group names using Pango markup (highlighting the active group with the cyan accent color).
4. It writes this formatted string to `/tmp/qtile-groups.txt`.
5. It sends a Unix signal (`pkill -RTMIN+8 waybar`) to tell Waybar to update.

## Waybar Configuration

Waybar is launched from `~/.config/waybar3` (kept separate to avoid breaking other compositor configs).

### Left
- **Custom Launcher:** Arch icon. Opens Rofi.
- **Custom Qtile Groups:** Reads `/tmp/qtile-groups.txt` on signal 8. Clicking cycles to the next group, scrolling goes prev/next.

### Center
- **Clock:** Date, time, and calendar.
- **Custom Weather:** Fetches weather via Ruby script.

### Right
- **CPU, Memory, Temperature:** Hardware monitors.
- **Battery:** Percentage and status.
- **Pulseaudio:** Volume control.
- **Custom Player:** 🎵 Media playback via `playerctl`.
- **Custom Notification:** SwayNC.
- **Custom Power:** Rofi power menu.
- **Tray:** System tray.

## 📜 Key Scripts

Located in `~/.config/waybar3/scripts/`:

| Script | Description |
| :--- | :--- |
| `workspace-click.sh` / `ws-click.sh` | Handlers for clicking workspace numbers in Waybar. |
| `weather.py` | Fetches weather data. |
| `launcher.sh` / `powermenu.sh` | Rofi launchers. |
