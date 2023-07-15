# WASD Camera Presets
These come in a few flavors. 
In order to use WASD keys for your camera some compromises have to be made, so be prepared to make some adjustements when switching to this configuration

# Gridmenu with WASD camera
To maintain gridmenu behavior with WASD camera some extra things have to happen.
- With a builder selected, the QWER ASDF keys are all free to use, and when a category is selected with ZXCV those keys are repurposed to use grid building hotkeys.
- With a lab selected, the QWER ASDF ZXCV keys are all claimed (if there's a unit in the respective position).

We can use this difference to take over WASD keys with minimal impact. the `builder` command can be appended to any of the grid build binds, e.g. 
`bind           Any+sc_a  gridmenu_key 2 1 builder` means the `A` key will *only* be active with a builder, and only when an active category is selected.
So at all other times, the `A` key can be used for the camera. Repeat for all the WASD keys, as can be seen in these presets.
The downside of this approach is that the WASD keys will be *unusable* in a lab, so if you use lab keys heavily this will not be an ideal setup for you.

# WASD controls with a space modifier
To sidestep these downsides, we can take a different approach. Instead of using WASD for the camera, we can use Space+WASD, 
which allows those keys to maintain their base functions, but the downside is that you have to hold space while moving the camera around.
