from guizero import App, Window, PushButton, Text, ButtonGroup, Box

def open_window():
    final_choice = choice.value
    window.show()

def close_window():
    window.hide()

def output_value():
    print(choice.value)

app = App(title="Class president YR13 vote")

window = Window(app, title="The candidates")
text = Text(window, "The Candidates", command=two)

window.hide()

question = Text(app, text="What class are you in?")
choice = ButtonGroup(app, options=["13GI", "13HM", "13KS", "13TP"], selected="13GI", command=output_value)


open_button = PushButton(app, text="Next", command=open_window)
close_button = PushButton(window, text="Close", command=close_window)



app.display()

