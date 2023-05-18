#Documentation Websites to modules used
#Mingus: https://bspaans.github.io/python-mingus/
#Mido: https://mido.readthedocs.io/en/latest/installing.html
#PyDub-GitHub: https://github.com/jiaaro/pydub
#Midi2Audio: https://github.com/bzamecnik/midi2audio
#FluidSynth Software: https://www.fluidsynth.org/
#All Imports Needed

from mingus.containers import Bar
from mingus.containers import Note
from random import randint
from mingus.containers import NoteContainer
from random import randint
import mingus.core.progressions as progressions
from mingus.containers.instrument import Instrument, Piano, Guitar
from mingus.containers.instrument import MidiInstrument
from mingus.containers import Track
from mingus.containers.instrument import MidiInstrument
from mido import MidiFile, MidiFile, MidiTrack
from mido import MetaMessage
from mido import bpm2tempo
from mingus.containers import Composition
from pydub import AudioSegment
from mingus.midi import fluidsynth
from mingus.midi import midi_file_out
from midi2audio import FluidSynth
from pydub import AudioSegment
from pydub.playback import play
from mingus.core import value
#adding pop chord
#Im assuming pop always as 3 notes in a chord


#duration notes (Andres)
dq = value.dots(value.quarter)
dh = (value.dots(value.half))
de = (value.dots(value.eighth))
ds = (value.dots(value.sixteenth))
tq = (value.tuplet(value.quarter,3,2))
th = (value.tuplet(value.half,3,2))

def addPopChord(chord):
    
    listNoteNames = []

    for note in chord:
        listNoteNames.append(note.name + "-" + str(note.octave))

    for note in chord:
        listNoteNames.append(note.name + "-" + str(note.octave + 1))

    newNoteContainer = NoteContainer(listNoteNames)

  
    return newNoteContainer
   
#randomize object (Sai)
def randomizeObject(choiceContainer):
    probList = [[1,choiceContainer[0][1]]]
    for choice in (choiceContainer[1::]):
        probList.append([probList[-1][1] + 1,probList[-1][1] + choice[1]])
    #random number between 1 through 100
    randomNumber = randint(1,100)

    #based on random number
    for idx in range(0,len(probList)):
        if(randomNumber >= probList[idx][0] and randomNumber <= probList[idx][1]):
            return choiceContainer[idx][0]

#build bar with chords (Sai Naru)
def buildBar(chordLists):
    b = Bar()
    for chordWithDuration in chordLists:
        b.place_notes(chordWithDuration[0],chordWithDuration[1])
    return b
    
# (Andres)
def RandBChoirA(chord, b):
    #initalize

    root = Note(chord[0])
    third = Note(chord[1])
    fifth = Note(chord[2])
    seventh = Note(chord[-1])

    root.change_octave(1)
    third.change_octave(1)
    fifth.change_octave(1)
    seventh.change_octave(1)



    chordlist = [(third,2),(seventh,2)]
    emptychordlist = [(None, 1)]
    b = buildBar(randomizeObject([(chordlist, 90), (emptychordlist, 10)]))
    return b


#(Andres)
def PopA(chord, b): #I love to eat sushi
    #print("We are inside of Pop-A")
    chord = addPopChord(chord)
    chordList = [(chord,8),(None,8),(chord,8),(chord,8),(None,8),(chord,8),(chord,8),(chord,8)]
    b = buildBar(chordList)
    return b

#(Andres)
def PopB(chord, b): #Riptide
    #print("Inside of Pop B")
    chord = addPopChord(chord)
    chordList = [(chord,8),(None,8),(chord,8),(None,8),(None,8),(chord,8),(chord,8),(chord,8)]
    b = buildBar(chordList)
    return b

#(Andres)
def PopC(chord, b): #Teen Spirit
    #print("Inside of Pop C")
    chord = addPopChord(chord)
    chordList = [(chord,16),(None,16),(None,16),(chord,16),(chord,16),(None,16),(None,16),(chord,16),
    (chord,16),(chord,16),(chord,16),(None,16),(chord,16),(None,16),(chord,16),(None,16)]

    b = buildBar(chordList)
    return b

#(Andres)
def JazzA(chord, b): #Bossa Nova:
   # print("In Jazz A")
    bassnote = chord[0]
    upperchord = chord[1:]
    
    chordList = [(chord,4),(upperchord,4),(bassnote,8),(upperchord,dq)]

    b = buildBar(chordList)
    return b

#(Andres)
def JazzB(chord,b): # 3 3 2
    #print("In Jazz B")
    chordList = [(chord,dq),(chord,dq),(chord,4)]
    b = buildBar(chordList)
    return b

