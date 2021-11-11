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

name = 'alexa'

listener = sr.Recognizer()
listener.dynamic_energy_threshold = False

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


rate = engine.getProperty('rate')   # getting details of current speaking rate
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
  

def checkSentence(sentence, claves):
  se = sentence.split()
  print(claves)
  print(se)
  i = 0
  for word in se:
    if word in claves:
      i=i+1
  if i>=3:
    return True
  if i ==claves.lenght:
    return True
  return False  


  

def oneAnswer(rec):
  checkList1 = ['cuántos', 'huesos', 'humano']
  checkList2 = ['cuántos','dientes','humano','persona']
  checkList3 = ['porcentaje','agua','humano', 'persona']
  checkList4 = ['cuántos','músculos','humano', 'persona']
  checkList5 = ['cuántos','órganos','humano', 'persona']
  
  if checkSentence(rec,checkList1):
    talk('El cuerpo humano adulto tiene nada menos que 206 huesos')
    return True
  elif checkSentence(rec, checkList2):
    talk('32 piezas dentales es la cantidad normal para un adulto')
    return True
  elif checkSentence(rec, checkList3):
    talk('El cuerpo humano está compuesto en un 60 por ciento de agua, el cerebro se compone en un 70 por ciento de agua, la sangre en un 80 por ciento y los pulmones se componen en un 90 por ciento de agua.')
    return True
  elif checkSentence(rec, checkList4):
    talk('El cuerpo humano contiene aproximadamente 650 músculos estriados.')
    return True
  elif checkSentence(rec, checkList5):
    talk('El cuerpo humano tiene 21 órganos')
    return True
  
  return False
  

def twoAnswers(rec):
  checkList1 = ['qué','acné']
  checkList2 = ['prevenir', 'acné']
  checkList3 = ['qué', 'menopausia']
  checkList4 = ['edad', 'menopausia']
  checkList5 = ['qué', 'piojos']
  checkList6 = ['cómo','contagian','piojos', 'contagio']
  checkList7 = ['qué', 'varicela']
  checkList8 = ['qué', 'adulto','varicela', 'contagia']
  checkList9 = ['aparato', 'digestivo']
  checkList10 = ['órganos','aparato', 'digestivo']
  if checkSentence(rec, checkList1):
    talk('El acne es una enfermedad cutánea que suele aparecer a partir de los 12 años de edad, sobre todo en la cara, y que, si no hay complicaciones graves, solo se desarrolla durante la pubertad y desaparece hacia los 18 o 20 años.')
    return True
  elif checkSentence(rec, checkList2):
    talk('Lávate la cara dos veces al día (no más) con agua tibia y un jabón suave fabricado específicamente para personas con acné. Masajéate suavemente la cara describiendo movimientos circulares. No te frotes la cara.')
    return True
  elif checkSentence(rec, checkList3):
    talk('Es un proceso biológico natural que marca el final de los ciclos menstruales. Se diagnostica después de que transcurren doce meses sin que tengas un período menstrual.')
    return True
  elif checkSentence(rec, checkList4):
    talk('La menopausia puede producirse entre los 40 y 50 años, pero la edad promedio es a los 51 años.')
    return True
  elif checkSentence(rec, checkList5):
    talk('Los piojos son pequeños insectos que viven en la cabeza de las personas. Los piojos adultos tienen el tamaño de las semillas de sésamo. Los huevos, llamados liendres, son incluso más pequeños, aproximadamente del tamaño de una escama de caspa.')
    return True
  elif checkSentence(rec, checkList6):
    talk('Los piojos se mueven arrastrándose, porque no pueden saltar ni volar. Se contagian a través del contacto cercano de persona a persona. En raras ocasiones, se pueden contagiar al compartir objetos personales como sombreros o cepillos para el cabello. La higiene personal y la limpieza no se relacionan con tener piojos.')
    return True
  elif checkSentence(rec, checkList7):
    talk('La varicela es una infección causada por el virus de la varicela-zóster. Causa una erupción en la piel con picazón y pequeñas ampollas con líquido. La varicela es muy contagiosa para personas que no han tenido la enfermedad antes o no se han vacunado. ')
    return True
  elif checkSentence(rec, checkList8):
    talk('Puede causar: deshidratación, neumonía, problemas de sangrado, infección o inflamación cerebral, infecciones bacterianas de la piel, infecciones del torrente sanguíneo (septicemia), síndrome de shock tóxico, infecciones de los huesos, infecciones de las articulaciones, o la muerte.')
    return True
  elif checkSentence(rec, checkList9):
    talk('Conjunto de órganos que procesan los alimentos y los líquidos para descomponerlos en sustancias que el cuerpo usa como fuente de energía, o para el crecimiento y la reparación de tejidos.')
    return True
  elif checkSentence(rec, checkList10):
    talk('El aparato digestivo está formado por el tracto gastrointestinal, también llamado tracto digestivo, y el hígado, el páncreas y la vesícula biliar.')
    return True

  return False

