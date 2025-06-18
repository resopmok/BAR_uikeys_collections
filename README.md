# BAR Hotkey Collection
This repository is meant to help players customize their keybinds for BAR. 
The files here are intended to provide drop-in custom presets, or to serve as reference for more specific customizations.
Please refer to the HOWTO and FAQ as documentation, and come find us on the official BAR discord in #keybind-help for more information and assistance.
- The .png's are visual layouts of the grid optimized layout, available in-game.
- custom_army_selection is an amalgam of selection keys players have found useful.
- old files are incomplete but may contain interesting binds and historical reference.

## How to install/use

> [!WARNING]
> When using your file browser, make sure the extensions are not hidden, so you don't create a `uikeys.txt.txt` file for example.

Make sure to download the desired file, named as `uikeys.txt` in your install folder (the same directory as `springsettings.cfg`).

If there's already a `uikeys.txt` file present, you can rename that file to a backup (e.g. `uikeys.backup.txt`) and do above.

For more specific instruction, see:
- [Custom keybind guide](keybind-guide.md)
- [Custom keybind FAQ](keybind-faq.md)

For keymaps of the shipped presets, check the preset-images directory.

### Windows users


# Built-in hotkey files
With the uikeys hotkey format it is possible to import other keybind files with all their binds with the `keyload` command. 
This can be done with any keybind file in the uikeys format. To import the keybind files included in the base game, use this reference:

| Keyload String                                        | Reference                                                                                                                                                       |
|-------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `keyload luaui/configs/hotkeys/grid_keys.txt`         | [Grid layout keybinds](https://github.com/beyond-all-reason/Beyond-All-Reason/blob/master/luaui/configs/hotkeys/grid_keys.txt)                                  |
| `keyload luaui/configs/hotkeys/grid_keys_60pct.txt`   | [Grid layout keybinds for 60% keyboards](https://github.com/beyond-all-reason/Beyond-All-Reason/blob/master/luaui/configs/hotkeys/grid_keys_60pct.txt)          |
| `keyload luaui/configs/hotkeys/gridmenu_keys.txt`     | [Gridmenu hotkeys](https://github.com/beyond-all-reason/Beyond-All-Reason/blob/master/luaui/configs/hotkeys/gridmenu_keys.txt) (ONLY includes building hotkeys) |
| `keyload luaui/configs/hotkeys/legacy_keys.txt`       | [Legacy keybinds ](https://github.com/beyond-all-reason/Beyond-All-Reason/blob/master/luaui/configs/hotkeys/legacy_keys.txt)                                    |
| `keyload luaui/configs/hotkeys/legacy_keys_60pct.txt` | [Legacy keybinds for 60% keyboards](https://github.com/beyond-all-reason/Beyond-All-Reason/blob/master/luaui/configs/hotkeys/legacy_keys_60pct.txt)             |
| `keyload luaui/configs/hotkeys/num_keys.txt`          | [Control group hotkeys](https://github.com/beyond-all-reason/Beyond-All-Reason/blob/master/luaui/configs/hotkeys/num_keys.txt)                                  |


This can be used to very easily compose together modular keybind sets, for example to combine legacy hotkeys with the gridmenu building keys, you can make a `uikeys.txt` file containing only these lines:
```
unbindall
keyload luaui/configs/hotkeys/gridmenu_keys.txt
keyload luaui/configs/hotkeys/legacy_keys.txt
```

# Keybind reference
https://github.com/beyond-all-reason/spring/blob/BAR105/doc/uikeys.txt

# VS Code extension
https://marketplace.visualstudio.com/items?itemName=nbusseneau.vscode-uikeys
