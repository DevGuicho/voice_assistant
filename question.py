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

class Question():
  def __init__(self,answer, claves):
      self.answer = answer
      self.claves = claves
      self.rating = 0

  def checkSentence(self, sentence):
    se = sentence.split()
    i = 0
    for word in se:
      if word in self.claves:
        i=i+1
    if i ==len(self.claves):
      return True
    return False



oneAnswerQuestions = [
  Question('El cuerpo humano adulto tiene nada menos que 206 huesos',['cuántos', 'huesos', 'humano']),
  Question('32 piezas dentales es la cantidad normal para un adulto',['cuántos','dientes','persona']),
  Question('El cuerpo humano está compuesto en un 60 por ciento de agua, el cerebro se compone en un 70 por ciento de agua, la sangre en un 80 por ciento y los pulmones se componen en un 90 por ciento de agua.',['porcentaje','agua','humano']),
  Question('El cuerpo humano contiene aproximadamente 650 músculos estriados.',['cuántos','músculos','tenemos']),
  Question('El cuerpo humano tiene 21 órganos',['cuántos','órganos','humano'])
]

twoAnswerQuestions = [
  Question('El acne es una enfermedad cutánea que suele aparecer a partir de los 12 años de edad, sobre todo en la cara, y que, si no hay complicaciones graves, solo se desarrolla durante la pubertad y desaparece hacia los 18 o 20 años.',['qué','acné']),
  Question('Lávate la cara dos veces al día (no más) con agua tibia y un jabón suave fabricado específicamente para personas con acné. Masajéate suavemente la cara describiendo movimientos circulares. No te frotes la cara.',['prevenir', 'acné']),
  Question('Es un proceso biológico natural que marca el final de los ciclos menstruales. Se diagnostica después de que transcurren doce meses sin que tengas un período menstrual.',['qué','es','menopausia']),
  Question('La menopausia puede producirse entre los 40 y 50 años, pero la edad promedio es a los 51 años.',['edad', 'da','menopausia']),
  Question('Los piojos son pequeños insectos que viven en la cabeza de las personas. Los piojos adultos tienen el tamaño de las semillas de sésamo. Los huevos, llamados liendres, son incluso más pequeños, aproximadamente del tamaño de una escama de caspa.',['qué', 'piojos']),
  Question('Los piojos se mueven arrastrándose, porque no pueden saltar ni volar. Se contagian a través del contacto cercano de persona a persona. En raras ocasiones, se pueden contagiar al compartir objetos personales como sombreros o cepillos para el cabello. La higiene personal y la limpieza no se relacionan con tener piojos.',['cómo','contagian','piojos']),
  Question('La varicela es una infección causada por el virus de la varicela-zóster. Causa una erupción en la piel con picazón y pequeñas ampollas con líquido. La varicela es muy contagiosa para personas que no han tenido la enfermedad antes o no se han vacunado.',['qué', 'es','varicela']),
  Question('Puede causar: deshidratación, neumonía, problemas de sangrado, infección o inflamación cerebral, infecciones bacterianas de la piel, infecciones del torrente sanguíneo (septicemia), síndrome de shock tóxico, infecciones de los huesos, infecciones de las articulaciones, o la muerte.',['qué','pasa','adulto','varicela', 'contagia']),
  Question('Conjunto de órganos que procesan los alimentos y los líquidos para descomponerlos en sustancias que el cuerpo usa como fuente de energía, o para el crecimiento y la reparación de tejidos.',['qué','es','aparato','digestivo']),
  Question('El aparato digestivo está formado por el tracto gastrointestinal, también llamado tracto digestivo, y el hígado, el páncreas y la vesícula biliar.',['cómo','se','conforma','aparato', 'digestivo'])
]

threeAnswerQuestions = [
  Question('Las enfermedades cardiovasculares (ECV) son un grupo de desórdenes del corazón y de los vasos sanguíneos.',['qué','son','enfermedades','cardiovasculares']),
  Question('Molestias en el pecho, molestias en los brazos, hombro izquierdo, mandíbula o espalda',['síntomas', 'comunes','enfermedades','cardiovasculares']),
  Question('Las causas más importantes son una dieta malsana, la inactividad física, el consumo de tabaco y el consumo nocivo de alcohol',['factores', 'riesgo', 'enfermedades', 'cardiovasculares']),
  Question('Son isquémicas y ocurren cuando las arterias que llevan sangre al cerebro se hacen angostas o se bloquean, causando una disminución severa o interrupción del flujo sanguíneo, conocida como isquemia.',['qué', 'son', 'enfermedades', 'cerebrovasculares']),
  Question('Alteración repentina de la visión en un ojo o ambos, Pérdida repentina de la fuerza en un brazo, una pierna o ambos. Sensación de hormigueo en la cara, brazo o pierna. Aparición repentina de: Problemas para hablar y/o entender lo que se escucha, acompañada por balbuceo. Desequilibrio o inestabilidad. Dolor de cabeza.',['cuáles', 'síntomas', 'enfermedades', 'cerebrovasculares']),
  Question('El sexo pues se presenta con mayor frecuencia en hombres que en mujeres. Alcoholismo. Tabaquismo. Inactividad física. Obesidad. Presión arterial alta. Diabetes Mellitus. Niveles de colesterol elevados.',['factores', 'riesgo', 'enfermedades', 'cerebrovasculares']),
  Question('Los coronavirus son una familia de virus que causan enfermedades (desde el resfriado común hasta enfermedades respiratorias más graves) y circulan entre humanos y animales.',['qué','coronavirus']),
  Question('Los coronavirus humanos se transmiten de una persona infectada a otras: a través de las gotículas que expulsa un enfermo al toser y estornudar ,al tocar o estrechar la mano de una persona enferma, un objeto o superficie contaminada con el virus y luego llevarse las manos sucias a boca, nariz u ojos.',['cómo', 'transmite', 'coronavirus']),
  Question('Una persona debe sospechar de COVID-19 cuando presenta al menos dos de los siguientes síntomas: Tos / Estornudos, Fiebre, Dolor de cabeza.',['cuándo','acudir', 'atención', 'médica']),
  Question('El sistema circulatorio se encarga de bombear, transportar y distribuir la sangre por todo el cuerpo.',['qué','sistema','circulatorio']),
  Question('Se integra con el corazón y los vasos sanguíneos: arterias, venas y capilares.',['cómo', 'esta', 'integrado','sistema','circulatorio']),
  Question('Es una bomba muscular y se considera el centro del sistema circulatorio.',['qué','es','corazón']),
  Question('El cáncer puede desarrollarse en cualquier parte del cuerpo. Se origina cuando las células crecen sin control y sobrepasan en número a las células normales. Esto hace que al cuerpo le resulte difícil funcionar de la manera que debería hacerlo',['qué', 'es', 'cáncer']),
  Question('La mayoría de las personas reciben una combinación de tratamientos, como cirugía con quimioterapia o radioterapia.',['cuál', 'tratamiento', 'cáncer']),
  Question('Tratamiento con medicamentos para interrumpir la formación de células cancerosas, ya sea mediante su destrucción o al impedir su multiplicación. La quimioterapia se administra por la boca, en inyección, por infusión o sobre la piel, según el tipo de cáncer y el estado en que este se encuentra. Se administra sola o con otros tratamientos como cirugía, radioterapia o terapia biológica.',['qué', 'quimioterapia'])
]