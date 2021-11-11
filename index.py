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
from assistant import Assistant
from question import oneAnswerQuestions, twoAnswerQuestions, threeAnswerQuestions 

alexa = Assistant('alexa',oneAnswerQuestions,twoAnswerQuestions, threeAnswerQuestions)
alexa.run()
