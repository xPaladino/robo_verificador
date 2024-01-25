import tkinter as tk
from tkinter import ttk


class SobreFrame(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        # Adiciona a barra de rolagem à instância atual
        scrollbar = ttk.Scrollbar(self, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        # Adiciona um Text widget para exibir o conteúdo com a barra de rolagem
        self.text_widget = tk.Text(self, wrap="word", yscrollcommand=scrollbar.set)
        self.text_widget.pack(side="left", fill="both", expand=True)

        # Configura a barra de rolagem para rolar o Text widget
        scrollbar.config(command=self.text_widget.yview)

        # Adiciona o conteúdo ao Text widget
        conteudo = ("Robo Verificador\n\nVersão 1.0\n"
                    "Programa criado para verificar a tela."
                    "\n----------\n")

        self.text_widget.config(state="normal")
        self.text_widget.insert("1.0", conteudo)
        self.text_widget.config(state="disabled")

        conteudo2 = ("\nVersão 1.1\n"
                     "Adicionado para ele verificar a pasta onde está e procura a pasta FOTOS,"
                     "pasta fotos serão inclusas as fotos que ele irá procurar\n"
                     "Adicionado barra de rolagem no sobre\n"
                     "----------\n")

        self.text_widget.config(state="normal")
        self.text_widget.insert("end", conteudo2)
        self.text_widget.config(state="disabled")

        criador = ("\n\n    Lucas Pavanelli \n\n")
        self.text_widget.config(state="normal")
        self.text_widget.insert("end", criador)
        self.text_widget.config(state="disabled")
        scrollbar.bind("<ButtonPress-1>", self.on_scroll_press)
        scrollbar.bind("<B1-Motion>", self.on_scroll_drag)

    def on_scroll_press(self, event):
        self.y_start = event.y

    def on_scroll_drag(self, event):
        delta_y = event.y - self.y_start
        self.text_widget.yview_scroll(int(-1 * (delta_y / 120)), "units")

def criar_frame_sobre(master):
    return SobreFrame(master)