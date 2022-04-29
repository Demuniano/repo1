##Juan Mario Rojas Rojas-1003568721-8/09/2021
di={1: ["licuadora",100000],2: ["nevera",1500000],3: ["monitor",600000],4:["microfono", 40000],5:["radio",30000],6: ["camara",70000],7: ["altavoces", 50000],8: ["ups", 90000],9: ["xbox one", 1300000],10: ["ventilador", 90000], 11: ["telefono", 70000]}
def descu(x): ##funcion para calcular el descuento
    if x>500000:
        x=x-(x*0.2)
    elif x>=250000:
        x=x-(x*0.15)
    elif x>=100000:
        x=x-(x*0.08)
    
    return x

def total(y):##funcion para sumar y hallar el total
    t=len(y)
    tot=0
    for i in range(t):
        tot+=y[i][5]
    return(tot)
comp=[]
pre="si"
while pre!="no":##ciclo para las entradas 
    li=[]
    print("FACTURA DE VENTA")
    nombre=input("Nombre Cliente: ")##datos del cliente
    nombre=nombre.upper()
    ide=input("Identificación: ")
    cel=input("No celular: ")
    while True:
        codigo=input("Codigo del producto: ")
        codigo=int(codigo)
        unidades=input("Cantidad de unidades: ")
        unidades=int(unidades)
        noiva= unidades*(di[codigo][1])##valor sin iva
        iva=noiva+(noiva*0.19)##valor con iva
        descuento=descu(iva)##valor del descuento
        li=[di[codigo][0],unidades,di[codigo][1],noiva,int(iva),int(descuento)]##añadir datos a la lista
        comp.append(li)##añadir datos a la tabla
        pre=input("¿Desea calcular mas productos?:(si/no)")##reiteracion o cierre del ciclo
        if pre=="no":
            break
archivo=open("factura.txt","w")##creacion del archivo
print("FACTURA DE VENTA", file=archivo)##escritura de datos
print("",file=archivo)
print("Nombre Cliente: ",nombre, file=archivo)
print("Identificación: ",ide, file=archivo)
print("No celular: ", cel, file=archivo)
print("Item | Producto | Cant. | VrUnitario | VrsinIVa | VrSinIva | VrDescuento", file=archivo)##creacion de formato
print("",file=archivo)
comp.sort(key=lambda x: x[1],reverse=True)##ordenamiento segun cantida de productos 
u=len(comp)
for e in range(u):
    a=comp[e][0]
    b=comp[e][1]
    c=comp[e][2]
    d=comp[e][3]
    f=comp[e][4]
    g=comp[e][5]
    print((e+1),a ,b ,c ,d ,f , g, sep=" | ", file=archivo)##escritura de la tabla dentro del archivo
print("",file=archivo)
print("***** Valor total a pagar: ","$",total(comp),"*****", file=archivo)##total a pagar
archivo.close()
        
    
    

