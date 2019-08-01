function validate() {
	
	//Definición de Variables
	//Datos Básicos
	var name = document.getElementById("_name").value;
	var surname = document.getElementById("_surname").value;
	var email = document.getElementById("_email").value;
	var esGenderM = document.getElementById("_generoM").checked;
	var pass = document.getElementById("_pass").value;
	var passVer = document.getElementById("_pass_ver").value;

	//Datos Adicionales
	var menssage = document.getElementById("_message").value;
	var medio = document.getElementById("_medio").value;

	//Validaciones
	//Nombre
	//Validación de Longitud del Texto
	if( name.length > 20 || name.length < 3 ) {
		alert("El nombre debe tener una longitud entre 3 y 20 caracteres");
		return;
	}
	
	//Apellido
	//Validación de Longitud del Texto
	if( surname.length > 20 || surname.length < 3 ) {
		alert("El apellido debe tener una longitud entre 3 y 20 caracteres");
		return;
	}

	//Email
	//Validación de Longitud del Texto
	if( email.length > 30 || email.length < 7 ) {
		alert("El correo electrónico debe tener una longitud entre 7 y 30 caracteres");
		return;
	}
	//Verificación de el caracter "@" en el Email
	if( email.indexOf("@") == -1 ) {
		alert("Favor colocar un correo electrónico valido");
		return;
	} else {
		// pperez   @    gmail.com
		// NICK          DOMINIO
		var nick = email.substr( 0 , email.indexOf("@") );
		var domain = email.substr( email.indexOf("@") + 1 ,
			                        email.length - email.indexOf("@") - 1 );

		//Validación de Longitud del Texto
		if( nick.length < 3 || domain.length < 3 ) {
			alert("Favor colocar un correo electrónico valido");
			return;
		}
		//Verificación de el caracter punto (.) en el Dominio
		if( domain.indexOf(".") == -1 ) {
			alert("Favor colocar un correo electrónico valido");
			return;
		} else {
			var domain = dominio.substr( 0 , domain.indexOf(".") );
			var domain = dominio.substr( domain.indexOf(".") + 1 ,
				                           domain.length - domain.indexOf(".") - 1 );
			//Validación de Longitud del Texto
			if( domain1.length < 2 || domain2.length < 2 ) {
				alert("Favor colocar un correo electrónico valido");
				return;
			}
		}
	}

	//Contraseña
	//Validación de Longitud del Texto
	if( pass.length > 30 || pass.length < 8 ) {
		alert("La Contraseña debe tener una longitud entre 8 y 30 caracteres");
		return;
	}
	//Comparación de Contraseñas para Validación
	if( pass !== passVer ) {
		alert("Las Contraseñas no coinciden");
		return;
	}

	//Envío de la Información al Servidor
	document.getElementById("form").submit();
}

