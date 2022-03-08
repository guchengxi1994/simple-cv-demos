import cv2
import time
from threading import Thread

from decorators import CvToolDecorator


@CvToolDecorator.checkParam("recordType", paramRange=["image", "video"])
def videoCapture(record: bool = False,
                 recordType: str = 'image',
                 recordTime: float = 0,
                 saveLocation: str = ""):
    cap = cv2.VideoCapture(0)

    print("====  Print 'q' to stop ====")

    while True:
        if recordTime > 0:
            time.sleep(recordTime)
        ret, frame = cap.read()
        cv2.imshow("capture", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()