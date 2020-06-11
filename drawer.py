from tkinter import *

canvasWidth = 800
canvasHeight = 500

paperColor = "white"
paperStyle = "plain"

marginColor = "black"

activeTool = "pen"

toPlace = "rb" # Variable to place on click

rbx = 0  # Rule begin x coord
rex = 0 # Rule end x coord
rby = 0 # Rule begin y coord
rey = 0 # Rule end y coord
cex = 0 # Circle center x
ccy = 0 # circle center y
cey = 0 # circle top edge y
rvx1 = 0 # rectange vortex 1 coords
rvy1 = 0
rvx2 = 0 #rectangle vortex 2 coords
rvy2 = 0
ovx1 = 0 # Oval vortex 1 coords
ovy1 = 0
ovx2 = 0 # Oval vortex 2 coords
ovy2 = 0
tx = 0 # Text coords
ty = 0
 # Text to place with text tool

marginColors = {
    "Black": "black",
    "Blue": "#009CFF",
    "Red": "#FF0048"
}

def SetTool_Pen():
    global activeTool
    activeTool = "pen"
    paintArea.config(cursor = "pencil")

def setTool_Rule():
    global activeTool, rbx, rby, rex, rey, toPlace
    activeTool = "rule"
    toPlace = "rb"
    paintArea.config(cursor = "crosshair")

def setTool_Circle():
    global activeTool, ccx, ccy, cey, toPlace
    activeTool = "circle"
    toPlace = "circleCenter"
    paintArea.config(cursor = "crosshair")

def setTool_Rect():
    global activeTool, toPlace
    activeTool = "rect"
    toPlace = "vortex1"
    paintArea.config(cursor = "crosshair")

def setTool_Oval():
    global activeTool, toPlace
    activeTool = "oval"
    toPlace = "vortex1"
    paintArea.config(cursor = "crosshair")

def setTool_Text():
    global activeTool
    activeTool = "text"
    paintArea.config(cursor = "crosshair")

def onClick(event):
    global toPlace, rbx, rby, rex, rey, ccx, ccy, cvx, cvy, rvx1, rvx2, rvy1, rvy2, ovx1, ovx2, ovy1, ovy2, tx, ty
    if activeTool == "rule":
        if toPlace == "rb":
            rbx = event.x
            rby = event.y
            toPlace = "re" # Specifies the next thing to place: the rule end.
        else:
            rex = event.x
            rey = event.y
            paintArea.create_line(rbx, rby, rex, rey, fill = inkColor, width = brushSize.get() * 2, tags = ("ink"))
            toPlace = "rb"
    elif activeTool == "circle":
        if toPlace == "circleCenter":
            ccx = event.x
            ccy = event.y
            toPlace = "circleEdge"
        else:
            cey = event.y
            cex = ccx - (ccy - cey)
            cex2 = ccx + (ccx - cex) # bottom left vortex coords
            cey2 = ccy + (ccy - cey)
            paintArea.create_oval(cex, cey, cex2, cey2, outline = inkColor, width = brushSize.get() * 2, tags = ("ink"))
            toPlace = "circleCenter"
    elif activeTool == "rect":
        if toPlace == "vortex1":
            rvx1 = event.x
            rvy1 = event.y
            toPlace = "vortex2"
        else:
            rvx2 = event.x
            rvy2 = event.y
            paintArea.create_rectangle(rvx1, rvy1, rvx2, rvy2, outline = inkColor, width = brushSize.get() * 2, tags = ("ink"))
            toPlace = "vortex1"
    elif activeTool == "oval":
        if toPlace == "vortex1":
            ovx1 = event.x
            ovy1 = event.y
            toPlace = "vortex2"
        else :
            ovx2 = event.x
            ovy2 = event.y
            paintArea.create_oval(ovx1, ovy1, ovx2, ovy2, outline = inkColor, width = brushSize.get() * 2, tags = ("ink"))
            toPlace = "vortex1"
    elif activeTool == "text":
        tx = event.x
        ty = event.y


        def placeText():
            global textToPlace
            paintArea.create_text(tx, ty, text = textToPlace.get(), font = ("Arial", textFontSize.get()), fill = inkColor, tags = ("ink"))
            textWindow.destroy()

        textWindow = Toplevel(mainWindow)
        textWindow.geometry("200x100+" + str(tx) + "+" + str(ty))
        textWindow.title("Insert text")
        textEntry = Entry(textWindow, textvariable = textToPlace)
        textPlaceBttn = Button(textWindow, text = "Enter", bg = "green", fg = "white", relief = "raised", command = placeText)
        textEntry.focus_set()
        fontSizeScale = Scale(textWindow, label = "Font size", variable = textFontSize, from_ = 5, to = 50, resolution = 1, tickinterval = 5, orient = "horizontal", length = 200)
        fontSizeScale.set(20)

        textEntry.pack()
        fontSizeScale.pack()
        textPlaceBttn.pack()

