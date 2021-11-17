from repositories.problems import Problems


class UI:

    def __init__(self) -> None:
        self.temp_solution = Problems()

        self.run()

    def run(self):

        print("************************")
        print("***BOULDER PAL - 9000***")
        print("************************")
        print()
        print()
        while (True):
            print(
                "Whats next buddy [L]ist your problems, [C]reate new problem, [B]rowse problems), [Q]uit ")
            sel = input(">").upper()
            if sel == "Q":
                break
            if sel == "L":
                print(self.temp_solution.get_problems("test"))
                pass
            if sel == "C":
              #  self.temp_solution.add_problem("current_user")
                pass
            if sel == "B":
                # print(problems.get_problems(all_users))
                pass


if __name__ == "__main__":
    UI()
