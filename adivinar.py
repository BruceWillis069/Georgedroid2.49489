import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

# Archivos de almacenamiento
ARCHIVO_PERSONAJES = "personajes.json"
ARCHIVO_PREGUNTAS = "preguntas.json"

# Cargar preguntas desde el archivo JSON si existe
def cargar_preguntas():
    if os.path.exists(ARCHIVO_PREGUNTAS):
        with open(ARCHIVO_PREGUNTAS, "r") as archivo:
            return json.load(archivo)
    else:
        return [
            ("sable_luz", "¿El personaje tiene un sable de luz?"),
            ("humano", "¿El personaje es humano?"),
            ("lado_oscuro", "¿El personaje pertenece al lado oscuro?"),
            ("jedi", "¿El personaje es un Jedi?"),
            ("wookie", "¿El personaje es un Wookie?"),
            ("droide", "¿El personaje es un droide?"),
            ("cazarrecompensas", "¿El personaje es un cazarrecompensas?"),
            ("casco", "¿El personaje usa casco?"),
            ("sith", "¿El personaje es un Sith?"),
            ("rebelde", "¿El personaje pertenece a la Alianza Rebelde?"),
            ("lider_batalla", "¿El personaje ha liderado una batalla importante?"),
            ("relacion_familiar", "¿El personaje tiene una relación familiar con otro personaje importante?"),
            ("saga", "¿El personaje pertenece a la trilogía original?")
        ]

# Guardar preguntas en el archivo JSON
def guardar_preguntas(preguntas):
    with open(ARCHIVO_PREGUNTAS, "w") as archivo:
        json.dump(preguntas, archivo, indent=4)

# Cargar personajes desde el archivo JSON si existe
def cargar_personajes():
    if os.path.exists(ARCHIVO_PERSONAJES):
        with open(ARCHIVO_PERSONAJES, "r") as archivo:
            return json.load(archivo)
    else:
        return [
            {"nombre": "Luke Skywalker", "sable_luz": True, "humano": True, "lado_oscuro": False, "jedi": True, "droide": False, "cazarrecompensas": False, "casco": False, "sith": False, "rebelde": True, "wookie": False, "lider_batalla": False, "relacion_familiar": True, "saga": "original"},
            {"nombre": "Leia Organa", "sable_luz": False, "humano": True, "lado_oscuro": False, "jedi": False, "droide": False, "cazarrecompensas": False, "casco": False, "sith": False, "rebelde": True, "wookie": False, "saga": "original"},
            {"nombre": "Darth Vader", "sable_luz": True, "humano": True, "lado_oscuro": True, "jedi": False, "droide": False, "cazarrecompensas": False, "casco": True, "sith": True, "rebelde": False, "wookie": False, "saga": "original"},
            {"nombre": "Emperador Palpatine", "sable_luz": False, "humano": True, "lado_oscuro": True, "jedi": False, "droide": False, "cazarrecompensas": False, "casco": False, "sith": True, "rebelde": False, "wookie": False, "saga": "original"},
            {"nombre": "Mace Windu", "sable_luz": True, "humano": True, "lado_oscuro": False, "jedi": True, "droide": False, "cazarrecompensas": False, "casco": False, "sith": False, "rebelde": False, "wookie": False, "lider_batalla": True, "relacion_familiar": False, "saga": "precuela"},
            {"nombre": "Yoda", "sable_luz": True, "humano": False, "lado_oscuro": False, "jedi": True, "droide": False, "cazarrecompensas": False, "casco": False, "sith": False, "rebelde": False, "wookie": False, "saga": "original"},
            {"nombre": "Chewbacca", "sable_luz": False, "humano": False, "lado_oscuro": False, "jedi": False, "droide": False, "cazarrecompensas": False, "casco": False, "sith": False, "rebelde": True, "wookie": True, "saga": "original"},
            {"nombre": "Cad Bane", "sable_luz": False, "humano": False, "lado_oscuro": True, "jedi": False, "droide": False, "cazarrecompensas": True, "casco": True, "sith": False, "rebelde": False, "wookie": False, "saga": "precuela"},
            {"nombre": "Jango Fett", "sable_luz": False, "humano": True, "lado_oscuro": False, "jedi": False, "droide": False, "cazarrecompensas": True, "casco": True, "sith": False, "rebelde": False, "wookie": False, "saga": "precuela"},
            {"nombre": "R2-D2", "sable_luz": False, "humano": False, "lado_oscuro": False, "jedi": False, "droide": True, "cazarrecompensas": False, "casco": False, "sith": False, "rebelde": True, "wookie": False, "saga": "original"}
        ]

# Guardar personajes en el archivo JSON
def guardar_personajes(personajes):
    with open(ARCHIVO_PERSONAJES, "w") as archivo:
        json.dump(personajes, archivo, indent=4)

