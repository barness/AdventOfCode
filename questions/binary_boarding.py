import math
from argparse import ArgumentParser
import sys


def process_binary(input, up, max):
    high = max
    low = 0

    for binary in input:
        if binary == up:
            low = math.ceil((high + low) / 2)
        else:
            high = math.floor((high + low) / 2)

    return low


def highest_id():
    with open("/app/inputs/binary_boarding.txt", "r") as input_file:
        highest_seat_id = 0
        for line in input_file:
            row = process_binary(line[:7], "B", 127)
            column = process_binary(line[7:], "R", 7)
            seat_id = (row * 8) + column
            if seat_id > highest_seat_id:
                highest_seat_id = seat_id
        return highest_seat_id


def your_id():
    with open("/app/inputs/binary_boarding.txt", "r") as input_file:
        seat_ids = []
        for line in input_file:
            row = process_binary(line[:7], "B", 127)
            column = process_binary(line[7:], "R", 7)
            seat_id = (row * 8) + column
            seat_ids.append(seat_id)
        for id in seat_ids:
            if (id + 1 not in seat_ids) and id + 2 in seat_ids:
                return id + 1


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--q", type=str, help="The type of password rule to use. Can be HighestID or YourID.")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    if args.q == "HighestID":
        answer = highest_id()
    elif args.q == "YourID":
        answer = your_id()
    else:
        print("Invalid --q argument provided")
        sys.exit(1)
    print("The answer is ", answer)