#set the horizontal rules for both ruled and grid styles
def setHorizontalRuling(spacing):
    for y in range(0, 800, spacing):
        paintArea.create_line(0, y, 3000, y, fill = "black", tags = ("paper"))

#set the vertical ruling for grid
def setVerticalRuling(spacing):
    for x in range(0, 1000, spacing):
        paintArea.create_line(x, 0, x, 1000, fill = "black", tags = ("paper"))

mainWindow = Tk()
mainWindow.title("Drawer")
inkColor = "#020044"
hasLeftMargin = IntVar()
hasRightMargin = IntVar()

sheetSpacingLg = IntVar()
sheetSpacingSm = IntVar()

leftMargin = IntVar()
rightMargin = IntVar()
ruleSpacing = IntVar()
verticalSpacing = IntVar()
squareGrid = IntVar()

practiceRuleSpacing = IntVar()

marginColorInput = StringVar()

brushSize = DoubleVar()

textToPlace = StringVar()
textFontSize = StringVar()


def paint(event):
    x1, y1 = (event.x - brushSize.get()), (event.y - brushSize.get())
    x2, y2 = (event.x + brushSize.get()), (event.y +brushSize.get())
    paintArea.create_oval(x1, y1, x2, y2, fill = inkColor, outline = "", tags = ("ink"))

def clear():
    paintArea.delete("ink")

def setMargins():
    global marginColor, marginColorInput
    if marginColorInput.get() in marginColors:
        marginColor = marginColors[marginColorInput.get()]
    mainWindow.update()
    canvasWidth = mainWindow.winfo_width()
    if hasLeftMargin.get():
        paintArea.create_line(leftMargin.get(), 0, leftMargin.get(), 1000, fill = marginColor, width = 3, tags = ("paper"))
    if hasRightMargin.get():
        paintArea.create_line(canvasWidth - rightMargin.get(), 0, canvasWidth - rightMargin.get(), 1000, fill = marginColor, width = 3, tags = ("paper"))

def openCredits():
    creditsWindow = Toplevel(mainWindow)
    creditsWindow.title("Credits and license")
    creditsText = Label(creditsWindow, text = "Drawer (formerly Calligraphic Paint) is an application created in 2020 by Redline Software, a Redline Network company. \n Open source software freely usable for any non-commercial purposes.")
    creditsText.pack()

def openHelp():
    helpWindow = Toplevel(mainWindow)
    helpText = Label(helpWindow, text = "How to use tools\n\nPen\nHold mouse button while dragging mouse.\n\nRule\nClick the endpoints of the desired straight line.\n\nCircle\nClick the center and highest/lowest y coordinate of the circle.\n\nRectangle and Oval\nClick the top left and bottom right corners of the desired rectangle/rectangle containing the oval.\n\nText\nClick where you want to put the text. In the appearing window, write the text then click \"Enter\" on the screen.")
    helpText.pack()

def setColorBlue():
    global inkColor
    inkColor = "#020044"
def setColorBlack():
    global inkColor
    inkColor = "#000000"
def setColorLtBlue():
    global inkColor
    inkColor = "#00BBC3"
