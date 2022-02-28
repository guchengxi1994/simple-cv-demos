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


class CvTool:
    def __init__(self,p:str) -> None:
        """p is the image path
        """
        self.image = load_image(p)