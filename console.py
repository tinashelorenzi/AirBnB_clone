#!/usr/bin/python3

"""Modules for the command interpreter.
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Defines the command interpreter."""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit The program."""
        return True

    def do_EOF(self, arg):
        """Exits the program by using  EOF condition."""
        print()
        return True

    def do_create(self, args):
        """Create a new instance"""
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]

    def empty_line(self):
        """Handles empty line"""
        return False

    def do_show(self, arg):
        """
        Prints the string represantation of an instance"""


if __name__ == '__main__':
    HBNBCommand().cmdloop()
