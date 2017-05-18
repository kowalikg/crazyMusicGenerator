from argparse import ArgumentParser
from FunctionGenerator import FunctionGenerator
from NoteGenerator import NoteGenerator
from SongGenerator import SongGenerator

def add_arguments(argparser): #add arguments
    argparser.add_argument('--name', type = str, help = 'name for song to output, default: mytrack', default = "mytrack")
    argparser.add_argument('--speed', type = int, help = 'your song\'s speed [10, 10000], default: 120', default = 120)
    argparser.add_argument('--mode', type = int, help = '0 - curvy style, 1 - slight style, default: 0', default = 0)
    argparser.add_argument('--notes_range', type = int, help = 'range of notes [1,60] up and down from 60, default: 30 (notes from 30 to 90)', default = 30)
    argparser.add_argument('--zeros_amount', type = int, help = 'max amount of zero places to function [1,100], default: 10', default = 10)
    argparser.add_argument('--zeros_range', type = int, help = 'range for +- zero places [1,1000], default: 10', default = 10)
    argparser.add_argument('--field', type = int, help = 'range of the +- field of the function [10,10000], default: 1000', default = 1000)
    argparser.add_argument('--notes_amount', type = int, help = 'how many notes in song [10,10000], default: 100', default = 100)
    return argparser

def check_arguments(args): #check if arguments are correct
    if(args.speed < 10 or args.speed > 10000):
        print("Wrong speed")
        return False
    if (int(args.mode) not in (0,1)):
        print("Wrong mode")
        return False
    if (args.notes_range < 1 or args.notes_range > 60 ):
        print("Wrong notes range")
        return False
    if (args.zeros_amount < 1 or args.zeros_amount > 100):
        print("Wrong number of zero places")
        return False
    if (args.zeros_range < 1 or args.zeros_range > 1000):
        print("Wrong range of zero places")
        return False
    if (args.field < 10 or args.field > 10000):
        print("Wrong field of the function")
        return False
    if (args.notes_amount < 10 or args.notes_amount > 10000):
        print("Wrong notes amonut")
        return False
    return True


argparser = ArgumentParser(description = 'Generate some crazy music based on mathematics (math is crazy)')
argparser = add_arguments(argparser)

args = argparser.parse_args()

if (check_arguments(args)):
    function_generator = FunctionGenerator(args.zeros_range, args.zeros_amount);
    function = function_generator.generate_function()
    note_generator = NoteGenerator(args.field, args.notes_amount)
    notes = note_generator.generate_notes(function)

    file_name = args.name + ".mid"
    song_generator = SongGenerator(file_name, args.speed, args.mode, args.notes_range, notes)
    song_generator.generate_song()
