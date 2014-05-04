from subprocess import Popen
import os.path
if not os.path.isfile("wikipedia.xml"):
    Popen(["python", "wikidownloader.py"])
