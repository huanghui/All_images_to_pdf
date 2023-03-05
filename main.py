##############解决循环图片重复添加的问题###############

###########添加中文文字成功，解决办法需要将字体直接添加到代码所在目录
############多次碰到照片也需要在该目录，需要解决目录访问的问题

##############path问题没有解决
###############2021/10/21
##################解决了整数整除情况下图片缺失的问题。

#################解决了path的问题################
#################尚未解决绝对路径生成和引用图片的问题。

#################暂时无法解决绝对路径问题和打包的问题。

###########由于该项目输出docx文件更方便，故升级为输出docx文件
##################1.2解决了访问子目录的问题，但排版比较混乱，没有严
#######没有严格按照不同社区来实现pdf拼接的问题。因为pdf一旦可以拼接
###############便可以分开处理各个社区的文件，然后拼接即可。
####必须要解决同一个目录下的索引的问题


##########1.4完成了PDF的合并转化成DOC文件并输出。



from fpdf import FPDF
from PIL import Image
#import Image
import os
import os.path
import sys

#from pdfmake import makePdf
from pdfmerge import pdf_merge
from makelastpdf2 import makeLastPdf 
from firstpage import make_First_Page

#sys.path.append("E:\images")
#from makeDocx import  makeDocx    ##########引入docx输出文件



#path="G:/Users/Administrator/AppData/Local/Programs/Python/Python38-32/Scripts/images"
#path="E:\\images"
path="F:\\2月2日\\2月2日"
#path1="F:\\abc"
#path2="F:\\11月16日\\草围"
#path="E:\images"

#path="G:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python38-32\\autodoc"
######cwd=os.getcwd()   ######
###########获取文件的绝对路径
########abspath=os.path.abspath(path)

#path1=os.path.abspath(path)

#print(path1)
#pdf.add_font('youyuan','','youyuan.ttf',True)
#f=open(path)
#path="G:/abc"

#def addTxt():
    #pdf.set_font('Arial',size=12)
   # pdf.cell(0,0,txt="城中村厨余垃圾收运处理服务",ln=1,align="L")



#pdf=FPDF()    ##############创建一个PDF对象

'''first_page=['航城街道城中村厨余垃圾8月收运处理明细',\
                             '——深圳市卫青环保科技有限公司',\
'项目服务总清单',\
'一、城中村厨余垃圾收运服务....................................1',\
'1.1后瑞社区收运...............................................1',\
'1.2黄田社区收运...............................................6',\
'1.3钟屋社区收运...............................................11',\
'1.4三围社区收运...............................................16',\
'1.5草围社区收运...............................................20',\
'1.6九围社区收运...............................................22',\
'1.7鹤洲社区收运...............................................28',\
'1.8黄麻布社区收运.............................................34',\
'1.9簕竹角城中村收运...........................................42',\
'二、城中村厨余垃圾处理服务....................................46',\
'2.1后瑞社区处理...............................................46',\
'2.2黄田社区处理...............................................46',\
'2.3钟屋社区处理...............................................47',\
'2.4三围社区处理...............................................48',\
'2.5草围社区处理...............................................49',\
'2.6九围社区处理...............................................49',\
'2.7鹤洲社区处理...............................................50',\
'2.8黄麻布社区处理.............................................51',\
'2.9簕竹角城中村处理...........................................52']

'''

###########具体社区
society=['1.1、后瑞社区（ 21个）',\
         '1.2、黄田社区收运（22个）',\
         '1.3、钟屋社区收运（19个）' ,\
         '1.4、三围社区收运（14个）',\
         '1.5、草围社区收运（11个）',\
         '1.6、九围社区收运（23个）',\
         '1.7、鹤州社区收运（23个）' ,\
         '1.8、黄麻布社区收运（33个）'\
         '1.9、簕竹角城中村收运（14个）']




