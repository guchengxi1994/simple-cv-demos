import sys

sys.path.append("..")
from cvtool import CvTool

CvTool.search("write an image")

print(CvTool.name)

CvTool.search()