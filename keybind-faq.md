# Keybinding FAQ
### Can I rebind my mouse buttons, or add bindings for extended mouse buttons?

- There's a widget (by MasterBel) with limited ability to bind mouse4 and mouse5 with normally bindable actions. Find it here: https://discord.com/channels/549281623154229250/1123878514827997195 Work is ongoing engine-side to decouple some features and build better support for mouse bindings.
- Binding or rebinding mouse presses isn't currently supported through the uikeys.txt channel. It is however possible to bind mouse presses in widgets via `MousePress` and `MouseRelease` but it is not recommended to pursue this without some knowledge of how the engine handles these calls.
- Some users have had success with third party software like AutoHotkey or software that provided by their mouse manufacturer to allow for the rebinding of mouse buttons.

### Controlling the camera with WASD

Please see the page dedicated to [WASD camera presets](./custom_presets/wasd_camera_presets/).

### What is different about the 60% layouts?

60% layouts are designed for players who have small mechanical gaming keyboards (they are roughly 60% the number of keys as a full-size keyboard). Typically, these keyboards lack F keys, and so these layouts have been modified to accomodate that. The majority of the change moves F key commands to a combination of spacebar and a number key. There are a few other changes too, so make sure to consult images or read the config files on the main repo (https://github.com/beyond-all-reason/Beyond-All-Reason/tree/master/luaui/configs). You can find images for all layouts, including grid and legacy 60% here: (https://github.com/resopmok/BAR_uikeys_collections/tree/main/keyboard_layout_pngs).

### I'm not satisfied with the function of Shift+_number key_. I want it to _add_ my selection to the control group and select the whole group.

During the recent hotkey update, group behavior was unified between grid and legacy keybinds. To restore the previous grid behavior (which is now Ctrl+Shift+), follow these steps:
- Put this file in your /data/ directory (same place as `uikeys.txt`): https://github.com/resopmok/BAR_uikeys_collections/blob/main/num_keys.txt
- Create a custom `uikeys.txt` following instructions in the how-to: https://github.com/resopmok/BAR_uikeys_collections/blob/main/keybind-guide.md
- Find the following line in the `uikeys.txt`:
```
keyload luaui/configs/hotkeys/num_keys.txt
```
  and replace it with:
```
keyload num_keys.txt
```
This sets the config to read your local `num_keys.txt` which has the changes, instead of the default from the repo.

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

### How do I invert map scrolling with the middle mouse button?

- When using Spring camera (Ctrl+F6 in grid bindings, Ctrl+F3 in legacy binds): you can type `/set MouseInvert 1` into everyone chat and it will invert the camera scroll while holding down the middle mouse button.
- When using TA (overhead) camera (Ctrl+F5 in grid bindings, Ctrl+F2 in legacy binds): when holding down middle mouse button to scroll, there is no option for inverting. If you enable "Middle click toggles camera move (Settings -> Control), you can use a mode which will reverse this middle mouse button click activated mouse panning. To do that, type `/set MiddleClickScrollSpeed -0.01` into everyone chat.
- These settings should save automatically for your next load.

