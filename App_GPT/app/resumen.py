class ResumeTexto:

    model_openai = "gpt-3.5-turbo"

    def __init__(self, api_key):
        self.api_key = api_key

    def resumen (self, texto, idioma):
        from openai import OpenAI
        client = OpenAI(api_key = self.api_key)

        response = client.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages = [
                {"role":"system","content":"Eres un generador de resumenes de textos"},
                {"role":"user","content":"Instrucción: Resumir el siguiente texto: "+ texto +" utilizando el idioma: "+ idioma}
            ]       
        )
        respuesta = response.choices[0].message.content
        client.close()
        print(idioma)
        return respuesta