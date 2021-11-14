# Asistente de Voz
Este asistente de voz creado con Python para dar información sobre el cuerpo humano, algunas afecciones y enfermedades. Para que el asistente responda debes pronunciar el nombre del asistente que por defecto es "alexa".
## Instalación
Este asistente virtual requiere de algunas dependecias para funcionar:
Para reconocimiento de voz
```
pip install SpeechRecognition
pip install PyAdudio
```
Si tienes problemas instalando PyAudio por favor ve a este [link](https://stackoverflow.com/questions/61290821/error-command-errored-out-with-exit-status-1-while-installing-pyaudio)

Para sintetizar voz a partir de texto
```
pip install pyttsx3
```

## Uso
- Para que el asistente detecte tus preguntas debes pronunciar su nombre ("**alexa**") en alguna parte de la oración.
- Para apagar el asistente virtual debes pronunciar la palabra "**apagate**" 

### Preguntas de Nivel 1
|Usuario| Asistente|
|--|--|
|¿Cuántos huesos tiene el cuerpo humano?|El cuerpo humano adulto tiene nada menos que 206 huesos|
|¿Cuántos dientes tiene una persona adulta?|32 piezas dentales es la cantidad normal para un adulto|
|¿Cuál es el porcentaje de agua en el cuerpo humano?|El cuerpo humano está compuesto en un 60 por ciento de agua, el cerebro se compone en un 70 por ciento de agua, la sangre en un 80 por ciento y los pulmones se componen en un 90 por ciento de agua.|
|¿Cuántos músculos tenemos?|El cuerpo humano contiene aproximadamente 650 músculos estriados.|
|¿Cuántos órganos tiene el cuerpo humano?|El cuerpo humano tiene 21 órganos|
### Preguntas de Nivel 2
Este grupo de preguntas esta enfocado en afecciones y enfermedades comunes
#### Acné
|Usuario|Asistente|
|--|--|
|¿Qué es el acné?|El acne es una enfermedad cutánea que suele aparecer a partir de los 12 años de edad, sobre todo en la cara, y que, si no hay complicaciones graves, solo se desarrolla durante la pubertad y desaparece hacia los 18 o 20 años.|
|¿Cómo prevenir el acné?|Lávate la cara dos veces al día (no más) con agua tibia y un jabón suave fabricado específicamente para personas con acné. Masajéate suavemente la cara describiendo movimientos circulares. No te frotes la cara.|
#### Menopausia
|Usuario|Asistente|
|--|--|
|¿Qué es la menopausia?|Es un proceso biológico natural que marca el final de los ciclos menstruales. Se diagnostica después de que transcurren doce meses sin que tengas un período menstrual.|
|¿A qué edad se da la menopausia?|La menopausia puede producirse entre los 40 y 50 años, pero la edad promedio es a los 51 años.|
#### Piojos
|Usuario|Asistente|
|--|--|
|¿Qué son los piojos?|Los piojos son pequeños insectos que viven en la cabeza de las personas. Los piojos adultos tienen el tamaño de las semillas de sésamo. Los huevos, llamados liendres, son incluso más pequeños, aproximadamente del tamaño de una escama de caspa.|
|¿Cómo se contagian los piojos?|Los piojos se mueven arrastrándose, porque no pueden saltar ni volar. Se contagian a través del contacto cercano de persona a persona. En raras ocasiones, se pueden contagiar al compartir objetos personales como sombreros o cepillos para el cabello. La higiene personal y la limpieza no se relacionan con tener piojos.|
#### Varicela
|Usuario|Asistente|
|--|--|
|¿Qué es la varicela?|La varicela es una infección causada por el virus de la varicela-zóster. Causa una erupción en la piel con picazón y pequeñas ampollas con líquido. La varicela es muy contagiosa para personas que no han tenido la enfermedad antes o no se han vacunado.|
|¿Qué pasa si a un adulto se contagia Varicela?|Puede causar: deshidratación, neumonía, problemas de sangrado, infección o inflamación cerebral, infecciones bacterianas de la piel, infecciones del torrente sanguíneo (septicemia), síndrome de shock tóxico, infecciones de los huesos, infecciones de las articulaciones, o la muerte.|
#### Aparato Digestivo
|Usuario|Asistente|
|--|--|
|¿Que es el aparato digestivo?|Conjunto de órganos que procesan los alimentos y los líquidos para descomponerlos en sustancias que el cuerpo usa como fuente de energía, o para el crecimiento y la reparación de tejidos.|
|¿Cómo se conforma el aparato digestivo?|El aparato digestivo está formado por el tracto gastrointestinal, también llamado tracto digestivo, y el hígado, el páncreas y la vesícula biliar.|
### Preguntas de Nivel 3
Grupo de preguntas enfocadas en enfermedades
#### Enfermedades Cardiovasculares
|Usuario|Asistente|
|--|--|
|¿Qué son enfermedades cardiovasculares?|Las enfermedades cardiovasculares (ECV) son un grupo de desórdenes del corazón y de los vasos sanguíneos.|
|¿Cuáles son los síntomas comunes de las enfermedades cardiovasculares?|Molestias en el pecho, molestias en los brazos, hombro izquierdo, mandíbula o espalda|
|¿Cuáles son las princípiales factores de riesgo de las enfermedades cardiovasculares?|Las causas más importantes son una dieta malsana, la inactividad física, el consumo de tabaco y el consumo nocivo de alcohol|
#### Enfermedades Cerebrovasculares
|Usuario|Asistente|
|--|--|
¿Qué son las enfermedades cerebrovasculares?|Son isquémicas y ocurren cuando las arterias que llevan sangre al cerebro se hacen angostas o se bloquean, causando una disminución severa o interrupción del flujo sanguíneo, conocida como isquemia.|
|¿Cuales son los síntomas de las enfermedades cerebrovasculares?|Alteración repentina de la visión en un ojo o ambos, Pérdida repentina de la fuerza en un brazo, una pierna o ambos. Sensación de hormigueo en la cara, brazo o pierna. Aparición repentina de: Problemas para hablar y/o entender lo que se escucha, acompañada por balbuceo. Desequilibrio o inestabilidad. Dolor de cabeza.|
|¿Cuáles son los factores de riesgo de las enfermedades cerebrovasculares?|El sexo. Se presenta con mayor frecuencia en hombres que en mujeres. Alcoholismo. Tabaquismo. Inactividad física. Obesidad. Presión arterial alta. Diabetes Mellitus. Niveles de colesterol elevados.|
#### Coronavirus
|Usuario|Asistente|
|--|--|
|¿Qué es el coronavirus?|Los coronavirus son una familia de virus que causan enfermedades (desde el resfriado común hasta enfermedades respiratorias más graves) y circulan entre humanos y animales.|
|¿Cómo se transmite el coronavirus?|Los coronavirus humanos se transmiten de una persona infectada a otras: a través de las gotículas que expulsa un enfermo al toser y estornudar ,al tocar o estrechar la mano de una persona enferma, un objeto o superficie contaminada con el virus y luego llevarse las manos sucias a boca, nariz u ojos.|
|¿Cuándo debo acudir a recibir atención médica?|Una persona debe sospechar de COVID-19 cuando presenta al menos dos de los siguientes síntomas: Tos / Estornudos, Fiebre, Dolor de cabeza.|
#### Sistema Circulatorio
|Usuario|Asistente|
|--|--|
|¿Qué es el sistema circulatorio?|El sistema circulatorio se encarga de bombear, transportar y distribuir la sangre por todo el cuerpo. |
|¿Cómo esta integrado el sistema circulatorio?|Se integra con el corazón y los vasos sanguíneos: arterias, venas y capilares.|
|¿Qué es el corazón?|Es una bomba muscular y se considera el centro del sistema circulatorio.|
#### Cancer
|Usuario|Asistente|
|--|--|
|¿Qué es el Cáncer?|El cáncer puede desarrollarse en cualquier parte del cuerpo. Se origina cuando las células crecen sin control y sobrepasan en número a las células normales. Esto hace que al cuerpo le resulte difícil funcionar de la manera que debería hacerlo|
|¿Cuál es el tratamiento para el cancer?|La mayoría de las personas reciben una combinación de tratamientos, como cirugía con quimioterapia o radioterapia.|
|¿Qué es Quimioterapia?|Tratamiento con medicamentos para interrumpir la formación de células cancerosas, ya sea mediante su destrucción o al impedir su multiplicación. La quimioterapia se administra por la boca, en inyección, por infusión o sobre la piel, según el tipo de cáncer y el estadio en que este se encuentra. Se administra sola o con otros tratamientos como cirugía, radioterapia o terapia biológica.|
# Autores
- Lilia Montserrat Fuentes Navarrete
- Rosa Jazmin Portillo Sanchez
- Luis Vazquez Padilla
