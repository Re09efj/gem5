import os
import re
import shutil
from datetime import datetime


def rawTxtReader(final_output_txt, NUM_NODES):
    with open(final_output_txt) as f:
        content = f.read()
        for i in range(NUM_NODES):
            name = f"mem_ctrl{i}"
            reads = re.search(rf"system\.{name}\.readReqs\s+(\d+)", content)
            writes = re.search(rf"system\.{name}\.writeReqs\s+(\d+)", content)
            print(
                f"node{i} ({name}): reads={reads.group(1) if reads else 0}, "
                f"writes={writes.group(1) if writes else 0}"
            )
