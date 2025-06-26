from textblob import TextBlob
from googletrans import Translator
import langdetect
from abc import ABC, abstractmethod

# Interfaz para la detección de idioma
class DetectorDeIdioma(ABC):
    @abstractmethod
    def detectar(self, texto): 
        pass

class DetectorLangDetect(DetectorDeIdioma):
    def detectar(self, texto):
        return langdetect.detect(texto)

# Interfaz para el análisis de sentimiento
class AnalizadorSentimiento(ABC):
    @abstractmethod
    def analizar(self, texto):
        pass

class AnalizadorTextBlob(AnalizadorSentimiento):
    def analizar(self, texto):
        analisis = TextBlob(texto)
        polaridad = analisis.sentiment.polarity
        if polaridad > 0:
            return "positivo 🙂"
        elif polaridad == 0:
            return "neutral 😐"            
        else:
            return "negativo ☹️"

# Clase principal con inyección de dependencias
class ChatbotSentimiento:
    def __init__(self, detector_idioma: DetectorDeIdioma, analizador: AnalizadorSentimiento):
        self.detector_idioma = detector_idioma
        self.analizador = analizador
        self.translator = Translator()  # Inicializamos el traductor

    def analizar_sentimiento(self, texto):
        if not texto.strip():
            return "Por favor, ingresa un texto válido."

        try:
            idioma = self.detector_idioma.detectar(texto)
            if idioma != "en":
                texto = self.translator.translate(texto, dest="en").text  # Traducimos con googletrans
        except Exception as e:
            return f"Error en la traducción: {e}"

        return self.analizador.analizar(texto)

# Inyección de dependencias
detector = DetectorLangDetect()
analizador = AnalizadorTextBlob()
chatbot = ChatbotSentimiento(detector, analizador)

# Chatbot interactivo
while True:
    texto_usuario = input("Escribe un mensaje (o 'salir' para terminar): ")
    if texto_usuario.lower() == "salir":
        break
    resultado = chatbot.analizar_sentimiento(texto_usuario)
    print("Análisis de sentimiento:", resultado)
