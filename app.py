import os
from flask import Flask, render_template, redirect, request, url_for, make_response
from psycopg2 import connect, extras
from fpdf import FPDF, HTMLMixin
#from fpdf2 import FPDF2, HTMLMixin
from codecs import utf_8_decode
#from datetime.datetime import strftime



l = u"""Por medio de la presente vego a manifestar mi adhesión y afiliación como socio al Sindicato Nacional de
Trabajadores del Seguro Social (S.N.T.S.S.) a partir de la fecha de mi contratación en el Instituto Mexicano
del Seguro Social, proporcionando los siguientes datos personales en términos de lo dispuesto por el artículo
5 del estatuto vigente del Sindicato Nacional de Trabajadores del Seguro Social (S.N.T.S.S.):"""


l1 ="""Declaro con fundamento en lo dispuesto en el Artículo 358 fracción I de la Ley Federal de Trabajo, por así convenir a mis
intereses, que es mi deseo afiliarme al Sindicato Nacional de Trabajadores del Seguro Social, manifestando desde este 
momento que conozco los estatutos sindicales que rigen la vida interna de dicha organización y es mi voluntad acatarlos.
Autorizando expresamente que el Instituto Mexicano del Seguro Social, entere a favor del Sindicato Nacional de 
Trabajadores del Seguro Social (S.N.T.S.S.) la cuota sindical corespondiente y aportaciones, a través del descuento 
directo que se realice a mi salario, en los términos y plazos que así lo disponga el estatuto interno de dicha organización
y con fundamento en lo dispuesto por el artícula 110 fracción VI de la Ley Federal de Trabajo"""




app = Flask(__name__, template_folder='templates', static_folder='static')

# cell(ancho, largo, contenido, borde, salto de línea)
WTTF_CSRF_SECRET_KEY = os.urandom(16)



def getConnection():
    try:
        conn = connect("dbname=cedulasdb2022 user=postgres password=Z4dk13l2017** port=5432")
        print('Conectado')
        return conn
    except:
        print('Mala conexión') 



@app.route('/')
def index():
    return 'hola mundo'






