from hyperlpr import *
import cv2
PR = LPR(os.path.join(os.path.split(os.path.realpath(__file__))[0],"models"))
def HyperLPR_plate_recognition(Input_BGR,minSize=30,charSelectionDeskew=True,region="CH"):
    return PR.plate_recognition(Input_BGR,minSize,charSelectionDeskew)
if __name__ == "__main__":
    #image = cv2.imread("timg.jpg")
    # print(type(image))
    video_capture = cv2.VideoCapture(0)
    while True:
        ret,draw = video_capture.read()
        image = HyperLPR_plate_recognition(draw)
        cv2.imshow('car_plate',image)
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()
    #  print(HyperLPR_plate_recognition(image))
