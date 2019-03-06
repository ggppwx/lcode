"""
This script downloads the code 
"""
import argparse
import requests
import json
import os
import string
import urllib.parse
from collections import defaultdict
import datetime

PROBELM_DIR = 'Algorithm'


class Problem(object):
    def __init__(self, id, title, slug,  url):
        self.id = id
        self.title = title
        self.slug = slug
        self.url = url
        self.tags = []


    def fillDescription(self):
        #print(connection.read())
        #soup = BeautifulSoup(connection)
        #body = soup.find('body')
        #app = body.find('div', {'id' : 'app'})
        #print(app.prettify())
        pass

    def add_tags(self, tags):
        """add tags to the problem"""
        self.tags = list(tags)

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
            id = int(problem['stat']['frontend_question_id'])
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
            f.write('# Info\n')
            f.write('## Tags\n')
            f.write('|'.join(problem.tags) + '\n')
            

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
        self._tag_problems = defaultdict(list)
        self._un_tag_problems = []
        self.get_info()
        with open('README.md.tmpl') as f:
            self._template = string.Template(f.read())

    def _get_tags_from_md(self, file_path):
        with open(file_path) as f:
            tag_line = False
            for line in f:
                if line.startswith('## Tags'):
                    # read tags
                    tag_line = True
                elif tag_line:
                    tags = list(filter(None, line.rstrip().split('|')))
                    return tags

            return []


    def get_info(self):
        """Get probelm in info """
        for root, dirs, _ in os.walk(self._dir):
            for dir_name in dirs:
                #print(dir_name)
                for problem_dir, _, files in os.walk(os.path.join(root, dir_name)):
                    id = int(dir_name.split('.')[0])
                    name = dir_name.split('.')[1].strip(' ')
                    location = None
                    slug = None
                    url = None
                    python_link = None
                    tags = []
                    for file_name in files:
                        #print(file_name)
                        if file_name.endswith('.py'):
                            location = os.path.join('.', problem_dir, file_name)
                            problem_dir_quoted = urllib.parse.quote(dir_name)
                            python_link  = os.path.join('https://github.com/ggppwx/lcode/blob/master/Algorithm', problem_dir_quoted , file_name)
                            slug = os.path.splitext(file_name)[0]
                            url = 'https://leetcode.com/problems/' + slug

                        if file_name.endswith('.md'):
                            # it contains the tag info
                            file_path = os.path.join('.', problem_dir, file_name)
                            tags = self._get_tags_from_md(file_path)
                            #print(tags)

                    modified_date =datetime.datetime.fromtimestamp(os.path.getmtime(location))
                    diff = (datetime.datetime.now() - modified_date).days
                    solution_title = 'python'
                    if diff >= 14:
                        solution_title += ' :alarm_clock:'

                    problem = {
                        'id': id,
                        'name': name,
                        'location' : location,
                        'url': url,
                        'solution' : solution_title,
                        'solution_link': python_link,
                        'tags' : tags
                    }
                    self._problems.append(problem)
                    for tag in tags:
                        self._tag_problems[tag].append(problem)
                    if not tags:
                        self._un_tag_problems.append(problem)


    def create_readme_content(self):
        with open(os.path.join(self._dest), 'w') as f:
            content = self._template.substitute()
            f.write(content)
            # tags ###
            for tag, problems in sorted(self._tag_problems.items()):
                f.write('### {}\n'.format(tag))
                f.write("| Id | Title | Solution |\n")
                f.write("|----|-------|----------|\n")
                for problem in sorted(problems, key = lambda x: x['id']):
                    line = "|{id}|[{name}]({url})|[{solution}]({solution_link})|\n".format(**problem)
                    f.write(line)
                f.write('\n')

            f.write('### {}\n'.format('Untagged'))
            f.write("| Id | Title | Solution |\n")
            f.write("|----|-------|----------|\n")
            for problem in self._un_tag_problems:
                line = "|{id}|[{name}]({url})|[{solution}]({solution_link})|\n".format(**problem)
                f.write(line)
            f.write('\n')



def main():
    parser = argparse.ArgumentParser()
    #parser.add_argument('-c', '--config', help='config file')
    parser.add_argument('-i', '--index', help='index of the probelms' )
    parser.add_argument('-t', '--tags', nargs='*', help='tag list')
    parser.add_argument('-r', '--refresh', action="store_true", default = False,  help='refresh')
    args = parser.parse_args()


    print(args)

    if args.index is not None:
        problem_index = int(args.index)


        web_parser = WebParser()
        problem = web_parser.get_problem(problem_index)

        if args.tags:
            problem.add_tags(args.tags)

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
