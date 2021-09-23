import os
import shutil
cur_path = r"D:\WJZ\学习\Python学习资料\968714133"
new_path = r"D:\WJZ\学习\Python学习资料\2020老男孩It教育最新Python3.8开发全套（学完可就业）"
used_name_dir = r"D:\WJZ\学习\Python学习资料\used_name.txt"
new_name_dir = r"D:\PyCharm_Code\Tutorials\example\2020老男孩It教育最新Python3.8开发全套（学完可就业）.txt"

# 将文件从当前文件夹移动至另一个文件夹中
def remove_files(cur_path, new_path):
    for root, dirs, files in os.walk(cur_path):
        for file in files:
            if not file.endswith('.mp4'):    # 筛选后缀名为.mp4的文件
                continue
            src = os.path.join(root, file)    # 文件的当前绝对路径
            dst = os.path.join(new_path, file)    # 移动后文件的绝对路径
            shutil.move(src, dst)  # 将文件从src路径移动至dst路径
            print("文件已全部从{}移动至{}".format(cur_path, new_path))


# def rename_files(path):
#     i = 0
#     with open(r"D:\PyCharm_Code\Tutorials\example\newname.txt", 'r', encoding='utf8') as f:
#         # new_name_list = []
#         new_name_list = f.read().splitlines()
#     for file in os.listdir(path):
#         if not file.endswith('.mp4'):
#             continue
#         used_name = os.path.join(path, file)
#         new_name = os.path.join(path, new_name_list[i]+'.mp4')
#         # print(used_name)
#         # print(new_name)
#         os.rename(used_name, new_name)
#         i += 1


############################ 将文件重新排序 ############################
# used_name_list = os.listdir(new_path)
# with open(used_name_dir, 'w', encoding='utf8') as f:
#     #sorted(used_name_list, key=lambda info: (int(info[:-6]), info[-4:]))按数字大小排序
#     for file in sorted(used_name_list, key=lambda info: (int(info[:-6]), info[-4:])):
#         f.write(file+"\n")
#
# new_names = []
# with open(used_name_dir, 'r', encoding='utf8') as f:
#     used_names = f.read().splitlines()
#     print(used_names)
#     for file in used_names:
#         new_names.append(os.path.join(new_path, file))
#     print(new_names)
# with open(used_name_dir, 'w', encoding='utf8') as f:
#     for file in new_names:
#         f.write(file+'\n')
############################ 将文件重新排序 ############################


# with open(used_name_dir, 'r', encoding='utf8') as f:
#     used_names = f.read().splitlines()
# with open(new_name_dir, 'r', encoding='utf8') as f:
#     new_names = f.read().splitlines()

for file in os.listdir(new_path):
    # print(file)
    os.rename(os.path.join(new_path, file), os.path.join("D:\WJZ\学习\Python学习资料", file[33:]+'.mp4'))
