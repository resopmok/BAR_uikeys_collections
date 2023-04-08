8 April 2023                 

# How to customize keybinds in Beyond All Reason           

## The Two Formats

As of the documented date, Beyond All Reason is able to interpret hotkey configuration files from two different formats. The first is in LUA and read directly by the bar hotkey widget. The second is uikeys.txt, which can be read by the engine, but requires that the bar hotkey widget be disabled.

### LUA format

To use custom keybindings:
- Open the launcher and click on "Open Installation Directory."
- Open "data" folder (not necessary on Linux systems).
- In-game (singleplayer skirmish against InactiveAI), select Settings -> Control -> Keybindings -> Custom
- Edit the file `bar_hotkeys_custom.lua` with your desired changes. 

Test your changes in real time:
- Switch off from and to the Custom preset in the in-game Settings.
- Press F11 (or type `/widgetselector` to everyone chat), disable, then re-enable `BAR  Hotkeys` in the widget list (click it to turn off and then on again).

If you're interested in customizing a preset instead of default hotkeys:
- Find the preset you want to customize from the main repo: https://github.com/beyond-all-reason/Beyond-All-Reason/tree/bf53d5b9297922225774dbfc31277b274a97e226/luaui/configs
- Copy the raw contents and overwrite any existing `bar_hotkey_custom.lua` in the data directory (opened from launcher).
- Make your changes and test as above.


References:

- Documentation for select action: https://github.com/beyond-all-reason/spring/blob/BAR105/doc/SelectionKeys.md
- Documentation for uikeys format: https://github.com/beyond-all-reason/spring/blob/BAR105/doc/uikeys.txt
- General repository of custom keybindings: https://github.com/resopmok/BAR_uikeys_collections

### uikeys.txt format

To use custom keybindings:
- Open the launcher and click on "Open Installation Directory."
- Open "data" folder (not necessary on Linux systems).
- In-game (singleplayer skirmish against InactiveAI), choose the preset you want to customize from Settings -> Control -> Keybindings -> Custom
- Open the chat box with enter (to everyone, not spectator or ally) and enter the command `/keysave`
- Open the file uikeys.tmp in your choice of text editor and make changes to your liking.
- Rename `uikeys.tmp` to `uikeys.txt`
- Press F11 (or type `/widgetselector` to everyone chat) and disable the `BAR Hotkeys` widget in the list. It should turn red when off.
- Type `/keyreload` to everyone chat to load the new bindings. The BAR Hotkey widget should remain disabled and the uikeys.txt loaded anytime you start a new game.

Test your changes in real time:
- Type `/keyreload` to everyone chat after you have saved additional changes to your uikeys.txt

References:

- Documentation for select action: https://github.com/beyond-all-reason/spring/blob/BAR105/doc/SelectionKeys.md
- Documentation for uikeys format: https://github.com/beyond-all-reason/spring/blob/BAR105/doc/uikeys.txt
- General repository of custom keybindings: https://github.com/resopmok/BAR_uikeys_collections
