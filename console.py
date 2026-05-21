#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

# Map all newly added models into the validation interface
VALID_CLASSES = {
    "BaseModel": BaseModel,
    "User": User,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Place": Place,
    "Review": Review
}


class HBNBCommand(cmd.Cmd):
    """
    Command interpreter for the HBNB application.
    """
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF signal to cleanly exit the program (Ctrl+D)"""
        print("")
        return True

    def emptyline(self):
        """Do nothing when receiving an empty line + ENTER"""
        pass

    def do_create(self, arg):
        """Creates a new instance, saves it and prints the id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in VALID_CLASSES:
            print("** class doesn't exist **")
            return
        
        new_instance = VALID_CLASSES[args[0]]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on class and id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in VALID_CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        
        key = "{}.{}".format(args[0], args[1])
        all_objects = storage.all()
        if key not in all_objects:
            print("** no instance found **")
            return
        
        print(all_objects[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in VALID_CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        
        key = "{}.{}".format(args[0], args[1])
        all_objects = storage.all()
        if key not in all_objects:
            print("** no instance found **")
            return
        
        del all_objects[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on class."""
        args = shlex.split(arg)
        all_objects = storage.all()
        obj_list = []

        if args:
            if args[0] not in VALID_CLASSES:
                print("** class doesn't exist **")
                return
            for key, obj in all_objects.items():
                if key.split('.')[0] == args[0]:
                    obj_list.append(str(obj))
        else:
            for obj in all_objects.values():
                obj_list.append(str(obj))
                
        print(obj_list)

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in VALID_CLASSES:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        
        key = "{}.{}".format(args[0], args[1])
        all_objects = storage.all()
        if key not in all_objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        
        obj = all_objects[key]
        attr_name = args[2]
        attr_val = args[3]

        if attr_name in ("id", "created_at", "updated_at"):
            return

        # Explicit data type recovery evaluation
        if hasattr(obj, attr_name):
            try:
                attr_val = type(getattr(obj, attr_name))(attr_val)
            except ValueError:
                pass
        else:
            if attr_val.isdigit():
                attr_val = int(attr_val)
            else:
                try:
                    attr_val = float(attr_val)
                except ValueError:
                    pass

        setattr(obj, attr_name, attr_val)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()