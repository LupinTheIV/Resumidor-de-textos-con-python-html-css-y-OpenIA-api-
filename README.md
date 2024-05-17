# Resumidor-de-textos-con-python-html-css-y-OpenIA-api-
Creado por: 
* Santiago Montenegro Woodcock
* Ian F. Blanco Llanos
  
En este repositorio está el código para una aplicación web que usa la API de OpenAI con la versión de Chat-GPT 3.5 para resumir textos utilizado un idioma indicado por el usuario.

# ¿Cómo se usa?
Esta aplicación web se creo utilizando Visual Studio Code en español, por lo cual los pasos serán de acuerdo a lo anterior.
# Aclaraciones previas
* Es necesario tener una cuenta en OpenAI y tener minimo 5 dolares para poder correr la aplicación (si no tenias una cuenta al crearla te dan 5 dolares de prueba)
* Es necesario crear una api key; esto lo podras hacer en la sección API Keys de la página OpenAI Platform con tu cuenta

# Pasos
1. Descarga / git clone
2. Abrimos Visual Studio Code
3. Creamos un archivo llamado .env por fuera de las carpetas eh ingresamos OPENAI_API_KEY = "Aquí pegas tu api key"
4. Iniciamos la consola con el comando Ctrl + ñ
5. Descargamos los requerimientos ingresando en la consola: pip install -r requirements.txt
6. Iniciamos el entorno ingresando en la consola: .\venv\Scripts\activate
7. Corremos la el comando ingresando en la consola: python .\app\__init__.py
8. Al correr te proporcionara una dirección local similar a esta http://127.0.0.1:5000, deberas acceder a esta mediante tu navegador (preferiblemente Google Chrom)

# Posibles errores
* Si no en el paso 4 no se crea la carpeta venv, ingresa en la consola: python -m venv .venv


