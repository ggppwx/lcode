"""
This script downloads the code 
"""
import argparse
import requests
import json




class Problem(object):
    def __init__(self, id, title, url):
        self.id = id
        self.title = title
        self.url = url



class WebParser(object):
    def __init__(self):
        self._problems = {}
        self.get_all_problems()

    def get_all_problems(self):
        """Get all problems """
        query = 'https://leetcode.com/api/problems/algorithms/'
        response = requests.get(query, verify=False)
        content = json.loads(response.content)
        problems = content['stat_status_pairs']
        for problem in problems:
            id = problem['stat']['question_id']
            title = problem['stat']['question__title']
            slug = problem['stat']['question__title_slug']
            url = '' + slug
            self._problems[id] = Problem(id, title, url)


    def get_problem(self, id):
        """Get the problem info based on id"""
        return self._problems.get(id, {})



class TemplateCreator(object):
    def __init__(self, dir):
        self._dir = dir
        

    def create_template(self, problem):
        """Create a local problem template
        dir
        - problem name
        -- README
        -- problem.py
        -- problem.cpp
        """
        dir_name = problem.title
        # generate a dir with title



        # generate file: readme
        # generate file: python code 


class ReadmeContent(object):
    pass





def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', help='config file')
    parser.add_argument('-i', '--index', help='index of the probelms' )
    args = parser.parse_args()


    print(args)
    problem_index = int(args.i)


    web_parser = WebParser()
    problem = web_parser.get_problem(problem_index)


    # going over all problems
    for i in range(1, problem_index):

        # get the problem from internet







        pass








if __name__ == "__main__":
    main()
