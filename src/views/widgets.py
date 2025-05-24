import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
import customtkinter as ctk

class WeekWidget(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.current_date = datetime.today()
        
        # Diccionarios de traducción al español
        self.days_spanish = {
            'Mon': 'Lun',
            'Tue': 'Mar', 
            'Wed': 'Mié',
            'Thu': 'Jue',
            'Fri': 'Vie',
            'Sat': 'Sáb',
            'Sun': 'Dom'
        }
        
        self.months_spanish = {
            'January': 'Enero', 'February': 'Febrero', 'March': 'Marzo',
            'April': 'Abril', 'May': 'Mayo', 'June': 'Junio',
            'July': 'Julio', 'August': 'Agosto', 'September': 'Septiembre',
            'October': 'Octubre', 'November': 'Noviembre', 'December': 'Diciembre'
        }
        
        self.months_spanish_short = {
            'Jan': 'Ene', 'Feb': 'Feb', 'Mar': 'Mar', 'Apr': 'Abr',
            'May': 'May', 'Jun': 'Jun', 'Jul': 'Jul', 'Aug': 'Ago',
            'Sep': 'Sep', 'Oct': 'Oct', 'Nov': 'Nov', 'Dec': 'Dic'
        }
        
        self.create_widgets()
        self.update_week()

    def create_widgets(self):
        # Top: Navigation + Month and Year (buttons fixed at edges)
        header_frame = ctk.CTkFrame(self, fg_color="transparent", corner_radius=50)
        header_frame.pack(fill=tk.X, pady=10)

        self.prev_btn = ctk.CTkButton(header_frame, text="⟨", width=32, command=self.prev_week, fg_color="transparent", text_color="black", hover_color="#b0b0b0")
        self.prev_btn.pack(side=tk.LEFT, anchor='w')

        self.header = ctk.CTkLabel(header_frame, font=('Segoe UI', 16, 'bold'), corner_radius=40)
        self.header.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=10)

        self.next_btn = ctk.CTkButton(header_frame, text="⟩", width=32, command=self.next_week, fg_color="transparent", text_color="black", hover_color="#b0b0b0")
        self.next_btn.pack(side=tk.RIGHT, anchor='e')

        # Middle: week days
        self.days_frame = ctk.CTkFrame(self, fg_color="transparent", corner_radius=0)
        self.days_frame.pack()
        
        # Bottom: Day names and dates
        self.day_labels = []
        self.date_labels = []
        for i in range(7):
            day_label = ctk.CTkLabel(self.days_frame, font=('Segoe UI', 10, 'bold'), corner_radius=150, width=25, height=25, anchor="center")
            day_label.grid(row=0, column=i, padx=0, pady=0, sticky="nsew")
            self.day_labels.append(day_label)

            date_label = ctk.CTkLabel(self.days_frame, font=('Segoe UI', 10), corner_radius=150, width=25, height=25, anchor="center")
            date_label.grid(row=1, column=i, padx=0, pady=(0, 10), sticky="nsew")
            self.date_labels.append(date_label)

        for i in range(7):
            self.days_frame.grid_columnconfigure(i, weight=1)

    def update_week(self):
        today = datetime.today()
        start_of_week = self.current_date - timedelta(days=self.current_date.weekday())
        end_of_week = start_of_week + timedelta(days=6)
        
        # Traducir nombres de meses
        if start_of_week.month == end_of_week.month:
            month_name = start_of_week.strftime('%B')
            month_year = f"{self.months_spanish[month_name]} {start_of_week.year}"
        else:
            start_month = start_of_week.strftime('%b')
            end_month = end_of_week.strftime('%b')
            month_year = f"{self.months_spanish_short[start_month]} - {self.months_spanish_short[end_month]} {end_of_week.year}"
        
        self.header.configure(text=month_year)

        for i in range(7):
            day = start_of_week + timedelta(days=i)
            is_today = (day.date() == today.date())
            is_current_week = (today >= start_of_week and today <= end_of_week)
            
            # Obtener día en inglés y traducir al español
            day_english = day.strftime('%a')
            day_spanish = self.days_spanish[day_english]
            
            # Default style
            self.day_labels[i].configure(
                text=day_spanish,
                fg_color="transparent",
                text_color="black"
            )
            self.date_labels[i].configure(
                text=day.strftime('%d'),
                fg_color="transparent",
                text_color="black"
            )
            # Highlight today if in current week
            if is_today and is_current_week:
                self.day_labels[i].configure(
                    fg_color="#fd6868",
                    text_color="black"
                )
                self.date_labels[i].configure(
                    fg_color="#fd6868",
                    text_color="black"
                )

    def prev_week(self):
        self.current_date -= timedelta(days=7)
        self.update_week()

    def next_week(self):
        self.current_date += timedelta(days=7)
        self.update_week()
        
class ScheduleWidget(ctk.CTkFrame):
    def __init__(self, master=None, schedule=None, **kwargs):
        super().__init__(master, **kwargs)
        self.schedule = schedule if schedule else []
        self.days_spanish = ['Lun', 'Mar', 'Mié', 'Jue', 'Vie', 'Sáb', 'Dom']
        self.create_widgets()

    def create_widgets(self):
        # Encabezados de días
        for col, day in enumerate(self.days_spanish):
            label = ctk.CTkLabel(self, text=day, font=('Segoe UI', 10, 'bold'), width=80, anchor="center")
            label.grid(row=0, column=col+1, padx=2, pady=2, sticky="nsew")

        # Horas (asumiendo de 7am a 8pm)
        for row, hour in enumerate(range(7, 21)):
            time_label = ctk.CTkLabel(self, text=f"{hour}:00", font=('Segoe UI', 10), width=60, anchor="e")
            time_label.grid(row=row+1, column=0, padx=2, pady=2, sticky="nsew")

        # Celdas de horario
        self.cells = {}
        for row, hour in enumerate(range(7, 21)):
            for col in range(7):
                cell = ctk.CTkLabel(self, text="", font=('Segoe UI', 10), width=80, height=28, anchor="center", fg_color="white")
                cell.grid(row=row+1, column=col+1, padx=1, pady=1, sticky="nsew")
                self.cells[(row, col)] = cell

        self.display_schedule()

    def display_schedule(self):
        # Limpia las celdas
        for cell in self.cells.values():
            cell.configure(text="", fg_color="white")
        # schedule: lista de dicts con keys: 'materia', 'dia', 'hora_inicio', 'hora_fin'
        for item in self.schedule:
            dia = item['dia']  # 0=Lun, 1=Mar, ..., 6=Dom
            hora_inicio = item['hora_inicio']  # int, ej: 8
            hora_fin = item['hora_fin']        # int, ej: 10
            materia = item['materia']
            for h in range(hora_inicio, hora_fin):
                row = h - 7
                if 0 <= row < 14 and 0 <= dia < 7:
                    self.cells[(row, dia)].configure(text=materia, fg_color="#e0eaff")