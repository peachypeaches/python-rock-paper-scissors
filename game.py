import random


class RPS:
    valid_input = ["R", "P", "S"]
    # user_choice = []
    # computer_choice = []

    def user_input(self):
        self.user_choice = input(
            "Please pick an option between: \"R\", \"P\", \"S\": ")
        return self.user_choice

    def check_user_input(self, user_choice):
        while True:
            if self.user_choice not in self.valid_input:
                print("Please Pick a Valid Option")
                self.user_input()
            else:
                break

    def computer_input(self):
        self.computer_choice = random.choice(self.valid_input)
        return self.computer_choice

    def display_participant_input(self, user_choice, computer_choice):
        return print("Player({}) : CPU({})".format(self.user_choice, self.computer_choice))

    def result_check(self, user_choice, computer_choice):
        if self.user_choice == self.computer_choice:
            print("It's a tie. Go again!")
        elif self.user_choice == "P" and self.computer_choice == "R":
            print("Winner, you beat the System!!!")
            exit(1)

        elif self.computer_choice == "P" and self.user_choice == "R":
            print("Shucks, you lose to Computer!")

        elif self.computer_choice == "R" and self.user_choice == "S":
            print("Winner, you beat the System!!!")
            exit(1)

        elif self.computer_choice == "S" and self.user_choice == "R":
            print("Shucks, you lose to Computer!")

        elif self.computer_choice == "S" and self.user_choice == "P":
            print("Winner, you beat the System!!!")
            exit(1)

        elif self.computer_choice == "P" and self.user_choice == "S":
            print("Shucks, you lose to Computer!")

        else:
            print("Something went wrong, Please contact the developer")


def main():

    while True:
        obj = RPS()
        user_choice = obj.user_input()
        obj.check_user_input(user_choice)
        computer_choice = obj.computer_input()
        obj.display_participant_input(user_choice, computer_choice)
        obj.result_check(user_choice, computer_choice)


if __name__ == "__main__":
    main()
