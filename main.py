import gradio as gr

def greet(name, intensity):
    return "Hallo Guten Tag " + name + "!" * int(intensity)

demonstration = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
)

demonstration.launch()