from codecs import utf_8_decode
import os
from fpdf import FPDF, HTMLMixin

# cell(ancho, largo, contenido, borde, salto de línea)

l = u"""Por medio de la presente vego a manifestar mi adhesión y afiliación como socio al Sindicato Nacional de
Trabajadores del Seguro Social (S.N.T.S.S.) a partir de la fecha de mi contratación en el Instituto Mexicano
del Seguro Social, proporcionando los siguientes datos personales en términos de lo dispuesto por el artículo
5 del estatuto vigente del Sindicato Nacional de Trabajadores del Seguro Social (S.N.T.S.S.):"""


l1 =u"""Declaro con fundamento en lo dispuesto en el Artículo 358 fracción I de la Ley Federal de Trabajo, por así convenir a mis
intereses, que es mi deseo afiliarme al Sindicato Nacional de Trabajadores del Seguro Social, manifestando desde este momento
que conozco los estatutos sindicales que rigen la vida interna de dicha organización y es mi voluntad acatarlos. Autorizando
expresamente que el Instituto Mexicano del Seguro Social, entere a favor del Sindicato Nacional de Trabajadores del Seguro
Social (S.N.T.S.S.) la cuota sindical corespondiente y aportaciones, a través del descuento directo que se realice a mi salario, en
los términos y plazos que así lo disponga el estatuto interno de dicha organización y con fundamento en lo dispuesto por el
artícula 110 fracción VI de la Ley Federal de Trabajo"""

html = """<B>Sindicato Naconal de Trabajadores del seguro Social</B>, con domicilio <B>en calle Zamora 107, colonia Condesa, Alcaldía
Cuauhtémoc, C.P. 06140, Ciudad de México</B>, en cumplimiento a los arículos 2, fracción II, 3 fracción 6,7,8,12,4,15 y
demás relativos de la Ley Federal de Protecci´n de datos Personales en Posecición de los Particulares, su Reglamento y
Lineamientos; es el <B>responsable</B> de la obtención, uso, divulgación o almacenamiento y protección de sus datos
personales, y al respecto le informo lo siguiente:
Los datos personales que recabamos de Usted en la cédula de afiliación, los utilizaremos para las siguientes
finalidades que son necesarias para el desarrollo de las actividades que nuestro marco estatutario establece:
<B>Dar cumplimiento a la fracción X del artículo 13 que se refiere a informar al secretario del Interior y propaganda: el
domicilio o cambio de él así como los datos previstos en los padrones.
Cumpli con la fracción IV del artículo 77 que señala que la Secretaría del Interior y Propaganda debe contar con el
registro de los miembros del Sindicato (nombre completo, fecha y lugar de nacimiento, estado civil, domicilio, 
categoría y sueldo, fecha de ingreso al trabajo y al Sindicato) para mantener al corriente el padrón de miembros.</B>


<B>Actualización de base de datos electrónicos.</B>
De manera adicional, utilizaremos su información personal para las siguientes finalidades que no son necesarias para
el servicio que otorgamos, pero que nos permiten y facilitan brindarle una mejor atención:
<B>Análisis estadísticos en el marco de la planeación de actividades sindicales.</B>


<B>TRANSFERENCIA DE DATOS PERSONALES.</B>
Conforme a las actividades propias y con el objetivo de cumplir con la finlidades mencionadas, se podrán transferir
algunos de sus datos personales a terceros tales como:
INTITUTO MEXICANO DEL SEGURO SOCIAL, SECRETARÍA DEL TRABAJO Y PREVISIÓN SOCIAL (DIRECCIÓN GENERAL DE
REGISTRO DE ASOCIACIONES); CENTOR FEDERAL DE CONCILIACIÓN Y REGISTRO LABORAL; AUTORIDADES LABORALES,
ADMINISTRATIVAS O JUDICIALES COMPETENTES; INAI).
Quienes se encontrarán obligados a darle a conocer su propio Aviso de Privacidad; lo anterior a fin de evitar daño,
pérdida, destrucción, alteración o un tratamiento no autorizado de sus datos personales.
En caso de que no desee que sus datos personales sean tratados para estos fines adicionales, desde este momento
usted nos puede comunicar lo anterior mediante <B>oficio dirigido a la Undiad de Transparencia del S.N.T.S.S. o la
Secretaria del interior y Propaganda del Cómite Ejecutivo Nacional</B>, acompañando <B>los siguientes datos:</B> Nombre del
titular, matrícula, adscripción, domicilio, correo electrónico y la descripción exacta de los datos personales
adicionales que menciona.


Los <B>Derechos</B> ARCO Acceso, Rectificación, Cancelación u oposición podrán ser ejercidos por el titular, previa
acreditación de su identidad, mediante <B>oficio dirigido a la Unidad de Transparencia del S.N.T.S.S. a la Secretaría del 
Interior y Propaganda del Cómite Ejecutivo Nacional</B> o través del adirección del correo electrónico
transparencia.sntss@hotmail.com, debiendo adjuntar copia de su identificación oficial vigente (INE, pasaporte,
Cédula Profesional o Cartilla Militar) o través del Representante legal del titular previa acreditación, la identidad del
representante y la acreditación de la representación, mediante instrumento notarial, carta poder firmada por el
titular y ante la presencia de dos testigos o mediante declaración en comparecencia personal del titular y
acompañando los datos del párrafo anterior.
En caso de ejecer el derecho de <B> Rectificación</B> de sus datos personales, deberá de indicar la corrección o actualización
que requiera se modifiquen, debiendo de aportar los documentos probatorios para sustentar la solicitud. Así mismo
le informamos que no se transfieren a terceros sus datos personales recabados en esta cédula.


Para mayor información, sobre los términos y condiciones en que serán tratados sus datos personales, así como la
actualización de este aviso y la forma en que podrá ejercer sus derechos (ARCO), puede consultar el aviso de 
privacidad integral en <U>www.sntss.org.mx/transparencia.</U>
"""

