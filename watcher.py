from inspect import signature
import sys

EMPTY_SIGNATURE_TYPE = "<class 'inspect._empty'>"


"""
A python dectorater to enforce type checks on your python functions
for your stupid colleagues who pass int type when you clearly told them to
pass string.
ヽ(ಠ_ಠ) ノ

"""


def parse_arguments(signature_object):
    """
    A function to parse signature object to return argument type

    parameters:
    signature_object -> Signature

    returns:
    types_list -> List
    """
    return ([repr(p.annotation).ljust(13)
             for p in signature_object.parameters.values()], signature_object.return_annotation)


def match_type(types, *args):
    """
   Matches types defined in the fucntion name to the given arguments/

   Parameters:
   types -> list
   args -> list

   returns:
   None if arguments match defined types
   Raises TypeError if not
    """

    for x, y in zip(types, args):
        if(str(type(y)) != x and x != EMPTY_SIGNATURE_TYPE):
            raise TypeError(
                f"Type mismatch value of type {type(y)} can not be assigned to parameter of type {x}")


def match_return_type(sig, val):
    if(type(val) != sig and str(sig) != EMPTY_SIGNATURE_TYPE):
        raise TypeError(
            f"Type mismatch value of type {type(val)} can not be assigned to return of type {sig}")
    return val


def watcher(f):
    def inner(*args, **kwargs):
        types, return_type = parse_arguments(signature(f))
        try:
            return match_type(
                types, *args) or match_return_type(return_type, f(*args, **kwargs))
        except TypeError as ve:
            tb = sys.exc_info()[2]
            raise ve.with_traceback(tb)
    return inner
