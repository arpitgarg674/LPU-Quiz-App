

#test
from tkinter import *
import random
import os
import sys
from tkinter import messagebox


def languageScreen():
	lang = Tk()
	lang.title("LPU QUIZ GAME")

	windowWidth = lang.winfo_reqwidth()
	windowHeight = lang.winfo_reqheight()
	positionRight = int(lang.winfo_screenwidth()/7 - windowWidth/3)
	positionDown = int(lang.winfo_screenheight()/4 - windowHeight/2)
	
	lang.geometry("900x700+{}+{}".format(positionRight+300, positionDown))

	title = Label(lang, width=30, text='LPU QUIZ',
			   font=('Gothic', '28', 'bold'))
	title.place(relx=0.5, rely=0, anchor=N)

	texto = Label(lang,
				text='Select one of the languages below',
				font=('Consolas', 18))
	texto.place(relx=0.5, rely=0.25, anchor=N)

	def getLanghn():
		global language
		language = 'hn'
		lang.destroy()
	
	def getLangEN():
		global language
		language = 'en'
		lang.destroy()

	def comingsoon():
		messagebox.showerror("Warning", "Sorry, for inconvenience but hindi language is not implemented yet", icon ='warning')
		print("Hello")

	hnLang = Button(lang, text='Coming Soon', width=20, height=2, font=('Arial', 22), fg='green', command=comingsoon)
	en = Button(lang, text='ENGLISH', width=20, height=2, font=('Arial', 22), fg='red', command=getLangEN)

	hnLang.place(relx=0.25, rely=0.6, anchor=S)
	en.place(relx=0.75, rely=0.6, anchor=S)


	lang.mainloop()
	
languageScreen()

if language == "en":
	from en import *


init = Tk()
init.title("LPU QUIZ GAME")


points = 0
close = 1
difficulty = ''


windowWidth = init.winfo_reqwidth()
windowHeight = init.winfo_reqheight()
positionRight = int(init.winfo_screenwidth()/7 - windowWidth/3)
positionDown = int(init.winfo_screenheight()/4 - windowHeight/2)
# Seta as dimensões da tela
init.geometry("900x700+{}+{}".format(positionRight+300, positionDown))




list_questions_initial = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
random.shuffle(list_questions_initial)
list_questions = []
y = 0
z = 0



list_questionsEasy = [2,3,5,8,11,13,15]
random.shuffle(list_questionsEasy)
list_questionsMedium = [1,9,12,14,16,18,20]
random.shuffle(list_questionsMedium)
list_questionsHard = [4,6,7,10,17,19]
random.shuffle(list_questionsHard)



lista_answers = [1.4,2.1,3.1,4.1,5.4,6.3,7.4,8.3,9.5,10.2,11.1,12.3,13.4,14.5,15.2,16.5,17.2,18.3,19.5,20.2]


def concatenation(difficulty_list, init_list_questions):
  for k in init_list_questions:
    if k in difficulty_list:
        pass
    else:
        difficulty_list.append(k)
  global list_questions
  list_questions = difficulty_list


def identification():
    identificar = Tk()
    identificar.title('LPU QUIZ App')

    identificar.geometry("900x700+{}+{}".format(positionRight+300, positionDown))

    def dice():
      global user
      user = name.get()

      erroname = Label(identificar, text='Type your name', font=('Arial', 14))
      erroname.place(relx=0.5, rely=0.22, anchor=N)
      
      if user != '':
        erroname['text'] = 'Name stored'
        erroname['bg'] = 'green'

    def easyBtn():
      global difficulty
      difficulty = 'easy'
      mediumDifficulty['bg'] = 'white'
      hardDifficult['bg'] = 'white'
      difficultyEasy['bg'] = 'green'

    def mediumBtn():
      global difficulty
      difficulty = 'medium'
      hardDifficult['bg'] = 'white'
      difficultyEasy['bg'] = 'white'
      mediumDifficulty['bg'] = 'orange'

    def hardBtn():
      global difficulty
      difficulty = 'difficult'
      mediumDifficulty['bg'] = 'white'
      difficultyEasy['bg'] = 'white'
      hardDifficult['bg'] = 'red'

    def playBtn():
      if difficulty != '' and user != '':
        identificar.destroy()
        if difficulty == 'easy':
          concatenation(list_questionsEasy,list_questionsEasy)
        elif difficulty == 'medium':
          concatenation(list_questionsMedium,list_questionsMedium)
        else:
          concatenation(list_questionsHard,list_questionsHard)
      else:
        dice()
        errorDifficulty = Label(identificar, text='Choose the difficulty please.', font=('Arial, 14'))
        errorDifficulty.place(relx=0.5, rely=0.95, anchor=S)

    titleUser = Label(identificar, text = 'Type your name below', font=('Gothic', 32, "bold"), fg = 'green')
    name = Entry(identificar, width=30, font=('Arial', 20))
    confirmarname = Button(identificar, width=15, text ='Confirm', font=(16), command=dice)
    textdifficulty = Label(identificar, text = 'Select the difficulty', font=('Gothic', 32, "bold"), fg = 'black')

    difficultyEasy = Button(identificar, text ='Easy', width=20, font=('Arial', 18), command=easyBtn)
    mediumDifficulty = Button(identificar, text = 'Normal', width=20, font=('Arial', 18), command=mediumBtn)
    hardDifficult = Button(identificar, text = 'Hard', width=20, font=('Arial', 18), command=hardBtn)
    start = Button(identificar, text = 'PLAY', width=20, font=('Arial', 22, 'bold'), command=playBtn)

    titleUser.place(relx=0.5, rely=0, anchor=N)
    name.place(relx=0.5, rely=0.1, anchor=N)
    confirmarname.place(relx=0.5, rely=0.16, anchor=N)
    textdifficulty.place(relx = 0.5, rely = 0.3, anchor=CENTER)

    difficultyEasy.place(relx=0.5, rely=0.5, anchor=S)
    mediumDifficulty.place(relx=0.5, rely=0.58, anchor=S)
    hardDifficult.place(relx=0.5, rely=0.66, anchor=S)
    start.place(relx=0.5, rely=0.9, anchor=S)

    identificar.mainloop()


