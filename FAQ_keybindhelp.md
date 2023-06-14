8 April 2023

# FAQs from #keybind-help

### How can I get camera pan on wasd?

1. Copy the contents of https://github.com/resopmok/BAR_uikeys_collections/blob/main/bar_hotkeys_custom_wasddefault.lua to a local file called `bar_hotkeys_custom.lua` in your game's data folder. Read the changes at the top of the file, and enable the layout in-game through Settings -> Control -> Keybinds -> Custom
2. If you want to create your own custom keyset with wasdpan, move commands off wasd according to your desires, and add this to your custom config file:
```
	{ "Any+sc_w",     "moveforward"  },
	{ "Any+sc_s",     "moveback"     },
	{ "Any+sc_d",     "moveright"    },
	{ "Any+sc_a",     "moveleft"     },
```
3. If you want to customize a wasdpan set with grid menu, ask @HoboJoe on the BAR official Discord channel #keybind-help.

### What is the "mnemonic" layout and should I use it?

There are "scancodes" in the config files that ensure the layout is positional ( if g were swapped with a, you would press g to atacck). The mnemonic layout is for people who have keyboard layouts different from qwerty but prefer their commands in their home keyboard's position instead (a would still attack, but that is located where g is on a qwerty keyboard).
This layout was made shortly after scancodes were introduced to keybindings to accomodate a few players who had learned the hotkeys in their home keyboard's layout. One colemak user in particular was very confused when pressing s caused his commander to dgun instead of stop.

### What is different about the 60% layouts? Do you have any images of the 60% layouts?

60% layouts are designed for players who have small mechanical gaming keyboards (they are roughly 60% the number of keys as a full-size keyboard). Typically, these keyboards lack F keys, and so these layouts have been modified to accomodate that. The majority of the change moves F key commands to a combination of spacebar and a number key. There are a few other changes too, so make sure to consult images or read the config files on the main repo (https://github.com/beyond-all-reason/Beyond-All-Reason/tree/master/luaui/configs). You can find images for all layouts, including default and grid 60% here: (https://github.com/resopmok/BAR_uikeys_collections/tree/main/keyboard_layout_pngs).

### How can I acces the widget list and why do I want to?

There may be an option in the in-game settings to enable the widget selector. If so, enable it, then press F11 to bring up the widget menu. If not, type `/widgetselector` into "everyone" chat. This menu is used to enable and disable custom widgets which you have installed in your `/data/LuaUI/Widgets/` directory. Some hotkey customizers use it to disable the "Bar Hotkey" widget if they use a uikeys.txt format config file.

### I want to invert the grid menu home row to QWER. How?

You can use this version of the grid opti config file (https://github.com/resopmok/BAR_uikeys_collections/blob/main/bar_hotkeys_custom_invertqwer.lua) to move your grid menu's home row from ZXCV to QWER. In this case, instead of the ZX keystrokes building you a solar, QW will do so. RA would build you a construction turret, and WS would be your basic anti-air. Currently we can't invert the actual layout of grid menu in game to accomodate, so your QWER row will still display in the same location on the menu that ZXCV was. The config also moves army selection, resurrect, repair, and reclaim order to ZXCV respectively.

### How do I invert map scrolling with the middle mouse button?

When using Spring camera (Ctrl+F3 in default binds, Ctrl+F6 in grid bindings): you can type `/set MouseInvert 1` into everyone chat and it will invert the camera scroll while holding down the middle mouse button.
When using TA (overhead) camera (Ctrl+F2 in default binds, Ctrl+F5 in grid bindings): when holding down middle mouse button to scroll, there is no option for inverting. If you enable "Middle click toggles camera move (Settings -> Control), you can use a mode which mode which will reverse with this middle mouse button click that activates mouse panning. To do that, type `/set MiddleClickScrollSpeed -0.01` into everyone chat.

### Can I rebind my mouse buttons, or add bindings for extended mouse buttons?

Keybinding doesn't currently support rebinding of mouse buttons. It is however possible to bind mouse presses in widgets via `MousePress` and `MouseRelease` but it is not recommended to pursue this without some knowledge of how the engine handles these calls.
Other users have had success with third party software to allow for the rebinding of mouse buttons. 
