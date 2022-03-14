#!/usr/bin/env python3
# build.py
# cell_8
import mpos
import dispatcher

class _build (mpos.Leaf):

    def __init__ (self, dispatcher, parent, idInParent):
        super ().__init__ (dispatcher, parent, idInParent)
        self.inputs=['go']
        self.outputs=['baton', 'quit']
    def react (self, inputMessage):
        import subprocess
        rc = subprocess.rc (["./make.bash", "helloworld.py"])
        if rc != 0:
            send ("quit", "./make.bash helloworld.py")
        else:
            send ("baton", True)
        
        return super ().react (inputMessage)
