# import the necessary packages
import argparse
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", required=True,
                help="name of the user")
args = vars(ap.parse_args())
# display a friendly message to the user
# print("Hi there {}, it's nice to meet you!".format(args["name"]))

print(f'Hi there {args["name"]}, it\'s nice to meet you!')
print(args)
print(ap.parse_args())


# python add_command_line_arguments.py --name Tea