# Clase principal del juego con GUI
class AdivinaPersonajeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Adivina el Personaje - Star Wars")
        self.personajes = cargar_personajes()  
        self.preguntas = cargar_preguntas()

        
        self.canvas = tk.Canvas(root, width=600, height=400)
        self.canvas.pack(fill="both", expand=True)

        
        self.fondo_imagen = tk.PhotoImage(file=r"C:\Gerogedroid2.3243\fondoespacio.gif")
        self.canvas.create_image(0, 0, image=self.fondo_imagen, anchor="nw")

        
        button_style = {"font": ("Arial", 12), "bg": "#5b9bd5", "fg": "white", "width": 20, "height": 2}
        
      
        self.ver_personajes_btn = tk.Button(root, text="Ver Personajes", command=self.ver_personajes, **button_style)
        self.canvas.create_window(300, 100, anchor="center", window=self.ver_personajes_btn)

        self.adivinar_btn = tk.Button(root, text="Adivinar Personaje", command=self.iniciar_adivinar, **button_style)
        self.canvas.create_window(300, 150, anchor="center", window=self.adivinar_btn)

        self.agregar_personaje_btn = tk.Button(root, text="Agregar Personaje", command=self.agregar_personaje, **button_style)
        self.canvas.create_window(300, 200, anchor="center", window=self.agregar_personaje_btn)

        self.eliminar_personaje_btn = tk.Button(root, text="Eliminar Personaje", command=self.eliminar_personaje, **button_style)
        self.canvas.create_window(300, 250, anchor="center", window=self.eliminar_personaje_btn)

        self.agregar_pregunta_btn = tk.Button(root, text="Agregar Pregunta", command=self.agregar_pregunta, **button_style)
        self.canvas.create_window(300, 300, anchor="center", window=self.agregar_pregunta_btn)

        self.salir_btn = tk.Button(root, text="Salir", command=root.quit, **button_style)
        self.canvas.create_window(300, 350, anchor="center", window=self.salir_btn)

    def ver_personajes(self):
        personajes_nombres = [p["nombre"] for p in self.personajes]
        messagebox.showinfo("Personajes Disponibles", "\n".join(personajes_nombres))

    def iniciar_adivinar(self):
        self.root.withdraw()  
        self.adivinador = AdivinaPersonaje(self.root, self.personajes, self.preguntas, self)

    def agregar_personaje(self):
        nombre = simpledialog.askstring("Agregar Personaje", "Ingrese el nombre del personaje:")
        if nombre:
            nuevo_personaje = {"nombre": nombre}
            for caracteristica, pregunta in self.preguntas:
                respuesta = messagebox.askyesno("Agregar Características", pregunta)
                nuevo_personaje[caracteristica] = respuesta
            self.personajes.append(nuevo_personaje)
            guardar_personajes(self.personajes)
            messagebox.showinfo("Personaje Agregado", f"{nombre} ha sido agregado exitosamente.")

    def eliminar_personaje(self):
        ventana_eliminar = tk.Toplevel(self.root)
        ventana_eliminar.title("Eliminar Personaje")
        ventana_eliminar.configure(bg="#3b3f45")

        tk.Label(ventana_eliminar, text="Seleccione el personaje a eliminar:", font=("Arial", 12), bg="#3b3f45", fg="white").pack(pady=10)

        opciones_personajes = [p["nombre"] for p in self.personajes]
        personaje_seleccionado = tk.StringVar(ventana_eliminar)
        personaje_seleccionado.set(opciones_personajes[0])

        lista_personajes = tk.OptionMenu(ventana_eliminar, personaje_seleccionado, *opciones_personajes)
        lista_personajes.pack(pady=10)

        def confirmar_eliminacion():
            nombre_a_eliminar = personaje_seleccionado.get()
            self.personajes = [p for p in self.personajes if p["nombre"] != nombre_a_eliminar]
            guardar_personajes(self.personajes)
            messagebox.showinfo("Personaje Eliminado", f"{nombre_a_eliminar} ha sido eliminado exitosamente.")
            ventana_eliminar.destroy()

        eliminar_btn = tk.Button(ventana_eliminar, text="Eliminar", command=confirmar_eliminacion, bg="#d9534f", fg="white")
        eliminar_btn.pack(pady=10)

    def agregar_pregunta(self):
        nueva_pregunta_texto = simpledialog.askstring("Nueva Pregunta", "Ingrese la nueva pregunta:")
        if nueva_pregunta_texto:
            nueva_caracteristica = nueva_pregunta_texto.replace(" ", "_").lower()
            self.preguntas.append((nueva_caracteristica, nueva_pregunta_texto))

            for personaje in self.personajes:
                respuesta = messagebox.askyesno("Respuesta para cada personaje", f"{personaje['nombre']}: {nueva_pregunta_texto}")
                personaje[nueva_caracteristica] = respuesta

            guardar_personajes(self.personajes)
            guardar_preguntas(self.preguntas)
            messagebox.showinfo("Pregunta Agregada", "La nueva pregunta ha sido agregada exitosamente.")