def setColorPurple():
    global inkColor
    inkColor = "#35005C"
def setColorRed():
    global inkColor
    inkColor = "#E60000"
def setColorGreen():
    global inkColor
    inkColor = "#003611"
def setColorOrange():
    global inkColor
    inkColor = "#FF9300"



def setPaperWhite():
    global paperColor
    paperColor = "white"
    paintArea.config(bg = paperColor)

def setPaperAntique():
    global paperColor
    paperColor = "#ffda85"
    paintArea.config(bg = paperColor)
def setPaperGray():
    global paperColor
    paperColor = "#c7c7c7"
    paintArea.config(bg = paperColor)


def stylePlain():
    global paperStyle, hasRightMargin, hasLeftMargin, leftMargin, rightMargin

    def setPlainStyle():
        global paperStyle, marginColor
        marginColor = marginColors[marginColorInput.get()]
        paintArea.delete("paper")
        setMargins()
        paperStyle = "plain"


    #define the plain style dialog


    plainStyleDialog = Toplevel(mainWindow)
    plainStyleDialog.title("Paper style options")

    leftMarginCB = Checkbutton(plainStyleDialog, text = "Left Margin", variable = hasLeftMargin)
    rightMarginCB = Checkbutton(plainStyleDialog, text = "Right Margin", variable = hasRightMargin)

    leftMarginScale = Scale(plainStyleDialog, label = "Set left margin", from_ = 10, to = 50, resolution = 1, tickinterval = 10, orient = "horizontal", variable = leftMargin, length = 150)
    rightMarginScale = Scale(plainStyleDialog, label = "Set right margin", from_ = 10, to = 50, resolution = 1, tickinterval = 10, orient = "horizontal", variable =rightMargin, length = 150)
    marginColorSelector = OptionMenu(plainStyleDialog, marginColorInput, "Black", "Blue", "Red")
    marginColorLabel = Label(plainStyleDialog, text = "Margin color")
    leftMarginScale.set(20)
    rightMarginScale.set(20)
    leftMarginCB.pack()
    leftMarginScale.pack()
    rightMarginCB.pack()
    rightMarginScale.pack()
    marginColorLabel.pack()
    marginColorSelector.pack()

    cancelButton = Button(plainStyleDialog, text = "Cancel", command =plainStyleDialog.destroy)
    applyButton = Button(plainStyleDialog, text = "Apply", relief = "raised", bg = "green", command = setPlainStyle)



    applyButton.pack()
    cancelButton.pack()


def styleRuled():
    global paperStyle, hasLeftMargin, hasRightMargin, leftMargin, rightMargin, ruleSpacing

    def setRuledStyle():
        global paperStyle, ruleSpacing
        paintArea.delete("paper")
        setMargins()
        setHorizontalRuling(ruleSpacing.get())
        paperStyle = "ruled"



    #define the ruled style dialog
    ruledStyleDialog = Toplevel(mainWindow)
    ruledStyleDialog.title("Ruled style options")

    leftMarginCB = Checkbutton(ruledStyleDialog, text = "Left Margin", variable = hasLeftMargin)
    rightMarginCB = Checkbutton(ruledStyleDialog, text = "Right Margin", variable = hasRightMargin)

    leftMarginScale = Scale(ruledStyleDialog, label = "Set left margin", from_ = 10, to = 50, resolution = 1, tickinterval = 10, orient = "horizontal", variable = leftMargin, length = 150)
    rightMarginScale = Scale(ruledStyleDialog, label = "Set right margin", from_ = 10, to = 50, resolution = 1, tickinterval = 10, orient = "horizontal", variable =rightMargin, length = 150)
    marginColorSelector = OptionMenu(ruledStyleDialog, marginColorInput, "Black", "Blue", "Red")
    marginColorLabel = Label(ruledStyleDialog, text = "Margin color")
    leftMarginScale.set(20)
    rightMarginScale.set(20)
    leftMarginCB.pack()
    leftMarginScale.pack()
    rightMarginCB.pack()
    rightMarginScale.pack()
    marginColorLabel.pack()
    marginColorSelector.pack()



    # the slider to set rule spacing
    spacingSlider = Scale(ruledStyleDialog, label = "Set spacing between rules", from_ = 10, to = 60, resolution = 1, tickinterval = 10, orient = "vertical", variable = ruleSpacing, length = 140, width = 50)
    spacingSlider.pack()

    cancelButton = Button(ruledStyleDialog, text = "Cancel", command = ruledStyleDialog.destroy)
    applyButton = Button(ruledStyleDialog, text = "Apply", relief = "raised", bg = "green", command = setRuledStyle)

    applyButton.pack()
    cancelButton.pack()


