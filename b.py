import os

def state_sort(path):
    #print("开始排序",state,"的文件，返回相对路径")
    jpg_files=[]

    for root,dirs,files in os.walk(path):
        for file in files:
            if file.find("后")==0:
                jpg_files.append(os.path.join(root,file))
        for file in files:
            if file.find("黄田")==0:
                jpg_files.append(os.path.join(root,file))
        for file in files:
            if file.find("钟屋")==0:
                jpg_files.append(os.path.join(root,file))
        for file in files:
            if file.find("三围")==0:
                jpg_files.append(os.path.join(root,file))
        for file in files:
            if file.find("草围")==0:
                jpg_files.append(os.path.join(root,file))
        for file in files:
            if file.find("九围")==0:
                jpg_files.append(os.path.join(root,file))
        for file in files:
            if file.find("鹤")==0:
                jpg_files.append(os.path.join(root,file))
        for file in files:
            if file.find("黄麻布")==0:
                jpg_files.append(os.path.join(root,file))
        for file in files:
            if file.find("簕")==0:
                jpg_files.append(os.path.join(root,file))
     
    #print(jpg_files[:5])
    #print(jpg_files)
    print(len(jpg_files))
   # number=len(jpg_files)
    #print("排序以后生成的图片有",number,"张")
    return jpg_files


#listImages= state_sort("F:\\11月16日\\产出图")
#listImages.sort()
#print(listImages)
#makeLastPdf("产出图.pdf",listImages)


#print("排序后生成的列表为",state_sort("F:\\11月16日\\产出图"),len(state_sort("F:\\11月16日\\产出图")))

#print("单独测试最后页")
