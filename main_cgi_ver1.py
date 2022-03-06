#xlsx 2 pdf

import win32com.client
import pathlib

#get all xlsx files
import glob
#merge
import PyPDF2
import xlwings

#pause
import subprocess

import logout

#log
outputlog = logout.Logger()


""" from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesize import A4,A3,landscape,portrait
from pdfrw import PdfReader
from pdfrw.toreportlab import makerl
from pdfrw.buildxobj import pagexobj """
import sys
import os

#マージ後のPDFファイル名
MERGE_PDF_FILENAME = "merge.pdf"

p_current = pathlib.Path()
p_current_abs = p_current.resolve()

#get all xlsx files
xlsx_list = glob.glob(str(p_current_abs.cwd())+r'\*.xlsx')

#all pdf to one pdf
merger = PyPDF2.PdfFileMerger()

#merge後のリスト出力用
mergelist = []

#each xlsx file to pdf
for i in range(len(xlsx_list)):
    p_sub = pathlib.Path(xlsx_list[i])
    p_abs = p_sub.resolve()
    print(p_abs.name + 'をPDFに変換しています...')
    #open Excel
    app = win32com.client.Dispatch('Excel.Application')
    app.Visible = False
    app.DisplayAlerts = False
    #read workbook
    book = app.Workbooks.Open(p_abs)
    
    #全てのシート名をリスト取得
    excelSheets = []
    for sheet in book.Sheets:
        excelSheets.append(sheet.Name)
    #excelファイル名、sheet名をログ出力
    outputlog.info(p_abs.name+' をPDFに変換しました。（sheet：'+str(excelSheets)+'）')

    #save book by pdf
    book.ExportAsFixedFormat(0,str(p_abs)+'.pdf',1)

    #save sheet by pdf
    #sheet = book.Worksheets("sheet1").Select()
    
    #merge
    merger.append(str(p_abs)+'.pdf')
    mergelist.append(str(p_abs.name) + '.pdf')
    #quit
    #app.Quit()
    #quit
    book.Close()

#write merge
merger.write(MERGE_PDF_FILENAME)
outputlog.info(str(mergelist) + 'をマージした'+MERGE_PDF_FILENAME+ 'を作成しました。')


merger.close()
#行するには何かキーを押してください . . .  を表示
subprocess.call('PAUSE', shell=True)