#!/usr/bin/env python3

from AppKit import NSWorkspace
import time
t = range(1,100)
for i in t:
    time.sleep(3)
    activeAppName = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName']
    print(activeAppName)