class FPDF(FPDF, HTMLMixin):
    def setLogo(self):
        path_dir = os.path.dirname('C:\\Users\\jazyi\\flask-projects\\cedulaOriginal\\static\\')
        path_file = os.path.join(path_dir, 'sntsslogo.png')
        self.image(path_file, x=5, y=5, w=20, h=20)
        self.ln(1)
        self.set_xy(7, 24)
        self.set_font('Arial','B', 5)
        self.cell(txt='SECCION III')
        self.ln(1)
        self.set_xy(8, 27)
        self.cell(txt='JALISCO')
        self.set_xy(40, 5)
        self.set_font('Arial', 'B',14)
        self.cell(150,10, 'Sindicato Nacional de Trabajadores del Seguro Social', 1)
        self.set_xy(55, 13)
        self.set_font('Arial', 'B', 12)
        self.cell(100, 10, 'CÉDULA DE AFILIACIÓN',1, 1, 'C')
        self.set_xy(40, 22)
        self.set_font('Arial', '', 5)
        self.multi_cell(150,1.5, l, 1, 'C')
        self.ln(1)
    def setData(self):
        #self.set_xy(5, 50)
        path_dir = os.path.dirname('C:\\Users\\jazyi\\flask-projects\\cedulaOriginal\\static\\')
        img = os.path.join(path_dir, 'rectrod.png')
        self.image(img, x=25, y=30, w=170, h=80)
        self.set_xy(70, 35)
        self.set_font('Arial', 'B', 10)
        self.cell(80, 8, 'DATOS PERSONALES', 1, 1, 'C')
        # form data
        self.set_xy(35, 45)
        self.set_font('Arial', '', 6)
        self.cell(30,8, 'NOMBRE:', 1, 1)
        # draw line
        self.line(45, 50, 170, 50)
        self.set_xy(52,51)
        self.set_font('Arial', '', 5)
        self.cell(23, 3, 'Apellido Paterno', 1, 1, 'L')
        self.set_xy(85, 51)
        self.set_font('Arial', '', 5)
        self.cell(23, 3, 'Apellido Materno',1 , 1, 'R')
        self.set_xy(120, 51)
        self.set_font('Arial', '', 5)
        self.cell(23, 3, 'Nombres', 1, 1, 'R')
        # data2
        self.set_xy(70, 52)
        self.set_font('Arial', 'B', 5)
        self.cell(80, 8, 'DOMICILIO PARTICULAR', 1, 1, 'C')

        self.line(35, 63, 80, 63)
        self.set_xy(38, 63.5)
        self.set_font('Arial', '', 5)
        self.cell(25, 3, 'Calle y No. Exterior y/o Interior', 1, 1, 'L')
        self.line(82, 63, 118, 63)
        self.set_xy(85, 63.5)
        self.set_font('Arial', '', 5)
        self.cell(25, 3, 'Colonia', 1, 1, 'C')
        self.line(120, 63, 185, 63)
        self.set_xy(140, 63.5)
        self.set_font('Arial', '', 5)
        self.cell(25, 3, 'Alcaldía y/o Municipio', 1, 1, 'C')

        self.line(35, 72, 55, 72)
        self.set_xy(39, 72.5)
        self.set_font('Arial', '', 5)
        self.cell(25, 3, 'Código Postal', 1, 1, 'L')
        self.line(60, 72, 80, 72)
        self.set_xy(59, 72.5)
        self.set_font('Arial', '', 5)
        self.cell(25, 3, 'Localidad', 1, 1, 'C')
        self.line(86, 72, 118, 72)
        self.set_xy(85, 72.5)
        self.set_font('Arial', '', 5)
        self.cell(25, 3, 'Tel. Celular', 1, 1, 'C')
        self.line(125, 72, 185, 72)
        self.set_xy(140 ,72.5)
        self.set_font('Arial', '', 5)
        self.cell(12, 3, 'Correo Electrónico', 1, 1, 'C')

        self.set_xy(35, 80)
        self.set_font('Arial', '', 5)
        self.cell(23, 3, 'NACIMIENTO:', 1, 1, 'L')

        self.line(52, 82.5, 110, 82.5)
        self.set_xy(70, 83)
        self.set_font('Arial', '', 5)
        self.cell(12, 3, 'Lugar', 1, 1, 'C')

        self.set_xy(115, 80)
        self.set_font('Arial', '', 5)
        self.cell(12, 3, 'FECHA:', 1, 1, 'C')
 
        self.line(130, 82.5, 160, 82.5)

        self.set_xy(140, 83)
        self.set_font('Arial', '', 5)
        self.cell(12, 3, 'Día-Mes-Año', 1, 1, 'C')

        self.line(35, 90, 70, 90)
        self.set_xy(40, 90.5)
        self.set_font('Arial', '', 5)
        self.cell(12, 3, 'Número de Seguridad Social')

        self.line(75, 90, 115, 90)
        self.set_xy(85, 90.5)
        self.set_font('Arial', '', 5)
        self.cell(12, 3, 'RFC', 1, 1, 'C')

        self.line(120, 90, 170, 90)
        self.set_xy(140, 90.5)
        self.set_font('Arial', '', 5)
        self.cell(12, 3, 'CURP', 1, 1, 'C')

        self.line(45, 99, 92, 99)
        self.set_xy(60, 99.5)
        self.set_font('Arial', '', 5)
        self.cell(12, 3, 'Estado Civil', 1, 1, 'C')

        self.line(105, 99, 150, 99)
        self.set_xy(120, 99.5)
        self.set_font('Arial', '', 5) 
        self.cell(12, 3, 'Sexo', 1, 1, 'C')
    def setData2(self):
        self.set_xy(70, 110)
        self.set_font('Arial', 'B', 10)
        self.cell(80, 8, 'DATOS LABORALES', 1, 1, 'C')
        
        path_dir = os.path.dirname('C:\\Users\\jazyi\\flask-projects\\cedulaOriginal\\static\\')
        img = os.path.join(path_dir, 'rectrod.png')
        self.image(img, x=25, y= 120, w=170, h=40)

        self.line(35, 132, 70, 132)
        self.set_xy(50, 132.5)
        self.set_font('Arial', '', 5)
        self.cell(12, 3, 'Matrícula', 1, 1, 'C')

        self.line(75, 132, 110, 132)
        self.set_xy(85, 132.5)
        self.set_font('Arial', '', 5)
        self.cell(12, 3, 'Categoría', 1, 1, 'C')
        
        self.line(120, 132, 150, 132)
        self.set_xy(130, 132.5)
        self.set_font('Arial', '', 5)
        self.cell(12, 3, 'Adscripción', 1, 1, 'C')
 
        self.line(155, 132, 180, 132)
        self.set_xy(165, 132.5)
        self.set_font('Arial', '', 5)
        self.cell(12, 3, 'Turno', 1, 1, 'C')
 

        self.line(35, 150, 80, 150)
        self.set_xy(50, 150.5)
        self.set_font('Arial', '', 5)
        self.cell(12, 3, 'Tipo de Contratación', 1, 1, 'C')
 
        self.line(85, 150, 150, 150)
        self.set_xy(100, 150.5)
        self.set_font('Arial', '', 5)
        self.cell(12, 3, 'Fecha de Ingreso al IMSS', 1, 1, 'C')
 
        self.line(155, 150, 180, 150)
        self.set_xy(165, 150.5)
        self.set_font('Arial', '', 5)
        self.cell(12, 3, 'Antiguedad', 1, 1, 'C')

    def setLegend(self):
        path_dir = os.path.dirname('C:\\Users\\jazyi\\flask-projects\\cedulaOriginal\\static\\')
        img = os.path.join(path_dir, 'rectrod.png')

        self.image(img, x=25, y=180, w=170, h=60)
        #multi_cell(w, h, txt, border = 0, align, fill)
        self.set_xy(40, 195)
        self.set_font('Arial', '', 6)
        self.multi_cell(130, 4, l1, 1, 'J')

    def setFoo(self):
        self.line(30, 270, 90, 270)
        self.set_xy(55, 270.5)
        self.set_font('Arial', '', 5)
        self.cell(12, 3, 'NOMBRE COMPLETO', 1, 1, 'C')       
        # 
        self.line(100, 270, 170, 270) 
        self.set_xy(130, 270.5)
        self.set_font('Arial', '', 5)
        self.cell(12, 3, 'FIRMA', 1, 1, 'C')



    def reverseFace(self):
        path_dir = os.path.dirname('C:\\Users\\jazyi\\flask-projects\\cedulaOriginal\\static\\')
        path_file = os.path.join(path_dir, 'sntsslogo.png')
        self.image(path_file, x=5, y=5, w=20, h=20)
        self.ln(1)
        self.set_xy(7, 24)
        self.set_font('Arial','B', 5)
        self.cell(20, 10, 'SECCION III',1,0)
        self.ln(1)
        self.set_xy(8, 27)
        self.cell(20,10, 'JALISCO',1, 0)
        self.set_xy(40, 5)
        self.set_font('Arial', 'B',14)
        self.cell(150,10, 'Sindicato Nacional de Trabajadores del Seguro Social', 1)

        # rect(x, y, w, h, style)
        self.rect(x=30, y=20, w=170, h=210)

        self.set_xy(115, 25)
        self.set_font('Arial', 'B', 7)
        self.cell(10, 3, 'Aviso de Privacidad', border=1, align='C')
        self.set_xy(35, 27)
        self.write_html(html)

 
if __name__ == '__main__':
    pdf = FPDF()
    pdf.add_page()
    #pdf.set_doc_option()
    pdf.setLogo()
    pdf.setData()
    pdf.setData2()
    pdf.setLegend()
    pdf.setFoo()
    pdf.add_page()
    pdf.reverseFace()
    pdf.output('3.pdf')#.encode('utf-8')