#(Andres)
def JazzC(chord,b): #Charleston
    #print("In in Jazz C")
    chordList = [(chord,dq),(chord,8),(None,2)]
    b = buildBar(chordList)
    return b

#(Andres)
def JazzD(chord,b): #Charleston modified
   # print("In in Jazz D")
    chordList = [(None,4),(chord,dq),(chord,8),(None,dq)]
    b = buildBar(chordList)
    return b

#(Andres)
def JazzE(chord,b): # 2 and 4
    #print("In Jazz E")
    chordList = [(chord,4),(chord,4),(chord,4),(chord,4)]
    b = buildBar(chordList)
    return b

#(Andres)
def RandBA(chord,b): #Flat Arpeggio and input needs to be at least a seventh
    #print("Iniside of R&B A")
    chordList = [(chord[0],8),(chord[1],8),(chord[2],8),(chord[1],8),(chord[3],8),(chord[1],8),(chord[0],8),(chord[1],8)]
    b = buildBar(chordList)
    return b

#(Andres)
def RandBB(chord,b): #Please do not lean arpeggio
    #print("Inside of R&BB")
    b.place_notes(chord[0], 16)
    b.place_notes(chord[2], 16)
    b.place_notes(chord[1], 16)
    b.place_notes(chord[3], 16)
    b.place_notes(chord[:2], 16)
    b.place_notes(chord[2], 16)
    b.place_notes(chord[1], 16)
    b.place_notes(chord[3], 16)
    b.place_notes(chord[:3], 16)
    b.place_notes(chord[2], 16)
    b.place_notes(chord[1], 16)
    b.place_notes(chord[3], 16)
    b.place_notes(chord, 16)
    b.place_notes(chord[2], 16)
    b.place_notes(chord[1], 16)
    b.place_notes(chord[3], 16)

    return b

#(Andres) chord --> chordFixed
def RandBC(chord,b): #Slow Keys
    #print("Inside of R&BC")
   # print(chord)

    b.place_notes(chord,dh)
    b.place_notes(chord[1],8) #Could randomize a leading root eighth note before the chord
    b.place_notes(chord[3],8)

    return b

# (Andres)
def RandBE(chord, b):
    #print("Inisde of R&BE")
    outerchordroot = Note(chord[0])
    outerchordseventh= Note(chord[-1])

    outerchordseventh.octave_down()
    outerchordroot.octave_up()

    outerchord = [outerchordroot,outerchordseventh]
    chordlist = [(chord,dq),(outerchord,8),(chord,2)]
    b = buildBar(chordlist)
    return b

# (Andres)
def PopBassA(chord,b): #basses need to be randomized heavily third,4 to be root or vice versa
    root = Note(chord[0])
    third = Note(chord[1])
    fifth = Note(chord[2])

    root.change_octave(-1)
    third.change_octave(-1)
    fifth.change_octave(-1)

    chordlist = [(third,value.dots(value.quarter)),(root,8),(fifth,8),(third,4),(third,8)]
    emptychordlist = [(None, 1)]
    b = buildBar(randomizeObject([(chordlist,80),(emptychordlist,20)]))
    return b

def PopBassB(chord,b): #randomize root third or none for last one
    root = Note(chord[0])
    third = Note(chord[1])

    root.change_octave(-1)
    third.change_octave(-1)

    chordlist = [(root,4),(None,8),(root,8),(root,4),(third,4)]
    emptychordlist = [(None, 1)]
    b = buildBar(randomizeObject([(chordlist,80),(emptychordlist,20)]))
    return b

def PopBassC(chord,b): #randomize last four as being None third or fifth or root
    root = Note(chord[0])
    third = Note(chord[1])
    fifth = Note(chord[2])
    
    chordlist = [(root,8),(None,8),(root,8),(None,8),(root,8),(root,8),(root,8),(root,8)]
    emptychordlist = [(None, 1)]
    b = buildBar(randomizeObject([(chordlist,80),(emptychordlist,20)]))
    return b

def PopBassD(chord,b):
    root = Note(chord[0])
    third = Note(chord[1])
    fifth = Note(chord[2])

    root.change_octave(-1)
    third.change_octave(-1)
    fifth.change_octave(-1)

    chordlist = [(root,4),(None,4),(root,4),(root,4)]
    emptychordlist = [(None, 1)]
    b = buildBar(randomizeObject([(chordlist,80),(emptychordlist,20)]))
    return b