@app.route('/registro', methods=['GET', 'POST'])
def registro():
    error = None
    if request.method == 'POST':
        try:
            app = request.form['app']
            if not app:
                print('caja vacía')
                error = 'Escribre Apellido Paterno'
                return render_template('errors.html', title='Error page', error= error)
            apm = request.form['apm']
            if not apm:
                print('caja vacía')
                error = 'Escribre Apellido Materno'
                return render_template('errors.html', error= error)
            name = request.form['name']
            if not name:
                print('caja vacía')
                error = 'Escribre Nombre'
                return render_template('errors.html', error= error)
            dom = request.form['dom']
            if not dom:
                print('caja vacía')
                error = 'Escribre  Domicilio'
                return render_template('errors.html', error= error)
            col = request.form['col']
            if not col:
                print('caja vacía')
                error = 'Escribre una Colonia'
                return render_template('errors.html', error= error)
            mcpio = request.form['mcpio']
            if not mcpio:
                print('caja vacía')
                error = 'Escribre una Municipio'
                return render_template('errors.html', error= error)
            cp = request.form['cp']
            if not cp:
                print('caja vacía')
                error = 'Escribre una CP'
                return render_template('errors.html', error= error)
            local = request.form['local']
            if not local:
                print('caja vacía')
                error = 'Escribre una Localidad'
                return render_template('errors.html', error= error)
            cel = request.form['cel']
            if not cel:
                print('caja vacía')
                error = 'Escribre una Celular'
                return render_template('errors.html', error= error)
            email = request.form['email']
            if not email:
                print('caja vacía')
                error = 'Escribre una Email'
                return render_template('errors.html', error= error)
            l_nac = request.form['l_nac']
            if not l_nac:
                print('caja vacía')
                error = 'Escribre una Lugar de Nacimiento'
                return render_template('errors.html', error= error)
            f_nac = request.form['f_nac']
            if not f_nac:
                print('caja vacía')
                error = 'Escribre una Fecha de Nacimiento'
                return render_template('errors.html', error= error)
            nss = request.form['nss']
            if not nss:
                print('caja vacía')
                error = 'Escribre una # de Seguro Social'
            rfc = request.form['rfc']
            if not rfc:
                print('caja vacía')
                error = 'Escribre una RFC'
                return render_template('errors.html', error= error)
            curp = request.form['curp']
            if not curp:
                print('caja vacía')
                error = 'Escribre una Colonia'
                return render_template('errors.html', error= error)
            edo_civil = request.form['edo_civil']
            if not edo_civil:
                print('caja vacía')
                error = 'Selecciona Estado Civil'
                return render_template('errors.html', error= error)
            sexo = request.form['sexo']
            if not sexo:
                print('caja vacía')
                error = 'Selecciona Sexo'
                return render_template('errors.html', error= error)
            matricula = request.form['matricula']
            if not matricula:
                print('caja vacía')
                error = 'Escribre una Matrícula'
                return render_template('errors.html', error= error)
            categoria = request.form['categoria']
            if not categoria:
                print('caja vacía')
                error = 'Escribre una Categoría'
                return render_template('errors.html', error= error)
            adscripcion = request.form['adscripcion']
            if not adscripcion:
                print('caja vacía')
                error = 'Selecciona Adscripción'
                return render_template('errors.html', error= error)
            turno = request.form['turno']
            if not turno:
                print('caja vacía')
                error = 'Selecciona Turno'
                return render_template('errors.html', error= error)
            t_contr = request.form['t_contr']
            if not t_contr:
                print('caja vacía')
                error = 'Selecciona Tipo de COntratación'
                return render_template('errors.html', error= error)
            f_ingr = request.form['f_ingr']
            if not f_ingr:
                print('caja vacía')
                error = 'Selecciona Fecha de Ingreso'
                return render_template('errors.html', error= error)
            antiguedad = request.form['antiguedad']
            if not antiguedad:
                print('caja vacía')
                error = 'Escribre Antiguedad'
                return render_template('errors.html', error= error)

            if not app or not apm or not name or not dom or not col or not mcpio or not cp or not local or not cel or not cel or not email or not l_nac or not f_nac or not nss or not rfc or not curp or not edo_civil or not sexo or not matricula or not categoria or not adscripcion or not t_contr or not f_ingr or not antiguedad:
                pass

            print(app, apm, name)

            try:
                con = getConnection()
                cur = con.cursor()
                cur.execute("INSERT INTO data (app, apm, name, dom, col, mcpio, cp, local, cel, email, l_nac, f_nac, nss, rfc, curp, edo_civil, sexo, matricula, categoria, adscripcion, turno, t_contr, f_ingr, antiguedad)\
                             VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id",  
                             (app, apm, name, dom, col, mcpio, cp, local, cel, email, l_nac, f_nac, nss, rfc, curp, edo_civil, sexo, matricula, categoria, adscripcion, turno, t_contr, f_ingr, antiguedad));
                    
                con.commit()
                cur.close()
                con.close()
                
            
        
            except Exception as e:
                print(e)
                error = 'Registro no Realizado'
        except:
            return redirect(url_for(index))        
    return render_template('registro.html', title='Registro de Cédula', error=error)
    #else:
    #    return render_template('registro.html')