def threeAnswers(rec):
  if 'qué son enfermedades cardiovasculares' in rec:
    talk('Las enfermedades cardiovasculares (ECV) son un grupo de desórdenes del corazón y de los vasos sanguíneos.')
    return True
  elif 'cuáles son los síntomas comunes de las enfermedades cardiovasculares' in rec:
    talk('Molestias en el pecho, molestias en los brazos, hombro izquierdo, mandíbula o espalda')
    return True
  elif 'cuáles son los principales factores de riesgo de las sv' in rec:
    talk('Las causas más importantes son una dieta malsana, la inactividad física, el consumo de tabaco y el consumo nocivo de alcohol')
    return True
  elif 'qué son las enfermedades cerebrovasculares' in rec:
    talk('Son isquémicas y ocurren cuando las arterias que llevan sangre al cerebro se hacen angostas o se bloquean, causando una disminución severa o interrupción del flujo sanguíneo, conocida como isquemia.')
    return True
  elif 'cuáles son los síntomas de las enfermedades cerebrovasculares' in rec:
    talk('Alteración repentina de la visión en un ojo o ambos, Pérdida repentina de la fuerza en un brazo, una pierna o ambos. Sensación de hormigueo en la cara, brazo o pierna. Aparición repentina de: Problemas para hablar y/o entender lo que se escucha, acompañada por balbuceo. Desequilibrio o inestabilidad. Dolor de cabeza.')
    return True
  elif 'cuáles son los factores de riesgo de las enfermedades cerebrovasculares' in rec:
    talk('El sexo. Se presenta con mayor frecuencia en hombres que en mujeres. Alcoholismo. Tabaquismo. Inactividad física. Obesidad. Presión arterial alta. Diabetes Mellitus. Niveles de colesterol elevados.')
    return True
  elif 'qué es el coronavirus' in rec:
    talk('Los coronavirus son una familia de virus que causan enfermedades (desde el resfriado común hasta enfermedades respiratorias más graves) y circulan entre humanos y animales.')
    return True
  elif 'cómo se transmite el coronavirus' in rec:
    talk('Los coronavirus humanos se transmiten de una persona infectada a otras: a través de las gotículas que expulsa un enfermo al toser y estornudar ,al tocar o estrechar la mano de una persona enferma, un objeto o superficie contaminada con el virus y luego llevarse las manos sucias a boca, nariz u ojos.')
    return True
  elif 'cuándo debo acudir a recibir atención médica' in rec:
    talk('Una persona debe sospechar de COVID-19 cuando presenta al menos dos de los siguientes síntomas: Tos / Estornudos, Fiebre, Dolor de cabeza.')
    return True
  elif 'qué es el sistema circulatorio' in rec:
    talk('El sistema circulatorio se encarga de bombear, transportar y distribuir la sangre por todo el cuerpo.')
    return True
  elif 'cómo está integrado el sistema circulatorio' in rec:
    talk('Se integra con el corazón y los vasos sanguíneos: arterias, venas y capilares.')
    return True
  elif 'qué es el corazón' in rec:
    talk('Es una bomba muscular y se considera el centro del sistema circulatorio.')
    return True
  elif 'qué es el cáncer' in rec:
    talk('El cáncer puede desarrollarse en cualquier parte del cuerpo. Se origina cuando las células crecen sin control y sobrepasan en número a las células normales. Esto hace que al cuerpo le resulte difícil funcionar de la manera que debería hacerlo')
    return True
  elif 'cuál es el tratamiento para el cáncer' in rec:
    talk('La mayoría de las personas reciben una combinación de tratamientos, como cirugía con quimioterapia o radioterapia.')
    return True
  elif 'qué es quimioterapia' in rec:
    talk('Tratamiento con medicamentos para interrumpir la formación de células cancerosas, ya sea mediante su destrucción o al impedir su multiplicación. La quimioterapia se administra por la boca, en inyección, por infusión o sobre la piel, según el tipo de cáncer y el estado en que este se encuentra. Se administra sola o con otros tratamientos como cirugía, radioterapia o terapia biológica.')
    return True

  return False

def options(rec):
  print(rec)
  if oneAnswer(rec):
    return True
  elif twoAnswers(rec):
    return True
  elif threeAnswers(rec):
    return True
  elif 'apaga te' in rec:
    talk('Hasta pronto')  
    return False  
  elif 'apagáte'  in rec:
    talk('Hasta pronto')  
    return False  
  elif 'hola' in rec:
    talk('Hola, ¿En que te puedo ayudar?')  
    return True  
  else:
    talk('No entendí eso')
  return True
  
flag = True
while flag:
  rec = listen()
  if name in rec:
    flag = options(rec)



engine.stop()