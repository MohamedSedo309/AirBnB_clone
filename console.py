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
    prompt = ("(hbnb)")
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def empty_line(self):
        """an empty line + ENTER t execute anything"""
        pass
    
    def do_quit(self, arg):
        """quit the console"""
        return True
    
    def do_EOF(self, arg):
        """EOF signal to exit the console"""
        print("")
        return True
    
    def do_help(self, arg):
        """List available commands with "help" or detailed help with "help cmd"."""
        if arg:
            try:
                doc = getattr(self, 'do_' + arg).__doc__
                if doc:
                    self.stdout.write('{}\n'.format(doc))
                    return
            except AttributeError:
                pass
            self.stdout.write('{} is not a valid command\n'.format(arg))
        else:
            commands = [cmd[3:] for cmd in dir(self) if cmd.startswith('do_')]
            self.stdout.write('Available commands:\n')
            self.stdout.write('\n'.join(sorted(commands)))
            self.stdout.write('\n')
    
if __name__ == '__main__':
    HBNBCommand().cmdloop()