def styleGrid():
    global paperStyle, hasLeftMargin, hasRightMargin, leftMargin, rightMargin, ruleSpacing, verticalSpacing, squareGrid

    def setGridStyle():
        global paperStyle, ruleSpacing
        paintArea.delete("paper")
        setMargins()
        setHorizontalRuling(ruleSpacing.get())
        if squareGrid.get():
            setVerticalRuling(ruleSpacing.get())
        else:
            setVerticalRuling(verticalSpacing.get())
        paperStyle = "grid"



    #define the grid style dialog
    gridStyleDialog = Toplevel(mainWindow)
    gridStyleDialog.title("Grid style options")

    leftMarginCB = Checkbutton(gridStyleDialog, text = "Left Margin", variable = hasLeftMargin)

    rightMarginCB = Checkbutton(gridStyleDialog, text = "Right Margin", variable = hasRightMargin)
    leftMarginScale = Scale(gridStyleDialog, label = "Set left margin", from_ = 10, to = 50, resolution = 1, tickinterval = 10, orient = "horizontal", variable = leftMargin, length = 120)
    rightMarginScale = Scale(gridStyleDialog, label = "Set right margin", from_ = 10, to = 50, resolution = 1, tickinterval = 10, orient = "horizontal", variable =rightMargin, length = 120)
    marginColorSelector = OptionMenu(gridStyleDialog, marginColorInput, "Black", "Blue", "Red")
    marginColorLabel = Label(gridStyleDialog, text = "Margin color")
    leftMarginScale.set(20)
    rightMarginScale.set(20)
    leftMarginCB.pack()
    leftMarginScale.pack()
    rightMarginCB.pack()
    rightMarginScale.pack()
    marginColorLabel.pack()
    marginColorSelector.pack()



    # the slider to set horizontal rule spacing
    horizontalSpacingSlider = Scale(gridStyleDialog, label = "Set horizontal spacing", from_ = 10, to = 60, resolution = 1, tickinterval = 10, orient = "horizontal", variable = ruleSpacing, length = 150, width = 50)
    horizontalSpacingSlider.pack()

    # the slider to set vertical rule spacing
    verticalSpacingSlider = Scale(gridStyleDialog, label = "Set vertical spacing", from_ = 10, to = 60, resolution = 1, tickinterval = 10, orient = "vertical", variable = verticalSpacing, length = 150, width = 50)

    squareGridCB = Checkbutton(gridStyleDialog, text = "Square Grid", variable = squareGrid)

    squareGridCB.pack()
    verticalSpacingSlider.pack()

    cancelButton = Button(gridStyleDialog, text = "Cancel", command = gridStyleDialog.destroy)
    applyButton = Button(gridStyleDialog, text = "Apply", relief = "raised", bg = "green", command = setGridStyle)

    applyButton.pack()
    cancelButton.pack()

