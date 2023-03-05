
from fpdf import FPDF
from PIL import Image


#title=[]
first_page=[ '——深圳市卫青环保科技有限公司',\
'项目服务总清单',\
'一、城中村厨余垃圾收运服务....................................1',\
'1.1后瑞社区收运...............................................1',\
'1.2黄田社区收运...............................................5',\
'1.3钟屋社区收运...............................................8',\
'1.4三围社区收运...............................................11',\
'1.5草围社区收运...............................................13',\
'1.6九围社区收运...............................................15',\
'1.7鹤洲社区收运...............................................18',\
'1.8黄麻布社区收运.............................................21',\
'1.9簕竹角社区收运.............................................26',\
'二、城中村厨余垃圾处理服务....................................28',\
'2.1后瑞社区处理...............................................28',\
'2.2黄田社区处理...............................................28',\
'2.3钟屋社区处理...............................................28',\
'2.4三围社区处理...............................................29',\
'2.5草围社区处理...............................................29',\
'2.6九围社区处理...............................................29',\
'2.7鹤洲社区处理...............................................30',\
'2.8黄麻布社区处理.............................................30',\
'2.9簕竹角城中村处理...........................................30']


#title="航城街道城中村厨余垃圾"+date+"收运处理明细"

def  make_First_Page(date):
    title="航城街道城中村厨余垃圾"+date+"收运处理明细"
  
    print(title)
    pdf=FPDF()
    pdf.add_page()
    pdf.add_font('simfang','','simfang.ttf',True) 
    n=len(first_page)
    pdf.set_font('simfang',size=20)
    pdf.cell(0,0,title,ln=1,align="C")           ###########处理大标题
    
    pdf.set_font('simfang',size=15)
    pdf.cell(0,15,first_page[0],ln=1,align="C")           ###########处理小标题

    pdf.set_font('simfang',size=15)
    pdf.cell(0,0,first_page[1],ln=1,align="C")           ###########处理小标题
    for i in range(2,n):
        #######添加字体  simfang为中文仿宋
        pdf.set_font('simfang',size=16)                   #######设置字体大小
        pdf.cell(10,12,first_page[i],ln=1,align="L",)                    #######添加到pdf文件的位置 


    pdf.output("首页.pdf","F")     



# 
#make_First_Page("8月2日")
#print("生成首页成功")