'''
Descripttion: 
version: 
Author: xiaoshuyui
email: guchengxi1994@qq.com
Date: 2022-02-28 19:43:43
LastEditors: xiaoshuyui
LastEditTime: 2022-02-28 19:44:25
'''

import difflib
import inspect
import os

from rich.console import Console
from rich.syntax import Syntax

from common.load_img import load_image
from qa import __keys__, __samples__
from tools.mosiac import img_mosiac

console = Console()

__functions__ = {
    "mosiac": img_mosiac,
}


class CvTool:

    __loaded_keys = {}

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
                "\n", "").replace("$projectDir/",
                                  os.path.dirname(_file_path) + "/").replace(
                                      " ", "")
            r = os.system("code {}".format(_doc_path))
            if r == 1:
                print("\n")
                print("\n")
                print("============== Warning ===============")
                print("======= vscode is not installed ======")
                print("\n")

                from rich.markdown import Markdown
                with open(_doc_path) as f:
                    markdown = Markdown(f.read())
                console.print(markdown)
                print("============ end of doc =============")

    @staticmethod
    def __matchSeq(a: list, b: list) -> float:
        return difflib.SequenceMatcher(lambda x: x == " " or x == "", a,
                                       b).ratio()

    @classmethod
    def search(cls, question: str = "", threshold: float = 0.3):
        if question != "":
            questionWordList = question.split(" ")
            matches = []
            if not cls.__loaded_keys:
                for i in range(len(__keys__)):
                    cls.__loaded_keys[__keys__[i]] = __keys__[i].split(" ")

            for i in cls.__loaded_keys.items():
                matches.append((cls.__matchSeq(questionWordList, i[1]), i[0]))

            matches.sort(key=lambda x: x[0], reverse=True)
            bestMatch = matches[0]

            if bestMatch[0] < threshold:
                print("Cannot find anything related to '{}',\nmaybe try '{}'".
                      format(question, bestMatch[1]))
            else:
                my_code = __samples__[bestMatch[1]]
                syntax = Syntax(my_code,
                                "python",
                                theme="monokai",
                                line_numbers=True)
                console.print(syntax)
        else:
            pass
