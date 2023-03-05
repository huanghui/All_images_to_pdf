from fpdf import FPDF
from PIL import Image
import os,sys
#from makepdf1.6 import add_pdf_Society

society=['2.1、后瑞社区处理站',\
         '2.2、黄田社区处理站',\
         '2.3、钟屋社区处理站' ,\
         '2.4、三围社区处理站',\
         '2.5、草围社区处理站',\
         '2.6、九围社区处理站',\
         '2.7、鹤州社区处理站' ,\
         '2.8、黄麻布社区处理站',\
         '2.9、簕竹角城中村处理站']


def addTxt(x,y,txt,pdf):
    pdf.set_font('simfang',size=12)   
    pdf.cell(x,y,txt,ln=1,align="L")
    #pdf.write(20,txt)
  

def addSociety(pdf,village):
    pdf.add_page()                 ##############首先要添加一个pdf页面
    txt="城中村厨余垃圾收运处理服务"
    pdf.add_font('simfang','','simfang.ttf',True)  #######添加字体  simfang为中文仿宋
    pdf.set_font('simfang',size=16)                   #######设置字体大小
    pdf.cell(0,0,txt,ln=1,align="L")                    #######添加到pdf文件的位置    
    
    pdf.set_font('simfang',size=12)   
    pdf.cell(12,12,village,ln=1,align="L")      #########添加小标题


def get_all_files2(path,find_end=".jpg"):
    print("开始读取后缀为",find_end,"的文件，返回相对路径")
    jpg_files=[]

    for root,dirs,files in os.walk(path):
        for file in files:
                if file.endswith(find_end):
                   jpg_files.append(os.path.join(root,file))
    #print(jpg_files[:5])
    print(jpg_files)                 
    return jpg_files


def makeLastPdf(pdfFileName,listPages):
    pdf=FPDF()
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
    length=40
    width=60
    basename=pdfFileName.split(".")[0]
    if(basename!="产出图"):
        basename=pdfFileName.split(".")[0]+"社区"
    

###########逐一添加到pdf矩阵当中
    for i in range(0,number,9):
        print("i的起始数值",i)
        if(i<number-9):
        
            addSociety(pdf,basename)   #########添加文字
            
            #pdf.image(path1+"\\" +images[i],20,20,length,width)
            #pdf.set_xy(0,0)
            addTxt(0,0,society[int(i/3)],pdf)   #########添加处理点名称
            #j=images.find("后瑞1")
            pdf.image(images[i],20,30,length,width)
            i+=1
            #j=images.find("后瑞2")
            pdf.image(images[i],20+60,30,length,width)
            #print(number)
            i+=1
            pdf.image(images[i],20+120,30,length,width)
            i+=1
            pdf.set_xy(10,95)
            addTxt(0,0,society[int(i/3)],pdf)
            #pdf.ln(20)
            pdf.image(images[i],20,30+70,length,width)
            i+=1
            #print("i的中间数值",i)
            pdf.image(images[i],20+60,30+70,length,width)
            i+=1
            pdf.image(images[i],20+120,30+70,length,width)
            i+=1
            pdf.set_xy(10,165)
            addTxt(0,0,society[int(i/3)],pdf)
            #pdf.ln(50)
            pdf.image(images[i],20,30+140,length,width)
            i+=1
            pdf.image(images[i],20+60,30+140,length,width)
            i+=1
            pdf.image(images[i],20+120,30+140,length,width)
        #pdf.add_page()
        #i+=1
        #print(images[0])
            print ("循环末端的数值",i)
        elif(i<number or i==number  and i>number-9):
            addSociety(pdf,basename)     ############增加一个pdf
           # i=i+1
            print ("最后非整页开始的数值",i)
            addTxt(0,0,society[6],pdf)   ##############增加小标题
            pdf.image(images[i],20,30,length,width)
            i=i+1
            if(i<number and i>number-9):
                pdf.image(images[i],20+60,30,length,width)
            #print(number)
                i+=1
                if(i<number and i>number-9):
                    pdf.image(images[i],20+120,30,length,width)
                    i+=1
                    if(i<number and i>number-9):
                        pdf.set_xy(10,95)
                        addTxt(0,0,society[7],pdf)   ##############增加小标题
                        pdf.image(images[i],20,30+70,length,width)
                        i+=1
                        print("i的中间数值",i)
                        if(i<number and i>number-9):
                            pdf.image(images[i],20+60,30+70,length,width)
                            i+=1
                            if(i<number and i>number-9):
                                pdf.image(images[i],20+120,30+70,length,width)
                                i+=1
                                if(i<number and i>number-9):
                                    pdf.set_xy(10,165)
                                    addTxt(0,0,society[8],pdf)   ##############增加小标题
                                    pdf.image(images[i],20,30+140,length,width)
                                    i+=1
                                    print("i的最后值",i)
                                    if(i<number):
                                        print("i的最后数值",i)
                                        pdf.image(images[i],20+60,30+140,length,width)
                                        i+=1
                                        print("i的最后数值",i)
                                        if(i<number or i==number):
                                            pdf.image(images[i],20+120,30+140,length,width)
                                        
                        
#############输出成pdf文件
    pdf.output(pdfFileName,"F")
    
    print("生成产出物图",pdfFileName,"成功")
    #pdf.Close()

listImages= get_all_files2("F:\\11月16日\\产出图",find_end=".jpg")
listImages.sort()
print(listImages)
makeLastPdf("产出图.pdf",listImages)
print("单独测试最后页")