def PopBassE(chord,b):
    root = Note(chord[0])
    third = Note(chord[1])
    fifth = Note(chord[2])

    root.change_octave(-1)
    third.change_octave(-1)
    fifth.change_octave(-1)

    chordlist = [(root,8),(root,8),(root,8),(root,8),(root,8),(root,8),(root,8),(root,8)]
    emptychordlist = [(None, 1)]
    b = buildBar(randomizeObject([(chordlist,80),(emptychordlist,20)]))
    return b

def PopBassF(chord,b):
    root = Note(chord[0])
    third = Note(chord[1])
    fifth = Note(chord[2])

    root.change_octave(-1)
    third.change_octave(-1)
    fifth.change_octave(-1)

    chordlist = [(root,16),(root,16),(root,16),(root,16),(root,16),(root,16),(root,16),(root,16),(root,16),(root,16),(root,16),(root,16),(None,4)]
    emptychordlist = [(None, 1)]
    b = buildBar(randomizeObject([(chordlist,80),(emptychordlist,20)]))
    return b

def JazzBassA1(chord,b): #walking bass descending
    root = Note(chord[0])
    third = Note(chord[1])
    fifth = Note(chord[2])

    root.change_octave(-1)
    third.change_octave(-1)
    fifth.change_octave(-1)

    seventh = ""
    if len(chord)==4:
        seventh = Note(chord[-1])
        seventh.change_octave(-1)
    else:
        #same issue, trying to accesss the fourth element, while only three elements exist?
        #orginally chord[3]
        seventh = Note(chord[3])
        seventh.change_octave(-1)

    ninth = Note(chord[-1])
    ninth.change_octave(-1)
    
    newNinth = ninth
    newNinth.change_octave(-1)

    chordlist = [(seventh,6),(None,12),(fifth,6),(None,12),(third,6),(None,12),(randomizeObject([(fifth,20),(root,70),(newNinth,10)]),6),(None,12)]
    emptychordlist = [(None, 1)]
    b = buildBar(randomizeObject([(chordlist,80),(emptychordlist,20)]))
    return b

def JazzBassA2(chord,b): #walking bass ascending

    root = Note(chord[0])
    third = Note(chord[1])
    fifth = Note(chord[2])

    root.change_octave(-1)
    third.change_octave(-1)
    fifth.change_octave(-1)

    seventh = ""
    if len(chord) == 4:
        seventh = Note(chord[-1])
        seventh.change_octave(-1)
    else:
        #Orginally chord was in chord[3]
        seventh = Note(chord[3])
        seventh.change_octave(-1)
        
    ninth = Note(chord[-1])
    ninth.change_octave(-1)

    chordlist = [(root,6),(None,12),(third,6),(None,12),(randomizeObject([(root,25),(fifth,75)]),6),(None,12),(seventh,6),(None,12)]
    emptychordlist = [(None, 1)]
    b = buildBar(randomizeObject([(chordlist,90),(emptychordlist,10)]))
    return b

def JazzBassB(chord, b):

    root = Note(chord[0])
    third = Note(chord[1])
    fifth = Note(chord[2])

    root.change_octave(-1)
    third.change_octave(-1)
    fifth.change_octave(-1)

    seventh = ""
    if len(chord) == 4:
        seventh = Note(chord[-1])
        seventh.change_octave(-1)
    else:
        #same error, trying to access the fourth element, while only 3 chords exist?
        seventh = Note(chord[3])
        seventh.change_octave(-1)

    ninth = Note(chord[-1])
    ninth.change_octave(-1)
    chordlist = [(third,4),(randomizeObject([(root,75),(fifth,25)]),4),(randomizeObject([(third,75),(fifth,25)]),4),(randomizeObject([(seventh,75),(third,25)]),4)]
    emptychordlist = [(None, 1)]
    b = buildBar(randomizeObject([(chordlist,90),(emptychordlist,10)]))
    return b

def JazzBassC(chord, b):

    root = Note(chord[0])
    third = Note(chord[1])
    fifth = Note(chord[2])

    root.change_octave(-1)
    third.change_octave(-1)
    fifth.change_octave(-1)

    if len(chord) == 4:
        seventh = Note(chord[-1])
        seventh.change_octave(-1)
    else:
        #same issue as JazzBassB, I think your trying to access the thrid note which is actually chord[2]
        seventh = Note(chord[3])
        seventh.change_octave(-1)

    ninth = Note(chord[-1])
    ninth.change_octave(-1)

    chordlist = [(root,4),(None,4),(None,4),(randomizeObject([(third,50),(seventh,25),(ninth,25)]),4)]
    emptychordlist = [(None, 1)]
    b = buildBar(randomizeObject([(chordlist,90),(emptychordlist,10)]))
    return b

