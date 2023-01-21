
"""
References
https://book.pythontips.com/en/latest/args_and_kwargs.html
"""

def process_names(id: int, *args):
    print("id:{}".format(id))
    for arg in args:
        print("arg: {}".format(arg))

process_names(1, "folau","kaveinga","jr")

def process_levels(id: int, **args):
    print("id:{}".format(id))
    for arg in args:
        print("arg name: {}, value={}".format(arg, args[arg]))

process_levels(1, level1="folau", level2="kaveinga",level3="jr")

print("\nno ** args\n")
process_levels(1)