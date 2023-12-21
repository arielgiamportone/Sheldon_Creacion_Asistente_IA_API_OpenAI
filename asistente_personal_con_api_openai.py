
import openai
import gradio as gr

# acceder con tu clave de openAI (puedes comprar tokens)
openai.api_key = ""

def ai_tool(prompt, behavior):
    # definimos comportamiento y formato prompt
    messages = [
        {"role": "system", "content": f"Eres un asistente experto en {behavior}"},
        {"role": "user", "content": prompt},
    ]
    
    # configuramos el asistente
    chat_response = openai.chat.completions.create(
        model="gpt-4",   # cambiamos el modelo del motor de AI
        messages=messages,
        temperature=0.6,
        max_tokens=1000,
        frequency_penalty=0.0
    )
    
    # Extracting chat message
    chat_message = chat_response.choices[0].message
    
    return chat_message

# Definimos los inputs para los usuarios
inputs = [
    gr.Textbox(label="Comportamiento", placeholder="¿Cómo quieres que actúe el asistente...?"),
    gr.Textbox(lines=7, label="Entrada", placeholder="¿Qué quieres preguntarle al asistente?")
]

# definimos la salida
outputs = gr.Textbox(label="Respuesta del Chat")

# Titulo de nuestro asistente
title = "Sheldon"

iface = gr.Interface(
    fn=ai_tool, 
    inputs=inputs, 
    outputs=outputs, 
    title=title, 
    theme = "Soft",
    description="Este es un prototipo de asistente personal"
)

iface.launch(share=True)