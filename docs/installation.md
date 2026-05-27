# 🛠️ Installation

Because this setup uses Waybar from a non-standard directory (`~/.config/waybar3`) to avoid conflicts with other compositors, symlinking is crucial.

## Prerequisites

**Core:**
- `qtile` (Compiled with Wayland backend)
- `waybar`
- `rofi`
- `swaync` (Notification center)

**Utilities:**
- `st` (Default terminal emulator)
- `brightnessctl` (Backlight)
- `amixer` / `alsa-utils` (Volume control)
- `grim` (Screenshots)
- `playerctl` (Media widget)

## Deploying the Config

1. Clone the repository:
        
        git clone https://codeberg.org/WgpArch/qtile-wayland.git ~/.dotfiles/qtile-wayland

2. Symlink the Qtile configuration:
        
        ln -sf ~/.dotfiles/qtile-wayland/configs/qtile ~/.config/qtile

3. Symlink the Waybar configuration (Crucial step!):
        
        ln -sf ~/.dotfiles/qtile-wayland/configs/waybar3 ~/.config/waybar3

4. Ensure scripts are executable:
        
        chmod +x ~/.config/qtile/rofi/*.sh
        chmod +x ~/.config/qtile/scripts/*.sh
        chmod +x ~/.config/waybar3/scripts/*.sh
