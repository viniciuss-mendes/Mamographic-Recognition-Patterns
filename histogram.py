from skimage import io
import matplotlib.pyplot as plt

def run_Histogram(image):

    plt.hist(image.ravel(), bins = 256)
    plt.title('Histograma de Frequência')
    plt.show()