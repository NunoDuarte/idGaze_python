# idGaze_python
Software for Identifying from Gaze Fixations the Recognized Object or Face

## Requirements to make it work
1. tensorflow models - object detection
2. pylsl
3. labstreaminglayer
4. yarp
5. pupil with zmq plugin
6. pupil-stream-lsl project (other repository)
7. check the requirements of the pupil-stream-lsl 

## if you find this problem when using codeblocks 
- pthread_create@2.25 
The solution is to add the thread library to both the compiler and linker 
- source: https://askubuntu.com/questions/568068/multithreading-in-codeblocks