def JazzBassD(chord,b):

    root = Note(chord[0])
    third = Note(chord[1])
    fifth = Note(chord[2])

    root.change_octave(-1)
    third.change_octave(-1)
    fifth.change_octave(-1)

    if len(chord) == 4:
        seventh = Note(chord[-1])
        seventh.change_octave(-1)
    else:
        ##same issue as JazzBassB, I think your trying to access the thrid note which is actually chord[2]
        #orginaly 4
        seventh = Note(chord[3])
        seventh.change_octave(-1)

    ninth = Note(chord[-1])
    ninth.change_octave(-1)
    chordlist = [(randomizeObject([(third,25),(seventh,25),(ninth,25),(None,25)]),4),(randomizeObject([(third,25),(seventh,25),(ninth,25),(None,25)]),4),(randomizeObject([(third,25),(seventh,25),(ninth,25),(None,25)]),4),(randomizeObject([(third,25),(seventh,25),(ninth,25),(None,25)]),4)]
    emptychordlist = [(None, 1)]
    b = buildBar(randomizeObject([(chordlist,90),(emptychordlist,10)]))
    return b


def RandBBassA(chord, b): #ghetto Gatsby

    root = Note(chord[0])
    third = Note(chord[1])
    fifth = Note(chord[2])
    seventh = Note(chord[-1])

    root.change_octave(-1)
    third.change_octave(-1)
    fifth.change_octave(-1)
    seventh.change_octave(-1)

    chordlist = [(root,8),(None,8),(None,4),(root,8),(None,8),(None,4)]
    emptychordlist = [(None,1)]
    b = buildBar(randomizeObject([(chordlist, 85), (emptychordlist, 15)]))
    return b

def RandBBassB(chord, b):

    root = Note(chord[0])
    third = Note(chord[1])
    fifth = Note(chord[2])
    seventh = Note(chord[-1])

    root.change_octave(-1)
    third.change_octave(-1)
    fifth.change_octave(-1)
    seventh.change_octave(-1)

    chordlist = [(root,2),(root,2)]
    emptychordlist = [(None, 1)]

    b = buildBar(randomizeObject([(chordlist,80),(emptychordlist,20)]))

    return b

def RandBBassC(chord, b):  #best part

    root = Note(chord[0])
    third = Note(chord[1])
    fifth = Note(chord[2])
    seventh = Note(chord[-1])

    root.change_octave(-1)
    third.change_octave(-1)
    fifth.change_octave(-1)
    seventh.change_octave(-1)

    chordlist = [(root,1)]
    emptychordlist = [(None, 1)]

    b = buildBar(randomizeObject([(chordlist, 75), (emptychordlist, 25)]))

    return b

def RandBBassD(chord, b):

    root = Note(chord[0])
    third = Note(chord[1])
    fifth = Note(chord[2])
    seventh = Note(chord[-1])

    root.change_octave(-1)
    third.change_octave(-1)
    fifth.change_octave(-1)
    seventh.change_octave(-1)
    
    chordlist = [(root, value.dots(value.eighth)),(root,8),(None,2)]
    emptychordlist = [(None, 1)]

    b = buildBar(randomizeObject([(chordlist, 75), (emptychordlist, 25)]))

    return b

#map of chord progressions based on genre
genreChordProgression = {
     "pop": [([1,5,6,4],10) , ([1,4,5,4],70) , ([4,5,6,3],20)],
    "r&b": [([4,5,3,2],10) , ([4,5,3,2],10),([4,2,6,3],80)],
    "jazz": [([2,5,1,1],30) , ([4,5,1,1],10),([2,5,3,1],15),([4,5,3,1],10),([4,5,1,6],10),([2,7,6,1],15),([2,5,3,3],10)],
}

#Sai
romanMap7ths = {
    1 : "I7",
    2 : "II7",
    3 : "III7",
    4 : "IV7",
    5 : "V7",
    6 : "VI7",
    7 : "VII7"
}

#Sai
romanMap6ths = {
    1 : "I6",
    2 : "II6",
    3 : "III6",
    4 : "IV6",
    5 : "V6",
    6 : "VI6",
    7 : "VII6"
}

#Sai 
romanMap1st = {
    1 : "I",
    2 : "II",
    3 : "III",
    4 : "IV",
    5 : "V",
    6 : "VI",
    7 : "VII"
}

#Sai
romanMap9ths = {
    1 : "I9",
    2 : "II9",
    3 : "III9",
    4 : "IV9",
    5 : "V9",
    6 : "VI9",
    7 : "VII9"
}

