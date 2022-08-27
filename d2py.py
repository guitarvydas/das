#!/usr/bin/env python3
# d2py.py
# cell_6
import mpos
import dispatcher
import abort
import tools
import build
import clean

class _d2py (mpos.Container):

    def __init__ (self, dispatcher, parent, idInParent):
        super ().__init__ (dispatcher, parent, idInParent)
        self.inputs=['cell_30']
        self.outputs=[]

        child0 = abort._abort (dispatcher, self, 'cell_25')
        child1 = tools._tools (dispatcher, self, 'cell_7')
        child2 = build._build (dispatcher, self, 'cell_8')
        child3 = clean._clean (dispatcher, self, 'cell_9')
        conn0 = mpos.Connector ([mpos.Sender ('cell_7', 'baton')], [mpos.Receiver ('cell_8', 'go')])
        conn1 = mpos.Connector ([mpos.Sender ('cell_9', 'baton')], [mpos.Receiver ('cell_7', 'go')])
        conn2 = mpos.Connector ([mpos.Sender ('', 'go')], [mpos.Receiver ('cell_9', 'go')])
        conn3 = mpos.Connector ([mpos.Sender ('cell_7', 'quit')], [mpos.Receiver ('cell_25', 'quit')])
        conn4 = mpos.Connector ([mpos.Sender ('cell_8', 'quit')], [mpos.Receiver ('cell_25', 'quit')])
        conn5 = mpos.Connector ([mpos.Sender ('cell_9', 'quit')], [mpos.Receiver ('cell_25', 'quit')])
        self.connections = [ conn0, conn1, conn2, conn3, conn4, conn5 ]
        self.children = {'cell_25':child0, 'cell_7':child1, 'cell_8':child2, 'cell_9':child3}
