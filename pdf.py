from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import letter
import os
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import Paragraph

cv = Canvas(filename='3.pdf')

pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))
pdfmetrics.registerFont(TTFont('Arial', 'ArialBd.ttf'))
pdfmetrics.registerFont(TTFont('Arial', 'ArialBI.ttf'))



path_dir = 'C:\\Users\\jazyi\\flask-projects\\cedulaOriginal\\static\\'
img_path = os.path.join(path_dir, 'sntss-logo.png')
t = 'SECCION III'
t1 = 'JALISCO'
cv.drawImage(img_path, 10, 750, width=45, height=60)
cv.setFont('Arial', 5)
cv.drawString(10,790, t)
cv.drawString(10, 783, t1)

s = 'Sindicato Nacional de Trabajadores del Seguro Social'
cv.setFont('Arial', 14)
cv.drawCentredString(300, 800, s)

s1 = 'CÉDULA DE AFILIACIÓN'
cv.setFont('Times-Bold', 12)
cv.drawCentredString(300, 785, s1)

l = """Declaro con fundamento en lo dispuesto en el Artículo 358 fracción I de la Ley Federal de Trabajo, por así convenir a mis
intereses, que es mi deseo afiliarme al Sindicato Nacional de Trabajadores del Seguro Social, manifestando desde este momento
que conozco los estatutos sindicales que rigen la vida interna de dicha organización y es mi voluntad acatarlos. Autorizando
expresamente que el Instituto Mexicano del Seguro Social, entere a favor del Sindicato Nacional de Trabajadores del Seguro
Social (S.N.T.S.S.) la couta sindical corespondiente y aportaciones, a través del descuento directo que se realice a mi salario, en
los términos y plazos que así lo disponga el estatuto interno de dicha organización y con fundamento en lo dispuesto por el
artícula 110 fracción VI de la Ley Federal de Trabajo"""
p = Paragraph(l)
cv.drawCentredString(60,60, p)
#cv.drawCentredString(300, 100, l)
print(cv.getAvailableFonts())
cv.showPage()
cv.save()



