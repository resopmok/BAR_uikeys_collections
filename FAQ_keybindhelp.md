8 April 2023

# FAQs from #keybind-help

### BAR recently updated the custom keybind format, and I am now missing grid menu unit hotkeys while wanting to use the default key layout. How do I fix?

One of the biggest changes with the new `uikeys.txt` format is that you can now include other preset files by using `keyload`. This might allow you to create a couple different presets (for example, one for playing and one for spectating or casting) and easily change between them by editing a single line in your uikeys.txt. In this case, you will need to put the default keyset with the keyset that manages grid menu hotkeys. 
- First, from the in-game Settings -> Control -> Keybindings, make sure you have "Custom" selected from the dropdown. WHen you do this a "grid" button will appear right below. The green toggle enables grid build menu, the red one default build menu.
- Then, make a `uikeys.txt` which contains only the following; put it in your BAR install /data/ directory (not needed on Linux, just put it in the install directory):
```
unbindall
keyload luaui/configs/hotkeys/gridmenu_keys.txt
keyload luaui/configs/hotkeys/default_keys.txt
```
Or, if you were previously using the default 60% layout with grid menu, your uikeys.txt would look like this:
```
unbindall
keyload luaui/configs/hotkeys/gridmenu_keys.txt
keyload luaui/configs/hotkeys/default_keys_60pct.txt
```
### I want to port an old bar_hotkeys_custom.lua format configuration to uikeys.txt (or it failed to update format with recent change).

- First, make sure your keybinds are set to custom ingame.
- Close the game
- Make sure your bar_hotkeys_custom.lua file is in your data directory
- Open springsettings.cfg (in your data folder) and find the line with `KeybindingFile`
- Set it to `KeybindingFile = bar_hotkeys_custom.lua`
- If you have a uikeys.txt file, delete or rename it
- Launch the game, and start a skirmish
  
### I want to move the camera with WASD.

Please see the page dedicated to [WASD camera presets](./custom_presets/wasd_camera_presets/).

### I'm not satisfied with the function of Shift+<number key>. I want it to _add_ my selection to the control group and select the whole group.

During the recent hotkey update, group behavior was unified between grid and default keybinds. To restore the previous grid behavior (which is now Ctrl+Shift+), follow these steps:
- Put this file in your /data/ directory (same place as `uikeys.txt`): https://github.com/resopmok/BAR_uikeys_collections/blob/main/old_keybinds/num_keys.txt
- Create a custom `uikeys.txt` following instructions in the how-to: https://github.com/resopmok/BAR_uikeys_collections/blob/main/HOWTO_customkeybind.md
- Find the following line in the `uikeys.txt`:
```
keyload luaui/configs/hotkeys/num_keys.txt
```
  and replace it with:
```
keyload num_keys.txt
```
This sets the config to read your local `num_keys.txt` which has the changes, instead of the default from the repo.

### What is the "mnemonic" layout and should I use it?

There are "scancodes" in the config files that ensure the layout is positional ( if g were swapped with a, you would press g to atacck). The mnemonic layout is for people who have keyboard layouts different from qwerty but prefer their commands in their home keyboard's position instead (a would still attack, but that is located where g is on a qwerty keyboard).
This layout was made shortly after scancodes were introduced to keybindings to accomodate a few players who had learned the hotkeys in their home keyboard's layout. One colemak user in particular was very confused when pressing s caused his commander to dgun instead of stop.

### How do I use hotkeys with orders that have multiple states you can toggle between (like hold fire and fire at will)?

