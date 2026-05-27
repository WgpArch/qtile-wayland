# 🎨 Look & Feel

This Qtile config utilizes a cohesive Cyan (`#00ffff`) accent theming across all elements, with a suite of 12 different layouts to suit any workflow.

## General Appearance
- **Accent Color:** `#00ffff` (Cyan) used for active borders, group highlights, and bar widgets.
- **Border Width:** 2px on all layouts.
- **Margins:** 4px on Monad and ThreeCol layouts.

## Layouts Available
1. **Floating**
2. **MonadTall** (Default master-stack)
3. **MonadWide** (Horizontal master-stack)
4. **MonadThreeCol** (Three column master)
5. **Bsp** (Binary Space Partitioning)
6. **RatioTile** (Proportional tiling)
7. **Tile** (Standard columns)
8. **VerticalTile** (Standard rows)
9. **Columns** (Stacked columns)
10. **Stack** (Two stacked columns)
11. **Matrix** (Grid layout)
12. **TreeTab** (Sidebar tree with sections)

## Floating Rules
The following applications are automatically set to float:
- Confirm Reset dialogs, SSH-askpass, Pinentry
- Qalculate!, VNC Viewer, Xterm, Feh

## ScratchPad
A hidden scratchpad is bound to group `scratchpad`, which automatically launches `bpytop` in a dropdown terminal taking up 75% of the screen height.

## Autostart
Applications are spawned via `~/.config/qtile/scripts/autostart.sh` on login.
