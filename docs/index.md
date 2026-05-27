<div align="center">
  <img src="https://img.shields.io/badge/Arch_Linux-1793D1?style=for-the-badge&logo=arch-linux&logoColor=white" alt="Arch Linux">
  <img src="https://img.shields.io/badge/Wayland-00B4F0?style=for-the-badge&logo=wayland&logoColor=white" alt="Wayland">
  <img src="https://img.shields.io/badge/Qtile-00B4F0?style=for-the-badge&logo=python&logoColor=white" alt="Qtile">
  <img src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge" alt="License">
</div>

# 🏠 Welcome to my Qtile Wayland Config

A fully Python-based tiling Window Manager running natively on Wayland. This configuration features a custom **Waybar integration bridge** that pipes Qtile's workspace data to Waybar, a suite of 12 layouts, and custom Rofi menus.

![Qtile Showcase](screenshots/Screenshot_2026-05-24_19-46-51.png)

## ✨ Highlights
- **Custom Waybar Bridge:** A Python hook writes workspace states to `/tmp/qtile-groups.txt` and signals Waybar, allowing full workspace integration that isn't natively supported.
- **11 Workspaces:** Mapped across standard keys (1-9, 0, and minus), plus a ScratchPad dropdown for `bpytop`.
- **12 Layouts:** Including MonadTall/Wide, Bsp, TreeTab, Matrix, and Columns.
- **Cyan Accent Theme:** A cohesive `#00ffff` accent color across borders, bars, and menus.
