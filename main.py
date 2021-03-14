import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import webbrowser


class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.say('Hello! Nice to meet you!')
engine.say('Speak out what you would like me to do')
engine.say('Would you like to know what climate change is?')
engine.say('Would you like to know some recent news related to climate change?')
engine.say('Should I educate you about the effects of climate change')
engine.say('Should I show you some of the most asked questions about climate change')
engine.say('Or would you like to try a quiz about climate change')
print('Hello! Nice to meet you!')
print('Speak out what you would like me to do')
print('1.Would you like to know what climate change is?')
print('2.Would you like to know some recent news related to climate change?')
print('3.Should I educate you about the effects of climate change')
print('4.Should I show you some of the most asked questions about climate change')
print('5.Or would you like to try a quiz about climate change')
engine.runAndWait()

def talk(text):
    engine.say('')
    engine.runAndWait()


def take_command():
    command = False
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                talk('Yes Sir!')
    except:

        pass
    return command


def run_alexa():
    command = take_command()
    if command == False:
        return
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'news' in command:
        news = command.replace('who is', '')
        talk('finding' + news)
        new=2;
        url="https://edition.cnn.com/specials/world/cnn-climate";
        webbrowser.open(url,new=new);

    elif 'most asked questions' in command:
        que = command.replace('who is', '')
        talk('finding' + que)
        new=2;
        url="https://19january2017snapshot.epa.gov/climatechange/frequently-asked-questions-about-climate-change_.html";
        webbrowser.open(url,new=new);

    elif 'what is climate change' in command:
        cli = command.replace('who is', '')
        talk('finding' + cli)
        new=2;
        url="https://www.nasa.gov/audience/forstudents/k-4/stories/nasa-knows/what-is-climate-change-k4.html";
        webbrowser.open(url,new=new);

    elif 'effects' in command:
        eff = command.replace('who is', '')
        talk('finding' + eff)
        new=2;
        url="https://www.businessinsider.in/science/22-devastating-effects-of-climate-change/articleshow/36405612.cms";
        webbrowser.open(url,new=new);

    elif 'quiz' in command:
        qui = command.replace('who is', '')
        talk('finding' + qui)
        question_prompts = [
            "What is the greenhouse effect?\n(a)Certain gases in the atmosphere trap heat and warm the Earth\n(b)Life on Earth 'exhales' gas that warms up the atmosphere\n(c)The tilt of the Earth changes the amount of solar energy the Earth receives\n(d)The Sun is putting out more radiant energy over time\n",
            "Which activities are the largest contributors of greenhouse gases?\n(a)Deforestation\n(b)Industry\n(c)Electricity generation\n(d)Transportation\n",
            "How much has CO2 in the atmosphere increased since the Industrial Revolution?\n(a)11 percent\n(b)43 percent\n(c)62 percent\n",
            "How has the global average temperature changed since the Industrial Revolution?\n(a)Cooler by 0.1 degree C\n(b)The temperature has gone up and down, but remains overall the same\n(c)Warmer by almost 2 degrees C\n(d)Warmer by more than 1 degree C\n",
            "When was the last time in Earth's history that CO2 was as high as it is now?\n(a)This is the highest it's ever been\n(b)CO2 was at least this high during the warm periods between the ice ages\n(c)CO2 has not been this high for almost one million years\n(d)The last time CO2 was this high was 3 million years ago\n",
            "What proportion of climate scientists has concluded that humans are the primary driver of today's climate warming?\n(a)34%\n(b)59%\n(c)76%\n(d)97%\n",
            "Which country has emitted the most CO2 over time?\n(a)China\n(b)USA\n(c)Russia\n(d)Saudi Arabia\n",
            "How long does CO2 remain in the atmosphere?\n(a)CO2 washes out of the atmosphere seasonally.\n(b)CO2 remains in the atmosphere for 5-10 years.\n(c)CO2 remains in the atmosphere for up to 200 years, or more\n",
            "If we stopped burning fossil fuels today, what would happen to the climate?\n(a)Earth's average temperature would immediately cool\n(b)Temperatures would slowly cool over the next 5 years\n(c)Temperatures would fluctuate, but stay the same on average\n(d)Temperatures would continue to rise for at least 10 years, and then would level off\n",
            "How fast to we need to stop burning fossil fuels to limit global temperature rise to 2 degrees C?\n(a)We need to stop burning fossil fuels by 2040\n(b)We need to stop burning fossil fuels by 2100\n(c)Fossil fuels don't matter, the Sun will cool and so will the Earth\n(d)It's already too late to stay below the 2-degree threshold. We should have stopped burning fossil fuels in the early 2000s"
            ]
        questions = [
            Question(question_prompts[0], "a"),
            Question(question_prompts[1], "d"),
            Question(question_prompts[2], "b"),
            Question(question_prompts[3], "d"),
            Question(question_prompts[4], "d"),
            Question(question_prompts[5], "d"),
            Question(question_prompts[6], "b"),
            Question(question_prompts[7], "c"),
            Question(question_prompts[8], "d"),
            Question(question_prompts[9], "a"),
        ]
        def run_test(questions):
            score = 0

            for question in questions:
                answer = input(question.prompt)
                if answer == question.answer:
                    print('Correct!')
                    score += 1
                    fscore = str(score) + "/" + str(len(questions))
                else:
                    print('Sorry your answer is wrong.')
            print('Your score is ' + fscore)
            print('What would you like to know next?')

        run_test(questions)

    elif 'near me' in command:
        location = command.replace('', '')
        talk('finding' + location + 'near me')
        pywhatkit.search(location)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'date' in command:
        date = datetime.datetime.today().strftime('%d:%m %Y')
        talk('The date is ' + date)

    elif 'who is' in command:
        info = command.replace('who is', '')
        talk('finding' + info)
        pywhatkit.info(info)
        talk(info)
    elif 'how to' in command:
        process = command.replace('how to', '')
        talk('finding' + process)
        pywhatkit.search(process)
    elif 'go to' in command:
        process = command.replace('go to', '')
        talk('reaching' + process)
        pywhatkit.search(process)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'run' in command:
        initializing = command.replace('run', '')
        talk('running' + initializing)
    elif 'open c' in command:
        os.startfile("C:")
    elif 'open d' in command:
        os.startfile("D:")


    else:
        talk('Please say the command again.')




while True:
    run_alexa()
