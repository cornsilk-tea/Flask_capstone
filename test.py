from deepface import DeepFace
import os


base_dir = os.getcwd()
# print("현재 디렉토리는 {}".format(base_dir))
name_list = os.listdir(os.path.join(base_dir, 'img_data'))
# print(name_list)
IMG_NAME = 'case2.jpg'
src_img = os.path.join(base_dir, IMG_NAME)
# print(src_img)

# 모든 폴더를 돌아가며 가장 첫번째 사진을 비교해서 
# 각 이미지의 dist를 res_list에 저장해준다.
res_list = []
for stu_name in name_list:
    data_list = os.listdir(os.path.join(base_dir, 'img_data', stu_name))
    res = DeepFace.verify(img1_path=src_img, 
    img2_path=os.path.join(base_dir, 'img_data', stu_name, data_list[0]),
    distance_metric='euclidean_l2', 
    detector_backend='mtcnn')
    res_list.append(res['distance'])

# res_list의 최솟값이 있는 인덱스를 name_list에 넣어 가장 일치하는 인물을 출력해준다.
print(name_list[res_list.index(min(res_list))])

