#!/usr/bin/python3

import cmd
import re
from shlex import split

def parse(arg):
    curly_brackets = re.search(r"\{(.*?)\}", arg)
    square_brackets = re.search(r"\[(.*?)\]", arg)
    if curly_brackets is None:
        if square_brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            text_till_brackets = split(arg[:square_brackets.span()[0]])
            splitted_tokens = [i.strip(",") for i in text_till_brackets]
            splitted_tokens.append(square_brackets.group())
            return splitted_tokens
    else:
        text_till_brackets = split(arg[:curly_brackets.span()[0]])
        splitted_tokens = [i.strip(",") for i in text_till_brackets]
        splitted_tokens.append(curly_brackets.group())
        return splitted_tokens
    
class HBNBCommand(cmd.Cmd):
    """create command interpreter"""
    prompt = ("(hbnb) ")
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """an empty line + ENTER t execute anything"""
        pass
    
    def do_quit(self, arg):
        """quit the console"""
        return True
    
    def do_EOF(self, arg):
        """EOF signal to exit the console"""
        print("")
        return True

    def help_quit(self):
        """Help documentation for the quit command"""
        print('Quit command to exit the program')

    def help_EOF(self):
        """Help documentation for the EOF command"""
        print('EOF command to exit the program')
    
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