@app.route('/cedulapdf/<int:id>')
def create_cedula(id):
    global FPDF
    id = id
    #if request.method == 'GET':
    con = getConnection()
    cur = con.cursor(cursor_factory=extras.DictCursor)
    cur.execute("SELECT * FROM data WHERE id= '{0}'".format(id))
    ctx = cur.fetchone()
    con.commit()
    cur.close()
    con.close()
    print(ctx)


    class FPDF(FPDF, HTMLMixin):
        from fpdf import FPDF, HTMLMixin
        def setLogo(self):
            path_dir = os.path.dirname('C:\\Users\\jazyi\\flask-projects\\cedulaOriginal\\static\\')
            path_file = os.path.join(path_dir, 'sntsslogo.png')
            self.image(path_file, x=5, y=5, w=20, h=20)
            #self.ln(1)
            self.set_xy(7, 26)
            #cell (w,h,txt. border, align, fill, link, markdown, new_x=XPos.RIGHT, new_y=YPos.TOP)
            self.set_font('Arial','B', 5)
            self.cell(12, 3, txt='SECCION III', border=0, ln=0, align='C')
            #self.ln(1)
            self.set_xy(8, 29)
            self.cell(txt='JALISCO')


            path_dir = os.path.dirname('C:\\Users\\jazyi\\flask-projects\\cedulaOriginal\\static\\')
            font = os.path.join(path_dir, 'sindi.png')
            self.set_xy(40, 5)
            self.image(font, x=40, y=5, w=130, h=7)
            #self.set_font('Arial', 'B',14)
            #self.cell(txt='Sindicato Nacional de Trabajadores del Seguro Social', border=0, align='C')
            self.set_xy(70, 13)
            self.set_font('Arial', 'B', 12)
            self.cell(txt='CÉDULA DE AFILIACIÓN', border=0, align='C')
            self.set_xy(55, 18)
            self.set_font('Arial', '', 5)
            self.multi_cell(90,2, l, 0, 'J')
            #self.ln(1)
        def setData(self):
            #self.set_xy(5, 50)
            #path_dir = os.path.dirname('C:\\Users\\jazyi\\flask-projects\\cedulaOriginal\\static\\')
            #img = os.path.join(path_dir, 'rectrod.png')
            #self.image(img, x=25, y=30, w=170, h=80)


            self.set_draw_color(255,255,255)
            self.set_line_width(0.22)
            self.set_draw_color(0,0,0)
            self.rect(25, 30, 170, 80, round_corners=True, style="D")
            self.rect(26, 31, 168, 78, round_corners=True, style="D")

            """self.set_draw_color(255,255,255)
            self.set_line_width(0.22)
            self.set_draw_color(0,0,0)
            self.rect(24, 29, 169, 79, round_corners=("TOP_LEFT", "TOP_RIGHT", "BOTTOM_LEFT", "BOTTOM_RIGHT"), style="D", corner_radius=0)"""






            self.set_xy(70, 35)
            self.set_font('Arial', 'B', 10)
            self.cell(80, 8, 'DATOS PERSONALES', 0, 1, 'C')
            # form data
            self.set_xy(35, 45)
            self.set_font('Arial', '', 6)
            self.cell(30,8, 'NOMBRE:', 0, 1)
            # add personal Data
            self.set_xy(55, 47)
            self.set_font('Arial', 'B', 8)
            self.cell(12, 3, ctx['app'], 0, 1, 'C')

            self.set_xy(95, 47)
            self.set_font('Arial', 'B', 8)
            self.cell(12, 3, ctx['apm'], 0, 1, 'C')

            self.set_xy(135, 47)
            self.set_font('Arial', 'B', 8)
            self.cell(12, 3, ctx['name'], 0, 1, 'C')


            # draw line
            self.line(45, 50, 170, 50)
            self.set_xy(52,51)
            self.set_font('Arial', '', 5)
            self.cell(23, 3, 'Apellido Paterno', 0, 1, 'L')
            self.set_xy(85, 51)
            self.set_font('Arial', '', 5)
            self.cell(23, 3, 'Apellido Materno', 0, 1, 'R')
            self.set_xy(120, 51)
            self.set_font('Arial', '', 5)
            self.cell(23, 3, 'Nombres', 0, 1, 'R')
            # data2
            self.set_xy(70, 52)
            self.set_font('Arial', 'B', 5)
            self.cell(80, 8, 'DOMICILIO PARTICULAR', 0, 1, 'C')

            # add address
            self.set_xy(45, 60)
            self.set_font('Arial', 'B', 8)
            self.cell(12, 3, ctx['dom'], 0, 1, 'C')
            self.set_xy(90, 60)
            self.set_font('Arial', 'B', 8)
            self.cell(12, 3, ctx['col'], 0, 1, 'C')
            self.set_xy(150, 60)
            self.set_font('Arial', 'B', 8)
            self.cell(12, 3, ctx['mcpio'], 0, 1, 'C')

            # draw line
            self.line(35, 63, 80, 63)
            self.set_xy(38, 63.5)
            self.set_font('Arial', '', 5)
            self.cell(25, 3, 'Calle y No. Exterior y/o Interior', 0, 1, 'L')
            self.line(82, 63, 118, 63)
            self.set_xy(85, 63.5)
            self.set_font('Arial', '', 5)
            self.cell(25, 3, 'Colonia', 0, 1, 'C')
            self.line(120, 63, 185, 63)
            self.set_xy(140, 63.5)
            self.set_font('Arial', '', 5)
            self.cell(25, 3, 'Alcaldía y/o Municipio', 0, 1, 'C')

            # add cp
            self.set_xy(36, 69.2)
            self.set_font('Arial', 'B', 8)
            self.cell(12, 3, ctx['cp'], 0, 1, 'C')
            self.set_xy(61.5, 69.2)
            self.set_font('Arial', 'B', 8)
            self.cell(12, 3, ctx['local'], 0, 1, 'C')
            self.set_xy(90, 69.2)
            self.set_font('Arial', 'B', 8)
            self.cell(12, 3, ctx['cel'], 0, 1, 'C')
            self.set_xy(141.5, 69.2)
            self.set_font('Arial', 'B', 8)
            self.cell(12, 3, ctx['email'], 0, 1, 'C')

            # draw line
            self.line(35, 72, 55, 72)
            self.set_xy(39, 72.5)
            self.set_font('Arial', '', 5)
            self.cell(25, 3, 'Código Postal', 0, 1, 'L')
            self.line(60, 72, 80, 72)
            self.set_xy(59, 72.5)
            self.set_font('Arial', '', 5)
            self.cell(25, 3, 'Localidad', 0, 1, 'C')
            self.line(86, 72, 118, 72)
            self.set_xy(85, 72.5)
            self.set_font('Arial', '', 5)
            self.cell(25, 3, 'Tel. Celular', 0, 1, 'C')
            self.line(125, 72, 185, 72)
            self.set_xy(140 ,72.5)
            self.set_font('Arial', '', 5)
            self.cell(12, 3, 'Correo Electrónico', 0, 1, 'C')

            self.set_xy(35, 80)
            self.set_font('Arial', '', 5)
            self.cell(23, 3, 'NACIMIENTO:', 0, 1, 'L')

            # add dirthday

            def transDate(dbd):
                newStr = dbd.split('-')  #['y', 'm', 'd']
                dte = newStr[2] + '-' + newStr[1] + '-' + newStr[0]
                return dte


            self.set_xy(75, 79.5)
            self.set_font('Arial', 'B', 8)
            self.cell(12, 3, ctx['l_nac'], 0, 1, 'C')
            self.set_xy(135, 79.5)
            self.set_font('Arial', 'B', 8)
            nBD = transDate(ctx['f_nac'])
            self.cell(12, 3, nBD, 0, 1, 'C')
            
            # draw line
            self.line(52, 82.5, 110, 82.5)
            self.set_xy(70, 83)
            self.set_font('Arial', '', 5)
            self.cell(12, 3, 'Lugar', 0, 1, 'C')

            self.set_xy(115, 80)
            self.set_font('Arial', '', 5)
            self.cell(12, 3, 'FECHA:', 0, 1, 'C')
     
            self.line(130, 82.5, 160, 82.5)

            self.set_xy(140, 83)
            self.set_font('Arial', '', 5)
            self.cell(12, 3, 'Día-Mes-Año', 0, 1, 'C')

            # add NSS
            self.set_xy(40, 87)
            self.set_font('Arial', 'B', 8)
            self.cell(12, 3, ctx['nss'], 0, 1, 'C')
            self.set_xy(85, 87)
            self.set_font('Arial', 'B', 8)
            self.cell(12, 3, ctx['rfc'], 0, 1, 'C')
            self.set_xy(142, 87)
            self.set_font('Arial', 'B', 8)
            self.cell(12, 3, ctx['curp'], 0, 1, 'C')

            # draw line
            self.line(35, 90, 70, 90)
            self.set_xy(40, 90.5)
            self.set_font('Arial', '', 5)
            self.cell(12, 3, 'Número de Seguridad Social')

            self.line(75, 90, 115, 90)
            self.set_xy(85, 90.5)
            self.set_font('Arial', '', 5)
            self.cell(12, 3, 'RFC', 0, 1, 'C')

            self.line(120, 90, 170, 90)
            self.set_xy(140, 90.5)
            self.set_font('Arial', '', 5)
            self.cell(12, 3, 'CURP', 0, 1, 'C')

            # add ec
            self.set_xy(55, 96)
            self.set_font('Arial', 'B', 8)
            self.cell(12, 3, ctx['edo_civil'], 0, 1, 'C')
            self.set_xy(120, 96)
            self.set_font('Arial', 'B', 8)
            self.cell(12, 3, ctx['sexo'], 0, 1, 'C')

            # draw line
            self.line(45, 99, 92, 99)
            self.set_xy(60, 99.5)
            self.set_font('Arial', '', 5)
            self.cell(12, 3, 'Estado Civil', 0, 1, 'C')

            self.line(105, 99, 150, 99)
            self.set_xy(120, 99.5)
            self.set_font('Arial', '', 5) 
            self.cell(12, 3, 'Sexo', 0, 1, 'C')
        def setData2(self):
            self.set_xy(70, 110)
            self.set_font('Arial', 'B', 10)
            self.cell(80, 8, 'DATOS LABORALES', 0, 1, 'C')
            
            #path_dir = os.path.dirname('C:\\Users\\jazyi\\flask-projects\\cedulaOriginal\\static\\')
            #img = os.path.join(path_dir, 'rectrod.png')
            #self.image(img, x=25, y= 120, w=170, h=40)
            self.rect(25, 120, 170, 40, round_corners=True, style="D")
            self.rect(26, 121, 168, 38, round_corners=True, style="D")
            def transDate(dbd):
                newStr = dbd.split('-')  #['y', 'm', 'd']
                dte = newStr[2] + '-' + newStr[1] + '-' + newStr[0]
                return dte

            # add mat
            self.set_xy(40, 129)
            self.set_font('Arial', 'B', 8)
            self.cell(12, 3, ctx['matricula'], 0, 1, 'C')
            self.set_xy(73, 129)
            self.set_font('Arial', 'B', 8)
            self.cell(12, 3, ctx['categoria'], 0, 1, 'C')
            self.set_xy(115, 129)
            self.set_font('Arial', 'B', 6)
            self.cell(12, 3, ctx['adscripcion'], 0, 1, 'C')
            self.set_xy(160, 129)
            self.set_font('Arial', 'B', 8)
            self.cell(12, 3, ctx['turno'], 0, 1, 'C')

            # draw line
            self.line(35, 132, 60, 132)
            self.set_xy(40, 132.5)
            self.set_font('Arial', '', 5)
            self.cell(12, 3, 'Matrícula', 0, 1, 'C')

            self.line(65, 132, 100, 132)
            self.set_xy(73, 132.5)
            self.set_font('Arial', '', 5)
            self.cell(12, 3, 'Categoría', 0, 1, 'C')
            
            self.line(105, 132, 145, 132)
            self.set_xy(115, 132.5)
            self.set_font('Arial', '', 5)
            self.cell(12, 3, 'Adscripción', 0, 1, 'C')
     
            self.line(155, 132, 180, 132)
            self.set_xy(165, 132.5)
            self.set_font('Arial', '', 5)
            self.cell(12, 3, 'Turno', 0, 1, 'C')
            
            # add tp
            self.set_xy(45, 147)
            self.set_font('Arial', 'B', 8)
            self.cell(12, 3, ctx['t_contr'], 0, 1, 'C')
            self.set_xy(110, 147)
            self.set_font('Arial', 'B', 8)
            nDI = transDate(ctx['f_ingr'])
            self.cell(12, 3, nDI, 0, 1, 'C')
            self.set_xy(160, 147)
            self.set_font('Arial', 'B', 8)
            self.cell(12, 3, ctx['antiguedad'], 0, 1, 'C')


            # draw line
            self.line(35, 150, 80, 150)
            self.set_xy(50, 150.5)
            self.set_font('Arial', '', 5)
            self.cell(12, 3, 'Tipo de Contratación', 0, 1, 'C')
     
            self.line(85, 150, 150, 150)
            self.set_xy(110, 150.5)
            self.set_font('Arial', '', 5)
            self.cell(12, 3, 'Fecha de Ingreso al IMSS', 0, 1, 'C')
     
            self.line(155, 150, 180, 150)
            self.set_xy(162, 150.5)
            self.set_font('Arial', '', 5)
            self.cell(12, 3, 'Antiguedad', 0, 1, 'C')

        def setLegend(self):
            #path_dir = os.path.dirname('C:\\Users\\jazyi\\flask-projects\\cedulaOriginal\\static\\')
            #img = os.path.join(path_dir, 'rectrod.png')
            #self.image(img, x=25, y=180, w=170, h=60)
            #multi_cell(w, h, txt, border = 0, align, fill)

            self.rect(25, 180, 170, 60, round_corners=True, style="D")
            self.rect(26, 181, 168, 58, round_corners=True, style="D")

            self.set_xy(38, 200)
            self.set_font('Arial', '', 4.5)
            self.set_stretching(165.5)
            self.multi_cell(145, 2, l1, 0, 'J')

        def setFoo(self):
            self.line(45, 260, 110, 260)
            self.set_xy(75, 260.5)
            self.set_font('Arial', '', 5)
            self.cell(12, 3, 'NOMBRE COMPLETO', 0, 1, 'C')       
            # 
            self.line(120, 260, 180, 260) 
            self.set_xy(145, 260.5)
            self.set_font('Arial', '', 5)
            self.cell(12, 3, 'FIRMA', 0, 1, 'C')



        def reverseFace(self):
            path_dir = os.path.dirname('C:\\Users\\jazyi\\flask-projects\\cedulaOriginal\\static\\')
            path_file = os.path.join(path_dir, 'sntsslogo.png')
            self.image(path_file, x=5, y=5, w=20, h=20)

            path_dir = os.path.dirname('C:\\Users\\jazyi\\flask-projects\\cedulaOriginal\\static\\')
            font = os.path.join(path_dir, 'sindi.png')
            self.set_xy(40, 15)
            self.image(font, x=40, y=20, w=130, h=7)
            #self.ln(1)
            #self.set_xy(7, 24)
            #self.set_font('Arial','B', 5)
            #self.cell(20, 10, 'SECCION III',1,0)
            #self.ln(1)
            #self.set_xy(8, 27)
            #self.cell(20,10, 'JALISCO',1, 0)
            #self.set_xy(40, 15)
            #self.set_font('Arial', 'B',10)
            #self.cell(txt='Sindicato Nacional de Trabajadores del Seguro Social', border=0)

            # rect(x, y, w, h, style)
            self.rect(x=30, y=40, w=140, h=200)

            path_dir = os.path.dirname('C:\\Users\\jazyi\\flask-projects\\cedulaOriginal\\static\\')
            legend = os.path.join(path_dir, 'legend3.png')
            self.image(legend, x=35, y=50, w=130, h=180)
            #self.set_xy(100, 35)
            #self.set_font('Arial', 'B', 7)
            #self.cell(10, 3, 'Aviso de Privacidad', 0, 1, 'C')

            #self.set_margins(32, 48)
            #self.set_font('Arial', '', 4)
            #self.set_stretching(60)
            # write(h, txt)
            
        def setFirm(self):
            self.line(35, 260, 75, 260)
            self.set_xy(50, 260.5)
            self.set_font('Arial', '', 5)
            self.cell(12, 3, 'Nombre Completo', 0, 1, 'C')

            self.line(91, 260, 125, 260)
            self.set_xy(102, 260.5)
            self.set_font('Arial', '', 5)
            self.cell(12,3, 'Firma', 0, 1, 'C')

            self.line(130, 260, 170, 260)
            self.set_xy(150, 260.5)
            self.set_font('Arial', '', 5)
            self.cell(12, 3, 'Fecha', 0, 1, 'C')

        def setAtt(self):

            t = """HAGO CONSTAR QUE LA PRESENTE FOTOSTÁTICA ES COPI FIEL DEL ORIGINAL QUE SE TIENE A LA VISTA Y OBRA EN EL ARCHIVO DEL CÓMITE EJECUTIVO
                 NACIONAL DEL SINDICATO NACIONAL DE TRABAJADORES DEL SEGURO SOCIAL. SE EXTIENDE LA PRESENTE A PETICIÓN DEL INTERESADO
                 ATENTAMENTE:
                 ING. GILBERTO DANIEL CASTILLO GARCÍA
                 SECRETARIO GENERAL    """
            self.set_xy(172, 70)
            self.set_font('Arial', '', 5)
            self.rotate(angle=90)
            #self.multi_cell(145,2, t, 1, 'C')
            self.set_stretching(150)
            self.write_html("""<p>HAGO CONSTAR QUE LA PRESENTE FOTOSTÁTICA ES COPIA FIEL DEL ORIGINAL QUE SE TIENE A LA VISTA Y OBRA EN EL ARCHIVO DEL CÓMITE EJECUTIVO
                               <p>NACIONAL DEL SINDICATO NACIONAL DE TRABAJADORES DEL SEGURO SOCIAL. SE EXTIENDE LA PRESENTE A PETICIÓN DEL INTERESADO
                               <p>ATENTAMENTE:
                               <p>ING. GILBERTO DANIEL CASTILLO GARCÍA
                               <p>SECRETARIO GENERAL  <img src="static/firmatrans.png" width="180" height="70"/>  """)
            path_dir = os.path.dirname('C:\\Users\\jazyi\\flask-projects\\cedulaOriginal\\static\\')
            firma = os.path.join(path_dir, 'firmatrans.png')

            #self.set_xy(180, 150)
            #self.rotate(angle=90)
            #self.image(firma, x=160, y=90, w=40, h=10)
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
    pdf.setFirm()
    pdf.setAtt()
    #pdf.output('3.pdf')#.encode('utf-8')   

    response = make_response(pdf.output())
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename= cedulaAfiliación' + ctx['app'] + ctx['apm'] + ctx['name']
    return response




@app.route('/search', methods=['GET', 'POST'])
def search():
    result = None
    #return render_template('search.html')
    if request.method == 'GET':
       q = request.args.get('q')
       if q:
            try:
                con = getConnection()
                cur = con.cursor(cursor_factory=extras.DictCursor)
                cur.execute("SELECT * FROM data WHERE matricula='{0}'".format(q))
                result = cur.fetchone()
                con.commit()
                cur.close()
                con.close()
                print(result)
               # return redirect(url_for('create_cedula', id=result['id']))
            except:
                print('No se encontro resultado alguno')    
     #return render_template('search.html')
    return render_template('search.html', result=result)



