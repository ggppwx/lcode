"""
This script downloads the code 
"""
import argparse
import requests
import json




class Problem(object):
    def __init__(self, id, title, url):
        self._id = id
        self._title = title
        self._url = url



class WebParser(object):
    def __init__(self):
        self._root_url = url
        self._problems = {}
        self.get_all_problems()

    def get_all_problems(self):
        """Get all problems """
        query = 'https://leetcode.com/api/problems/algorithms/'
        response = requests.get(query)
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



class LocalProblemCreator(object):
    pass



class ReadmeContent(object):
    pass





def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', help='config file')
    parser.add_argument('-i', '--index', help='index of the probelms' )
    args = parser.parse_args()


    print(args)
    problem_index = args.i





    # going over all problems
    for i in range(1, problem_index):

        # get the problem from internet







        pass








if __name__ == "__main__":
    main()
