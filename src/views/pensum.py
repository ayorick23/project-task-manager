import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import sqlite3
from models.task_manager import obtener_info_materias
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas

class PensumWindow(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self._build_ui()

    def _build_ui(self):
        # Título principal
        title_label = ctk.CTkLabel(self, text="Pensum", font=ctk.CTkFont(size=48, weight="bold"), anchor="w", justify="left")
        title_label.grid(row=0, column=0, sticky="nw", padx=15, pady=10)
        
        # Crear el frame principal
        frame = ctk.CTkFrame(self, corner_radius=10)
        frame.grid(row=1, column=0, padx=60, pady=10, sticky="nsew")

        # Encabezados de año
        years = ["Año I", "Año II", "Año III", "Año IV"]
        for i, year in enumerate(years):
            frame.grid_columnconfigure(i*2, weight=1)
            label = ctk.CTkLabel(frame, text=year, font=ctk.CTkFont(size=14, weight="bold"))
            label.grid(row=0, column=i*2, columnspan=2, sticky="nsew", padx=2, pady=5)

        # Encabezados de ciclo
        cycles = ["Ciclo I", "Ciclo II", "Ciclo III", "Ciclo IV", "Ciclo V", "Ciclo VI", "Ciclo VII", "Ciclo VIII"]
        for i, cycle in enumerate(cycles):
            label = ctk.CTkLabel(frame, text=cycle, font=ctk.CTkFont(size=12, weight="bold"))
            label.grid(row=1, column=i, sticky="nsew", padx=2, pady=5)

        # (columnas = ciclos, filas = materias por ciclo)
        materias = obtener_info_materias()
        num_filas = 5  # materias por ciclo
        num_columnas = 8  # ciclos

        for col in range(num_columnas):  # columnas 0 a 7 (ciclos)
            for row in range(num_filas):  # filas 0 a 4 (materias por ciclo)
                grid_row = row + 2  # ajustar por encabezados
                grid_col = col
                cell_frame = ctk.CTkFrame(frame, corner_radius=6)
                cell_frame.grid(row=grid_row, column=grid_col, padx=5, pady=5, sticky="nsew")
                frame.grid_rowconfigure(grid_row, weight=1)
                frame.grid_columnconfigure(grid_col, weight=1)

                index = col * num_filas + row
                if index < len(materias):
                    materia = materias[index]
                    ctk.CTkLabel(cell_frame, text=materia.get("Codigo", ""), width=60, justify="center").grid(row=0, column=0, padx=1, pady=1)
                    ctk.CTkLabel(cell_frame, text=materia.get("MateriaID", ""), width=60, justify="center").grid(row=0, column=1, padx=1, pady=1)
                    ctk.CTkLabel(cell_frame, text=materia.get("Nombre", ""), width=130, justify="center", wraplength=120).grid(row=1, column=0, columnspan=2, padx=1, pady=20)
                    ctk.CTkLabel(cell_frame, text=materia.get("RequisitosPrevios", ""), width=60, justify="center").grid(row=2, column=0, padx=1, pady=1)
                    ctk.CTkLabel(cell_frame, text=materia.get("UnidadesValorativas", ""), width=60, justify="center").grid(row=2, column=1, padx=1, pady=1)

                cell_frame.grid_rowconfigure(1, weight=1)
                cell_frame.grid_columnconfigure(0, weight=1)
                cell_frame.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)