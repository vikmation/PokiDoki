#here i am going to create the gradio

#player one
    #Player Avatars or Icons: Visual representation of each player.
    #Player Names: Display player names.
    #Chip Count: Show the number of chips each player has.
    #Player Status: Indicate if a player is active, folded, all-in, etc.
    #cards --> https://www.gradio.app/docs/gallery --> markdown
#gr.Interface(fn=display, inputs="Image", outputs="Image").launch()
#display(Image(filename='@king.png'))

#player two
#player three
#player four

#next round

#cards table
#https://www.gradio.app/docs/gallery

#small blind and big blind

#pot/bet size

#restart game 

#logging window
    #contains all spoken words of all participants



import gradio as gr
from PIL import Image

def resize_image(image_path, size=(100, 100)):
    image = Image.open(image_path)
    return image.resize(size)

with gr.Blocks() as demo:
    with gr.Row():
        with gr.Row():
            with gr.Column():
                gr.Markdown("# Player 1")
                gr.Markdown("""![Imgur](https://i.imgur.com/y0J34Kk.png)""") 
                gr.Textbox("coins: 2000 status: fold small blind")
            with gr.Column():
                gr.Textbox("coins: 2000 status: fold")
                gr.Markdown("""![Imgur](https://i.imgur.com/cBmgK2I.png)""")
                gr.Markdown("# Player 3")
        with gr.Row():
            gr.Column()
            with gr.Column():
                gr.Markdown("""![Imgur](https://i.imgur.com/cBmgK2I.png)""")
        with gr.Row():
            with gr.Column():
                gr.Markdown("# Player 2")
                gr.Markdown("""![Imgur](https://i.imgur.com/y0J34Kk.png)""") 
                gr.Textbox("coins: 2000 status: fold big blind")
            with gr.Column():
                gr.Textbox("coins: 2000 status: fold")
                gr.Markdown("""![Imgur](https://i.imgur.com/cBmgK2I.png)""")
                gr.Markdown("# Player 4")
        with gr.Column():
                with gr.Row():
                    gr.Button('Round 1')
                with gr.Row():
                    gr.Textbox(lines=35, placeholder='Logs will be displayed here')

demo.launch(server_name="localhost")