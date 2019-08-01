<?php
	function enviar_bd($sql) {
		//Conección con el manejador de BD
		$conn = mysql_connect('localhost','iacc','');
		if($conn){
			//Selección de BD
			mysql_select_db('proyecto_iacc',$conn);
					
			//Envio de sentencia SQL a la BD
			$resul = mysql_query($sql, $conn);
			if(!$resul) { die("Sentencia incorrecta: " . mysql_error($conn)); }

			//Cierre de conección con el manejador de la BD
			mysql_close($conn);
		} else {
			//Mensaje en caso de errores de conección
			die("Conexión incompleta: " . mysql_error($conn));
		}
		return $resul;
	}
?>




