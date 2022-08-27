#!/usr/bin/env python3
# clean.py
# cell_9
import mpos
import dispatcher

class _clean (mpos.Leaf):

    def __init__ (self, dispatcher, parent, idInParent):
        super ().__init__ (dispatcher, parent, idInParent)
        self.inputs=['cell_28']
        self.outputs=['cell_14', 'cell_16']
    def react (self, inputMessage):
        import subprocess
        r = subprocess.run (["make", "clean"])
        if (r.returncode != 0):
             self.send ("quit", f"error {r} in make clean")
        else:
            self.send ("baton", True)
        return super ().react (inputMessage)
