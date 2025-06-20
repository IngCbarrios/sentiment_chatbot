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
   ```bash
   git clone https://github.com/tu_usuario/sentiment_chatbot.git
   cd sentiment_chatbot