def getGame():
    global z, close


    if close == 1:
      init.destroy()
      identification()
      if difficulty == '' or user == '':
        exit()


    game = Tk()
    game.title('Questions' + "- LPU QUIZ App")




    game.geometry("900x700+{}+{}".format(positionRight+300, positionDown))


    def verification(y,z):
      global points
      if (x+y) in lista_answers:
        points += 1
        game.destroy()
        if points == 20:
          feedback(x)
        else:
          getGame()
      else:
        game.destroy()
        feedback(x)


    def y_alt1():
        y = 0.1
        verification(y,z)


    def y_alt2():
        y = 0.2
        verification(y,z)


    def y_alt3():
        y = 0.3
        verification(y,z)

        
    def y_alt4():
        y = 0.4
        verification(y,z)
    
    def y_alt5():
        y = 0.5
        verification(y,z)
        


    x = list_questions[z]
    y = 0.1
    z += 1

    close += 1
    
    question = Label(game, text=questions[x], fg = 'black', font=('Arial', 20))

    letterA = Label(game,
                  text='a)',
                  font=('Arial', 16, 'bold'))

    alt1 = Button(game,
                  text=answers[x+y],
                  width=50,
                  height=2,
                  font=('Arial', 12),
                  command = y_alt1)

    y += 0.1

    letterB = Label(game,
                  text='b)',
                  font=('Arial', 16, 'bold'))

    alt2 = Button(game,
                  text=answers[x+y],
                  width=50,
                  height=2,
                  font=('Arial', 12),
                  command=y_alt2)

    y += 0.1

    letterC = Label(game,
                  text='c)',
                  font=('Arial', 16, 'bold'))

    alt3 = Button(game,
                  text=answers[x+y],
                  width=50,
                  height=2,
                  font=('Arial', 12),
                  command=y_alt3)

    y += 0.1

    letterD = Label(game,
                  text='d)',
                  font=('Arial', 16, 'bold'))

    alt4 = Button(game,
                  text=answers[x+y],
                  width=50,
                  height=2,
                  font=('Arial', 12),
                  command=y_alt4)

    y += 0.1

    letterE = Label(game,
                  text='e)',
                  font=('Arial', 16, 'bold'))

    alt5 = Button(game,
                  text=answers[x+y],
                  width=50,
                  height=2,
                  font=('Arial', 12),
                  command=y_alt5)

    
    punctuation = Label(game, text='Score:', font=('Arial', 16))
    punctuationNum = Label(game, text=points, font=('Arial', 16), fg='#006600')
    punctuation.place(relx=0.9, rely=0.7, anchor=CENTER)
    punctuationNum.place(relx=0.97, rely=0.7, anchor=CENTER)


    alt1.place(relx = 0.05, rely = 0.4, anchor = W)
    letterA.place(relx = 0, rely = 0.4, anchor = W)
    alt2.place(relx = 0.05, rely = 0.5, anchor = W)
    letterB.place(relx = 0, rely = 0.5, anchor = W)
    alt3.place(relx = 0.05, rely = 0.6, anchor = W)
    letterC.place(relx = 0, rely = 0.6, anchor = W)
    alt4.place(relx = 0.05, rely = 0.7, anchor = W)
    letterD.place(relx = 0, rely = 0.7, anchor = W)
    alt5.place(relx = 0.05, rely = 0.8, anchor = W)
    letterE.place(relx = 0, rely = 0.8, anchor = W)
    question.place(relx = 0.5, rely = 0, anchor = N)


    game.mainloop()


