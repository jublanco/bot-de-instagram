#importamos la libreria que vamos a utilizar
from instabot import Bot

#creamos una nueva variable Bot que va a ser el encargado de hacer todo el trabajo
mi_bot = Bot()

#luego tenemos que iniciar sesion en nuestra cuenta y contraseña, por cuestiones de seguridad voy a poner un nombre cualquiera, aunque se puede hacer mas seguro
mi_bot.login(username="mi_cuenta", password="contraseña")

#ahora para poer seguir los seguidores de una cuenta en particular solo tenemos que poner este codigo
mi_bot.follow_followers('cuenta_objetivo')