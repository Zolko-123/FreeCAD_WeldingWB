# FreeCAD Welding workbench

Current version 0.0.1



## Overview

This workbench intends to make it easy to create welded tubing frames. Any types of sections (round tube, square tube, I or L sections...) can be used. The resulting frame is created inside an _App::Part_ container, that can be re-used with any FreeCAD tool handling _App::Part_ objects


**Please Note:** This workbench uses tools povided by the [Assembly4 workbenc](https://github.com/Zolko-123/FreeCAD_Assembly4), thus this must be installed. 



## Installation

### Addon Manager

not yet available


### Manual Installation

It is possible to install this workbench manually into FreeCAD's local workbench directory. This can be useful for testing local modifications to the workbench, or to remove an old stale version of the workbench. 

In this case, download the Github [FreeCAD_Welding-master.zip](https://github.com/Zolko-123/FreeCAD_Welding/archive/master.zip) archive from [github.com/Zolko-123/FreeCAD_Welding](https://github.com/Zolko-123/FreeCAD_Welding) to a temporary directory, and extract the Zip archive. Then, remove any existing Welding directory from FreeCAD's local workbench directory, and copy (or link) the folder *FreeCAD_Welding-master* into the directory containing all FreeCAD addon modules :

* for Windows: `C:\Users\******\AppData\Roaming\FreeCAD\Mod`
* for MacOS: `~/Library/Preferences/FreeCAD/Mod/`
* for Linux, _FreeCAD version v0.19_ : `~/.FreeCAD/Mod` 
* for Linux, _FreeCAD version v0.20_ : `~/.local/share/FreeCAD/Mod/` 



**Important Note:** Welding WB needs the Assembly4 workbech. Assembly 4 is available through the FreeCAD Addon Manager (menu **Tools > Addon Manager**). It is called _Assembly4_ in the Addon Repository.  



## Getting Started

You can get more information in the [user instructions](INSTRUCTIONS.md), the [technical manual](TECHMANUAL.md), and you can use the provided [example assemblies](https://github.com/Zolko-123/FreeCAD_Examples) to experiment with this workbench's features. There are also online tutorials :

* [a quick assembly from scratch](https://github.com/Zolko-123/FreeCAD_Examples/blob/master/Asm4_Tutorial1/README.md)
* [a cinematic assembly in one file, using a master sketch](https://github.com/Zolko-123/FreeCAD_Examples/blob/master/Asm4_Tutorial2/README.md)
* [a Lego assembly](https://github.com/Zolko-123/FreeCAD_Examples/blob/master/Asm4_Tutorial3/README.md)
* [Some examples to play with](https://github.com/Zolko-123/FreeCAD_Examples)







## Release notes

* 2022.04.11 (**0.0.1**) :  
Initial commit  



## Discussion
Please offer feedback or connect with the developers in the [dedicated FreeCAD forum thread](https://forum.freecadweb.org/viewtopic.php?f=20&t=34806).



## Addon Repository
This addon is hosted on a [GitHub repository](https://github.com/Zolko-123/FreeCAD_Welding). 



## License

LGPLv2.1 (see [LICENSE](LICENSE))
