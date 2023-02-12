#!/usr/bin/python3
"""
    Define the HBNBCommand class.
"""
import cmd
from models import storage
from models.base_model import BaseModel
import shlex


E_CLASS_MISS = "** class name missing **"
E_CLASS_NFOUND = "** class doesn't exist **"
E_ID_MISS = "** instance id missing **"
E_ATTR_MISS = "** attribute name missing **"
E_VALUE_MISS = "** value missing **"
CLS_NAMES = [
    "BaseModel",
]


class HBNBCommand(cmd.Cmd):
    """
        Entry point of the command interpreter.
        Launches an interactive command interpreters.
    """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_create(self, line):
        """
            Creates a new instance of BaseModel,
            saves it (to the JSON file) and prints the id.

            If the class name is missing, print
            ** class name missing **.
            If the class name doesn’t exist, print
            ** class doesn't exist **.
        """
        rules = [
            E_CLASS_MISS,
        ]
        args = self._validate_line(line, rules)
        if args is False:
            return

        cls_name = args[0]
        instance = eval(cls_name + "()")
        storage.new(instance)
        storage.save()
        print(instance.id)

    def help_create(self):
        """
            Prints create command help.
        """
        self._print_help([
            "Creates a new instance of BaseModel.",
            "Usage: create <class name>"
        ])

    def do_show(self, line):
        """
            Prints the string representation of an
            instance based on the class name and id.

            - If the class name is missing, prints
              ** class name missing **.
            - If the class name doesn’t exist, prints
              ** class doesn't exist **.
            - If the id is missing, prints
              ** instance id missing **.
            - If the instance of the class name doesn’t exist
              for the id, print ** no instance found **.
        """
        rules = [
            E_CLASS_MISS,
            E_ID_MISS
        ]
        args = self._validate_line(line, rules)
        if args is False:
            return

        key = "{}.{}".format(args[0], args[1])
        items = storage.all()
        if len(items) > 0 and key in items:
            item = items[key]
            if (item):
                print(item)
                return
        print("** no instance found **")

    def help_show(self):
        """
            Prints show command help.
        """
        self._print_help([
            "Prints the string representation of an instance.",
            "Usage: show <class name> <instance id>"
        ])

    def do_destroy(self, line):
        """
            Deletes an instance based on the class name and id.

            - If the class name is missing, prints
              ** class name missing **
            - If the class name doesn’t exist, prints
              ** class doesn't exist **
            - If the id is missing, prints
              ** instance id missing **
            - If the instance of the class name doesn’t exist for
              the id, prints ** no instance found **
        """
        rules = [
            E_CLASS_MISS,
            E_ID_MISS
        ]
        args = self._validate_line(line, rules)
        if args is False:
            return

        key = "{}.{}".format(args[0], args[1])
        res = storage.remove(key)
        if res is False:
            print("** no instance found **")
            return
        storage.save()

    def help_destroy(self):
        """
            Prints destroy command help.
        """
        self._print_help([
            "Deletes an instance based on the class name and id.",
            "Usage: delete <class name> <instance id>"
        ])

    def do_all(self, line):
        """
            Prints all string representation of all instances
            based or not on the class name.
        """
        items = storage.all()
        items = [items[k].to_dict() for k in items.keys()]
        if len(line.strip().split()) > 0:
            cls_name = line.strip().split()[0]
            if cls_name not in CLS_NAMES:
                print(E_CLASS_NFOUND)
                return
            items = filter(lambda v:
                           v["__class__"]
                           == cls_name, items)
            items = list(items)

        items = ["{}".format(item) for item in items]
        print(items)

    def help_all(self):
        """
            Prints all command help.
        """
        self._print_help([
            "Prints all string representation of all instances.",
            "Usage: all [<class name>]"
        ])

    def do_update(self, line):
        """
            Updates an instance based on the class name and
            id by adding or updating attribute.
            Only one attribute can be updated at the time.

            - If the class name is missing, prints
              ** class name missing **
            - If the class name doesn’t exist, prints
              ** class doesn't exist **
            - If the id is missing, prints
              ** instance id missing **
            - If the instance of the class name doesn’t exist
              for the id, print ** no instance found **
            - If the attribute name is missing, prints
              ** attribute name missing **
            - If the value for the attribute name doesn’t
              exist, print ** value missing **
        """
        rules = [
            E_CLASS_MISS,
            E_ID_MISS,
            E_ATTR_MISS,
            E_VALUE_MISS
        ]
        args = self._validate_line(line, rules)
        if args is False:
            return
        key = "{}.{}".format(args[0], args[1])
        update_args = args[2:]
        update_args.insert(0, key)
        storage.update(*update_args)
        storage.save()

    def help_update(self):
        """
            Prints update command help.
        """
        msg = ("Updates an instance based on the class name"
               + " and id by adding or updating attribute.")

        usge = ("Usage: update <class name> <instance's id> "
                + "<attribute name> <attribute value>")

        self._print_help([
            msg,
            usge
        ])

    def do_EOF(self, line):
        """CTRL-D to exit the program
        """
        return True

    def default(self, line):
        """Default command (e.g: when the user press enter
           without writing a command)
        """
        pass

    def do_help(self, line):
        """Displays help about other commands
        """
        return cmd.Cmd.do_help(self, line)

    def _print_help(self, lines):
        """
            Helper for buidling command help.
        """
        print("\n".join(lines), end="\n\n")

    def _validate_line(self, line, constraints):
        """
            Validate an argument line against contraints.
            Returns a list of parsed arguments or False
            if the arguments do not meet all the constraints.
        """
        args = shlex.split(line.strip())
        l_args = len(args)
        if l_args == 0 and E_CLASS_MISS in constraints:
            print(E_CLASS_MISS)
            return False
        if args[0] not in CLS_NAMES:
            print(E_CLASS_NFOUND)
            return False
        if l_args == 1 and E_ID_MISS in constraints:
            print(E_ID_MISS)
            return False
        if l_args == 2 and E_ATTR_MISS in constraints:
            print(E_ATTR_MISS)
            return False
        if l_args == 3 and E_VALUE_MISS in constraints:
            print(E_VALUE_MISS)
            return False

        return args


if __name__ == '__main__':
    HBNBCommand().cmdloop()
