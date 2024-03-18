# How to customize keybinds in Beyond All Reason 

Keybinds in BAR are handled differently than most games, having no built-in keybind editor. This can be cumbersome and annoying, but with the expansiveness of the keybind capabilities, it is hard to build a UI for editing it that comes close to capturing the full capabilities.

To use custom keybind files, you need to edit a text file, specifically one called `uikeys.txt`

## Setting up a custom keybind file

- Open the launcher and click on "Open Installation Directory."
- Open "data" folder (not necessary on Linux systems). This is where the custom keybind config file, `uikeys.txt`, will  live.
- In-game (singleplayer skirmish against InactiveAI), first choose the preset you want to customize from Settings -> Control -> Keybindings
- Then from Settings -> Control -> Keybindings, select "Custom" from the drop-down and the game will create a `uikeys.txt` for you to edit with your favorite text editor. This first version of your custom file is based on the last preset you had chosen.
  - We recommend using [VS Code](https://code.visualstudio.com/) with the [`uikeys` extension](https://marketplace.visualstudio.com/items?itemName=nbusseneau.vscode-uikeys), for syntax highlighting and completion suggestions.
- To test your changes in real time: Type `/keyreload` after you have saved additional changes to your `uikeys.txt`.

## Select command

[This page](https://beyond-all-reason.github.io/spring/articles/select-command/) explain how to create your unit selection.

Available categories for `category_` filter are not mentioned in this page.
Here are available categories:
```
ALL
BOT
CANBEUW
COMMANDER
EMPABLE
GROUNDSCOUT
HOVER
LIGHTAIRSCOUT
MINE
MOBILE
NOTAIR
NOTHOVER
NOTLAND
NOTSHIP
NOTSUB
NOWEAPON
PHIB
SHIP
SURFACE
T4AIR
TANK
UNDERWATER
VTOL
WEAPON
```

## Customize by using the Ingame Keybind Editor widget (by MasterBel)

- You can find this widget on the official BAR discord here: https://discord.com/channels/549281623154229250/1113861314582954078
- There are special instructions for the installation of this widget, be sure to read them and follow them carefully to ensure it works properly.
- It has a variety of useful features and allows you to search keybinds and manage them without tabbing out of the game.

## References:

- Documentation for select action: https://beyond-all-reason.github.io/spring/articles/select-command/
- Documentation for uikeys format: https://github.com/beyond-all-reason/spring/blob/BAR105/doc/uikeys.txt
- General repository of custom keybindings: https://github.com/resopmok/BAR_uikeys_collections
- BAR master preset layouts: https://github.com/beyond-all-reason/Beyond-All-Reason/tree/master/luaui/configs/hotkeys
