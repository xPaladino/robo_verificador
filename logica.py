# logica.py
import pyautogui as py
import os
import sys
import time
from PIL import Image


class Logica:
    @staticmethod
    def esperar_elemento(funcao, timeout, intervalo):
        tempo_inicial = time.time()
        while time.time() - tempo_inicial < timeout:
            if funcao():
                return True
            time.sleep(intervalo)
        return False

    @staticmethod
    def encontrar_elemento_na_tela(imagem_elemento):
        # Capturar a tela
        try:
            diretorio_script = os.path.dirname(os.path.abspath(__file__))
            if getattr(sys, 'frozen', False):
                diretorio_atual = os.path.dirname(sys.executable)
            else:
                diretorio_atual = diretorio_script

            imagem_path = os.path.join(diretorio_atual, imagem_elemento)
            screenshot = py.screenshot()

            # Salvar a captura de tela em um arquivo temporário
            screenshot.save(os.path.join(diretorio_atual, "01.png"))

            # Abrir a imagem do elemento a ser encontrado
            imagem_busca = Image.open(imagem_path)

            # Procurar o elemento na captura de tela
            try:
                posicao = list(py.locateAllOnScreen(imagem_busca, confidence=0.9))
                # Se o elemento for encontrado, posicao é uma tupla (x, y, largura, altura)
                if posicao is not None:
                    # Se o elemento for encontrado, posicao é uma tupla (x, y, largura, altura)
                    x, y, largura, altura = posicao[0]

                    # Mover o cursor do mouse para a posição do elemento encontrado
                    # py.moveTo(x + largura / 2, y + altura / 2)
                    py.moveTo(x + largura, y + altura / 2)
                    print("Achei")

                    return True
                else:
                    print("Elemento não encontrado na tela.")
                    return False

            except Exception as e:
                print("Deu erro")
                return False

        except Exception as e:
            print(f"Erro: {e}")
            return False
