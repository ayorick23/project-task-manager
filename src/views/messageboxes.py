import customtkinter as ctk

class CTkMessageBox:
    def __init__(self, title="Mensaje", message="", icon="info", option_1="OK", option_2=None, option_3=None):
        self.root = ctk.CTkToplevel()
        self.root.title(title)
        self.root.geometry("400x200")
        self.root.resizable(False, False)
        self.root.grab_set()  #hace que esta ventana sea modal
        
        #Centrar la ventana
        self.center_window()
        
        #Crear contenido
        self.frame = ctk.CTkFrame(self.root)
        self.frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Iconos
        iconos = {
            "info": "ℹ️",
            "warning": "⚠️",
            "error": "❌",
            "question": "❓"
        }
        
        icon_label = ctk.CTkLabel(self.frame, text=iconos.get(icon, "ℹ️"), font=("Segoe UI", 30))
        icon_label.pack(pady=10)
        
        # Mensaje
        msg_label = ctk.CTkLabel(self.frame, text=message, wraplength=300, font=("Segoe UI", 12))
        msg_label.pack(pady=10)
        
        # Frame para botones
        button_frame = ctk.CTkFrame(self.frame, fg_color="transparent")
        button_frame.pack(pady=10, fill="x")
        
        # Botones
        self.result = None
        
        # Agregar los botones necesarios
        if option_1:
            btn1 = ctk.CTkButton(button_frame, text=option_1, command=lambda: self.set_result(option_1))
            btn1.pack(side="left", padx=10, expand=True)
        
        if option_2:
            btn2 = ctk.CTkButton(button_frame, text=option_2, command=lambda: self.set_result(option_2))
            btn2.pack(side="left", padx=10, expand=True)
        
        if option_3:
            btn3 = ctk.CTkButton(button_frame, text=option_3, command=lambda: self.set_result(option_3))
            btn3.pack(side="left", padx=10, expand=True)
        
        # Configurar el comportamiento al cerrar
        self.root.protocol("WM_DELETE_WINDOW", lambda: self.set_result(None))
        
        #Hacerlo modal
        self.root.transient()
        self.root.wait_visibility()
        self.root.wait_window()
    
    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"+{x}+{y}")
    
    def set_result(self, result):
        self.result = result
        self.root.destroy()

#Tipos de messagebox
def showinfo(title="", message=""):
    msgbox = CTkMessageBox(title=title, message=message, icon="info")
    return msgbox.result

def showerror(title="", message=""):
    msgbox = CTkMessageBox(title=title, message=message, icon="error")
    return msgbox.result

def showwarning(title="", message=""):
    msgbox = CTkMessageBox(title=title, message=message, icon="warning")
    return msgbox.result

def askyesno(title="", message=""):
    msgbox = CTkMessageBox(title=title, message=message, icon="question", option_1="Sí", option_2="No")
    return msgbox.result == "Sí"

def askyesnocancel(title="Pregunta", message=""):
    msgbox = CTkMessageBox(title=title, message=message, icon="question", 
                           option_1="Sí", option_2="No", option_3="Cancelar")
    return msgbox.result
