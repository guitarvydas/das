#!/usr/bin/env python3
# tools.py
# cell_7
import mpos
import dispatcher

class _tools (mpos.Leaf):

    def __init__ (self, dispatcher, parent, idInParent):
        super ().__init__ (dispatcher, parent, idInParent)
        self.inputs=['go']
        self.outputs=['baton', 'quit']
    def react (self, inputMessage):
        import subprocess
        rc = subprocess.run (["make", "tools"])
        if rc != 0:
            send ("quit", "make tools")
        else:
            send ("baton", True)
        return super ().react (inputMessage)
