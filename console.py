#!/usr/bin/python3
"""based console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """based command interpreter for BNB clone"""
        prompt = '(hbnb) '

    def do_quit(self, arg):
        """You're just going to quit, eh?!"""
        return True

    def do_EOF(self, arg):
        """Very well, goodbye!"""
        return True

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
