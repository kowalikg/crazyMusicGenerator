from random import randint
from miditime.miditime import MIDITime

class SongGenerator:
    def __init__(self, file_name, song_speed, song_mode, tones_range, notes):
        self.song = MIDITime(song_speed, file_name) #song
        self.song_mode = song_mode #if curvy or slight
        self.tones_range = tones_range # (60 - range ... 60 ... 60 + range)
        self.notes = notes #list with notes

    def generate_song(self):
        bit = 0 #start bit counter
        notes = [] #cut notes

        main_note = 60 #begin with 60 (C0)
        prev_note = 0 #previous note (needed to slighty style)

        for note in self.notes:
            note_details = [] #list to put in main notes list

            note_details.append(bit) # at n bit
            bit += 1

            main_note = self.generate_single_note(self.song_mode, note, prev_note, main_note) #generate note
            note_details.append(main_note)
            prev_note = note #set previous as current

            note_details.append(127) #velocity
            note_details.append(randint(0, 10)) #duration of note

            notes.append(note_details) #add note details do main notes list

        print("Notes details:")
        self.song.add_track(notes) #add list to song
        self.song.save_midi() #save song
        print("Song succesfully saved!")

    def generate_single_note(self, mode, current_note, prev_note, main_note): #generate note using a note list
        start_note = 60 #begin with c0

        if mode == 0: #if curvy then return note parsed to [60 - tones_range ... 60 ... 60 + tones_range]
            return current_note % (self.tones_range * 2) + (start_note - self.tones_range)
        else: #if slightly then main note depends on previous note
            if (prev_note > current_note > (start_note - self.tones_range)) :
                return main_note - 1
            elif (prev_note < current_note < (start_note + self.tones_range)):
                return main_note + 1
            return main_note
