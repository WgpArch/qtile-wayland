# 🙏 Credits & Attribution

This Qtile Wayland configuration was built using knowledge and code from the following excellent repositories. Without their work, the Waybar integration and Rofi menus would not have been possible.

## stefur/qtile-config
**[GitHub Repository](https://github.com/stefur/qtile-config/blob/main/README.md)**

The logic for bridging Qtile's workspace data to Waybar was heavily inspired by and adapted from stefur's configuration. The method of writing Pango-marked text to a temporary file (`/tmp/qtile-groups.txt`) and signaling Waybar via `pkill -RTMIN+8` was the crucial workaround needed to make Waybar display Qtile workspaces correctly on Wayland.

## ahmad-shaban/qtile
**[GitHub Repository](https://github.com/ahmad-shaban/qtile)**

The Rofi launcher and power menu scripts used in this setup were adapted from ahmad-shaban's Qtile configuration. While originally used for an X11 Qtile setup, the scripts translated perfectly to the Wayland environment with minor path adjustments.
