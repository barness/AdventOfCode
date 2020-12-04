from argparse import ArgumentParser
import sys


def count_num_trees(right, down):
    location = 0
    trees_encountered = 0
    count_line = down
    with open("/app/inputs/toboggan_trajectory.txt", "r") as input_file:
        for line in input_file:
            if count_line == 0:
                count_line = down
                if location > len(line) - 2:
                    location = location - (len(line)-1)
                if line[location] == '#':
                    trees_encountered += 1
            count_line -= 1
            # print('location', location)
            # print('trees_encountered', trees_encountered)
            # print(" ")
            location += right
            # print('increment', location)

    return trees_encountered


def all_slopes():
    slope1=count_num_trees(1,1)
    slope2=count_num_trees(3,1)
    slope3=count_num_trees(5,1)
    slope4=count_num_trees(7,1)
    slope5=count_num_trees(1,2)

    return slope1*slope2*slope3*slope4*slope5

def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--check", type=str, help="")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    if args.check == "NumTrees":
        count_type = "NumTrees"
    else:
        print("Invalid --check argument provided")
        sys.exit(1)

    print("Number of trees encountered:", all_slopes())
