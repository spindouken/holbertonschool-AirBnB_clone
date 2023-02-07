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
	import re


	valid_class = {
	    "BaseModel": BaseModel,
	    "User": User,
	    "State": State,
	    "City": City,
	    "Amenity": Amenity,
	    "Place": Place,
	    "Review": Review
	}


class HBNBCommand(cmd.Cmd):
    """foundational class for the interpreter"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """exits the program if the user types the quit command"""
        return True

    def do_EOF(self, arg):
        """exits the interpreter when user types CTL+D (EOF command)"""
        return True
    
    def emptyline(self):
        return False

    def do_create(self, arg):
        pass

    def do_show(self, arg):
        pass

    def do_destroy(self, arg):
        pass

    def do_destroy(self, arg):
        pass

    def do_all(self, arg):
        pass

    def do_update(self, arg):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
