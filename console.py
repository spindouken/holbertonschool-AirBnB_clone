#!/usr/bin/python3
"""module containing code for command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """foundational interpreter class"""
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
