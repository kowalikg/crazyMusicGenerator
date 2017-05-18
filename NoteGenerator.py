class NoteGenerator:
    def __init__(self, start_x, tones_amount):
        self.__start_x = start_x #where to start -> x from [-start_x ... 0 ... start_x]
        self.__tones_amount = tones_amount #how many tones

    def __f_range(self, step = 1.0): #range with possible floating step
        x = -self.__start_x
        while x < self.__start_x:
            yield x
            x += step

    def generate_notes(self, function):
        notes = [] #generated list of notes

        step = (self.__start_x * 2) / self.__tones_amount #what is the step

        for x in self.__f_range(step):
            notes.append(int(function(x)))

        return notes


