'''
    Unidad Profesional Interdisciplinaria en Ingeniería y Tecnologías Avanzadas
    Instituto Politécnico Nacional
    Multimedia
    Noe Sierra Romero
    Asistente de Voz para Enfermedades y Afecciones
    Alumnos: 
      - Lilia Montserrat Fuentes Navarrete
      - Rosa Jazmin Portillo Sanchez
      - Luis Vazquez Padilla Luis
'''
import speech_recognition as sr
import pyttsx3

class Assistant():
  isOn = True
  engine = pyttsx3.init()
  engine.setProperty('rate',140)
  listener = sr.Recognizer()
  listener.dynamic_energy_threshold = False
  
  def __init__(self,name, oneAnswerQuestions,twoAnswerQuestions,threeAnswerQuestions):
      self.name = name
      self.oneAsnwerQuestions = oneAnswerQuestions
      self.twoAnswerQuestions = twoAnswerQuestions
      self.threeAnswerQuestions = threeAnswerQuestions

  # Sintetiza voz a apartir de un texto
  def talk(self, text):
    self.engine.say(text)
    self.engine.runAndWait()

  # Función para reconocimiento de voz en español
  def listen(self):
    try:
      with sr.Microphone() as source:
        print("Escuchando...")
        voice = self.listener.listen(source)
        rec = self.listener.recognize_google(voice,language='es-ES')
        rec = rec.lower()
        return rec
    except sr.UnknownValueError:
      self.talk('No entendí eso')
      return "Google Speech Recognition could not understand audio"

  # Selecciona una respuesta a partir del texto reconocido y algunas palabras clave
  def checkAnswer(self, questions, text):
    # Obtenemos la respuesta más apropieda y la sintentiza
    for q in questions:
      if q.checkSentence(sentence = text):
        self.talk(q.answer)
        return True
    self.talk('No tengo información sobre eso')
    return False
# El asistente comienza la escuha activa
  def run(self):
    while self.isOn:
      text = self.listen()
      print(text)
      # Verifica que la palabra clave se pronuncie para comenzar a buscar una respuesta
      if 'alexa' in text:
        if 'hola' in text: 
          self.talk('Hola, ¿En que te puedo ayudar?')
        elif any(word in text for word in ['hueso','órgano','diente','músculos', 'agua']):
          self.checkAnswer(text = text,questions = self.oneAsnwerQuestions)
        elif any(word in text for word in ['acné','menopausia','piojos','varicela', 'aparato digestivo']):
          self.checkAnswer(text = text, questions=self.twoAnswerQuestions)
        elif any(word in text for word in ['cardiovasculares', 'cerebrovasculares','coronavirus','sistema circulatorio','cáncer', 'corazón','médica', 'quimioterapia']):
          self.checkAnswer(text = text, questions=self.threeAnswerQuestions)
        elif 'apaga te' in text:
          self.isOn = False
          self.talk('Hasta pronto')
        else:
          self.talk('No tengo información sobre eso')
    self.engine.stop()

