# mosiac image

## how to use

## ```img_mosiac```,  ```img_mosiac(p: str, step: int = 2, begin=(0, 0), end=(np.Inf, np.Inf)``` params:

param ```p``` is the image location or an image
param ```step``` is the mosiac size,default 2 
param ```begin``` is the mosiac region top-left position, default (0,0)  
param ```end``` is the mosiac region right-bottom positon, default image size


## eg.

```python

    from tools.mosiac import img_mosiac
    result = img_mosiac("D:\\github_repo\\simple-cv-demos\\static\\0.png",step=20)
    
```

### the result is a numpy.ndarray
### you can save it with cv2(opencv-python), such as 
```python
    cv2.imwrite("result.jpg",result)
```

|  origin   | mosiac image  |
|  ----  | ----  |
| ![image1](../static/0.png)  | ![image1](./doc_images/result1.jpg) |

### if the image file is not accessible, it will raise an exception
```
    Traceback (most recent call last):
    File ".\test_mosiac.py", line 8, in <module>
        result = img_mosiac("D:\\github_repo\\simple-cv-demos\\static\\1.png",step=20)
    File "D:\github_repo\simple-cv-demos\tools\mosiac.py", line 13, in img_mosiac
        raise FileNotFoundException("{} is not exists".format(p))
    models.exceptions.FileNotFoundException: D:\github_repo\simple-cv-demos\static\1.png is not exists
```

### if ```begin``` and ```end``` is specified, such as ```img_mosiac("D:\\github_repo\\simple-cv-demos\\static\\0.png",step=20,begin=(200,200),end=(400,400)) ```, the result will be

|  origin   | mosiac image  |
|  ----  | ----  |
| ![image1](../static/0.png)  | ![image1](./doc_images/result2.jpg) |