def stylePractice():
    global paperStyle, hasRightMargin, hasLeftMargin, leftMargin, rightMargin, practiceRuleSpacing

    def setPracticeStyle():
        global paperStyle
        paintArea.delete("paper")
        setMargins()
        paperStyle = "practice"

        _lineIndex = 1
        for y in range(-1, 1000, practiceRuleSpacing.get()):
            if _lineIndex == 3:
                paintArea.create_line(0, y, 5000, y, fill = "black", width = 2, tags = ("paper"))
                _lineIndex = 1
            else:
                paintArea.create_line(0, y, 5000, y, fill = "black", width = 1, tags = ("paper"))
                _lineIndex += 1

    #define the writing practice style dialog


    practiceStyleDialog = Toplevel(mainWindow)
    practiceStyleDialog.title("Paper style options")

    leftMarginCB = Checkbutton(practiceStyleDialog, text = "Left Margin", variable = hasLeftMargin)
    rightMarginCB = Checkbutton(practiceStyleDialog, text = "Right Margin", variable = hasRightMargin)

    leftMarginScale = Scale(practiceStyleDialog, label = "Set left margin", from_ = 10, to = 50, resolution = 1, tickinterval = 10, orient = "horizontal", variable = leftMargin, length = 120)
    rightMarginScale = Scale(practiceStyleDialog, label = "Set right margin", from_ = 10, to = 50, resolution = 1, tickinterval = 10, orient = "horizontal", variable =rightMargin, length = 120)
    marginColorSelector = OptionMenu(practiceStyleDialog, marginColorInput, "Black", "Blue", "Red")
    marginColorLabel = Label(practiceStyleDialog, text = "Margin color")
    leftMarginScale.set(20)
    rightMarginScale.set(20)
    leftMarginCB.pack()
    leftMarginScale.pack()
    rightMarginCB.pack()
    rightMarginScale.pack()
    marginColorLabel.pack()
    marginColorSelector.pack()
    practiceSpacingSlider = Scale(practiceStyleDialog, label = "Set line spacing", from_ = 10, to = 50, resolution = 1, tickinterval = 10, orient = "vertical", variable = practiceRuleSpacing, length = 150, width = 50)

    practiceSpacingSlider.pack()


    cancelButton = Button(practiceStyleDialog, text = "Cancel", command = practiceStyleDialog.destroy)
    applyButton = Button(practiceStyleDialog, text = "Apply", relief = "raised", bg = "green", command = setPracticeStyle)

    applyButton.pack()
    cancelButton.pack()


def styleMusic():
    global paperStyle, hasLeftMargin, hasRightMargin, leftMargin, rightMargin, sheetSpacingSm, sheetSpacingLg

    def setMusicStyle():
        global paperStyle, sheetSpacingLg, sheetSpacingSm
        paintArea.delete("paper")
        setMargins()

        for sheetLineY in range(30, 1000, sheetSpacingLg.get() + (5 * sheetSpacingSm.get())):
            for sheetRuleY in range(sheetLineY, sheetLineY + (sheetSpacingSm.get() * 5), sheetSpacingSm.get()):
                paintArea.create_line(-800, sheetRuleY, 1000, sheetRuleY, fill = "black", tags = ("paper"))

        paperStyle = "music"



    #define the music style dialog
    musicStyleDialog = Toplevel(mainWindow)
    musicStyleDialog.title("Paper style options")

    leftMarginCB = Checkbutton(musicStyleDialog, text = "Left Margin", variable = hasLeftMargin)
    rightMarginCB = Checkbutton(musicStyleDialog, text = "Right Margin", variable = hasRightMargin)

    leftMarginScale = Scale(musicStyleDialog, label = "Set left margin", from_ = 10, to = 50, resolution = 1, tickinterval = 10, orient = "horizontal", variable = leftMargin, length = 150)
    rightMarginScale = Scale(musicStyleDialog, label = "Set right margin", from_ = 10, to = 50, resolution = 1, tickinterval = 10, orient = "horizontal", variable =rightMargin, length = 150)
    marginColorSelector = OptionMenu(musicStyleDialog, marginColorInput, "Black", "Blue", "Red")
    marginColorLabel = Label(musicStyleDialog, text = "Margin color")
    leftMarginScale.set(20)
    rightMarginScale.set(20)
    leftMarginCB.pack()
    leftMarginScale.pack()
    rightMarginCB.pack()
    rightMarginScale.pack()
    marginColorLabel.pack()
    marginColorSelector.pack()

    largeSpacingScale = Scale(musicStyleDialog, label = "Gap between rows", from_ = 20, to = 70, resolution = 1, tickinterval = 10, orient = "vertical", variable = sheetSpacingLg, length = 150, width = 50)
    largeSpacingScale.pack()

    smallSpacingScale = Scale(musicStyleDialog, label = "Music rule spacing", from_ = 10, to = 50, resolution = 1, tickinterval = 10, orient = "vertical", variable = sheetSpacingSm, length = 150, width = 50)
    smallSpacingScale.pack()


    cancelButton = Button(musicStyleDialog, text = "Cancel", command = musicStyleDialog.destroy)
    applyButton = Button(musicStyleDialog, text = "Apply", relief = "raised", bg = "green", command = setMusicStyle)

    applyButton.pack()
    cancelButton.pack()





