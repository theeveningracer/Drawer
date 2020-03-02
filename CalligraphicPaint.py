from tkinter import *

canvasWidth = 800
canvasHeight = 500

paperColor = "white"
paperStyle = "plain"



#set the horizontal rules for both ruled and grid styles
def setHorizontalRuling(spacing):
    for y in range(0, 800, spacing):
        paintArea.create_line(0, y, 1000, y, fill = "black", tags = ("paper"))

#set the vertical ruling for grid
def setVerticalRuling(spacing):
    for x in range(0, 1000, spacing):
        paintArea.create_line(x, 0, x, 800, fill = "black", tags = ("paper"))

mainWindow = Tk()
mainWindow.title("Calligraphic Pen Board")
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
 

brushSize = DoubleVar()

def paint(event):
    x1, y1 = (event.x - brushSize.get()), (event.y - brushSize.get())
    x2, y2 = (event.x + brushSize.get()), (event.y +brushSize.get())
    paintArea.create_oval(x1, y1, x2, y2, fill = inkColor, outline = "", tags = ("ink"))

def clear():
    paintArea.delete("ink")

def setMargins():
    mainWindow.update()
    canvasWidth = mainWindow.winfo_width()
    if hasLeftMargin.get():
        paintArea.create_line(leftMargin.get(), 0, leftMargin.get(), 1000, fill = "black", width = 3, tags = ("paper"))
    if hasRightMargin.get():
        paintArea.create_line(canvasWidth - rightMargin.get(), 0, canvasWidth - rightMargin.get(), 1000, fill = "black", width = 3, tags = ("paper"))

