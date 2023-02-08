#!/usr/bin/python3
"""module containing the code for command interpreter"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """foundational class for the interpreter"""
    prompt = '(hbnb) '
    valid_class = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_quit(self, arg):
        """exits the program if the user types the quit command"""
        return True

    def do_EOF(self, arg):
        """exits the interpreter when user types CTL+D (EOF command)"""
        return True
    
    def emptyline(self):
        return False

    def do_create(self, arg):
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return
        obj = models.classes[class_name]()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        obj_id = args[1]
        obj = models.storage.all().get(class_name + "." + obj_id)
        if obj is None:
            print("** no instance found **")
            return
        print(obj)

    def do_destroy(self, arg):
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        obj = models.storage.all().get(class_name + "." + obj_id)
        if obj is None:
            print("** no instance found **")
            return
        del obj
        storage.save()
        return

    def do_all(self, arg):
        args = line.split()
        all_objects = storage.all()
        if len(args) == 0:
            print([str(obj) for obj in all_objects.values()])
        elif args[0] in models.classes:
            print([str(obj) for obj in all_objects.values()
                if type(obj).__name__ == args[0]])
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        obj_id = args[1]
        if obj_id not in storage.all():
            print("** no instance found **")
            return
        obj = storage.all()[obj_id]
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        attr_name = args[2]
        if attr_name in ["id", "created_at", "updated_at"]:
            print("** cannot update id, created_at, and updated_at attributes **")
            return
        attr_value = args[3].strip('"')
        setattr(obj, attr_name, type(getattr(obj, attr_name))(attr_value))
        obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
