import speech_recognition as sr
import pyttsx3

name = 'alexa'

listener = sr.Recognizer()
listener.dynamic_energy_threshold = False

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 140) 

def talk(text):
  engine.say(text)
  engine.runAndWait()

def listen():
  try:
    with sr.Microphone() as source:
      print("Escuchando...")
      voice = listener.listen(source)
      rec = listener.recognize_google(voice,language='es-ES')
      rec = rec.lower()
      return rec
  except sr.UnknownValueError:
    talk('No entendí eso')
    return "Google Speech Recognition could not understand audio"
  
  

def options(rec):
  flag = True
  print(rec)
  if 'apaga te' in rec:
    talk('Hasta pronto')  
    flag = False
  elif 'qué es linux' in rec:
    talk('Linux es un kernel de código abierto creado por Linus Torvalds')
  elif 'cuántas temporadas tiene doctor house' in rec:
    talk('Dr House: Diagnóstico Médico cuenta con ocho temporadas emitidas entre 2004 y 2012')
  else:
    talk('No entendí eso')
  return flag
  
flag = True
while flag:
  rec = listen()
  if name in rec:
    flag = options(rec)
  

engine.stop()