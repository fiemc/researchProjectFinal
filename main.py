from guizero import App, Text, CheckBox

app = App(title="Hello world", width=1000, height=400, bg="red")
message = Text(app, text="Welcome to my application", size=30, font="Arial")
question = Text(app, text="Is the weather nice today?")
app.error("HELP ME", "This is a test")
glitter = CheckBox(app, text="Add glitter")

app.display()

