"""
Logarithmic
"""
import numpy as np


def log_transform(parent, ui_function, pixels):
    """
    Faz a transformação logaritmica em uma imagem, usando de uma constante * a operação de log na base 10 do pixel + 1
    :param ui_function:
    :param parent: uma instancia da classe MainWindow
    :param pixels: os pixels da imagem que tera o seguinte filtro aplicado
    """

    c = 255/np.log10(255+1)
    min_nonzero = np.min(pixels[np.nonzero(pixels)])
    pixels[pixels == 0] = min_nonzero
    pixels = np.log10(pixels) * c
    pixels = pixels.astype(int)

    ui_function.set_image(parent, pixels, False, True)