The stateful orders which have actions exposed for binding are `repeat`, `onoff`, `wantcloak`, `firestate`, and `movestate`. There are some orders which do not have actions exposed for binding, they are priority, fly/land, and retreat percentage. There are two ways you can create keybindings for stateful orders as part of your custom keyset:
- Define the state using a keychain and an integar as argument. This is how grid optimized uses toggles so that a player does not need to know a unit's current state in order to set it to the desired state (1 tap green, 2 taps red, 3 taps yellow). For example, `firestate` is bound as follows in grid optimized:
```
bind     sc_l,sc_l,sc_l  firestate 1
bind          sc_l,sc_l  firestate 0
bind               sc_l  firestate 2
bind Shift+sc_l,Shift+sc_l,Shift+sc_l  firestate 1
bind Shift+sc_l,Shift+sc_l  firestate 0
bind         Shift+sc_l  firestate 2
```
- Use the keypress as a toggle, the same behavior as clicking on the order menu. To do this, you do not need a keychain and you put no integars as argument to the action. For example:
```
bind               sc_l  firestate
bind         Shift+sc_l  firestate
```
Bada-bing! Now you have hotkeys for those order menu toggles.

### What is different about the 60% layouts? Do you have any images of the 60% layouts?

60% layouts are designed for players who have small mechanical gaming keyboards (they are roughly 60% the number of keys as a full-size keyboard). Typically, these keyboards lack F keys, and so these layouts have been modified to accomodate that. The majority of the change moves F key commands to a combination of spacebar and a number key. There are a few other changes too, so make sure to consult images or read the config files on the main repo (https://github.com/beyond-all-reason/Beyond-All-Reason/tree/master/luaui/configs). You can find images for all layouts, including default and grid 60% here: (https://github.com/resopmok/BAR_uikeys_collections/tree/main/keyboard_layout_pngs).

### How can I access the widget list and why do I want to?

There may be an option in the in-game settings to enable the widget selector. If so, enable it, then press F11 to bring up the widget menu. If not, type `/widgetselector` into "everyone" chat. This menu is used to enable and disable custom widgets which you have installed in your `/data/LuaUI/Widgets/` directory. This isn't necessarily a hotkey-related question anymore but it comes up frequently anyway.

### I want to invert the grid menu home row to QWER. How?

You can use this version of the grid opti config file (https://github.com/resopmok/BAR_uikeys_collections/blob/main/bar_hotkeys_custom_invertqwer.lua) to move your grid menu's home row from ZXCV to QWER. In this case, instead of the ZX keystrokes building you a solar, QW will do so. RA would build you a construction turret, and WS would be your basic anti-air. Currently we can't invert the actual layout of grid menu in game to accomodate, so your QWER row will still display in the same location on the menu that ZXCV was. The config also moves army selection, resurrect, repair, and reclaim order to ZXCV respectively.
Note: this .lua config file will not work in the game anymore. Sometime in the near future I'll make preset file you can include which would replace your `gridmenu_keys.txt` and makes the swap. It's more likely to happen sooner if someone bothers me about it.

### How do I invert map scrolling with the middle mouse button?

- When using Spring camera (Ctrl+F3 in default binds, Ctrl+F6 in grid bindings): you can type `/set MouseInvert 1` into everyone chat and it will invert the camera scroll while holding down the middle mouse button.
- When using TA (overhead) camera (Ctrl+F2 in default binds, Ctrl+F5 in grid bindings): when holding down middle mouse button to scroll, there is no option for inverting. If you enable "Middle click toggles camera move (Settings -> Control), you can use a mode which will reverse this middle mouse button click activated mouse panning. To do that, type `/set MiddleClickScrollSpeed -0.01` into everyone chat.
- These settings should save automatically for your next load.

### Can I rebind my mouse buttons, or add bindings for extended mouse buttons?

- Keybinding doesn't currently support rebinding of mouse buttons. It is however possible to bind mouse presses in widgets via `MousePress` and `MouseRelease` but it is not recommended to pursue this without some knowledge of how the engine handles these calls.
- Some users have had success with third party software like AutoHotkey to allow for the rebinding of mouse buttons.
- Depending on your needs, this widget from MasterBel might be helpful: https://discord.com/channels/549281623154229250/1123878514827997195
- You could modify this and use it as a custom widget: https://github.com/beyond-all-reason/Beyond-All-Reason/blob/master/luaui/Widgets/gui_buildspacing.lua
  - Replace input on Spring.SendCommands with what you want to be done
