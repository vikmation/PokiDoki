#here i am going to create the gradio

#player one
    #Player Avatars or Icons: Visual representation of each player.
    #Player Names: Display player names.
    #Chip Count: Show the number of chips each player has.
    #Player Status: Indicate if a player is active, folded, all-in, etc.
    #cards --> https://www.gradio.app/docs/gallery --> markdown

import gradio as gr

def welcome(name):
    return f"Welcome to Gradio, {name}!"

with gr.Blocks() as demo:
    gr.Markdown(
    """
    # Hello World!
    Start typing below to see the output.
    <p float="left">
      <img src="https://picsum.photos/200/300" width="100" height="150" />
      <img src="https://picsum.photos/200/300" width="100" height="150" /> 
    </p>
    """)
    inp = gr.Textbox(placeholder="What is your name?")
    out = gr.Textbox()
    inp.change(welcome, inp, out)

if __name__ == "__main__":
    demo.launch()




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


