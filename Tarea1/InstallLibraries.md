# Instalacion de Librerias
Para la instalacion de la librerias se hara lo siguiente:

    -Crear un espacio virtual en caso de que no se tenga uno usando el siguiente comando:
        - $virtualenv nombre_env
        - $python -m venv nombre_env

    -Dirigirse a la carpeta donde se encuetran el espacio virtual y realizar su activacion. 
        - WIN: $nombre_env\Scripts\activate
        - MAC: $source nombre_env/bin/activate

    -  Una vez en el enviroment, usar el comando para instalar librerias: 
        - $pip install -r requirements.txt