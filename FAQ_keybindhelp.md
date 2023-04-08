8 April 2023

#FAQs from #keybind-help

### How can I get camera pan on wasd?

1. Copy the contents of https://github.com/resopmok/BAR_uikeys_collections/blob/main/bar_hotkeys_custom_wasdcamera.lua to a local file called `bar_hotkeys_custom.lua` in your game's data folder. Read the changes at the top of the file, and enable the layout in-game through Settings -> Control -> Keybinds -> Custom
2. Move commands off wasd according to your desires, and add this to your custom config file:
	{ "Any+sc_w",     "moveforward"  },
	{ "Any+sc_s",     "moveback"     },
	{ "Any+sc_d",     "moveright"    },
	{ "Any+sc_a",     "moveleft"     },
3. If you want to customize a wasdpan set with grid menu, review the Hobo Joe guide here: