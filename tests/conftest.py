#!/usr/bin/env python3

__version__ = "0.1.0"

import os
import sys

dir = os.path.dirname(os.path.abspath(__file__))
path = os.path.abspath(os.path.join(dir, "../src"))
sys.path.append(path)
