8 April 2023

# FAQs from #keybind-help

### How can I get camera pan on wasd?

1. Copy the contents of https://github.com/resopmok/BAR_uikeys_collections/blob/main/bar_hotkeys_custom_wasdcamera.lua to a local file called `bar_hotkeys_custom.lua` in your game's data folder. Read the changes at the top of the file, and enable the layout in-game through Settings -> Control -> Keybinds -> Custom
2. Move commands off wasd according to your desires, and add this to your custom config file:
```
	{ "Any+sc_w",     "moveforward"  },
	{ "Any+sc_s",     "moveback"     },
	{ "Any+sc_d",     "moveright"    },
	{ "Any+sc_a",     "moveleft"     },
```
3. If you want to customize a wasdpan set with grid menu, review the Hobo Joe guide here:

### What is the "mnemonic" layout and should I use it?

There are "scancodes" in the config files that ensure the layout is positional ( if g were swapped with a, you would press g to atacck). The mnemonic layout is for people who have keyboard layouts different from qwerty but prefer their commands in their home keyboard's position instead (a would still attack, but that is located where g is on a qwerty keyboard).
This layout was made shortly after scancodes were introduced to keybindings to accomodate a few players who had learned the hotkeys in their home keyboard's layout. One colemak user in particular was very confused when pressing s caused his commander to dgun instead of stop.

### What is different the 60% layouts? Do you have any images of the 60% layouts?

### How can I acces the widget list and why do I want to?

### How do I invert map scrolling with the middle mouse button?

### Can I rebind my mouse buttons, or add bindings for extended mouse buttons?

Unforunately no, not at this time. 
