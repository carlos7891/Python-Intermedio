##Entornos Virtuales 

#####**Comando para crear entorno virutal:**
    py -m venv venv

#####**Activar entorno virtual:**
    .\venv\Scripts\activate

#####**Desactivar entorno virtual:**
    deactivate

#####**Acortador de comandos:**
    alias avenv=.\venv\Scripts\activate
    avenv => para activar

##Gestionar dependecias con pip

#####**Ver dependencias instaladas:**
    pip freeze

#####**Instalar dependencias:**
    pip install pandas

#####**Guardar dependencias para compartir:**
    pip freeze > requirements.txt

#####**Instalar dependencias compartidas:**
    pip install -r requirements.txt
