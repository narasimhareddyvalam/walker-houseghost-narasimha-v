# BLENDER-NOTES — the six parts of the window

**Blender** 5.2.2 LTS · macOS 26.6.2, Apple Silicon · written 2026-10-14, after building the three Assignment 3 assets

My screenshot: `evidence/a3-blender-window.png` — my own session, `bookshelf.blend` open, the
middle shelf `BS_Shelf_Mid` selected, the N sidebar open on its Item tab.

![My Blender session with BS_Shelf_Mid selected](evidence/a3-blender-window.png)

## 1. The 3D viewport

The big central area where the scene is drawn — the part of Blender you are actually looking
*into*. I used it for three things. I orbited and zoomed around each asset to inspect it from
different sides, which is how I judged whether the first versions looked too plain. I clicked
directly on parts to select them; the selected part gets an orange outline. And I switched the
shading to Material Preview to see the real colours, because the default solid shading shows
everything a flat grey, which tells you nothing about whether the brass looks like brass.

## 2. The toolbar

The column of tool icons down the left edge of the viewport: Select, Cursor, Move, Rotate,
Scale and the rest. I used the select and transform tools on whole objects. The orange
outline and the small dot at a selected object's origin come from here, and the dot is worth
noticing — it shows where the object's origin is, which is the point Godot will place it by.

## 3. The Outliner

The list at the top right of every object in the file, shown as a tree. It showed me how each
asset is organised: one root — `Bookshelf`, `MusicBox` or `BedsideLamp` — with its parts nested
under it, each with its own name. I also selected parts by clicking their names in the list,
which is easier than clicking in the viewport when parts sit inside each other, like the
shelves behind the side panels.

## 4. The Properties editor

The tall panel below the Outliner, with a column of tabs down its left side (render, output,
scene, object, modifiers, materials and more). With an object selected, the Object tab shows
its name and its Transform — location, rotation and scale — the same values as the sidebar.
It is also where an object's materials and modifiers live.

## 5. The sidebar (press N)

A panel that slides out on the right edge of the viewport when you press N. Its **Item** tab
is where I checked every object's numbers: location, rotation, scale and — the one that matters
most here — **Dimensions**, the real size in metres. That is the number I compared against my
change brief and against Godot's bounding box. In my screenshot it reads 0.56 × 0.264 × 0.02 m
for the shelf, with rotation 0° and scale 1.000, which is what "transforms applied" looks like.
One thing I noticed: the sidebar has its own tabs (Item, Tool, View, and an **MCP for Blender**
tab added by the add-on), and the Item tab only offers itself once an object is active.

## 6. The mode selector

The drop-down at the top left of the viewport header that reads **Object Mode**. In Object
Mode you work with whole objects — select, move, rotate, scale. I stayed in Object Mode for
almost everything, and briefly switched to **Edit Mode**, where the same object turns into its
individual vertices, edges and faces — the level at which a cube becomes a bevelled board.
For assets built from whole primitives, Object Mode was where nearly all the work happened.

## What the window taught me

Every number that mattered for this assignment — size, rotation, scale — is visible somewhere
in this window without writing code: in the sidebar's Item tab and in the Properties editor.
Being able to read them there is what let me check Claude's reports against Blender itself
instead of taking them on trust.
