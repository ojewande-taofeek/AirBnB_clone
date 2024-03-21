#!/usr/bin/python3
"""contains the entry point of the command interpreter"""
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
all_class = ["BaseModel", "User", "City", "Place",
             "Review", "State", "Amenity"]


class HBNBCommand(cmd.Cmd):
    """The command interpreter"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """Overrides the default EOF method"""
        return True
    
    def do_quit(self, line):
        """Terminates the interpreter"""
        return True
    
    def emptyline(self):
        """Overrides the default emptyline"""
        pass

    # def postloop(self):
    #    """To decide what happens when a loop is terminated"""
    #    print()

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        line_parsed = shlex.split(line)
        if len(line_parsed) == 0:
            print("** class name missing **")
            return
        if line_parsed[0] not in all_class:
            print("** class doesn't exist **")
            return
        class_cmd = globals()[line_parsed[0]]
        new_instance = class_cmd()
        new_instance.save()
        print(new_instance.id)
    
    def do_show(self, line):
            """Shows an instance based on its class name and id"""
            line_parsed = shlex.split(line)
            if len(line_parsed) == 0:
                print("** class name missing **")
                return
            if line_parsed[0] not in all_class:
                print("** class doesn't exist **")
                return
            if len(line_parsed) == 2:
                try:
                    key = "{}.{}".format(line_parsed[0], line_parsed[1])
                    all_objects = storage.all()
                    print(all_objects[key])
                except KeyError:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
                
    def do_destroy(self, line):
            """Shows an instance based on its class name and id"""
            line_parsed = shlex.split(line)
            if len(line_parsed) == 0:
                print("** class name missing **")
                return
            if line_parsed[0] not in all_class:
                print("** class doesn't exist **")
                return
            if len(line_parsed) == 2:
                try:
                    key = "{}.{}".format(line_parsed[0], line_parsed[1])
                    all_objects = storage.all()
                    del all_objects[key]
                    storage.save()
                except KeyError:
                    print("** no instance found **")
            else:
                print("** instance id missing **")

    def do_all(self, line):
        """Prints all string representation of all
            instances based or not on the class name
        """
        line_parsed = shlex.split(line)
        all_objects = storage.all()
        if len(line_parsed) == 0:
            for key in all_objects.keys():
                print(all_objects[key])
            return
        elif len(line_parsed) == 1:
            if line_parsed[0] in all_class:
                class_name = line_parsed[0]
                if all_objects:
                    for key in all_objects.keys():
                        if key.startswith(class_name):
                            print(all_objects[key])
            else:
                print("** class doesn't exist **")

    def do_update(self, line):
        """Updates an instance based on the class
           name and id by adding or updating attribute
           (save the change into the JSON file)
        """
        line_parsed = shlex.split(line)
        if len(line_parsed) == 0:
            print("** class name missing **")
            return
        if line_parsed[0] not in all_class:
            print("** class doesn't exist **")
            return
        if len(line_parsed) == 1:
            print("** instance id missing **")
            return
        if len(line_parsed) == 2:
            print("** attribute name missing **")
            return
        if len(line_parsed) == 3:
            print("** value missing **")
            return
        if len(line_parsed) >= 4:
            try:
                key = "{}.{}".format(line_parsed[0], line_parsed[1])
                all_objects = storage.all()
                obj = all_objects[key]
                setattr(obj, line_parsed[2], line_parsed[3])
                storage.save()
            except KeyError:
                print("** no instance found **")
    
    def do_count(self, line):
        """Count the number of instances of a class"""
        line_parsed = shlex.split(line)
        if len(line_parsed) == 0 or len(line_parsed) > 1:
            return
        if line_parsed[0] in all_class:
            counter = 0
            all_objects = storage.all()
            for key in all_objects.keys():
                if key.startswith(line_parsed[0]):
                    counter += 1
            print(counter)
            return

    def default(self, line):
        """Execute other commands"""
        line = line.replace(".", " ").replace("(", " ").replace(")", "")
        line = line.replace(",", "")
        line_parsed = shlex.split(line)
        line_len = len(line_parsed)
        try:
            # class_name = line_parsed[0]
            if line_len == 1:
                mtd_str = line_parsed[0]
            else:
                mtd_str = line_parsed[1]
        except IndexError:
            return
        new_line = ""
        if line_len > 1:
            for i in range(line_len):
                if i == 1:
                    continue
                new_line += line_parsed[i] + " "
        # print(new_line)
        # if class_name in all_class:
        try:
            called_mtd = getattr(self, "do_" + mtd_str)
            if called_mtd:
                called_mtd("{}".format(new_line))
        except AttributeError:
            pass
        # else:
        #    pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()