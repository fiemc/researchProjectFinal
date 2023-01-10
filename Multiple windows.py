from guizero import App, Window, PushButton, Text, TextBox, Box, ButtonGroup

name_box = None
info = []

def open_window():
    win_info = Window(app, title="Info")
    win_info.show(wait=True)
    app.bg ="light yellow"
    app.text_size = 13
    Text(win_info, text="A little bit about each candidate ")
    can_1 = Box(win_info ,height=70, width=650, border=True)
    Text(can_1, text=info[0], align="top")
    Text(can_1, text=info[1], align="top")
    Text(can_1, text=info[2], align="top")
    can_2 = Box(win_info ,height=70, width=650, border=True)
    Text(can_2, text=info[3], align="top")
    Text(can_2, text=info[4], align="top")
    Text(can_2, text=info[5], align="top")
    can_3 = Box(win_info ,height=70, width=650, border=True)
    Text(can_3, text=info[6], align="top")
    Text(can_3, text=info[7], align="top")
    Text(can_3, text=info[8], align="top")
def open_the_vote_window():
    win_vote = Window(app, title="The vote")
    win_vote.show(wait=True)
    app.bg = "light pink"
    app.text_size = 13
    Text(win_vote, text="Pick your president")
    names = []

    def save_vote():
         info.append(choice)
    for i in range(0,len(info),3):
        names.append(info[i])
    choice = ButtonGroup(win_vote, options=names)
    button = PushButton(win_vote, command=save_vote, text="Submit", align="top")







def insert_a_candidate():
    global name_box
    global facts_box
    global year_box
    def save():
        info.append(name_box.value)
        info.append(facts_box.value)
        info.append(year_box.value)
        print(info)
    win_candidate = Window(app,title="Nominate yourself")
    win_candidate.show(wait=True)
    app.bg ="light blue"
    app.text_size = 13
    Text(win_candidate, text="Want to become a candidate?")
    name = Text(win_candidate, text="Enter you're name", align="top")
    name_box = TextBox(win_candidate, text="Name", align="top")
    facts = Text(win_candidate, text="Enter your quick facts", align="top")
    facts_box = TextBox(win_candidate, text="Facts", align="top")
    year = Text(win_candidate, text="Your class", align="top")
    year_box = TextBox(win_candidate, text="Year", align="top")
    button = PushButton(win_candidate, command=save, text="Submit", align="top")
    app.display()


app = App(title="Main window")
text = Text(app, text="Welcome to the 2023 class president vote")
open_button = PushButton(app, text="Info", command=open_window)
open_button = PushButton(app, text="Vote", command=open_the_vote_window)
open_button = PushButton(app, text="Nominate yourself", command=insert_a_candidate)
app.display()