def getQuit():  
    init.destroy()
    exit()


def fbquit():
    fb.destroy()
    exit()


def fbrestart():
    os.execl(sys.executable, sys.executable, * sys.argv)
    

def feedback(x):
    global fb
    

    fb = Tk()
    fb.title("Feedback - LPU QUIZ App")
    
 
    fb.geometry("900x700+{}+{}".format(positionRight+300, positionDown))

    titleFeed = Label(fb, text='YOU FAILED', font=('Gothic', 32, "bold"), fg = 'red')
    justificativa = Label(fb, text = 'Feedback:', font=('Arial', 23, "bold"), fg = 'black')
    answer = Label(fb, text=explain[x], fg = 'black', font=('Arial', 18))
    titleFeed.place(relx=0.5,rely=0,anchor=N)
    
   
    if points == 0:
      textOfPrimary = "Noob"
      textOfSecondary = 'You have to improve your skills!'
    elif points > 0 and points < 6:
      textOfPrimary = "Novice"
      textOfSecondary = 'You could have gone better...'
    elif points > 5 and points < 11:
      textOfPrimary = "Median"
      textOfSecondary = 'Continue practing, you are growing!'
    elif points > 10 and points < 16:
      textOfPrimary = "Expert!"
      textOfSecondary = "That's good! Show me more!"
    elif points > 15 and points < 20:
      textOfPrimary = "Professional!"
      textOfSecondary = 'Wow! Almost done!'
    elif points == 20:
      titleFeed['text'] = 'YOU WON! CONGRATS!!'
      titleFeed['fg'] = '#66ff66'
      titleFeed['font'] = ('Gothic', 72, "bold")
      titleFeed.place(relx=0.5, rely=0.18, anchor=N)
      answer['text'] = ''
      justificativa['text'] = ''
      textOfPrimary = "Masterpiece!"
      textOfSecondary = 'You got it all!'
    else:
      pass


    
    messagefb = Label(fb, text=f'{user}, your score was:', font=('Gothic', 20, "bold"))
    punctuation = Label(fb, text=points, font=('Gothic', 42, "bold"), fg = "#330000")
    textosfeedbackpri = Label(fb, text=textOfPrimary, font=('Gothic', 52, "bold"), fg = '#b30000')
    textosfeedbacksec = Label(fb, text=textOfSecondary, font=('Gothic', 18, "bold"))
    nothing = Label(fb, text='', width= 0, height=8)
    getOut = Button(fb, text='QUIT', width=20, font=('Arial', 18, 'bold'), fg = '#b30000', command=fbquit)
    again = Button(fb, text='PLAY AGAIN', width=20, font=('Arial', 18, 'bold'), fg = '#006600', command=fbrestart)


   
    justificativa.place(relx=0, rely=0.15, anchor=W)
    answer.grid(row=30, column=0)
    nothing.grid(row=0, column=0)
    messagefb.place(relx= 0.5, rely= 0.5, anchor=S)
    punctuation.place(relx = 0.5, rely= 0.6, anchor=S)
    textosfeedbackpri.place(relx=0.5,rely=0.75, anchor=S)
    textosfeedbacksec.place(relx=0.5,rely=0.80, anchor=S)
    getOut.place(relx=0.3, rely=0.95, anchor=S)
    again.place(relx=0.7, rely=0.95, anchor=S)
    




title = Label(init, width=30, text='LPU QUIZ',
               font=('Gothic', '28', 'bold'))
title.place(relx=0.5, rely=0, anchor=N)



play = Button(init, text='START', width=20, height=2, font=('Arial', 22), fg='green', command=getGame)
getOut = Button(init, text='QUIT', width=20, font=('Arial', 18, 'bold'), command=getQuit)




preGame = Label(init,
                text='Read the rules below and\nstart when you are ready ',
                font=('Consolas', 12))

rules = Label(init,
              text='This Quiz is made by 20 (twenty) questions about mathematic, physics and chemistry,\n'
			  'you have to choose one out of five ohnions for each question.\n'
			  'If you choose them wrong, the Quiz will end and the feedback window will show the explanation for the correct answer.\n'
			  'Beyond that, your classification score will be there as well with a nice text :)',
              width=800,
              bg = 'black',
              fg = '#FACA2F',
              font=('Times', 14))



play.place(relx=0.5, rely=0.2, anchor=N)
preGame.place(relx=0.5, rely=0.38, anchor=N)
rules.place(relx=0.5, rely=0.55, anchor=CENTER)
getOut.place(relx=0.5, rely=0.8, anchor=S)



init.mainloop()
