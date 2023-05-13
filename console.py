#!/usr/bin/python3

"""Modules for the command interpreter.
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.city import City
from models.review import Review
from models.place import Place
from models.state import State
from models.user import User
from models.amenity import Amenity
import json

classes = {"BaseModel": BaseModel, "User": User, "State": State, 
           "Place": Place, "Amenity": Amenity, "Review": Review, "City": City}


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
        elif args not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            ins = eval([args])
            ins.save
            print(ins.id)

    def empty_line(self):
        """Handles empty line"""
        pass

    def do_show(self, args):
        """Prints str representation of an instance"""
        try:
            class_name, instance_id = args.split()
        except ValueError:
            print("** class name and/or instance id missing **")
            return

        if class_name not in classes:
            print("** class doesn't exist **")
            return

        instance = storage.get(class_name, instance_id)
        if instance is None:
            print("** no instance found **")
        else:
            print(instance)
    def do_destroy(self,args):
        """ Deletes an instance based on the class name and id """
        args = args.split()
        if not args:
            print("** class name missing **")
            return
        elif len(args) < 2:
            print("** instance id missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        for v, k in storage.all().items():
            if args[1] == v.id:
                del storage.all()[k]
                storage.save()
                return
        print("** no instance found **")

        



if __name__ == '__main__':
    HBNBCommand().cmdloop()
