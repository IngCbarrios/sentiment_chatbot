# Chatbot de Análisis de Sentimiento Multilenguaje🌍🤖

Este proyecto es un chatbot simple pero potente que analiza el **sentimiento** de textos escritos por el usuario. Es capaz de detectar el idioma automáticamente, traducirlo al inglés y analizar el sentimiento utilizando procesamiento de lenguaje natural (NLP). 

## 🧠 ¿Cómo funciona?

1. Detecta automáticamente el idioma del texto (por ejemplo, español, francés, alemán).
2. Si no está en inglés, lo traduce al inglés con Google Translate.
3. Analiza el sentimiento con **TextBlob** y responde con una interpretación positiva, neutral o negativa (¡con emojis!).

## 🧰 Tecnologías utilizadas

- `TextBlob` – Análisis de sentimiento
- `langdetect` – Detección automática de idioma
- `googletrans` – Traducción automática
- Python 3.8+

## 🚀 Instalación
1. Clona el repositorio:
   git clone https://github.com/tu_usuario/sentiment_chatbot.git
   cd sentiment_chatbot

2. Instala las dependencias:
   pip install -r requirements.txt

3. Ejecuta el chatbot:
   python chatbot.py

## 💬 Ejemplo de uso
Escribe un mensaje (o 'salir' para terminar): Me siento feliz
Análisis de sentimiento: positivo 🙂

## 📦 Estructura del proyecto
chatbot.py              # Código principal
requirements.txt        # Librerías necesarias
README.md               # Esta documentación


## ✍️ Autor
Christian Alejandro Barrios Quiroz  
Ingeniero Biomédico y Desarrollador en formación


