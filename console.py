#!/usr/bin/python3
"""
This module contains a class that defines an
entry point to a command interpreter
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place
from models.amenity import Amenity
from models import storage


class HBNBCommand(cmd.Cmd):
    """create command interpreter"""

    prompt = "(hbnb) "

    def do_create(self, arg):
        """
        Create a instance and print its id
        """

        if arg:
            try:
                cls = globals()[arg]
                new_obj = cls()
                new_obj.save()
                print(new_obj.id)
            except KeyError:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, arg):
        """
        Display the string representation of an instance of a given id
        """
        if arg:

            args = arg.split()
            try:  # check if class name exits
                cls = globals()[args[0]]
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    name_id = args[0] + "." + args[1]
                    file_data = storage.all()
                    for key, value in file_data.items():
                        if key == name_id:
                            print(value)
                            return
                    print("** no instance found **")
            except KeyError:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, arg):
        """
        Delete a class instance of a given id
        """

        if arg:
            args = arg.split()
            try:  # check if class name exits
                cls = globals()[args[0]]
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    name_id = args[0] + "." + args[1]
                    file_data = storage.all()
                    for key, value in file_data.items():
                        if key == name_id:
                            del file_data[key]
                            storage.save()
                            return
                    print("** no instance found **")
            except KeyError:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_update(self, arg):
        """
            Update a class instance of a given id by adding or updating
            a given attribute key/value pair or dictionary.
        """
        if not arg:
            print("** class name missing **")
            return

        if arg:
            args = arg.split()

            try:
                cls = globals()[args[0]]
                if len(args) == 1:
                    print("** instance id missing **")
                else:
                    name_id = args[0] + "." + args[1]
                    loaded_data = storage.all()
                    for key, value in loaded_data.items():
                        if key == name_id:
                            if len(args) == 2:
                                print("** attribute name missing **")
                            elif len(args) == 3:
                                print("** value missing **")
                            else:
                                attr_name = args[2]
                                attr_value = args[3]
                                setattr(value, attr_name, attr_value)
                                storage.save()
                            return
                    print("** no instance found **")
            except KeyError:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, arg):
        """
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects.
        """

        all_objs = storage.all()
        if arg:
            try:
                cls = globals()[arg]
                for key, value in all_objs.items():
                    if type(value) == cls:
                        print(value)
            except KeyError:
                print("** class doesn't exist **")
        else:
            for key, value in all_objs.items():
                print(value)

    def emptyline(self):
        """an empty line + ENTER t execute anything"""
        pass

    def do_quit(self, line):
        """Exits the program"""
        exit(1)

    def do_EOF(self, line):
        """handles End of File"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