# Clase para el juego de adivinanza
class AdivinaPersonaje:
    def __init__(self, root, personajes, preguntas, app):
        self.root = root
        self.personajes_restantes = personajes
        self.preguntas = preguntas
        self.preguntas_realizadas = []
        self.pregunta_actual = None
        self.app = app
        self.imagen_cambiada = False

        # Interfaz de adivinanza
        self.adivinar_ventana = tk.Toplevel(root)
        self.adivinar_ventana.title("Adivinanza en Proceso")
        self.adivinar_ventana.configure(bg="#3b3f45")

        self.label = tk.Label(self.adivinar_ventana, text="Piensa en un personaje de Star Wars", font=("Arial", 16, "bold"), bg="#3b3f45", fg="white")
        self.label.pack(pady=20)

        self.imagen = tk.PhotoImage(file=r"C:\Gerogedroid2.3243\georgedroid.gif")
        self.imagen_label = tk.Label(self.adivinar_ventana, image=self.imagen, bg="#3b3f45")
        self.imagen_label.pack(pady=10)

        self.pregunta_label = tk.Label(self.adivinar_ventana, text="", font=("Arial", 14), bg="#3b3f45", fg="white")
        self.pregunta_label.pack(pady=10)

        button_style = {"font": ("Arial", 12), "bg": "#5cb85c", "fg": "white", "width": 10}
        
        self.si_button = tk.Button(self.adivinar_ventana, text="Sí", command=self.responder_si, **button_style)
        self.no_button = tk.Button(self.adivinar_ventana, text="No", command=self.responder_no, **button_style)
        self.si_button.pack(side="left", padx=20, pady=10)
        self.no_button.pack(side="right", padx=20, pady=10)

        self.siguiente_pregunta()

    def siguiente_pregunta(self):
        if len(self.preguntas_realizadas) >= 3 and not self.imagen_cambiada:
            self.cambiar_imagen()
        
        if len(self.preguntas_realizadas) < len(self.preguntas):
            caracteristica, pregunta_texto = self.preguntas[len(self.preguntas_realizadas)]
            self.pregunta_actual = (caracteristica, pregunta_texto)
            self.pregunta_label.config(text=pregunta_texto)
        else:
            self.finalizar_adivinanza()

    def cambiar_imagen(self):
        nueva_imagen = tk.PhotoImage(file=r"C:\Gerogedroid2.3243\georgedroirdtinkin.gif")
        self.imagen_label.config(image=nueva_imagen)
        self.imagen_label.image = nueva_imagen
        self.imagen_cambiada = True

    def responder_si(self):
        self.responder(True)

    def responder_no(self):
        self.responder(False)

    def responder(self, respuesta):
        caracteristica, _ = self.pregunta_actual
        self.personajes_restantes = [p for p in self.personajes_restantes if p.get(caracteristica) == respuesta]
        self.preguntas_realizadas.append(self.pregunta_actual)
        
        if len(self.personajes_restantes) == 1:
            personaje_adivinado = self.personajes_restantes[0]["nombre"]
            self.opciones_finales(personaje_adivinado)
        elif len(self.personajes_restantes) == 0:
            messagebox.showinfo("Adivinanza", "No pude adivinar tu personaje. ¡Intenta con otro!")
            self.adivinar_ventana.destroy()
            self.app.root.deiconify()
        else:
            self.siguiente_pregunta()

    def opciones_finales(self, personaje_adivinado):
        confirmacion = messagebox.askyesno("Confirmación", f"¿Es {personaje_adivinado} el personaje que pensaste?")
        if confirmacion:
            messagebox.showinfo("Adivinanza", f"¡He adivinado! El personaje es: {personaje_adivinado}")
        else:
            messagebox.showinfo("Adivinanza", "Parece que no acerté. ¡Intentémoslo de nuevo!")

        if messagebox.askyesno("Volver al Menú", "¿Deseas volver al menú principal?"):
            self.adivinar_ventana.destroy()
            self.app.root.deiconify()
        else:
            self.root.quit()

    def finalizar_adivinanza(self):
        messagebox.showinfo("Adivinanza", "No quedan más preguntas. ¡Intenta con otro personaje!")
        self.adivinar_ventana.destroy()
        self.app.root.deiconify()

# Inicializar y ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = AdivinaPersonajeApp(root)
    root.mainloop()
