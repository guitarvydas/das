#!/usr/bin/env python3
# tools.py
# cell_7
import mpos
import dispatcher

class _tools (mpos.Leaf):

    def __init__ (self, dispatcher, parent, idInParent):
        super ().__init__ (dispatcher, parent, idInParent)
        self.inputs=['']
        self.outputs=['baton', 'quit']
    def react (self, inputMessage):
        make_process = subprocess.Popen("make tools", stderr=subprocess.STDOUT)
        if make_process.wait() != 0:
            send ("quit", "make tools")
        else:
            send ("baton", True)
        
        return super ().react (inputMessage)
