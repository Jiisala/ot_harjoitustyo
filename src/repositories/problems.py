
from entities.problem import Problem


class Problems:

    def __init__(self) -> None:
        self._problems_list = []
        self._problems_list.append(Problem("Sam", "portaat", "1a", "kotona", "esimerkkireitti esimerkinvuoks"))
        self._test_list = ["jotein", "muuta", "viel'"]

    def add_problem(self, ):#problem: Problem):
      #  self._problems_list.append(problem)
      pass
    
    def get_problems(self, user):
        if user == "test":
            return self._test_list
        if user == "all_users":
            return self._problems_list
        else:
            l = [p for p in  self._problems_list if p.get_auth() == user]
            return l
    #Fast method for testing, due to be scrapped
    def get_problems_temp(self):
        return self._problems_list[0]
problems = Problems()