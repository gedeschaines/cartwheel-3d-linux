# Cartwheel 3D - Linux - Getting Started #
---
## Introduction ##

This page will give you all the steps required to compile and execute the project on a x86_64 GNU/Linux platform. Right now it works under Ubuntu 18.04 LTS and this document focuses on a Code::Blocks + Spyder IDE environment.

## Initial set-up ##

The project has been built and tested on an Ubuntu 18.04 LTS platform with [GNU GCC 8.4](https://gcc.gnu.org/), [SWIG 3.0.12](https://www.swig.org/), [Python 2.7.17](https://www.python.org/downloads/release/python-2717/) plus [wxPython 3.0.2](https://wxpython.org/news/wxpython-3.0.2.0-release/index.html), and [Python 3.6.9](https://www.python.org/downloads/release/python-369/) plus [wxPython 4.0.1](https://wxpython.org/news/wxpython-4.0.1-release/index.html), using [Code::Blocks 17.12](https://www.codeblocks.org/) to build the shared libraries and Python modules, and [Spyder-IDE](https://www.spyder-ide.org/) to debug modules and the Basic Editor. You can install all of these using the `apt` command line interface to the APT package management system. The Spyder-IDE is useful if you want to edit and debug the Python code. The project uses a git repository. Under Linux, you can use [git](https://git-scm.com/) to create and maintain a local clone of the GitHub **cartwheel-3d-linux** code repository.

Use `git` to clone or `unzip` to unpack a ZIP copy of the **cartwheel-3d-linux** code repository at [https://github.com/gedeschaines/cartwheel-3d-linux](https://github.com/gedeschaines/cartwheel-3d-linux) into a user home subdirectory of your choice, such as `~/Work` or `~/Projects`. The complete directory path of the cloned or unzipped `cartwheel-3d-linux` subdirectory constitutes CW3D_HOME.

In additon to `build-essential`, `gcc`, `swig3`, `git`, `python[3]`, `codeblocks` and `spyder` packages the following library 'dev' packages are needed to build cartwheel-3d shared libraries:

* python-dev or python3-dev
* libgl1-mesa-dev
* libglew-dev
* freeglut3-dev
* libgsl-dev
* libgslcblas0

Additionally, `python-wxgtk3.0` plus `python-opengl` for Python 2, and `python3-wxgtk4.0` plus `python3-opengl` for Python 3 packages are required to run the Basic Editor. Also, `ffmpeg` is used to combine a sequence of saved screenshot BMP image files into a MP4 video file (see [bmptomp4](../tools/bmptomp4) shell script).

**Important!** The project creates shared libraries and Python library interface modules in `$CW3D_HOME/lib/[Debug|Release|Debug3|Release3]`. You will therefore need to add those directories to your LD_LIBRARY_PATH and PYTHONPATH environment variables as is done in the `start_*` shell scripts if you intend to execute the Basic Editor or other cartwheel-3d Python scripts external to the `start_*` scripts or Spyder-IDE.

## Compiling the C++ code ##

Open `$CW3D_HOME/cartwheel-3d.workspace` with Code::Blocks. Then select "Release" or "Release3" target in the drop-down box on the tool bar below the menu bar 'Settings' and 'Help' items, then right-click on the `cartwheel-3d` project and select 'Build workspace' to invoke SWIG and the C++ compiler to build shared libraries and associated Python interface modules. Once built, you should be able to use the provided `start_*` shell scripts to either execute Basic Editor, Basic Walker or module tests, or invoke the Spyder-IDE to run and debug Python scripts.

If you need to debug the C++ code, you can build a "Debug" or "Debug3" target. However the `start_*` shell scripts will require editing to change TARGET from "Release" to "Debug".

## Writing and debugging the Python 2 and 3 code ##

If you want to edit and debug the Python code, including all the user interface code, you can use the Spyder-IDE environment by invoking `start_spyder` or `start_spyder3` in the $CW3D_HOME directory.

### Spyder with Python 2 ###

In Spyder, check that the $CW3D_HOME/lib/Debug path has been added to the PYTHONPATH manager as the **top most entry**. Go to 'Tools' --> 'PYTHONPATH manager', remove $CW3D_HOME/lib/Release if present and add $CW3D_HOME/lib/Debug in its place. Also, the paths to Python `App`, `Controllers`, `Data`, `PyUtils` and `UI` modules should be entered in this order below the $CW3D_HOME/lib/Debug entry.

The appropriate Run Configuration setting per file should be 'Execute in current console' for Console, 'Directly enter debugging when errors appear' for General Settings and 'The following directory: $CW3D_HOME/Python' for Working Directory settings. Also, the default Python2.7 interpreter should be selected under 'Tools' --> 'Preferences' --> 'Python interpreter'.

### Spyder with Python 3 ###

In Spyder, check that the $CW3D_HOME/lib/Debug3 path has been added to the PYTHONPATH manager as the **top most entry**. Go to 'Tools' --> 'PYTHONPATH manager', remove $CW3D_HOME/lib/Release3 if present and add $CW3D_HOME/lib/Debug3 in its place. Also, the paths to Python3 `App`, `Controllers`, `Data`, `PyUtils` and `UI` modules **must be** entered in this order below the $CW3D_HOME/lib/Debug3 entry.

The appropriate Run Configuration setting per file should be 'Execute in current console' for Console, 'Directly enter debugging when errors appear' for General Settings and 'The following directory: $CW3D_HOME/Python3' for Working Directory settings. Also, the default Python3.6 interpreter should be selected under 'Tools' --> 'Preferences' --> 'Python interpreter'.
