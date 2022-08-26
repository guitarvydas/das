#!/usr/bin/env python3
import dispatcher
import hw
disp = dispatcher.Dispatcher ()
top = hw._hw (disp, None, '')
top.kickstart ()
disp.dispatch ()
