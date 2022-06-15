import citas.cita as modelo

class Acciones:

    def crear(self, usuario):
        print(f"OK {usuario[1]}, Se creara una nueva consulta")

        paciente = input("Introduce el nombre del paciente: ")
        descripcion = input("Escribe la descripcion de la cita/consulta: ")
        horaAtencion = input("Escribe El horario de antencion: ")
        costo = input("Escribe el costo: ")
        cita = modelo.Cita(usuario[0], paciente, descripcion, horaAtencion, costo)
        guardar = cita.guardar()

        if guardar[0] >=1:
            print(f"\nSe ha Agendado la cita de {paciente}")
        else:
            print(f"\nNo se registro la cita la cita {usuario[1]}")

    def mostrar(self, usuario):
        print(f"\nLista de consultas de {usuario[1]}")
        cita = modelo.Cita(usuario[0])
        citas = cita.listar()
        #print(notas)
        for cita in citas:
            print("\n***********************")
            print(cita[2])
            print(cita[3])
            print("\n***********************")
    
    def modificar(self, usuario):
            print(f"\n Vas a editar las consultas {usuario[1]} ")
            print("Introduca los nuevos datos")

            Paciente = input("Introduce el nombre del paciente: ")
            Descripcion = input("Escribe la descripcion de la consulta: ")
            HoraAtencion = input("Escribe la hora de la consulta: ")
            Costo = input("Escribe el precio de la consulta: ")
            cita = modelo.Cita(usuario[0], Paciente, Descripcion, HoraAtencion, Costo)
            modificar = cita.modificar()
            

            
    def borrar(self, usuario):
            print(f"\nVas a borrar una consulta {usuario[1]} ")

            paciente = input("Introduce el nombre del paciente ")
            cita = modelo.Cita(usuario[0], paciente)
            eliminar = cita.eliminar()
            if eliminar[0]>=1:
                print(f"Se borro correctamente la consulta de {paciente}")
            else:
                print("No se borro la consulta")
