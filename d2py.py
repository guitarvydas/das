#!/usr/bin/env python3
# d2py.py
# cell_6
import mpos
import dispatcher
import tools
import build
import clean

class _d2py (mpos.Container):

    def __init__ (self, dispatcher, parent, idInParent):
        super ().__init__ (dispatcher, parent, idInParent)
        self.inputs=['']
        self.outputs=['baton', 'quit']

        child0 = tools._tools (dispatcher, self, 'tools')
        child1 = build._build (dispatcher, self, 'build')
        child2 = clean._clean (dispatcher, self, 'clean')
        conn0 = mpos.Connector ([mpos.Sender ('clean', 'baton')], [mpos.Receiver ('tools', '')])
        conn1 = mpos.Connector ([mpos.Sender ('clean', 'quit')], [mpos.Receiver ('', 'quit')])
        conn2 = mpos.Connector ([mpos.Sender ('clean', 'quit')], [mpos.Receiver ('', 'quit')])
        conn3 = mpos.Connector ([mpos.Sender ('clean', 'quit')], [mpos.Receiver ('', 'quit')])
        conn4 = mpos.Connector ([mpos.Sender ('clean', 'quit')], [mpos.Receiver ('', 'quit')])
        conn5 = mpos.Connector ([mpos.Sender ('clean', 'quit')], [mpos.Receiver ('', 'quit')])
        conn6 = mpos.Connector ([mpos.Sender ('clean', 'quit')], [mpos.Receiver ('', 'quit')])
        conn7 = mpos.Connector ([mpos.Sender ('clean', 'quit')], [mpos.Receiver ('', 'quit')])
        conn8 = mpos.Connector ([mpos.Sender ('clean', 'quit')], [mpos.Receiver ('', 'quit')])
        conn9 = mpos.Connector ([mpos.Sender ('tools', 'baton')], [mpos.Receiver ('build', '')])
        conn10 = mpos.Connector ([mpos.Sender ('tools', 'quit')], [mpos.Receiver ('', 'quit')])
        conn11 = mpos.Connector ([mpos.Sender ('tools', 'quit')], [mpos.Receiver ('', 'quit')])
        conn12 = mpos.Connector ([mpos.Sender ('tools', 'quit')], [mpos.Receiver ('', 'quit')])
        conn13 = mpos.Connector ([mpos.Sender ('tools', 'quit')], [mpos.Receiver ('', 'quit')])
        conn14 = mpos.Connector ([mpos.Sender ('tools', 'quit')], [mpos.Receiver ('', 'quit')])
        conn15 = mpos.Connector ([mpos.Sender ('tools', 'quit')], [mpos.Receiver ('', 'quit')])
        conn16 = mpos.Connector ([mpos.Sender ('tools', 'quit')], [mpos.Receiver ('', 'quit')])
        conn17 = mpos.Connector ([mpos.Sender ('tools', 'quit')], [mpos.Receiver ('', 'quit')])
        conn18 = mpos.Connector ([mpos.Sender ('build', 'baton')], [mpos.Receiver ('', 'baton')])
        conn19 = mpos.Connector ([mpos.Sender ('build', 'baton')], [mpos.Receiver ('', 'baton')])
        conn20 = mpos.Connector ([mpos.Sender ('build', 'baton')], [mpos.Receiver ('', 'baton')])
        conn21 = mpos.Connector ([mpos.Sender ('build', 'baton')], [mpos.Receiver ('', 'baton')])
        conn22 = mpos.Connector ([mpos.Sender ('build', 'baton')], [mpos.Receiver ('', 'baton')])
        conn23 = mpos.Connector ([mpos.Sender ('build', 'baton')], [mpos.Receiver ('', 'baton')])
        conn24 = mpos.Connector ([mpos.Sender ('build', 'baton')], [mpos.Receiver ('', 'baton')])
        conn25 = mpos.Connector ([mpos.Sender ('build', 'baton')], [mpos.Receiver ('', 'baton')])
        conn26 = mpos.Connector ([mpos.Sender ('build', 'quit')], [mpos.Receiver ('', 'quit')])
        conn27 = mpos.Connector ([mpos.Sender ('build', 'quit')], [mpos.Receiver ('', 'quit')])
        conn28 = mpos.Connector ([mpos.Sender ('build', 'quit')], [mpos.Receiver ('', 'quit')])
        conn29 = mpos.Connector ([mpos.Sender ('build', 'quit')], [mpos.Receiver ('', 'quit')])
        conn30 = mpos.Connector ([mpos.Sender ('build', 'quit')], [mpos.Receiver ('', 'quit')])
        conn31 = mpos.Connector ([mpos.Sender ('build', 'quit')], [mpos.Receiver ('', 'quit')])
        conn32 = mpos.Connector ([mpos.Sender ('build', 'quit')], [mpos.Receiver ('', 'quit')])
        conn33 = mpos.Connector ([mpos.Sender ('build', 'quit')], [mpos.Receiver ('', 'quit')])
        conn34 = mpos.Connector ([mpos.Sender ('', '')], [mpos.Receiver ('clean', '')])
        self.connections = [ conn0, conn1, conn2, conn3, conn4, conn5, conn6, conn7, conn8, conn9, conn10, conn11, conn12, conn13, conn14, conn15, conn16, conn17, conn18, conn19, conn20, conn21, conn22, conn23, conn24, conn25, conn26, conn27, conn28, conn29, conn30, conn31, conn32, conn33, conn34 ]
        self.children = {'tools':child0, 'build':child1, 'clean':child2}
