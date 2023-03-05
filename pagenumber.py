#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''add page number to pdf file'''

import sys
import os

import reportlab
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from PyPDF2 import PdfFileWriter, PdfFileReader


def create_pdf_with_pagenumber(tmp, num):
    '''create tmp pdf that only include page number'''
    pdfmetrics.registerFont(
        TTFont('Times-New-Roman', 'C:\\Windows\\Fonts\\times.ttf'))
    c = canvas.Canvas(tmp)
    for i in range(num):
        c.setFont('Times-New-Roman', 12)
        c.drawString((104)*mm, (8)*mm, str(i + 1))
        c.showPage()
    c.save()


def addPageNumber(path):
    #path = 'merge.pdf'
    if len(sys.argv) == 1:
        if not os.path.isfile(path):
            sys.exit(1)
    else:
        path = os.path.basename(sys.argv[1])

    tmp = "tmp.pdf"
    dst_pdf = PdfFileWriter()
    with open(path, 'rb') as f:
        src_pdf = PdfFileReader(f, strict=False)
        n = src_pdf.getNumPages()
        create_pdf_with_pagenumber(tmp, n)

        with open(tmp, 'rb') as ftmp:
            num_pdf = PdfFileReader(ftmp)
            for i in range(n):
                print('page: %d of %d' % (i+1, n))
                page = src_pdf.getPage(i)
                num_layer = num_pdf.getPage(i)

                page.mergePage(num_layer)
                dst_pdf.addPage(page)

        if dst_pdf.getNumPages():
            output = '{}_new.pdf'.format(path.split('.')[0])
            with open(output, 'wb') as f:
                dst_pdf.write(f)

        os.remove(tmp)
    print("执行成功",n)
#print("页码数为",n)
#main()
#print("执行成功",n)