paintArea = Canvas(mainWindow, width = canvasWidth, height = canvasHeight, bg = paperColor, cursor = "pencil")
paintArea.pack(fill = "both")

paintArea.bind( "<B1-Motion>", paint) # Binding for pen action
paintArea.bind("<Button>", onClick)  # This is the binding for non-pen tools' usage

message = Label(mainWindow, text = "Ink Flow")
message.pack()

#set the ink color menu
colorMenu = Menu(mainWindow, tearoff = True, title = "Ink tray")
colorMenu.add_command(label = "Ink Blue", command = setColorBlue)
colorMenu.add_command(label = "Calligraphic Black", command = setColorBlack)
colorMenu.add_command(label = "Electric Blue", command = setColorLtBlue)
colorMenu.add_command(label = "Royal Purple", command = setColorPurple)
colorMenu.add_command(label = "Important Red", command = setColorRed)
colorMenu.add_command(label = "Natural Green", command = setColorGreen)
colorMenu.add_command(label = "Fruity Orange", command = setColorOrange)


#sset the paper color and style menus
paperMenu = Menu(mainWindow, tearoff = False)
paperMenu.add_command(label = "White Copy", command = setPaperWhite)
paperMenu.add_command(label = "Antique", command = setPaperAntique)
paperMenu.add_command(label = "Recycled Gray", command = setPaperGray)


styleMenu = Menu(mainWindow, tearoff = False)
styleMenu.add_command(label = "Plain", command = stylePlain)
styleMenu.add_command(label = "Ruled", command = styleRuled)
styleMenu.add_command(label = "Grid", command = styleGrid)
styleMenu.add_command(label = "Music Sheet", command = styleMusic)
styleMenu.add_command(label = "Writing Practice", command = stylePractice)

toolMenu = Menu(mainWindow, tearoff = True)
toolMenu.add_command(label = "Pen", command = SetTool_Pen)
toolMenu.add_command(label = "Rule", command = setTool_Rule)
toolMenu.add_command(label = "Circle", command = setTool_Circle)
toolMenu.add_command(label = "Rectangle", command = setTool_Rect)
toolMenu.add_command(label = "Oval", command = setTool_Oval)
toolMenu.add_command(label = "Text", command = setTool_Text)

aboutAndHelp = Menu(mainWindow, tearoff = False)
aboutAndHelp.add_command(label = "About", command = openCredits)
aboutAndHelp.add_command(label = "Help", command = openHelp)

actionBar = Menu(mainWindow)
actionBar.add_command(label = "Clear", command = clear)
actionBar.add_cascade(label = "Change ink", menu = colorMenu)
actionBar.add_cascade(label = "Select tool", menu = toolMenu)
actionBar.add_cascade(label = "Switch paper", menu = paperMenu)
actionBar.add_cascade(label = "Paper style", menu = styleMenu)
actionBar.add_cascade(label = "Help & About", menu = aboutAndHelp)

mainWindow.config(menu = actionBar)

brushSizeScale = Scale(mainWindow, variable = brushSize, from_ = 1.0, to = 5.0, orient = "horizontal", length = canvasWidth, tickinterval = 1, resolution = 0.1)
brushSizeScale.set(3.0)
brushSizeScale.pack()


mainloop()
