import os

from PyPDF2 import PdfFileMerger

from pdf2docx import Converter

from pagenumber import addPageNumber

def pdf_merge(target_path,sdate):
    #pdf_lst=[f for f in os.listdir(target_path)if f.endswith('.pdf')]
    pdf_lst=[]
    #pdf_lst=[os.path.join(target_path,filename) for filename in pdf_lst]
    pdf_lst.insert(0,"首页.pdf")
    pdf_lst.insert(1,"后瑞.pdf")
    pdf_lst.insert(2,"黄田.pdf")
    pdf_lst.insert(3,"钟屋.pdf")
    pdf_lst.insert(4,"三围.pdf")
    pdf_lst.insert(5,"草围.pdf")
    pdf_lst.insert(6,"九围.pdf")
    pdf_lst.insert(7,"鹤洲.pdf")
    pdf_lst.insert(8,"黄麻布.pdf")
    pdf_lst.insert(9,"簕竹角.pdf")
    pdf_lst.insert(10,"产出图.pdf")
       
    file_merger=PdfFileMerger()

    file_merger.append(pdf_lst[0])
    for pdf in pdf_lst:
        if(("产出图" in str(pdf))!=True):
            if(("首页" in str(pdf))!=True):
                file_merger.append(pdf)
                print(pdf)
        else:
            print(pdf+"发现了")
    file_merger.append("产出图.pdf")
    
    file_merger.write(str(sdate)+'.pdf')
    print("合并生成merge.pdf成功")
    #print(allfile)
    addPageNumber(str(sdate)+'.pdf')  ############增加页码
    #idoc=Converter('merge_new.pdf')
    #idoc.convert('台帐.docx')
   # idoc.close()
    print("生成pdf文件成功")
   


#pdf_merge("F:")
