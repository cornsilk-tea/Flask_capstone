from deepface import DeepFace
from deepface.basemodels import Facenet512
import shutil, path, os
import cv2
import numpy as np

base_dir = os.getcwd()
# print("현재 디렉토리는 {}".format(base_dir))
# name_list = os.listdir(os.path.join(base_dir, '팀원사진'))
# print(name_list)
IMG_NAME = 'case2.jpg'
src_img = os.path.join(base_dir, IMG_NAME)
# print(src_img)
# 모든 폴더를 돌아가며 가장 첫번째 사진을 비교해서 출력해준다.
# res_list = []
# for stu_name in name_list:
#     data_list = os.listdir(os.path.join(base_dir, '팀원사진', stu_name))
    # print(data_list)
    # res = DeepFace.verify(img1_path=src_img, 
    # img2_path=os.path.join(base_dir, '팀원사진', stu_name, data_list[0]),
    # distance_metric='euclidean_l2', 
    # model_name='ArcFace', 
    # detector_backend='mtcnn')
    # res = DeepFace.verify(img1_path=src_img, img2_path=os.path.join(base_dir, '팀원사진', stu_name, data_list[0]))
    # print(res)
    # print(src_img)
    # print(os.path.join(base_dir, '팀원사진', stu_name, data_list[0]))
# print(os.path.join(base_dir, '팀원사진', '왕능가', '왕능가.jpg'))

# stream = open(os.path.join(base_dir, '팀원사진', '왕능가', '왕능가.jpg').encode("utf-8"), "rb")
# bytes = bytearray(stream.read())
# img = cv2.imdecode(np.asarray(bytes, dtype=np.uint8), cv2.IMREAD_UNCHANGED)
res = DeepFace.verify(img1_path=src_img, img2_path=os.path.join(base_dir, 'img_data', "20150597", "20150597.jpg"))
print(res)
# img = cv2.imread('팀원사진\\왕능가\\왕능가.jpg')
# img = cv2.imread(os.path.join(base_dir, "case2.jpg"))
# print(os.path.join(base_dir, "case2.jpg"))
# print(img)