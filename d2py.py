#!/usr/bin/env python3
# d2py.py
# cell_8
import mpos
import dispatcher

class _d2py (mpos.Leaf):

    def __init__ (self, dispatcher, parent, idInParent):
        super ().__init__ (dispatcher, parent, idInParent)
        self.inputs=['']
        self.outputs=['baton', 'quit']
    def react (self, inputMessage):
        import subprocess
        make_process = subprocess.Popen("make helloworld.py", stderr=subprocess.STDOUT)
        if make_process.wait() != 0:
            send ("quit", "./make.bash helloworld.py")
        else:
            send ("baton", True)
        
        return super ().react (inputMessage)
