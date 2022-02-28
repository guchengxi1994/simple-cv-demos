# mosiac image

## how to use

```python

    from tools.mosiac import img_mosiac
    result = img_mosiac("D:\\github_repo\\simple-cv-demos\\static\\0.png",step=20)
    # param step is the mosiac size
```

### the result is a numpy.ndarray
### you can save it with cv2(opencv-python), such as 
```python
    cv2.imwrite("result.jpg",result)
```

### if the image file is not accessible, it will raise an exception
```
    Traceback (most recent call last):
    File ".\test_mosiac.py", line 8, in <module>
        result = img_mosiac("D:\\github_repo\\simple-cv-demos\\static\\1.png",step=20)
    File "D:\github_repo\simple-cv-demos\tools\mosiac.py", line 13, in img_mosiac
        raise FileNotFoundException("{} is not exists".format(p))
    models.exceptions.FileNotFoundException: D:\github_repo\simple-cv-demos\static\1.png is not exists
```