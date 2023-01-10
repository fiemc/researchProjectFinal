from guizero import App, PushButton, Text

def do_nothing():
    global num
    print("Button was pressed")
    app.bg = "hot pink"
    app.text_size = 12
    message.value = "You clicked"
    message.value += num
app = App()
button = PushButton(app, command=do_nothing)
message = Text(app, text="^ press it ^")
app.display()

