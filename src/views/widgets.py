import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
import customtkinter as ctk

class WeekWidget(ctk.CTkFrame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.current_date = datetime.today()
        self.create_widgets()
        self.update_week()

    def create_widgets(self):
        # Top: Navigation + Month and Year (buttons fixed at edges)
        header_frame = ctk.CTkFrame(self, fg_color="transparent", corner_radius=50)
        header_frame.pack(fill=tk.X, pady=10)

        self.prev_btn = ctk.CTkButton(header_frame, text="⟨", width=32, command=self.prev_week, fg_color="#e0e0e0", text_color="black", hover_color="#b0b0b0")
        self.prev_btn.pack(side=tk.LEFT, anchor='w')

        self.header = ctk.CTkLabel(header_frame, font=('Segoe UI', 16, 'bold'), corner_radius=40)
        self.header.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=10)

        self.next_btn = ctk.CTkButton(header_frame, text="⟩", width=32, command=self.next_week, fg_color="#e0e0e0", text_color="black", hover_color="#b0b0b0")
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
        if start_of_week.month == end_of_week.month:
            month_year = start_of_week.strftime('%B %Y')
        else:
            month_year = f"{start_of_week.strftime('%b')} - {end_of_week.strftime('%b %Y')}"
        self.header.configure(text=month_year)

        for i in range(7):
            day = start_of_week + timedelta(days=i)
            is_today = (day.date() == today.date())
            is_current_week = (today >= start_of_week and today <= end_of_week)
            # Default style
            self.day_labels[i].configure(
                text=day.strftime('%a'),
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