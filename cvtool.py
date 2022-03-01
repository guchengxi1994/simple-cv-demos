'''
Descripttion: 
version: 
Author: xiaoshuyui
email: guchengxi1994@qq.com
Date: 2022-02-28 19:43:43
LastEditors: xiaoshuyui
LastEditTime: 2022-02-28 19:44:25
'''

from common.load_img import load_image
from tools.mosiac import img_mosiac
import os
import inspect

__functions__ = {
    "mosiac": img_mosiac,
}


class CvTool:
    def __init__(self, p: str) -> None:
        """p is the image path
        """
        self.image = load_image(p)

    def then(self, operation: str = "", *args, **kwargs):
        assert self.image is not None, "image is None"
        _operation = __functions__.get(operation, None)
        if _operation is not None:
            self.image = _operation(self.image, *args, **kwargs)
        return self

    def showDoc(self, operation: str = ""):
        _operation = __functions__.get(operation, None)
        if _operation is not None and _operation.__doc__ is not None:
            _file_path = inspect.getabsfile(self.__class__)
            _doc_path = _operation.__doc__.replace("see:", "").replace(
                "\n", "").replace("$projectDir/", os.path.dirname(_file_path)+"/").replace(" ", "")
            r = os.system("code {}".format(_doc_path))
            if r == 1:
                print("\n")
                print("\n")
                print("============== Warning ===============")
                print("======= vscode is not installed ======")
                print("\n")
                with open(_doc_path) as f:
                    lines = f.readlines()
                    print("============   {} doc  ==============".format(
                        operation))
                    for i in lines:
                        print(i)
                    print("============ end of doc =============")
