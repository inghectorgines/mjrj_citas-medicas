
from usuarios import acciones

print("""
\n
####### BIENVENIDO #######

""")

hazEl = acciones.Acciones()

def bienvenida():
  
  print("""

  ¿Qué deseas hacer?
  \n
  -¿Eres nuevo? ¡Registrarte! (Escribe 'registro')
  \n
  -¿Ya tienes cuenta? Inicia Sesión (Escribe 'login')
  \n
  -¿Deseas salir? (Escribe 'salir')
  """)

  accion = input("¿Que quieres hacer?:")

  if accion == "registro":
   hazEl.registro()
   bienvenida()

  elif accion == "login":
    hazEl.login()

  elif accion == "salir":
     print ("Proyecto realizado por MILTON JAIR RUBIO JUÁREZ DDI el dia 12/06/2022")
     exit()

bienvenida()
