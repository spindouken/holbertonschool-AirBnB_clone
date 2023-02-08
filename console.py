#!/usr/bin/python3
"""module containing the code for command interpreter"""
import cmd
from models.base_model import *
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """foundational class for the interpreter"""
    prompt = '(hbnb) '
    classes = ["Review", "Place", "State",
               "User", "BaseModel", "City", "Amenity"]
    cantDeal = ["created_at", "updated_at", "id"]

    def do_quit(self, arg):
        """exits the program if the user types the quit command"""
        return True

    def do_EOF(self, arg):
        """exits the interpreter when user types CTL+D (EOF command)"""
        return True

    def emptyline(self):
        """hard pass"""
        pass

    def do_create(self, arg):
        """creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.classes:
            print("** class doesn't exist **")
            return
        new_model = eval(arg + "()")
        new_model.save()
        print(new_model.id)

    def do_show(self, arg):
        """prints the string representation of an instance
        based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        all_models = storage.all()
        for key, value in all_models.items():
            class_name, id = key.split(".")
            if class_name == args[0] and id == args[1]:
                print(value)
                return
        print("** no instance found **")

    def do_destroy(self, arg):
        """deletes an instance based on the class name
        and id (save the change into the JSON file)"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        all_models = storage.all()
        for key in list(all_models.keys()):
            class_name, id = key.split(".")
            if class_name == args[0] and id == args[1]:
                del all_models[key]
                storage.save()
                return
        print("** no instance found **")

    def do_all(self, arg):
        """prints all string representations of all
        instances based or not on the class name"""
        all_models = storage.all()
        if not arg:
            print([str(value) for value in all_models.values()])
            return
        if arg not in self.classes:
            print("** class doesn't exist **")
            return
        print([str(value) for key, value in all_models.items() if key.startswith(arg)])

    def do_update(self, arg):
        """Updates an instance based on class name and id
        by adding or updating attribute"""
        args = arg.split(maxsplit=3)
        num_args = len(args)
        if num_args < 4:
            if num_args == 0:
                print("** class name missing **")
                return
            elif num_args == 1:
                print("** instance id missing **")
                return
            elif num_args == 2:
                print("** attribute name missing **")
                return
            elif num_args == 3:
                print("** value missing **")
                return
        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        key = "{}.{}".format(args[0], args[1])
        obj = storage.all().get(key)
        if obj is None:
            print("** no instance found **")
            return
        if args[2] in HBNBCommand.cantDeal:
            return
        try:
            setattr(obj, args[2], eval(args[3]))
        except Exception as error:
            print(error)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
