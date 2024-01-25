# interface.py
import tkinter as tk
from tkinter import ttk, messagebox
from logica import Logica
from sobre import SobreFrame
import time
import threading
import pyautogui as py

class Interface(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Controle")
        self.geometry("200x250")

        self.notebook = ttk.Notebook(self)
        self.programa_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.programa_frame, text="Programa")
        self.sobre_frame = SobreFrame(self.notebook)
        self.notebook.add(self.sobre_frame, text="Sobre")
        self.notebook.select(self.programa_frame)
        self.notebook.pack(expand=1, fill="both")

        self.programa_em_execucao = False
        self.thread = None

        self.btn_iniciar_parar = ttk.Button(self.programa_frame, text="Iniciar Programa", command=self.iniciar_programa)
        self.btn_iniciar_parar.pack(pady=10)
        self.btn_fechar = ttk.Button(self.programa_frame, text="Parar Programa", command=self.para_programa)
        self.btn_fechar.pack(pady=10)

        self.status_label = tk.Label(self.programa_frame, text="Status: Inativo")
        self.status_label.pack(side="bottom", fill="x")

        self.protocol("WM_DELETE_WINDOW",self.on_close)

    def iniciar_arrastar(self, event):
        self.x = event.x
        self.y = event.y

    def arrastar(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        new_x = self.winfo_x() + deltax
        new_y = self.winfo_y() + deltay
        self.geometry(f"+{new_x}+{new_y}")

    def habilitar_botao(self, habilitar):
        state = tk.NORMAL if habilitar else tk.DISABLED
        self.btn_fechar["state"] = state

    def atualizar_status(self, status):
        self.status_label["text"] = status
    def iniciar_parar_programa(self):
        if self.programa_em_execucao:
            print("iniciado")
            self.para_programa()
        else:
            self.iniciar_programa()

    def iniciar_programa(self):
        self.programa_em_execucao = True
        self.atualizar_status("Status: Ativo")
        # Iniciar a thread
        self.thread = threading.Thread(target=self.executar_programa)
        self.thread.start()

    def on_close(self):
        if self.programa_em_execucao:
            print("Aguarde até o programa ser parado")
            messagebox.showinfo("Aviso","Aguarde até o programa ser parado!")
        else:
            self.destroy()
    def para_programa(self):

        self.programa_em_execucao = False

        if self.thread is not None:
            self.thread.join()
        self.atualizar_status("Status: Inativo")
        self.habilitar_botao(True)
        #self.destroy()

    def executar_programa(self):
        print("Executou")
        while self.programa_em_execucao:
            print("Iniciando verificação")
            for _ in range(60):
                if not self.programa_em_execucao:
                    break
                time.sleep(1)
            if not self.programa_em_execucao:
                break
            #time.sleep(60)
            if Logica.encontrar_elemento_na_tela("fotos/conectado2.png"):
                #time.sleep(30)
                print("Elemento encontrado")
            else:
                try:
                    print("Elemento não encontrado, iniciando o encerramento do programa")
                    time.sleep(1)
                    Logica.encontrar_elemento_na_tela("fotos/foto_x2.png")
                    #esperar_elemento(lambda: Logica.encontrar_elemento_na_tela("fotos/foto_x2.png"), 10, 1)
                    py.click()
                    time.sleep(2)
                    Logica.encontrar_elemento_na_tela("fotos/sim2.png")
                    py.click()
                    time.sleep(1)
                    py.hotkey('win', 'r')
                    py.write('desktop\Servidor Catraca.Ink')
                    time.sleep(2)
                    py.press('enter')
                    #time.sleep(30)
                    Logica.encontrar_elemento_na_tela("fotos/conf.png")
                    py.click()

                except Exception as e:
                    print("Erro ao tentar fechar o programa, valor não encontrado")
                    break
        print("Saindo do loop")
        return False