#Sai
genreRomanChords = {
    "pop" : romanMap1st,
    "r&b" : romanMap7ths,
    "jazz" : [romanMap6ths,romanMap7ths,romanMap9ths]
}

#Pattern types for pop and also based on type of track (instrument, bass, choir)
popPatternsInstrument = [PopA,PopB,PopC]
popPatternsBass = [PopBassA,PopBassB,PopBassC,PopBassD,PopBassE,PopBassF]

#Pattern types for R&B based on type of track (instrument, bass, choir)
rbPatternsInstrument = [RandBA,RandBB,RandBC,RandBE]
#rbPatternsInstrument = [RandBB,RandBA]
rbPatternsBass = [RandBBassA,RandBBassB,RandBBassC,RandBBassD]

#Pattern types of jazz and based on type of track (instrument, bass, choir)
jazzPatternsInstrument = [JazzA,JazzB,JazzC,JazzD,JazzE]
#jazzPatternsInstrument = [JazzE]
jazzPatternsBass = [JazzBassA1,JazzBassA2,JazzBassB,JazzBassC,JazzBassD]

patternMap = {
    "pop" : {"instrument" : popPatternsInstrument,
              "bass" : popPatternsBass
                } ,
    "jazz" : {"instrument" : jazzPatternsInstrument,
              "bass" : jazzPatternsBass
                } ,
    "r&b" : {"instrument" : rbPatternsInstrument,
              "bass" : rbPatternsBass
                } 
}



# (Sai)
#randomizer function()
#choiceContainer should have format of [(Object,Probability),(Object,Probability),...]        
#chooses specfic pattern under a genre
#retunrs a pattern function
def chooseGenrePattern(genre,trackType):
    #print("Genre: ",genre)
    #print("Track Type: ",trackType)
    randomIdx = randint(0,len(patternMap[genre][trackType])-1)
    return patternMap[genre][trackType][randomIdx]
    
# (Sai)
#finds interval
def findInterval(randomNum,intervals):
    for idx in range(0,len(intervals)):
        if(randomNum >= intervals[idx][0] and randomNum <= intervals[idx][1]):
            return idx

# (Sai)
#genreates a list of intervals(i.e [[1-20],[21-50],[51-100]])
def generateInterval(genre):
    #intialize interval
    intervals = [[1,genreChordProgression[genre][0][1]]]

    #iterate through chord progressions based on genre and add probablity 
    for chordProgression in (genreChordProgression[genre][1::]):
        intervals.append([intervals[-1][1] + 1,intervals[-1][1] + chordProgression[1]])

    return intervals

# (Sai)
def chordFixer(chord):
    badNoteList =['Ab','A','A#','Bb','B','B#','Cb','C','C#','Db','D','D#','Eb','E','E#','Fb','F','F#','Gb','G','G#']
    #change to note container
    chord = NoteContainer(chord)

    tempBadidx = badNoteList.index(chord[0].name)
    tempBadList = badNoteList[0:tempBadidx]
            
    for note in chord:
        note.change_octave(-1)
        
    return chord

# (Lawernce)
#converts the numerical coords to numerial values --> [5,1,2,3] --> ["V","I","II","III"]
def convertNumerial(chordProgression,userGenre):
    romanVal = []

    #based on roman map, is able to make the conversion between numbers to roman numerials
    for chordNum in chordProgression:
        if(userGenre == "jazz"):
            randomIdx = randint(0,2)
            romanVal.append(genreRomanChords[userGenre][randomIdx][chordNum])
        else:
            romanVal.append(genreRomanChords[userGenre][chordNum])

    return romanVal

# (Lawernce)
def convertToNotes(chordProgressionList,userGenre,key):
    noteChordProgressionList = []

     #[["C","A","B"]
    #[[5,1,2,2],[3,1,4,2],......] --> chordProgressionList --> [["C","C","G"],.....]
    for chordProgression in chordProgressionList:
        #chordProgression --> [5,1,2,2]
        #                      -> [A,B,C]
        numerialChordProgression = convertNumerial(chordProgression,userGenre)
        noteChordProgressionList.append(progressions.to_chords(numerialChordProgression,key))

    return noteChordProgressionList

          
