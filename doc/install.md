# Installation 
to import **utils** you need to install tensorflow with gpu then get the models of tensorflow for object recognition to recognize the import 
```
from utils import label_map_util
from utils import visualization_utils as vis_util
```
you need the following (after you have followed the instructions on how to install tensorflow models)
``` 
cd software/tensorflow/models/research
export PYTHONPATH=$PYTHONPATH:$(pwd)/slim
echo $PYTHONPATH 
export PYTHONPATH=$PYTHONPATH:$(pwd):$(pwd)/object_detection 
```
5. pylsl
6. labstreaminglayer/liblsl (both work)
7.1. I got https://github.com/NunoDuarte/lsl_archived which has the version I need (because it was working)
8. Install, compile, and sudo make from the lsl_archived
9. yarp
10. pupil with zmq plugin
11. pupil LSL plugin (**pupil_lsl_relay.py**)
12. pupil with pupil remote and frame publisher activated
13. connect lsl with pupil and yarp (follow the instructions on [LSL_Pupil_Yarp](lsl_pupil.md))
14. check the requirements of the pupil_lsl_yarp
15. check that pupil_lsl_yarp has the correct threads activated
