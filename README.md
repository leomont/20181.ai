# Inteligencia Artificial I 2018-1

_Regístrate [aquí](https://goo.gl/forms/yHRFSYVXfCUlDpyY2)_. Algunos vídeos de clases en ediciones anteriores del curso están [disponibles en YouTube](https://www.youtube.com/watch?v=ZxJBwkDqB9E&list=PL8ytk70JVz1_SdCzC3c7rlPoEotq79DjL)

## Máquina Virtual

Usaremos esta máquina virtual que tiene instalado un entorno Python Anaconda con Jupyter Notebooks disponibles en  [localhost:8008/tree](http://localhost:8008/tree) una vez que la máquina arranca.

**Observa la configuración de la máquina**

- Si tu máquina física tiene al menos 4GB de memoria configura la máquina virtual **con 2GB de memoria**
- Aunque casi no necesitarás un terminal, el interfaz de Jupyter Notebooks tiene un terminal para acceder a través del navegador. En cualquier caso, la máquina virtual tiene un servidor SSH en el puerto 2222 con user/user como usuario y pwd. Si tu máquina física es mac o linux usa `ssh -p 2222 user@localhost` para conectarte. Si es windows, usa [putty](https://www.putty.org/)
- Si compartes una carpeta entre la física y virtual asegúrate que **el nombre cone el que se comparte** sea `share` (aunque el nombre de la carpeta en la máquina física puede ser distinto)

**Para montar la carpeta compartida** ejecuta lo siguiente en un terminal y la carpeta aparecerá en /home/user/share:

    sudo mount share

**Si la máquina arranca en modo mantenimiento**, edita el fichero `/etc/fstab` como `root`:

    sudo nano /etc/fstab
    
y actualiza la linea con la definición de `share` para que quede así

    share                                     /home/user/share vboxsf uid=1000,rw,auto,x-systemd.automount 0 1



## Calificación
40% Problemsets<br/>
30% Quizes<br/>
30% Online courses (MOOC)

## Online Courses (MOOC)
Habrás de realizar algún MOOC online que habrá de tratar un tecnológica y ha de cubrir aproximadamente 15 horas de esfuerzo, que se evaluarán según la definición y dinámica de cada caso. Puedes hacerlo en cualquier plataforma existente, como por ejemplo: [Coursera](www.coursera.org), [EDX](www.edx.org), [Udacity](www.udacity.org),  [MiriadaX](https://miriadax.net/), etc.

Tendrs que hacer un informe de tu seguimiento del MOOC. La entrega ha de constar de:

- Un archivo PDF llamado MOOC_descripcion.pdf donde se describa el MOOC (primera entrega)
- Un archivo PDF llamado MOOC_completado.pdf donde se incluya la evidencia de la realizacin del MOOC
- Un directorio llamado MOOC_materiales donde se incluyan los materiales pertinentes (scripts, datos, etc.) que apoyen la evidencia mostrada en el archivo PDF.

**TODA ENTREGA QUE NO CUMPLA CON ESTAS CONVENCIONES SERÁ CONSIDERADA COMO NO REALIZADA**

La calificación del curso vendrá dada por los siguientes criterios con el mismo peso cada uno:

- COMPLEJIDAD DEL MOOC
- COMPLECIÓN 
- CLARIDAD DEL REPORTE

## Calendario y plazos

                       SESSION 1     SESSION 2     STUDENT DEADLINES

    W05 Ene29-Feb02    1.PYTHON      2.PANDAS
    W06 Feb05-Feb09    PSETS         PSETS
    W07 Feb12-Feb16    3.STATS       4.BAYES       
    W08 Feb19-Feb23    PSETS         PSETS         Feb 25 PSETS 1 2
    W09 Feb26-Mar02    QUIZPREP      QUIZ          Mar 04 MOOC DATASET
    W10 Mar05-Mar09    5.ML INTRO    6.ML METHODS
    W11 Mar12-Mar16    7.NAIVE       PSETS
    W12 Mar19-Mar23    PROJECT       PROJECT
    W13 Mar26-Mar30    8.IMGINTRO    9.IMGCLASS    
    W14 Abr02-Abr06    PSETS         PSETS         Abr 01 PSETS 3 4 5 
    W15 Abr09-Abr13    QUIZPREP      QUIZ   
    W16 Abr16-Abr20    10.PLAN       PSETS
    W17 Abr23-Abr27    11.GA         PSETS
    W18 Abr30-May04    12.SA         PSETS         MAY 06 PSETS 7 8 9
    W19 May07-May11    QUIZPREP      QUIZ
    W20 May14-May18    PROJECT       PROJECT
    W21 May21-May25    SEMINAR       SEMINAR       MAY 27 MOOC FINAL


    Mar09 - Registro primera calificación
    Mar11 - Último día cancelación materias
    May28-Jun06 Evaluaciones finales
    Jun08 - Registro calificaciones finales



**CUALQUIER ENTREGA FUERA DE PLAZO SERÁ PENALIZADA CON UN 50%**
    
[Calendario academico](https://www.uis.edu.co/webUIS/es/academia/calendariosAcademicos/2017/acAcad014-2017.pdf)

