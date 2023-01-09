# Cartwheel 3D - Linux - Getting Started #
---
## Introduction ##

This page will give you all the steps required to compile and execute the project on a x86_64 GNU/Linux platform. Right now it works uunder Ubuntu 18.04 LTS and this document focuses on a Code::Blocks + Spyder IDE environment.

## Initial set-up ##

The project has been built and tested on an Ubuntu 18.04 LTS platform with [GNU GCC 8.4](https://gcc.gnu.org/), [Swig 3.0.12](https://www.swig.org/) and [Python 2.7.17](https://www.python.org/download/releases/2.7/) using [Code::Blocks 17.12](https://www.codeblocks.org/) to build the shared libraries and Python modules, and [Spyder-IDE](https://www.spyder-ide.org/) to debug modules and the Basic Editor. You can install all of these using the `apt` command line interface to the APT package management system. The Spyder-IDE is useful if you want to edit and debug the Python code. The project uses a git repository. Under Linux, you can use [git](https://git-scm.com/) to create and maintain a local clone of the GitHub cartwheel-3d code repository.

Use `git` to clone or `unzip` to unpack a ZIP copy of the cartwheel-3d code respository at [https://github.com/gedeschaines/cartwheel-3d-linux](https://github.com/gedeschaines/cartwheel-3d-linux) into a user home subdirectory of your choice, such as `~/Work` or `~/Projects`. The complete directory path of the cloned or unzipped `cartwheel-3d` subdirectory constitutes CW3D_HOME.

In additon to `build-essential`, `gcc`, `swig3`, `git`, `python2`, `codeblocks` and `spyder` packages the following library 'dev' packages are needed to build cartwheel-3d shared libraries:

* python-dev
* libgl1-mesa-dev
* libglew-dev
* freeglut3-dev
* libgsl-dev
* libgslcblas0

Additionally, the `python-opengl` package is required to run the Basic Editor and `ffmpeg` is used to combine a sequence of saved screenshot BMP image files into a MP4 video file (see [bmptomp4](../tools/bmptomp4) shell script).

**Important!** The project creates shared libraries and Python library interface modules in `$CW3D_HOME/lib/[Release|Debug]`. You will therefore need to add those directories to your LD_LIBRARY_PATH and PYTHONPATH environment variables as is done in the `start_*` shell scripts if you intend to execute the Basic Editor or other cartwheel-3d Python scripts external to the `start_*` scripts or Spyder-IDE.

## Compiling the C++ code ##

Open `$CW3D_HOME/cartwheel-3d.workspace` with Code::Blocks. Then select "Release" target in the drop-down box on the tool bar below the menu bar 'Settings' and 'Help' items, then right-click on the `cartwheel-3d` project and select 'Build workspace' to invoke the Swig and C++ compiler to build shared libraries and associated Python modules. Once built, you should be able to use the provided `start_*` shell scripts to either execute Basic Editor, Basic Walker or module tests, or invoke the Spyder-IDE to run and debug Python scripts.

If you need to debug the C++ code, you can build a "Debug" target. However the `start_*` shell scripts will require editing to change TARGET from "Release" to "Debug".

## Writing and debugging the Python code ##

If you want to edit and debug the Python code, including all the user interface code, you can use the Spyder-IDE environment by invoking `start_spyder` in the $CW3D_HOME directory.

In Spyder, check that the $CW3D_HOME/lib/Debug path has been added to the PYTHONPATH manager. Go to 'Tools' --> 'PYTHONPATH manager', remove $CW3D_HOME/lib/Release if present and add $CW3D_HOME/lib/Debug in its place.

The appropriate Run Configuration setting per file should be 'Execute in current console' for Console, 'Directly enter debugging when errors appear' for General Settings and 'The following directory: $CW3D_HOME/Python' for Working Directory settings. Also, the default Python2.7 interpreter should be selected under 'Tools' --> 'Preferences' --> 'Python interpreter'.
