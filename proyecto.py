
class alumno:
    def __init__(self,apellido,nombre,numalum) -> None:
        self.apellido = apellido 
        self.nombre = nombre
        self.numalum = numalum 
    def __str__(self) -> str:
        return f"Apellido: {self.apellido} Nombre: {self.nombre}"
    
alumno1 = alumno ("Amaya","Jeremias",1)
alumno2 = alumno ("Bulacio","Santiago",2)
alumno3 = alumno ("Carunchio","Julieta",3)
alumno4 = alumno ("Castillo","Maximiliano",4)
alumno5 = alumno ("Cordoba","Joaquin",5)
alumno6 = alumno ("Cordoba","Solange",6)
alumno7 = alumno ("Corzo","Juan",7)
alumno8 = alumno ("Diaz","Tobias",8)
alumno9 = alumno ("Espindola","Ludmila",9)
alumno10 = alumno ("Giupponi","Kevin",10)
alumno11 = alumno ("Lazzarini","Emiliano",11)
alumno12 = alumno ("Loza","Fabrizio",12)
alumno13 = alumno ("Luna","Ulises",13)
alumno14 = alumno ("Medina","Lucas",14)
alumno15 = alumno ("Pedraza","Tiago",15)
alumno16 = alumno ("Pedraza","Thomas",16)
alumno17 = alumno ("Quinteros","Azul",17)
alumno18 = alumno ("Riachi","Zahir",18)
alumno19 = alumno ("Rodriguez","Esteban",19)
alumno20 = alumno ("Soria","Mateo",20)
alumno21 = alumno ("Strauss","Kevin",21)
alumno22 = alumno ("Vera","Mateo",22)
alumno23 = alumno ("Vergara","Nelson",23)

def menu ():
    seleccion = 0
    while seleccion !=5:
        print ("Registro de asistencias 6to B")
        print ("Elija una de las opciones: ")
        print ("------------------------------------------------------------------")
        print ("1. Registro de inasistencias del mes por alumno")
        print ("2. Registro de tardanzas del mes por alumno")
        print ("3. Calcular el total de inasistencias")
        print ("4. Calcular el total de tardanzas")
        print ("5. Salir")
        seleccion = int(input ("Elije una opcion:"))
        if seleccion == 1:
            registro_de_inasis ()
        if seleccion == 2:
            registro_de_tard ()
        if seleccion == 3:
            total_inasis ()
        if seleccion == 4:
            total_tard ()
        if seleccion == 5:
            salir ()

def registro_de_inasis ():
    print ("La cantidad de inasistencias que tuvo el alumno este mes son: ")
def registro_de_tard ():
    print ("La cantidad de tardanzas que tuvo el alumno este mes son: ")
def total_inasis ():
    print ("El total de inasistencias es: ")
def total_tard ():
    print ("El total de tardanzas es: ")
def salir ():
    print ("Todos los cambios han sido guardados correctamente")

#-------------------------------------------------------------------------------------
menu ()





    

