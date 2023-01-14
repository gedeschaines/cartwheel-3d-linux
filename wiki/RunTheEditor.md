# Cartwheel 3D - Run The Editor #
---
## Introduction ##

This page explains how to download and run the style and character editor presented at SIGGRAPH 2010. This application works under Windows using the original downloaded code and under Linux by building cartwheel-3d using source from a GitHub code repository.

 * On a Windows platform, get `cartwheel.zip` from the [downloads section](https://code.google.com/archive/p/cartwheel-3d/downloads). Unzip it in the directory of your choice and run `simbicon.bat`.
 * On a Linux platform, clone or copy the [https://github.com/gedeschaines/cartwheel-3d-linux](https://github.com/gedeschaines/cartwheel-3d-linux) repository into a directory of your choice, build cartwheel-3d shared libraries and Python 2 (or 3) compatible modules with Code::Blocks using the provided `cartwheel-3d.workspace` file, then run `start_bedit` (or `start_bedit3`) to invoke the basic Style Editor case (see [GettingStarted-Linux](./GettingStarted-Linux.md) for build instructions).

 <div margin="0px" align="left"><br>
 <img src="../web/editorScreenShot.jpg" width="640" height="390" alt="Cartwheel-3d Style Editor screenshot"/>
 </div><br>

## How to use the editor ##

You can click the `Play` button to start the default walk. At any point in time, for example if the character falls down, click the `Rewind` button to restart from the initial pose.

Showing and hiding the style editor is controlled by checking the `Edit style` checkbox. You can edit the character shape by clicking the `Edit character` checkbox.

## Editing the gait parameters ##

You can use the `Speed`, `Duration` and `Width` sliders to modify the character's walking speed, the stepping frequency and the step width, respectively. Be careful: extreme values will generally make the character fall down.

## Editing the motion style ##

In the style editor, you can manipulate any yellow handle in the side or front view. If you want to add or remove a keyframe, simply check one of the three box in the top row. You cannot edit the swing foot position at the beginning or end of a stride, but you can edit it mid-stride.

## Editing the character shape ##

In the character editor, play with the yellow handles to change the body shape. Once you're satisfied, click on the `Create` button. If you want to go back to the initial character, click `Reset character`. To create an asymmetrical character, uncheck `Symmetrical`.

Extremely large or small limbs will result in overly light or heavy body part. These usually don't behave well and may cause the character to fall.

## Going further ##

The editor is full of hidden features that are not quite ready for prime time. If you want to push things further, download the original [WIN32](http://code.google.com/p/cartwheel-3d/wiki/GettingStarted) code or latest [GNU/Linux](https://github.com/gedeschaines/cartwheel-3d-linux) ported code and start playing with the Python scripts. You can also discuss the project or ask questions on the [Forum](http://groups.google.com/group/cartwheel-3d). Don't hesitate to propose ways in which the editor could be made better!
