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
        make_process = subprocess.Popen("make clean", stderr=subprocess.STDOUT)
        if make_process.wait() != 0:
             send ("quit", "./make.bash clean")
        else:
            send ("baton", True)
        return super ().react (inputMessage)
