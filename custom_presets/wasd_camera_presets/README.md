# Presets with `WASD` camera movement

Since `WASD` are bound to other actions in both the default keys and the grid keys presets, some compromises have to be made in order to use `WASD` for camera movement, generally by moving around important commands such as `D-Gun`.

Some options are provided below, and can be used a starting point for making your own preferred `WASD`-compatible keys.

_(Click on a title to open the configuration file for that setup.)_

## [`Meta`+`WASD` for grid keys](./grid_meta_wasd.txt)

This is probably the easiest setup, as it requires absolutely no changes to the grid keys.

The `Meta` key is `Space` by default, so in this setup:

- `Space`+`WASD` are inserted into the grid keys, and can always be used to move the camera.
- `WASD` can also be used to move the camera **if there is currently nothing actionable with `WASD`**:
  - `WASD` can be used to move the camera:
    - With no unit selected.
    - With only non-combat units selected (e.g. builders).
  - `WASD` cannot be used to move the camera:
    - With a combat unit selected (due to `Attack` command, etc.).
    - With a factory selected (due to entering build menu).
    - After pressing `ZXCV` with a builder selected (due to entering grid build menu).

## [`WASD` for grid keys](grid_wasd.txt)

It is possible to move around all commands associated with `WASD` on grid keys, however since they are originally intended as an optimized preset for usage with the grid build menu, we try to leave `WASD` usable for when the grid build menu is active.

In this setup:

- `WASD` are inserted into the grid keys, and can almost always be used to move the camera, including when units are selected.
- `WASD` cannot be used to move the camera:
  - With a factory selected (due to entering grid build menu).
  - After pressing `ZXCV` with a builder selected (due to entering grid build menu).
- Commands previously bound to `WASD` are changed as follows:
  - `W` (`Capture`, `Resurrect`) moved to `Shift`+`W`.
  - `A` (`Attack`) moved to `Shift`+`A`.
  - `S` (`Set target`) moved to `Shift`+`S`.
  - `D` (`D-Gun`, `Launch`) moved to `Shift`+`D`.

Arguably, the grid build menu can be seen as mostly useful for builders and less so for factories, since builders have multiple categories (`ZXCV`) filled with options, whereas factories tend to have only one page in most cases.

If you are OK with clicking units in factories and would like `WASD` to also move the camera with a factory selected, then remove the `factory` action binds and only leave the `builder` action binds.

## [Hobo Joe's `WASD` for grid keys](./grid_hobo_joe.txt)

An opinionated grid keys config with `WASD` camera controls plus some other changes, made by Hobo Joe, who contributed the bindable actions `builder` and `factory` for `gridmenu_key` binds.

## [`WASD` for default keys](./default_wasd.txt)

It is possible to move around all commands associated with `WASD` (incl. modifiers) on default keys, and have `WASD` usable in absolutely all circumstances, along with `Ctrl` and `Shift` modifiers for camera move speed.

In this setup:

- `WASD` are inserted into the default keys, and can always be used to move camera.
  - `Shift`+`WASD` will move camera faster.
  - `Ctrl`+`WASD` will move camera slower.
- Commands previously bound to `WASD` (incl. modifiers) are changed as follows:
  - `W` (`Wait`) moved to `T`, replacing `Track unit` (still available via `Alt`+`T`).
  - `Ctrl`+`W` (`Select armed units`) removed.
  - `A` (`Attack`) moved to `F,F` (double tap `F`).
  - `Alt`+`A` (`Area attack`) moved to `Alt`+`F`.
  - `Ctrl`+`A` (`Select all units`) moved to `Ctrl`+`E`.
  - `S` (`Stop`) moved to `Q`, replacing map labels / drawings (still available via `` ` ``).
  - `Ctrl`+`S` (`Clear queue`) moved to `Ctrl`+`Q`.
  - `D` (`D-Gun`, `Launch`, `Self-destruct`) moved to `B`.
  - `Ctrl`+`B` (`Select idle builder`) moved to `Ctrl`+`X`.
