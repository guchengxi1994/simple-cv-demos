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
from models.exceptions import InputMustBeAnInteger
from qa import __keys__, __samples__
from tools.mosiac import img_mosiac
from tools.mosiac_with_masks import img_mosiac_with_masks

console = Console()

__functions__ = {
    "mosiac": img_mosiac,
    "mosiac with masks":img_mosiac_with_masks,
}


class CvTool:

    loaded_keys = {}
    name = "cv-tool"

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
        else:
            from rich.table import Table
            table = Table(title="Supported tools")
            table.add_column("Id",
                             justify="center",
                             style="cyan",
                             no_wrap=True)
            table.add_column("Tools", justify="center", style="cyan")
            fkeys = __functions__.keys()
            for i in range(0,len(fkeys)):
                table.add_row(str(i + 1), fkeys[0])
            
            console.print(table)


    @staticmethod
    def __matchSeq(a: list, b: list) -> float:
        return difflib.SequenceMatcher(lambda x: x == " " or x == "", a,
                                       b).ratio()

    @classmethod
    def search(cls, question: str = "", threshold: float = 0.3):
        if question != "":
            questionWordList = question.replace("how",
                                                "").replace("to",
                                                            "").split(" ")
            matches = []
            if not cls.loaded_keys:
                for i in range(len(__keys__)):
                    cls.loaded_keys[__keys__[i]] = __keys__[i].replace(
                        "how to", "").split(" ")

            for i in cls.loaded_keys.items():
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
            from rich.table import Table
            table = Table(title="Supported questions")
            table.add_column("Id",
                             justify="center",
                             style="cyan",
                             no_wrap=True)
            table.add_column("Question", justify="center", style="cyan")

            for i in range(0, len(__keys__)):
                table.add_row(str(i + 1), __keys__[0])

            console.print(table)

            key = ""

            while key != 'q':
                key = input("Input an id, or press 'q' to quit:")
                # print(key)
                try:
                    key = int(key)
                    if key - 1 in range(0, len(__keys__)):
                        my_code = __samples__[__keys__[key - 1]]
                        syntax = Syntax(my_code,
                                        "python",
                                        theme="monokai",
                                        line_numbers=True)
                        console.print(syntax)
                        break
                    else:
                        print("input was not in range")
                except:
                    raise InputMustBeAnInteger("input must be an integer")
