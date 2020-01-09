# idGaze_python
Software for Identifying from Gaze Fixations the Recognized Object or Face

## Requirements to make it work
1. tensorflow models - object detection
2. pylsl
3. labstreaminglayer
4. yarp
5. pupil with zmq plugin
6. pupil LSL plugin (**pupil_lsl_relay.py**)
7. pupil with pupil remote and frame publisher activated
8. pupil-stream-lsl project (other repository)
9. check the requirements of the pupil-stream-lsl 
10. check that pupil-stream-lsl has the correct threads activated

## if you find this problem when using codeblocks 
- pthread_create@2.25 
The solution is to add the thread library to both the compiler and linker 
- source: https://askubuntu.com/questions/568068/multithreading-in-codeblocks

## issue with not recognizing libYARP_init.so.3 even though it recognizes libYARP_init.so
- quick workaround is to add the path to the yarp libs to the Search directories -> Linker 
- source: http://forums.codeblocks.org/index.php?topic=18661.0 
- e.g. project->Build options...->Search directories->Linker and add the directory there
- ../../../../middleware/yarp/build/lib

## where to find Pupil LSL Relay Plugin
- https://github.com/labstreaminglayer/App-PupilLabs/releases/tag/v1.0
- https://github.com/labstreaminglayer/App-PupilLabs/tree/b921ee217888812dce2abe8defc7c0b12db33e8c/pupil_capture
### Apparently there is a 2nd version! (you should check it out)