#########添加文字
def add_pdf_Society(village):
    pdf.add_page()                 ##############首先要添加一个pdf页面
    txt="城中村厨余垃圾收运处理服务"
    pdf.add_font('simfang','','simfang.ttf',True)  #######添加字体  simfang为中文仿宋
    pdf.set_font('simfang',size=16)                   #######设置字体大小
    pdf.cell(0,0,txt,ln=1,align="L")                    #######添加到pdf文件的位置    
    
    pdf.set_font('simfang',size=12)   
    pdf.cell(12,12,village,ln=1,align="L")      #########添加小标题



##################获取文件夹目录下的所有图片文件##############
def get_all_files(path,find_end='.jpg' or '.jpeg' or '.png'):
    print("开始读取后缀为",find_end,"的文件，返回相对路径")
    jpg_files=[]

    for root,dirs,files in os.walk(path):
        for file in files:
            if file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.png'):
                jpg_files.append(os.path.join(root,file))
                #print(file)   
    #print(jpg_files)                 
    return jpg_files

##################获取文件夹目录下的所有图片文件############

def get_all_files2(path,find_end=".jpg" or ".jpeg" or ".png"):
    print("开始读取后缀为",find_end,"的文件，返回相对路径")
    jpg_files=[]

    for root,dirs,files in os.walk(path):
        for file in files:
                if file.endswith(find_end):
                   jpg_files.append(os.path.join(root,file))
    #print(jpg_files[:5])
    print(jpg_files)                 
    return jpg_files



##################制作第一页台帐文件#############

'''def  make_First_Page():
    pdf.add_page()
    pdf.add_font('simfang','','simfang.ttf',True) 
    n=len(first_page)
    pdf.set_font('simfang',size=20)
    pdf.cell(0,0,first_page[0],ln=1,align="L")           ###########处理大标题
    
    pdf.set_font('simfang',size=15)
    pdf.cell(0,10,first_page[1],ln=1,align="R")           ###########处理小标题

    pdf.set_font('simfang',size=18)
    pdf.cell(0,8,first_page[2],ln=1,align="C")           ###########处理小标题
    for i in range(3,n):
        #######添加字体  simfang为中文仿宋
        pdf.set_font('simfang',size=16)                   #######设置字体大小
        pdf.cell(10,12,first_page[i],ln=1,align="L",)                    #######添加到pdf文件的位置 


    pdf.output("首页.pdf","F")     

'''



def get_date(path):

    j=path.rfind("\\")
    print(j)
    k=path.find("\\")
    
    print(k)
    l=len(path)
    date=path[j+1 :]
    print(date)

    return date
############制作PDF文件##########################



def makePdf(pdfFileName,listPages):

    #make_First_Page()    ###########加入第一页面

    #########由于采用分开设计，所以暂不将第一页加入。
    


###########对所有图片排序，并计数，以便后续逐一添加
    images=listPages
    #print(images)
    #images.sort()
    number=len(images)
    #print(images)
    print("该目录下的图片数量为",+number)
    font_size=10
    length=66.7
    width=50
    basename=pdfFileName.split(".")[0]
    if(basename!="产出图"):
        basename=pdfFileName.split(".")[0]+"社区"
        if(basename=="后瑞社区"):
            basename="1.1、后瑞社区"+"(21个收运点)"
        if(basename=="黄田社区"):
            basename="1.2、黄田社区"+"(22个收运点)"
        if(basename=="钟屋社区"):
            basename="1.3、钟屋社区"+"(19个收运点)"
        if(basename=="三围社区"):
            basename="1.4、三围社区"+"(14个收运点)"
        if(basename=="草围社区"):
            basename="1.5、草围社区"+"(11个收运点)"
        if(basename=="九围社区"):
            basename="1.6、九围社区"+"(23个收运点)"
        if(basename=="鹤洲社区"):
            basename="1.7、鹤洲社区"+"(23个收运点)"
        if(basename=="黄麻布社区"):
            basename="1.8、黄麻布社区"+"(33个收运点)"
        if(basename=="簕竹角社区"):
            basename="1.9、簕竹角社区"+"(14个收运点)"
  

