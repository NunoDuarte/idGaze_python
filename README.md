# Identifying from Gaze Fixations the Desired Objects and Faces

<img src="doc/python.gif" width="800" height="450" />

### Current version of main.py uses tensorflow object detection network trained on icub faces
So you need to get the [icub-face-detection](https://github.com/NunoDuarte/icub-face-detection) repo to make it work 

# Table of Contents

- [Instructions](#instructions)
- [Dependencies](#dependencies)
- [Installation](https://github.com/NunoDuarte/idGaze_python/doc/install.md)
- [Possible Issues](#issues)

## Instructions
1. main.py runs the software connected to the PupilLabs eye-tracker using LSL
2. main_offline.py runs the software for a video (.mp4) 

## Dependencies
- There are two conda virtual environments which were tested and was running (**pupilos** and **pupilos-10**). Pupilos was working for tensorflow 1.9 and CUDA-8.0 and pupilos-10 was working for tensorflow 2.7 and CUDA-11.2
1. add anaconda
2. source activate pupilos***
3. tensorflow models - object detection
4. import utils

## Issues
If you find this problem when using codeblocks:
```
pthread_create@2.25 
```
The solution is to add the thread library to both the compiler and linker. You can find an example in this [link](https://askubuntu.com/questions/568068/multithreading-in-codeblocks).

If you find that it does not recognize libYARP_init.so.3 even though it recognizes libYARP_init.so. A good quick workaround is to add the path to the yarp libs to the Search directories. You can find an example in this [link](http://forums.codeblocks.org/index.php?topic=18661.0). You have to go to project->Build options...->Search directories->Linker and add the directory there "../../../../middleware/yarp/build/lib"

If you cannot find shared library (e.g. liblsl64.so.1.2.0) it works if you right click project->Build options...->Search directories->Linker and add the directory there. The directory where liblsl64.so.1.2.0 is for example