# (Sai)
#builds [5,1,2,3] .. 
#generate accompanyment for song, and builds chords at specfic beats
def generateChordProgressionList(genre,BPM,songMin):
    #genertes interval list --> [[1-20],[21-100]]
    intervals = generateInterval(genre)
    chordProgressions = genreChordProgression[genre]

    #BPM(Beats per minute) * minutes of song  = Total Beats
    #Total Beats / 4 (4 beats in a bar) = Bars in song
    #(Measures / 4) = Number of Chord Progressions
    lenChordProgressions = (BPM * songMin) / (16)

    #stores final chord progression
    chordProgressionList = []

    #how many times do I run this? 
    #based on length of time, BPM, tempo?s
    for idx in range(0,int(lenChordProgressions)): #change the end val
        randomNum = randint(1,100)
        intervalIdx = findInterval(randomNum,intervals)
        chordProgressionList.append(chordProgressions[intervalIdx][0])

    return chordProgressionList

# (Sai)
#builds accompianmnet
def createAccompniment(noteChordProgressionList,instrumentIdx,genrePattern):
    #intialzing instrument
    m = MidiInstrument()
    m.instrument_nr = instrumentIdx

    #creating track and assigining the instrument
    fullTrack = Track()
    fullTrack.instrument = m
    
    #iterating through each chord in a chord-progression and creating a bar and appending to track
    for chordProgression in noteChordProgressionList:
        for chord in chordProgression:
            #genre --> randomizeFunction
            tempBar = Bar()
            #print("test-2?
            chord = chordFixer(chord)
            tempBar = genrePattern(chord,tempBar)
            #print("test-3?")
            #adding bar to full track
            fullTrack.add_bar(tempBar)

    return fullTrack


# (Lawernce)
def createTrack(genre,BPM,instrumentNum,songLen,trackType,noteChordProgressionList):
    #In the format of [[5,1,3,2],[2,3,1,1]]
    #this changes based on the type of track and genre (i.e instrument, choir, bass)
    genrePattern = chooseGenrePattern(genre,trackType)
    fullTrack = createAccompniment(noteChordProgressionList,instrumentNum,genrePattern)
    return fullTrack
    #return fullTrack

# (Sai)
#this assumes taht user genre, user-instrument,add
def generateCompo(userGenre,addInstrument,userInstrumentNumber,addBass,userBassNumber,userBPM,songLen,userKey):

    #initialzing composition(composed of mulitple tracks) and instrument track
    backtracker = Composition()

    #intializing different track
    instrumentalTrack = Track()
    bassTrack = Track()

    #Genre Chord List which all isntruments abide by
    numberChordProgressionList = generateChordProgressionList(userGenre,userBPM,songLen)

     #converts [[5,1,2,3],..] --> [[[A,B,C],[D,E,F]],...]
    noteChordProgressionList = convertToNotes(numberChordProgressionList,userGenre,userKey)
    
    if(addInstrument == 'Y'):
        instrumentalTrack = createTrack(userGenre,userBPM,userInstrumentNumber,songLen,"instrument",noteChordProgressionList)
        backtracker.add_track(instrumentalTrack)
    if(addBass == 'Y'):
        #get steel Drums number
        #steel drums is 114 
        bassTrack = createTrack(userGenre,userBPM,userBassNumber,songLen,"bass",noteChordProgressionList)
        backtracker.add_track(bassTrack)
   
    return [backtracker,instrumentalTrack,bassTrack]
    
#Credit goes to: https://github.com/mido/mido/issues/228
#Git-hub Users who helped:
#https://github.com/csarami
#https://github.com/olemb
#https://github.com/EFeru
#(Lawrence)
def melody_method(melody_track, bpm):
    melody_track = MidiFile(melody_track)
    MetaMessage('set_tempo', tempo = 250000)
    track = MidiTrack()
    melody_track.tracks.append(track)
    mytempo = bpm2tempo(bpm)
    track.append(MetaMessage('set_tempo',tempo=mytempo, time = 0))
    for msg in melody_track:
        if msg.type == 'set_tempo':
            bpm2tempo(msg.tempo)
    melody_track.save("tempOutputs/melody.mid")
   # print("bro")

 
#Credit goes to: https://github.com/mido/mido/issues/228
#Git-hub Users who helped:
#https://github.com/csarami
#https://github.com/olemb
#https://github.com/EFeru
#(Lawrence)        
def addDrums1(filename,BPM,only):
    drum_name = "Drums. MidiFiles/" + filename
    drum = MidiFile(drum_name)
    MetaMessage('set_tempo', tempo = 250000)
    track = MidiTrack()
    drum.tracks.append(track)

    mytempo = bpm2tempo(BPM)
    track.append(MetaMessage('set_tempo',tempo=mytempo, time = 0))
    for msg in drum:
         if msg.type == 'set_tempo':
            bpm2tempo(msg.tempo)
    drum.save("tempOutputs/drumTrack.mid")

    fs = FluidSynth("drums.sf2")
          
     #check if only drum is being played
    if(not only):
        fs.midi_to_audio("tempOutputs/drumTrack.mid","tempOutputs/drumTrack.wav")
    else:
        fs.midi_to_audio("tempOutputs/drumTrack.mid","outputBackTracker.wav")



