""" 1.Cuales son los 5 barrios mas comentados? ✔
 2. Cuantas personas tienen entre 1 y 3 propiedades? cuantas entre 3 y 6? etc ✔
 3. Cual es la zona que en promedio es la mas cara de la ciudad? y la mas barata? ✔
 4. Teniendo en cuenta un solo barrio, cual es el promedio de precio de: hoteles, casas/deptos y habitaciones"""

import csv


def cargaDeDatos(name):
    datos = []
    with open(name, encoding="utf-8") as File:
        archivo = csv.reader(File)
        for indice, fila in enumerate(archivo):
            if indice == 0:
                titulos = fila
            else:
                diccionario = {}
                for columna, valor in zip(titulos, fila):
                    if columna == "host_id" or columna == "price" or columna == "neighbourhood" or columna == "number_of_reviews" or columna == "room_type" or columna == "calculated_host_listings_count":
                        diccionario[columna] = valor
                datos.append(diccionario)

    return datos


# Pregunta 1 (5 barrios mas comentados)


def cuenta_resenias(lista, neighbourhood_keys, num_reviews_keys):
    res_barrio = {}
    for diccionario in lista:
        for keys, values in diccionario.items():
            if keys == neighbourhood_keys:
                contador = diccionario[num_reviews_keys]
                if values in res_barrio:
                    res_barrio[values] += int(contador)
                else:
                    res_barrio[values] = int(contador)

    return res_barrio


def ordenar_comentarios(diccionario):
    list_ordenar_come = []
    for barrios, comentarios in diccionario.items():
        list_ordenar_come.append([barrios, comentarios])
        list_ordenar_come.sort(reverse=True, key=lambda x: x[1])

    print(
        f"\nLos 5 barrios mas comentados son: \n 1. {list_ordenar_come[0]} \n 2. {list_ordenar_come[1]} \n 3. {list_ordenar_come[2]} \n 4. {list_ordenar_come[3]} \n 5. {list_ordenar_come[4]}")
    return list_ordenar_come

# Pregunta 2 (canditdad de propiedades)


def cant_prop(lista, host_id_key, calc_host_listings_key):
    can_prop_dic = {}
    for diccionario in lista:
        for keys, values in diccionario.items():
            if keys == host_id_key:
                can_prop_dic[values] = diccionario[calc_host_listings_key]

    return can_prop_dic


def cuant_pers_prop(diccionario, numero):
    contador = 0
    for propiedades in diccionario.values():
        if int(propiedades) == numero:
            contador += 1
    return contador


def repetidor():
    contador = 1
    cantidad_de_prop_xpersona = {}
    for i in range(10):
        propiedad = cuant_pers_prop(dicc, contador)
        cantidad_de_prop_xpersona["propiedades"+" "+str(contador)] = propiedad
        contador += 1

    return cantidad_de_prop_xpersona


# Pregunta 3 (barrio mas caro y mas barato)


def precios(lista, neighbourhood_key, price_key):
    dic_precio = {}
    promedios = []
    barrios = []

    for dic in lista:
        for key, values in dic.items():
            precio = dic[price_key]
            if key == neighbourhood_key:
                lista = []

                if values in dic_precio:
                    dic_precio[values].append(int(precio))
                else:
                    dic_precio[values] = lista
                    dic_precio[values].append(int(precio))

    for k, v in dic_precio.items():
        promedios.append(round(sum(v) / len(v), 2))
        #promedios.sort(reverse=True, key=lambda x: x[0])
        barrios.append(k)

    print(promedios, barrios)
    return promedios, barrios


# Pregunta 4 (En el barrio mas caro promedio de tipo de habitacion)


def promedio_tipo_hab(lista, room_type_key, price_key, neighbourhood_key):
    promedios_precio = precios(datos, neighbourhood_key, price_key)
    barrio_caro = promedios_precio[0][1]

    room_types_dic = {}
    room_type_price_avg = []
    for alquiler in lista:

        neighbourhood = alquiler[neighbourhood_key]
        if barrio_caro != neighbourhood:
            continue

        room_type = alquiler[room_type_key]
        price = alquiler[price_key]

        if room_type not in room_types_dic:
            room_types_dic[room_type] = []

        room_types_dic[room_type].append(int(price))

    for key, value in room_types_dic.items():
        avg = round(sum(value)/len(value), 2)
        room_type_price_avg.append([avg, key])
    room_type_price_avg.sort(reverse=True, key=lambda x: x[0])

    print(room_type_price_avg)
    return room_type_price_avg


datos = cargaDeDatos('listings.csv')
res_x_barrio = cuenta_resenias(datos, "neighbourhood", "number_of_reviews")
mi_lista = ordenar_comentarios(res_x_barrio)
dicc = cant_prop(datos, "host_id", "calculated_host_listings_count")
promedio = precios(datos, "neighbourhood", 'price')
cantidad_de_prop_xpersona = repetidor()
room_type_price_avg = promedio_tipo_hab(
    datos, "room_type", "price", "neighbourhood")
