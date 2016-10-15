#!/usr/bin/python

# built-ins
import argparse
import os

# own modules
from facebook import Graph
from facebook import Analysis

# test code
TOKEN = os.environ['FB_TOKEN']
fb = Graph(TOKEN)
print(fb.whoami())
print(fb.comments("670874126401553"))