#Credit goes to:https://stackoverflow.com/questions/2890703/how-to-join-two-wav-files-using-python  
#Author: https://stackoverflow.com/users/2908/jiaaro       
# (lawrence)
def compileTracksToWav(compo,BPM,addDrums,drumFileName):
   
    #initalize instrument to use
    fluidsynth.init("essential.sf2")

    #from mingus.midi import fluidsynth
    fs = FluidSynth("essential.sf2")

    #keep track of waves with note objects in them
    actualTracks = []
          
    #using the same midi file, and audio file to overwrite music file
    #skips first composition element
    for track in (compo[1::]):
        if(len(track) > 0):
            actualTracks.append(track)

    #print(actualTracks)
    #hear no tracks
    if(len(actualTracks) == 0 and addDrums != 'Y'):
        return

    #user only wants to hear one track
    if(len(actualTracks) == 1 and addDrums != 'Y'):
        print("Only one track!")
        midi_file_out.write_Track("tempOutputs/tempMidi.mid",actualTracks[0],BPM)
        fs.midi_to_audio("tempOutputs/tempMidi.mid","outputBackTracker.wav")
        return

    #hear only drums
    if(len(actualTracks) == 0 and addDrums != 'N'):
        addDrums1(drumFileName,BPM,True)
        return

    #Know there is at least one track in actual tracks
    midi_file_out.write_Track("tempOutputs/tempMidi.mid",actualTracks[0],BPM)
    fs.midi_to_audio("tempOutputs/tempMidi.mid","tempOutputs/tempSong.wav")
    currentOverlay = AudioSegment.from_wav("tempOutputs/tempSong.wav")
    
    for idx in range(0,len(actualTracks)-1):
        #creat wav file for track in front of me
        midi_file_out.write_Track("tempOutputs/tempMidi.mid",actualTracks[idx+1],BPM)
        fs.midi_to_audio("tempOutputs/tempMidi.mid","tempOutputs/tempSong.wav")

        #create next sound
        nextSound = AudioSegment.from_wav("tempOutputs/tempSong.wav")

        #overlay new sound
        currentOverlay = currentOverlay.overlay(nextSound,position=0)

    
    if(addDrums == 'Y'):
        #print("Drum-File-Name: ",drumFileName)
        addDrums1(drumFileName,BPM,False)
        beatSound = AudioSegment.from_wav("tempOutputs/drumTrack.wav")
        currentOverlay = currentOverlay.overlay(beatSound,position=0)

    currentOverlay.export("outputBackTracker.wav",format="wav")
  

#Solution Found:https://stackoverflow.com/questions/43679631/python-how-to-change-audio-volume
#Credit to user: https://stackoverflow.com/users/5936628/anil-m
#(Sai)
def mergeBackingTrack(melody_track,BPM):
    #print("melody_track")
    melody_method(melody_track,BPM)

    #from mingus.midi import fluidsynth
    fs = FluidSynth("essential.sf2")

    #turn melody midi to melody wav
    fs.midi_to_audio("tempOutputs/melody.mid","tempOutputs/melody.wav")
    melodySound = AudioSegment.from_wav("tempOutputs/melody.wav")

    # but let's make him *very* quiet
    melodySound += 9

    # save the output
    melodySound.export("tempOutputs/enhanceMelody.wav", "wav")

    #merge melody wav file to nacking track
    currentOverlay = AudioSegment.from_wav("outputBackTracker.wav")
    currentOverlay = currentOverlay.overlay(melodySound,position=0)

    currentOverlay.export("mergedMelody.wav",format="wav")


# (lawrence)
#diatonic keys
basicKeys = ['Gb', 'Db', 'Ab', 'Eb', 'Bb', 'F', 'C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#', 'G#', 'D#', 'A#']

# (Andres)
def handleYorN(message):
    print(message)

    while (True):
        userChoice = (input(message + "(Type in 'Y' for yes or 'N' for no)")).upper()
        
        if(userChoice == 'Y' or userChoice == 'N'):
            return userChoice
        else:
            print("Please enter a valid entry (Y or N)")

# (Sai)
def handleMenu():

    while(True):
        try:
            userGenre = int(input("Type in an Menu Option (1,2,3,4)"))
            
            if(userGenre < 1 or userGenre > 4):
                print("Value is out of range!(please type in in-bonuds range)")
            else:
                return userGenre
        except:
            print("Invalid input type! (please type in int)")
        
