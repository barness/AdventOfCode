import sys
from argparse import ArgumentParser


def all_answered():
    with open("/app/inputs/custom_customs.txt", "r") as input_file:
        total_yes = 0
        person_list = []
        for person in input_file:
            answer_list = []
            if person == '\n':
                #print(person_list)
                total_yes += common_letters(person_list)
                person_list = []
            else:
                for answer in person:
                    if answer != '\n':
                        answer_list.append(answer)
                person_list.append(answer_list)
        total_yes += common_letters(person_list)
        return total_yes


def common_letters(person_list):
    common_letters = []
    for letter in person_list[0]:
        keep_letter = True
        for answers in person_list:
            if letter not in answers:
                keep_letter = False
        if keep_letter:
            common_letters.append(letter)
    return len(common_letters)


def sum_answered():
    with open("/app/inputs/custom_customs.txt", "r") as input_file:
        yes_list = []
        total_yes = 0
        for person in input_file:
            if person == '\n':
                total_yes += len(yes_list)
                yes_list = []
            for answer in person:
                if answer not in yes_list and answer != '\n':
                    yes_list.append(answer)
        total_yes += len(yes_list)
        return total_yes


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("--q", type=str, help="The type of password rule to use. Can be SumAnswered or AllAnswered.")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    if args.q == "SumAnswered":
        answer = sum_answered()
    elif args.q == "AllAnswered":
        answer = all_answered()
    else:
        print("Invalid --q argument provided")
        sys.exit(1)
    print("The answer is ", answer)