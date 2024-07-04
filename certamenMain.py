from os import system
system("cls")
import random





detalle_pedido = (6, 10, 20)
sectores = ("concepcion", "chiguayante", "talcahuano", "hualpen", "san pedro")
pedidos = []


def registrar_pedido(pedidos):
    disp_6 = 0
    disp_10 = 0
    disp_20 = 0
    id = random.randint(100000, 999999)
    while True:
        nombre = input("Ingrese su nombre: ")
        if nombre.isalpha() and len(nombre)>3:
            break
        else:
            print("Ingrese un nombre correcto.")
    while True:
        apellido = input("Ingrese su apellido: ")
        if apellido.isalpha() and len(apellido)>3:
            break
        else:
            print("Ingrese un apellido correcto.")
    while True:
        comuna = input("Ingrese su comuna: (concepcion, chiguayante, talcahuano, hualpen, san pedro) :")
        if comuna in sectores:
            break
        else:
            print("Ingrese una comuna disponible. ")
    while True:
        direccion = input("Ingrese la direccion de su domicilio: ")
        if direccion != "":
            break
        else:
            print("Ingrese una direccion.....")
    while True:
        detalle = int(input("Ingrese los cilindros a comprar: "))
        if detalle >= 1:
            while True:
                disp = int(input("""
1. Dispensador de 6 litros
2. Dispensador de 10 litros
3. Dispensador de 20 litros
4. Seguir con el pedido.
"""))
                match disp:
                    case 1:
                        print(f"Usted a agregado {detalle} dispensador de 6 litros")
                        disp_6 =+ detalle
                        break
                    case 2:
                        print(f"Usted a agregado {detalle} dispensador de 10 litros")
                        disp_10=+detalle
                        break
                    case 3:
                        print(f"Usted a agregado {detalle} dispensador de 20 litros")
                        disp_20=+detalle
                        break
                    case 4:
                        break
                    case other:
                        print("Ingrese una opcion valida.....")
            print("Pedido agregado con exito....")
            pedido = {
                "ID pedido": id,
                "Nombre": nombre,
                "Apellido": apellido,
                "Direccion": direccion,
                "Sector": comuna,
                "Disp.6lts": disp_6,
                "Disp.10lts": disp_10,
                "Disp.20lts": disp_20

            }
            pedidos.append(pedido)
        break


def listar(pedidos):
    print(f"""
ID PEDIDO           CLIENTE             DIRECCION               SECTOR     DISP.6LTS   DISP.10LTS     DISP.20LTS
    """)
    for pedido in pedidos:
          print(f"""
{pedido["ID pedido"]}                {pedido["Nombre"]}              {pedido["Direccion"]}          {pedido["Sector"]}         {pedido["Disp.6lts"]}            {pedido["Disp.10lts"]}         {pedido["Disp.20lts"]}                                      
                            {pedido["Apellido"]}      
          """)

def buscar(pedidos):
    while True:
        id_buscar=input("Ingrese la ID del pedido a buscar: ")
        if id_buscar.isnumeric():
            id_buscar=int(id_buscar)
            break
        else:
            print("Ingrese un ID valido")

    for pedido in pedidos:
        if pedido["ID pedido"]==id_buscar:
                print(f"""
ID PEDIDO           CLIENTE             DIRECCION               SECTOR     DISP.6LTS   DISP.10LTS     DISP.20LTS
    """)
    for pedido in pedidos:
          print(f"""
{pedido["ID pedido"]}                {pedido["Nombre"]}              {pedido["Direccion"]}          {pedido["Sector"]}         {pedido["Disp.6lts"]}            {pedido["Disp.10lts"]}         {pedido["Disp.20lts"]}                                      
                            {pedido["Apellido"]}      
          """)


def hoja_ruta(pedidos):
    archivo = open ("Hojaruta.csv","w")
    archivo.write(pedido["ID pedido"], pedido["Nombre"], pedido["Apellido"], pedido["Direccion"], pedido["Sector"], pedido["Disp.6lts"], pedido["Disp.10lts"], pedido["Disp.20lts"])
    for pedido in pedidos:
        linea = ";".join(map(str, pedido)) + "\n"
        archivo.write(linea)










while True:
    op = int(input("""
****************BIENVENIDO A CLEANWASSER****************
1. Registrar pedido
2. Listar todos los pedidos
3. Imprimir hoja de ruta
4. Buscar un pedido por ID
5. Salir
Seleccione una opción: """))
    match op:
        case 1:
            registrar_pedido(pedidos)
        case 2:
            listar(pedidos)
        case 3:
            pass
        case 4:
            buscar(pedidos)
        case 5:
            break
        case other:
            print("Ingrese una opción correcta...")