# (Sai)
def handleGenre():
    genreList = {"r&b","pop","jazz"}
    while(True):
        
        userGenre = (input("Type in Genre (type pop, r&b, or jazz")).lower()
            
        if(userGenre not in genreList):
            print("Genre does not exist!(please type in valid genre!)")
        else:
            return userGenre
    
# (Andres)
def handleSongLen():
    print("Enter the Desired Length of Back Tracker in format (M:SS) for example (2:30)")
    
    while True:
        userSongLen = input("Enter length of song (M:SS for example 2:30)")
            
        if(userSongLen.index(":") == -1 or len(userSongLen) != 4 or userSongLen[1] != ":" or userSongLen[0].isnumeric() == False or userSongLen[2:].isnumeric() == False or int(userSongLen[2::]) <= 59):
            userSongLen = float(userSongLen[0]) + (float(userSongLen[2::]) / 60)
            return userSongLen
        else:
            print("Invalid entry type (please type in format MM:SS")

# (Sai)
def handleBPM():
    print("What BPM (beats per minute do you want)? ")
    while True:
        try:
            userBPM = int(input("Enter BPM (i.e 120)"))
            return userBPM
        except:
            print("Invalid type entry! (please enter an int like 120)")
# (Sai)
def handleKey():
    
    basicKeys = ['Gb', 'Db', 'Ab', 'Eb', 'Bb', 'F', 'C', 'G', 'D', 'A', 'E', 'B', 'F#', 'C#', 'G#', 'D#', 'A#']


    while True:
        userKey = input("Pick a key (i.e C)")
        
        if(userKey not in basicKeys):
            print("Not a valid key! (look at the list of valid keys)")
        else:
            return userKey

# (Lawernce)
def handleUserFileName():
    print("Enter a valid file name")
    while True:
        try:
            userFileName = input("Enter a valid melody Midi file")
            MidiFile("melodyInputMidiFiles/" + userFileName)
            return "melodyInputMidiFiles/" + userFileName
        except:
            print("Invalid filename (please enter again) !")
# (Lawernce)
def handleInstrument(possibleChoices):
    print("Choose a valid instrument index in table")

    while True:
        try:
            instrumentIdx = int(input("Choose a valid instrument idx"))
            if(instrumentIdx not in possibleChoices):
                print("Not one of the avaiable choices! (look at the table for valid choice!)")
            else:
                return instrumentIdx
        except:
            print("Invalid entry type!(type in an index in the range)")

# (Lawernce)
def displayGenreInstruments(userGenre,trackType):

    #get map key (combines userGenre + trackType)
    #for example pop + chord = pop-chord
    userGenre = userGenre.lower()
    trackType = trackType.lower()

    mapKey = userGenre + trackType
    allInstruments = MidiInstrument.names
    possibleChoices = []

    genreInstrumentMap = { 
    #check actual mappings
    "popchord" : ["Acoustic Guitar (steel)","Electric Guitar (clean)",
    "Distortion Guitar","Overdriven Guitar", "Electric Piano 1"] ,
    "jazzchord" : ["Acoustic Grand Piano","Electric Guitar (jazz)"] ,
    "r&bchord" : ["Acoustic Grand Piano", "Acoustic Guitar (nylon)", "Electric Guitar (clean)"],
    "popbass" : ["Electric Bass (finger)","Electric Bass (pick)"],
    "jazzbass" : ["Acoustic Bass"], 
    "r&bbass" : ["Fretless Bass","Electric Bass (finger)"]
    }


    print("Idx |   Instrument Name     ")
    print("----|-----------------------")

    for instrument in genreInstrumentMap[mapKey]:
        possibleChoices.append(allInstruments.index(instrument))
        print(str(allInstruments.index(instrument)) + " | " + instrument)


    print()
    userInstrumentIdx = handleInstrument(possibleChoices)
    return userInstrumentIdx


# (Lawernce)
def displayGenre():
    print("     Genre List    ")
    print('------------------')
    print(" - Jazz")
    print(" - R&B")
    print(" - Pop")
    print("-------------------")

# (Lawernce)
def displayMenu():
    print("      Welcome to Backtrack Builder (type in a number for choice)    ")
    print("--------------------------------------")
    print("   - 1) Generate Backtracker    ")
    print("   - 2) Merge Midi File with Backtracker  ")
    print("   - 3) Display Sheet Music    ")
    print("   - 4) Exit ")
    print( "--------------------------------------")
    print("                                     ")

    
    

