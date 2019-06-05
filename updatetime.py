### Changes the timestamp in the content to reflect accurate changes made to
### the file

import os
import datetime
import time

def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

folder = "C:\\Users\\david.odonohue\\Videos\\Project\\Website\\promathean.github.io"

for file in listdir_fullpath(folder):
    if file.endswith(".html"):
        updated = False
        fp = open(file, "r")
        content = fp.readlines()
        modified_stat = os.stat(file)
        modified = time.ctime(modified_stat.st_mtime)
        modified = modified.split(" ")
        del modified[4]
        del modified[2]
        modified[1], modified[2] = modified[2], modified[1]
        modified = " ".join(modified)
        for (index,line) in enumerate(content):
            if "Last updated" in line and ("Last updated: " + modified) not in line:
                content[index] = "Last updated: " + modified + ".<br>"
                updated = True
        if updated:
            fp = open(file, "w")
            for line in content:
                fp.write(line)
    