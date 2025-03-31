# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 10:26:09 2025

@author: Tu papá 201275
"""
import re
texto= ("Jorge para realizar un tramite en el sat descubrio que su firma electronica se le borró, así que tendía que realizar el tramite poresencialmente, así que buco su CURP en la pagina de gobierno federal https://www.gob.mx/curp/ , y obtuvo que su CURP es RAMJ040324HNLMLRA7 , Jorge despues de haber obtenido su curp creo una cuenta en el portal del Sat para obtener una cita uso como contraseña confal57, Jorge y pusó como número de contacto 8123702605, sin embargo Jorge nunca pudo sacar dicha cita y nunca pudo hacer su aclaración de ingresos, y ahora le debe 7 bolas a hacienda")
#Encontrar sitio web url
url = re.search(r"https?://[^\s]+", texto)
#Numero de telefono
telefono= re.search(r"\b\d{10}\b", texto)
#CURP 
curp= re.search(r"[A-Z]{4}\d{6}[HM][A-Z]{5}[A-Z\d]{2}", texto)
#Contraseña
contraseña= re.search(r"\b[a-zA-Z0-9]{8}\b", texto)
#Hacer remplazo
print(re.sub(r"Jorge","Tu papá", texto))

#En caso de que no se encuentre ninguna coincidencia
if url is None:
    print("No hay coincidencias de URL en el texto")    
else:
    print("url encontrados", url.group())
if telefono is None:
    print("No hay coincidencias de telefono en el texto")
else:
    print("telefonos encontrados", telefono.group())
if curp is None:
    print("No hay coincidencias de CURP en el texto")
else:
    print("CURP encontrados", curp.group())    
if contraseña is None:
    print("No hay coincidencias de contraseñas de 8 digitos en el texto")  
else:
    print("contraseñas encontradas", contraseña.group())    
    

