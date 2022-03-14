#!/usr/bin/env python3
# clean.py
# cell_9
import mpos
import dispatcher

class _clean (mpos.Leaf):

    def __init__ (self, dispatcher, parent, idInParent):
        super ().__init__ (dispatcher, parent, idInParent)
        self.inputs=['']
        self.outputs=['baton', 'quit']
    def react (self, inputMessage):
        import subprocess
        rc = subprocess.run (["make.bash", "clean"])
        if rc != 0:
             send ("quit", "make clean")
        else:
            send ("baton", True)
        return super ().react (inputMessage)
