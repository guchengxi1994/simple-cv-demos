from typing import  TypeVar

import numpy as np
StrOrArray =  TypeVar('StrOrArray',str,np.ndarray)
IntOrTupleOrArray = TypeVar('IntOrTupleOrArray',int,tuple,np.ndarray)
IntOrTuple = TypeVar('IntOrTuple',int,tuple)

del np