###########逐一添加到pdf矩阵当中
    for i in range(0,number,8):
        print("i的起始数值",i)
        if(i<number-8):
        
            add_pdf_Society(basename)   #########添加文字
            
            #pdf.image(path1+"\\" +images[i],20,20,length,width)

            pdf.image(images[i],20,20,length,width)
            i=i+1
            pdf.image(images[i],20+90,20,length,width)
            #print(number)
            i+=1
            pdf.image(images[i],20,20+70,length,width)
            i+=1
            pdf.image(images[i],20+90,20+70,length,width)
            i+=1
            #print("i的中间数值",i)
            pdf.image(images[i],20,20+140,length,width)
            i+=1
            pdf.image(images[i],20+90,20+140,length,width)
            i+=1
            pdf.image(images[i],20,20+210,length,width)
            i+=1
            pdf.image(images[i],20+90,20+210,length,width)
        #pdf.add_page()
        #i+=1
        #print(images[0])
            print ("循环末端的数值",i)
        elif(i<number or i==number  and i>number-8):
    

            add_pdf_Society(basename)     ############增加一个pdf
           # i=i+1
            print ("最后非整页开始的数值",i)
            pdf.image(images[i],20,20,length,width)
            i=i+1
            if(i<number and i>number-8):
                pdf.image(images[i],20+90,20,length,width)
            #print(number)
                i+=1
                if(i<number and i>number-8):
                    pdf.image(images[i],20,20+70,length,width)
                    i+=1
                    if(i<number and i>number-8):
                        pdf.image(images[i],20+90,20+70,length,width)
                        i+=1
                        print("i的中间数值",i)
                        if(i<number and i>number-8):
                            pdf.image(images[i],20,20+140,length,width)
                            i+=1
                            if(i<number and i>number-8):
                                pdf.image(images[i],20+90,20+140,length,width)
                                i+=1
                                if(i<number and i>number-8):
                                    pdf.image(images[i],20,20+210,length,width)
                                    i+=1
                                    print("i的最后值",i)
                                    if(i<number):
                                        print("i的最后数值",i)
                                        pdf.image(images[i],20+90,20+210,length,width)
        
#############输出成pdf文件
    pdf.output(pdfFileName,"F")
    
    print("生成",pdfFileName,"成功")
    #pdf.Close()









################主程序执行#########
if __name__=='__main__':

   #listImages=[imageFileName for imageFileName in os.listdir(path)\
                    #if (imageFileName.endswith("jpg") or imageFileName.endswith("png"))]


################不能查询子目录的文件
############获取文件目录所有文件夹极其子目录的图片并且存入数组。

##############1.3子目录的文件分别建立单个PDF文档，并且以子目录名命名。
################################ 制作首页
    
    
    sdate=get_date(path)
    make_First_Page(sdate)
    
    print("生成首页成功")

 ###########制作其他页   
    dirs=os.listdir(path)
    print(dirs)
    for file in dirs:
        #print(subdir_name)
        #subpath=os.getcwd()
        if(file.find("产出图")!=0):
            #listImages= get_all_files(os.path.join(path,file),find_end=".jpg")
            listImages= get_all_files(os.path.join(path,file),find_end='.jpg'or '.jpeg' or'.png')
            pdf=FPDF()
            print("文件名为",file)
            print(os.path.join(path,file))
            #print(listImages)
        #print(os.path.join(path))
        #print(listImages)
            makePdf(str(file)+".pdf",listImages)   
        elif(file.find("产出图")==0):
            print("这是产出图吗？",file)
            print("产出图生成独立的PDF")
            #listImages= get_all_files(os.path.join(path,file),find_end=".jpg")
            #listImages= state_sort(os.path.join(path,file))
            #pdf=FPDF()
            makeLastPdf(str(file)+".pdf",os.path.join(path,file))
            print("产出图不一样",os.path.join(path,file))
#############开始合并PDF成一个PDF
    pdf_merge("F:\\ipdf",sdate)
#############开始转化成doc文件
    #i#doc=Converter(allfile)
    #idoc.convert('台帐.docx')
    #idoc.close()

    input('Press <enter>')



     

