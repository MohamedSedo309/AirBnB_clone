#!/usr/bin/python3

import cmd
import re
from shlex import split


    
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
