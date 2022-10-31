import re
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import *
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog



# Creamos la interfaz
ventana = tk.Tk()
ventana.title("Generador de QRs")
ventana.config(width=800, height=150)
ventana.iconbitmap("icon.ico")


# Creamos la función para generar los códigos QR
def generar_qr():
    regex = "^((http|https)://)[-a-zA-Z0-9@:%._\\+~#?&//=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%._\\+~#?&//=]*)$"
    r = re.compile(regex)

    try:
        url = caja_url.get()
        if url == "":
            messagebox.showinfo(message="Por favor, ingresa una URL para crear el código QR.", title="URL vacía")
            
        elif not (re.search(r, url)):
            messagebox.showinfo(message="Por favor, ingresa una URL válida para crear el código QR. Ejemplo: https://dsav.me/", title="URL no válida")

        else:
            qr= qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
            qr.add_data(url)   
            img_1 = qr.make_image(image_factory= StyledPilImage, module_drawer=SquareModuleDrawer())
            ruta_guardado = filedialog.asksaveasfilename(initialdir = "/",title = "1º Escoge la carpeta, 2º Escribe un nombre")
            img_1.save(f"{ruta_guardado}.png")
            mensaje_completado = tk.Label(text=f"Se ha generado el QR con éxito en la ruta: {ruta_guardado}")
            mensaje_completado.place(x=95, y=82)
                      

    except:
        mensaje_completado = tk.Label(text="Lo sentimos, ha ocurrido un error inesperado.")
        mensaje_completado.place(x=95, y=82)


# Sección 1 - URL
etiqueta_url = tk.Label(text="Ingresa la URL")
etiqueta_url.place(x=20, y=40)
caja_url = tk.Entry()
caja_url.place(x=140, y=40, width=600)

#Sección 2 - Botón crear QR
boton_convertir = tk.Button(text="Generar QR", command=generar_qr)
boton_convertir.place(x=20, y=80)



# Mantiene abierta la interfaz hasta que se cierra la aplicación
ventana.mainloop()
