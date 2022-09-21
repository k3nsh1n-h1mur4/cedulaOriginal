//alert('hoal mundo')
const form = document.querySelector("form");

form.addEventListener('sumbit', (e) => {
	e.preventDefault();

	app = form['app'].value;
	apm = form['apm'].value;
	name = form['name'].value;
	dom = form['dom'].value;
	col = form['col'].value;
	mcpio = form['mcpio'].value;
	cp = form['cp'].value;
	local = form['local'].value;
	cel = form['cel'].value;
	email = form['email'].value;
	l_nac = form['lnac'].value;
	f_nac = form['f_nac'].value;
	nss = form['nss'].value;
	rfc = form['rfc'].value;
	curp = form['curp'].value;
	edo_civil = form['edo_civil'].value;
	sexo = form['sexo'].value;
	matricula = form['matricula'].value;
	categoria = form['categoria'].value;
	adscripcion = form['adscripcion'].value;
	turno = form['turno'].value;
	t_contr = form['t_contr'].value;
	f_ingr = form['f_ingr'].value;
	antiguedad = form['antiguedad'].value;


})

console.log(form);