from .imread_sample_code import sample_code as imread_sample_code
from .imwrite_sample_code import sample_code as imwrite_sample_code
from .imshow_sample_code import sample_code as imshow_sample_code

__keys__ = [
    "how to read an image",
    "how to write an image",
    "how to display or show an image"
]

__samples__ = {
    __keys__[0]: imread_sample_code,
    __keys__[1]: imwrite_sample_code,
    __keys__[2]: imshow_sample_code,
}
