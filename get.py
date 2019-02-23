"""
This script downloads the code 
"""
import argparse
import requests
import json
import os
import string
import urllib.parse

PROBELM_DIR = 'Algorithm'


class Problem(object):
    def __init__(self, id, title, slug,  url):
        self.id = id
        self.title = title
        self.slug = slug
        self.url = url


    def fillDescription(self):
        #print(connection.read())
        #soup = BeautifulSoup(connection)
        #body = soup.find('body')
        #app = body.find('div', {'id' : 'app'})
        #print(app.prettify())
        pass

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
            id = problem['stat']['frontend_question_id']
            title = problem['stat']['question__title']
            slug = problem['stat']['question__title_slug']

            url = 'https://leetcode.com/problems/' + slug
            self._problems[id] = Problem(id, title, slug,  url)



    def get_problem(self, id):
        """Get the problem info based on id"""
        # TBD: use beautiful soup to get the description 
        problem = self._problems.get(id, {})
        problem.fillDescription()
        return problem





class TemplateCreator(object):
    def __init__(self, dir):
        self._dir = dir
        self._templates = {}

        with open('source_code.py.tmpl') as f:
            self._templates['py'] =   string.Template( f.read() )

        

    def create_template(self, problem):
        """Create a local problem template
        dir
        - problem name
        -- README
        -- problem.py
        -- problem.cpp
        """
        print('creating ... ')
        dir_name = self._dir + '/' + str(problem.id) + '. ' + problem.title
        # generate a dir with title

        try:
            print(dir_name)
            os.mkdir(dir_name)
        except FileExistsError:
            print("Dir ", dir_name, " already exists ")

        # generate file: readme
        with open(dir_name + '/' + 'README.md', 'w') as f:
            f.write('# test')

        # generate file: python code 
        file_path  = dir_name + '/' + problem.slug + '.py'
        substitutes = {'title' : problem.title, 'url': problem.url}
        py_source = self._templates['py'].substitute(substitutes)
        with open(file_path, "w") as f:
            f.write( py_source)

class ReadmeContent(object):
    def __init__(self, dir, dest='./README.md'):
        self._dest = dest
        self._dir = dir
        self._problems = []
        self.get_info()
        with open('README.md.tmpl') as f:
            self._template = string.Template(f.read())

    def get_info(self):
        """Get probelm in info """
        for root, dirs, _ in os.walk(self._dir):
            for dir_name in dirs:
                print(dir_name)
                for problem_dir, _, files in os.walk(os.path.join(root, dir_name)):
                    for file_name in files:
                        print(file_name)
                        if file_name.endswith('.py'):
                            id = dir_name.split('.')[0]
                            name = dir_name.split('.')[1].strip(' ')
                            location = os.path.join('.', problem_dir, file_name)
                            problem_dir_quoted = urllib.parse.quote(dir_name)
                            python_link  = os.path.join('https://github.com/ggppwx/lcode/blob/master/Algorithm', problem_dir_quoted , file_name)
                            slug = os.path.splitext(file_name)[0]
                            url = 'https://leetcode.com/problems/' + slug
                            problem = { 'id': id, 'name': name, 'location' : location, 'url': url, 'python': python_link}
                            self._problems.append(problem)
            

    def create_readme_content(self):
        with open(os.path.join(self._dest), 'w') as f:
            content = self._template.substitute()
            f.write(content)
            f.write("| Id |Name| Title | Solution |\n")
            f.write("|----|----|-------|----------|\n")
            for problem in self._problems:
                line = "|{id}|{name}|[{name}]({url})|[python]({python})|\n".format(**problem)
                f.write(line)


                


def main():
    parser = argparse.ArgumentParser()
    #parser.add_argument('-c', '--config', help='config file')
    parser.add_argument('-i', '--index', help='index of the probelms' )
    parser.add_argument('-r', '--refresh', action="store_true", default = False,  help='refresh')
    args = parser.parse_args()


    print(args)

    if args.index is not None:
        problem_index = int(args.index)


        web_parser = WebParser()
        problem = web_parser.get_problem(problem_index)


        tmpl = TemplateCreator(PROBELM_DIR)
        tmpl.create_template(problem)


        readme_content = ReadmeContent(PROBELM_DIR)
        readme_content.create_readme_content()

    elif args.refresh:
        print('---refresh-----')
        readme_content = ReadmeContent(PROBELM_DIR)
        readme_content.create_readme_content()
    


if __name__ == "__main__":
    main()
