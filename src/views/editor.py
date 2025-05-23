import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText
import markdown
from fpdf import FPDF
import os
import customtkinter as ctk

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

class LineNumberCanvas(ctk.CTkCanvas):
    def create_text(self, *args, **kwargs):
        # Cambio de fuente y color de numeros
        kwargs["font"] = ("JetBrains Mono", 12)
        kwargs["fill"] = "#ffffff"
        return super().create_text(*args, **kwargs)
    
    def __init__(self, master, text_widget, **kwargs):
        super().__init__(master, **kwargs)
        self.text_widget = text_widget
        self.text_widget.bind('<KeyRelease>', self.redraw)
        self.text_widget.bind('<MouseWheel>', self.redraw)
        self.text_widget.bind('<Button-1>', self.redraw)
        self.redraw()

    def redraw(self, event=None):
        self.delete("all")
        i = self.text_widget.index("@0,0")
        while True:
            dline = self.text_widget.dlineinfo(i)
            if dline is None:
                break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2, y, anchor="nw", text=linenum, font=self.text_widget['font'])
            i = self.text_widget.index(f"{i}+1line")

class MarkdownEditor(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
        title_label = ctk.CTkLabel(self, text="Notas de clases", font=("Segoe UI", 48, "bold"), anchor="w")
        title_label.pack(side="top", anchor="w", padx=15, pady=(10, 0))
        # Top frame for buttons
        top_frame = ctk.CTkFrame(self, fg_color="transparent")
        top_frame.pack(side="top", fill="x", padx=5, pady=5)
        
        export_md_btn = ctk.CTkButton(top_frame, text="Exportar Markdown", command=self.export_markdown)
        export_md_btn.pack(side="right", padx=6, pady=6)

        export_pdf_btn = ctk.CTkButton(top_frame, text="Exportar PDF", command=self.export_pdf)
        export_pdf_btn.pack(side="right", padx=6, pady=6)
        
        # Main frame for editor
        editor_frame = ctk.CTkFrame(self)
        editor_frame.pack(fill="both", expand=True, padx=5, pady=5)

        # Line numbers
        self.text = ScrolledText(editor_frame, wrap="word", font=("JetBrains Mono", 12), undo=True, bg="#23272e", fg="#f8f8f2", insertbackground="#f8f8f2")
        self.text.pack(side="right", fill="both", expand=True, padx=(0, 2), pady=2)

        self.linenumbers = LineNumberCanvas(editor_frame, self.text, width=35, bg="#1a1d23", highlightthickness=0)
        self.linenumbers.pack(side="left", fill="y", padx=(2, 0), pady=2)

        self.text.bind('<KeyRelease>', self.linenumbers.redraw)
        self.text.bind('<MouseWheel>', self.linenumbers.redraw)
        self.text.bind('<Button-1>', self.linenumbers.redraw)

    def export_markdown(self):
        content = self.text.get("1.0", tk.END)
        file_path = filedialog.asksaveasfilename(defaultextension=".md", filetypes=[("Markdown files", "*.md")])
        if file_path:
            try:
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(content)
                messagebox.showinfo("Exportar Markdown", "Archivo Markdown exportado exitosamente.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo exportar: {e}")

    def export_pdf(self):
        content = self.text.get("1.0", tk.END)
        html = markdown.markdown(content)
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if file_path:
            try:
                pdf = FPDF()
                pdf.add_page()
                pdf.set_auto_page_break(auto=True, margin=15)
                pdf.set_font("Arial", size=12)
                for line in html.split('\n'):
                    pdf.multi_cell(0, 10, line, 0, 1)
                pdf.output(file_path)
                messagebox.showinfo("Exportar PDF", "Archivo PDF exportado exitosamente.")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo exportar: {e}")
"""
if __name__ == "__main__":
    root = ctk.CTk()
    root.title("Editor Markdown")
    root.geometry("800x600")
    app = MarkdownEditor(root)
    root.mainloop()
"""