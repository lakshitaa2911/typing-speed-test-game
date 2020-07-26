from tkinter import *
import random
from tkinter import messagebox

#WORDS FOR GAME

words = ['grapes','mango','laptop','television','toy','software','music','dance','helicopter','life','snake','jelly','hardware','live','drawing'
,'silly','stupid','jungle','college','team','dream','school','daily','household','technology','computer','art','doodle','happen','eyes'
,'skin','child','toffee','hustle','bustle','dreaming','hospital','hostel','entertainment','python','cobra','lion','successful','danger'
,'endangered','swift','leaf','edge','dog','snow','cartoon','swiggy','swirl','black','grey','pink','night','dusting','sleep','table','sanitizer'
,'mask','corona','movies','deaf','orange','personal','chair','canada','switzerland','distance','highway','india','new zealand','tokyo','money']

#FUNCTION
def labelSlider():
	global count,sliderwords
	text = 'WELCOME TO TYPING SPEED INCREASER GAME'
	if(count >= len(text)):
		count = 0
		sliderwords=''
	sliderwords += text[count]
	count += 1
	fontLabel.configure(text = sliderwords)
	fontLabel.after(150,labelSlider)



def startGame(event):
    global score,miss
    if(timeleft==60):
      timer()
    gamePlayDetails.configure(text='')
    if(wordEntry.get()==wordLabel['text']):
        score+=1
        scoreLabelCount.configure(text=score)
        print('score:',score)
    else:
        miss+=1
        print('miss:',miss)
    random.shuffle(words)
    wordLabel.configure(text=words[0])
    wordEntry.delete(0,END)



def timer():
    global timeleft,score,miss
    if(timeleft>=11):
        pass
    else:
        timeLabelCount.configure(fg='red')

    if(timeleft>=0):
        timeleft-=1
        timeLabelCount.configure(text=timeleft)
        timeLabelCount.after(1000,timer)
    else:
        gamePlayDetails.configure(text='Hit={} | Miss={} | Total Score={}'.format(score,miss,score-miss))
        rr = messagebox.askretrycancel('Notificatioin','For play again Hit Retry button')
        if(rr == True):
            score = 0
            timeleft = 60
            miss = 0
            timeLabelCount.configure(text=timeleft)
            wordLabel.configure(text=words[0])
            scoreLabelCount.configure(text=score)  


#ROOT METHOD
root = Tk()
root.geometry('800x600+400+100')
root.configure(bg='yellow')
root.title('TYPING SPEED INCREASER GAME')

#VARIABLE
score=0
timeleft = 60
count = 0
sliderwords = ' '
miss = 0

#LABEL METHODS
fontLabel = Label(root,text=' ', font=('airal',20,'italic bold'),bg='black',fg='yellow',width = 45)
fontLabel.place(x=20,y=20)
labelSlider()

random.shuffle(words)
wordLabel = Label(root,text=words[0],font=('airal',40,'italic bold'),bg='white')
wordLabel.place(x=350,y=200)

scoreLabel = Label(root,text='Your Score :',font=('airal',25,'italic bold'),bg='yellow',fg='black')
scoreLabel.place(x=10,y=100)

scoreLabelCount = Label(root,text=score,font=('airal',25,'italic bold'),bg='yellow',fg='black')
scoreLabelCount.place(x=80,y=180)

timerLabel = Label(root,text='Time Left',font=('airal',25,'italic bold'),bg='yellow',fg='black')
timerLabel.place(x=600,y=100)

timeLabelCount = Label(root,text=timeleft,font=('airal',25,'italic bold'),bg='yellow',fg='black')
timeLabelCount.place(x=680,y=180)

gamePlayDetails = Label(root,text = 'Type word and hit Enter Button',font=('airal',30,'italic bold'),bg='yellow',fg='black')
gamePlayDetails.place(x=120,y=450)

#ENTRY METHOD
wordEntry = Entry(root, font=('airal',25,'italic bold'),bd=10,justify='center')
wordEntry.place(x=250,y=300)
wordEntry.focus_set()

root.bind('<Return>',startGame)
root.mainloop()