def openCredits():
    creditsWindow = Toplevel(mainWindow)
    creditsWindow.title("Credits and license")
    creditsText = Label(creditsWindow, text = "This program was created in 2020 by Redline Software, a Redline Network company. \n Open source software freely usable for any non-commercial purposes.")
    creditsText.pack()

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
        global paperStyle
        paintArea.delete("paper")
        setMargins()
        paperStyle = "plain"


    #define the plain style dialog

    
    plainStyleDialog = Toplevel(mainWindow)
    plainStyleDialog.title("Paper style options")

    leftMarginCB = Checkbutton(plainStyleDialog, text = "Left Margin", variable = hasLeftMargin)
    rightMarginCB = Checkbutton(plainStyleDialog, text = "Right Margin", variable = hasRightMargin)

    leftMarginScale = Scale(plainStyleDialog, label = "Set left margin", from_ = 10, to = 50, resolution = 1, tickinterval = 10, orient = "horizontal", variable = leftMargin)
    rightMarginScale = Scale(plainStyleDialog, label = "Set right margin", from_ = 10, to = 50, resolution = 1, tickinterval = 10, orient = "horizontal", variable =rightMargin)
    leftMarginScale.set(20)
    rightMarginScale.set(20)
    leftMarginCB.pack()
    leftMarginScale.pack()
    rightMarginCB.pack()
    rightMarginScale.pack()

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

    leftMarginScale = Scale(ruledStyleDialog, label = "Set left margin", from_ = 10, to = 50, resolution = 1, tickinterval = 10, orient = "horizontal", variable = leftMargin)
    rightMarginScale = Scale(ruledStyleDialog, label = "Set right margin", from_ = 10, to = 50, resolution = 1, tickinterval = 10, orient = "horizontal", variable =rightMargin)
    leftMarginScale.set(20)
    rightMarginScale.set(20)
    leftMarginCB.pack()
    leftMarginScale.pack()
    rightMarginCB.pack()
    rightMarginScale.pack()

    

    # the slider to set rule spacing
    spacingSlider = Scale(ruledStyleDialog, label = "Set spacing between rules", from_ = 10, to = 60, resolution = 1, tickinterval = 10, orient = "horizontal", variable = ruleSpacing) 
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

    leftMarginScale = Scale(gridStyleDialog, label = "Set left margin", from_ = 10, to = 50, resolution = 1, tickinterval = 10, orient = "horizontal", variable = leftMargin)
    rightMarginScale = Scale(gridStyleDialog, label = "Set right margin", from_ = 10, to = 50, resolution = 1, tickinterval = 10, orient = "horizontal", variable =rightMargin)
    leftMarginScale.set(20)
    rightMarginScale.set(20)
    leftMarginCB.pack()
    leftMarginScale.pack()
    rightMarginCB.pack()
    rightMarginScale.pack()

    

    # the slider to set horizontal rule spacing
    horizontalSpacingSlider = Scale(gridStyleDialog, label = "Set horizontal spacing", from_ = 10, to = 60, resolution = 1, tickinterval = 10, orient = "horizontal", variable = ruleSpacing) 
    horizontalSpacingSlider.pack()

    # the slider to set vertical rule spacing
    verticalSpacingSlider = Scale(gridStyleDialog, label = "Set vertical spacing", from_ = 10, to = 60, resolution = 1, tickinterval = 10, orient = "horizontal", variable = verticalSpacing)

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
                paintArea.create_line(0, y, 3000, y, fill = "black", width = 2, tags = ("paper"))
                _lineIndex = 1
            else:
                paintArea.create_line(0, y, 3000, y, fill = "black", width = 1, tags = ("paper"))
                _lineIndex += 1

    #define the writing practice style dialog

    
    practiceStyleDialog = Toplevel(mainWindow)
    practiceStyleDialog.title("Paper style options")

    leftMarginCB = Checkbutton(practiceStyleDialog, text = "Left Margin", variable = hasLeftMargin)
    rightMarginCB = Checkbutton(practiceStyleDialog, text = "Right Margin", variable = hasRightMargin)

    leftMarginScale = Scale(practiceStyleDialog, label = "Set left margin", from_ = 10, to = 50, resolution = 1, tickinterval = 10, orient = "horizontal", variable = leftMargin)
    rightMarginScale = Scale(practiceStyleDialog, label = "Set right margin", from_ = 10, to = 50, resolution = 1, tickinterval = 10, orient = "horizontal", variable =rightMargin)
    leftMarginScale.set(20)
    rightMarginScale.set(20)
    leftMarginCB.pack()
    leftMarginScale.pack()
    rightMarginCB.pack()
    rightMarginScale.pack()
    practiceSpacingSlider = Scale(practiceStyleDialog, label = "Set line spacing", from_ = 10, to = 50, resolution = 1, tickinterval = 10, orient = "horizontal", variable = practiceRuleSpacing)

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

    leftMarginScale = Scale(musicStyleDialog, label = "Set left margin", from_ = 10, to = 50, resolution = 1, tickinterval = 10, orient = "horizontal", variable = leftMargin)
    rightMarginScale = Scale(musicStyleDialog, label = "Set right margin", from_ = 10, to = 50, resolution = 1, tickinterval = 10, orient = "horizontal", variable =rightMargin)
    leftMarginScale.set(20)
    rightMarginScale.set(20)
    leftMarginCB.pack()
    leftMarginScale.pack()
    rightMarginCB.pack()
    rightMarginScale.pack()

    largeSpacingScale = Scale(musicStyleDialog, label = "Gap between rows", from_ = 20, to = 70, resolution = 1, tickinterval = 10, orient = "horizontal", variable = sheetSpacingLg)
    largeSpacingScale.pack()

    smallSpacingScale = Scale(musicStyleDialog, label = "Music rule spacing", from_ = 10, to = 50, resolution = 1, tickinterval = 10, orient = "horizontal", variable = sheetSpacingSm)
    smallSpacingScale.pack()


    cancelButton = Button(musicStyleDialog, text = "Cancel", command = musicStyleDialog.destroy)
    applyButton = Button(musicStyleDialog, text = "Apply", relief = "raised", bg = "green", command = setMusicStyle)

    applyButton.pack()
    cancelButton.pack()





paintArea = Canvas(mainWindow, width = canvasWidth, height = canvasHeight, bg = paperColor)
paintArea.pack(fill = "both")

paintArea.bind( "<B1-Motion>", paint)

message = Label(mainWindow, text = "Ink Flow")
message.pack()

#set the ink color menu
colorMenu = Menu(mainWindow, tearoff = True)
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

actionBar = Menu(mainWindow)
actionBar.add_command(label = "Clear", command = clear)
actionBar.add_cascade(label = "Change Ink", menu = colorMenu)
actionBar.add_cascade(label = "Switch Paper", menu = paperMenu)
actionBar.add_cascade(label = "Paper Style", menu = styleMenu)
actionBar.add_command(label = "About", command = openCredits)

mainWindow.config(menu = actionBar)

brushSizeScale = Scale(mainWindow, variable = brushSize, from_ = 1.0, to = 5.0, orient = "horizontal", length = canvasWidth, tickinterval = 1, resolution = 0.1)
brushSizeScale.pack()


mainloop()
