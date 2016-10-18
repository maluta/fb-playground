#!/usr/bin/python

# built-ins
import argparse
import os

# own modules
from facebook import Graph
from facebook import Analysis

# test code
TOKEN = os.environ['FB_TOKEN']
# fb = Graph(TOKEN)

# get data and save it!
# fb.toJSON(fb.whoami(),"whoami.json")
# fb.toJSON(fb.comments("670874126401553"),"comments.json")

# analysis
a = Analysis()
a.words('comments.json')
