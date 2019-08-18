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
import re

PROBELM_DIR = 'algorithm'


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
        content = json.loads(response.content.decode('utf-8'))
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
            self._templates['py'] = string.Template(f.read())
        with open('source_code.cpp.tmpl') as f:
            self._templates['cpp'] = string.Template(f.read())
        with open('problem_readme.md.tmpl') as f:
            self._templates['md'] = string.Template(f.read())
        
    def create_template(self, problem, language=None):
        """Create a local problem template
        dir
        - problem name
        -- README
        -- problem.py
        -- problem.cpp
        """
        print('creating ... ')
        problem_md_path = self._dir + '/' + str(problem.id) + '. ' + problem.title + '.md'
        
        # generate a dir with title
        if os.path.exists(problem_md_path):
            print('{} already exists'.format(problem_md_path))
            return

        # generate file: readme
        with open(problem_md_path, 'w') as f:
            substitutes = {
                'title': problem.title,
                'url': problem.url,
                'tags': '|'.join(problem.tags)
            }
            readme = self._templates['md'].substitute(substitutes)
            f.write(readme)


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

    def _get_info_from_md(self, file_path):
        with open(file_path, encoding="utf8") as f:
            tags = []
            marks = []
            name = None
            timestamp = None
            url = None
            tag_line = False
            mark_line = False
            problem_url_line = False
            for line in f:
                if line.startswith('# '):
                    name = line[2:].rstrip()
                    problem_url_line = True
                elif problem_url_line:
                    found = re.search('\[.*\]\((.*?)\)', line)
                    url = found.group(1) if found else None 
                    if url:
                        problem_url_line = False

                if line.startswith('## Tags'):
                    # read tags
                    tag_line = True
                elif tag_line:
                    tags = list(filter(None, line.rstrip().split(',')))
                    if tags or line.startswith('#'):
                        tag_line = False

                if line.startswith('## Marks'):
                    mark_line = True
                elif mark_line:
                    marks = list(filter(None, line.rstrip().split(',')))
                    if marks or line.startswith('['):
                        mark_line = False                

                if line.startswith('[comment]: <timestamp'):
                    found = re.search('<timestamp:(\d{4}-\d{2}-\d{2})>', line)
                    timestamp = found.group(1) if found else None
                    # print(timestamp)
            return (name, tags, marks, timestamp, url)

    def get_info(self):
        """Get probelm in info """
        for root, dirs, files in os.walk(self._dir):
            for file_name in files:
                if file_name.startswith('.'):
                    continue

                if not file_name.endswith('.md'):
                    continue
                                
                id = None
                try:
                    id = int(file_name.split('.')[0])
                except:
                    continue
                
                slug = None
                url = None
                solutions = []
                tags = []
                tag_text = ""
                marks = []
                timestamp = None
                problem_dir = self._dir
                problem_dir_quoted = urllib.parse.quote("")
                problem_dir_link = os.path.join('https://github.com/ggppwx/lcode/blob/master/Algorithm/', problem_dir_quoted)                                                                
                location = os.path.join('.', problem_dir, file_name)
                file_path = os.path.join('.', problem_dir, file_name)                
                name, tags, marks, timestamp, url = self._get_info_from_md(file_path)
                                                
                modified_date = (datetime.datetime.fromtimestamp(os.path.getmtime(location))
                                    if not timestamp
                                    else datetime.datetime.strptime(timestamp, "%Y-%m-%d"))
                diff = (datetime.datetime.now() - modified_date).days
                need_review = False
                expected_diff = 60
                for mark in marks:
                    if mark == 'Overtime':
                        tag_text += ' ![Overtime](https://img.shields.io/badge/stats-Overtime-yellowgreen.svg)'
                        expected_diff = 40
                    if mark == 'Hard':
                        tag_text += ' ![Hard](https://img.shields.io/badge/-Hard-red.svg) '
                        expected_diff = 35 
                    if mark == 'Star':
                        tag_text += ' ⭐ '
                        expected_diff = 30
                    if mark == 'Help':                            
                        tag_text += ' ![Help](https://img.shields.io/badge/stats-Help-yellow.svg)'
                        expected_diff = 25
                    if mark == 'Help2':
                        tag_text += ' ![Help2](https://img.shields.io/badge/stats-Help-orange.svg)'
                        expected_diff = 15
                    if mark == '2':
                        tag_text += ' ![Redone](https://img.shields.io/badge/-Redone-green.svg)'
                        expected_diff += 30

                if diff >= expected_diff:
                    name += ' ⏰ '
                    need_review = True

                problem = {
                    'id': id,
                    'name': name,
                    'location' : location,
                    'url': url,
                    'tags': tags,
                    'marks' : marks,
                    'solutions' : [{'solution': 'link', 'solution_link': ''}],                    
                    'need_review' : need_review,
                    'diff' : diff,
                    'tag_text': tag_text
                }                
                print(problem)
                self._problems.append(problem)
                for tag in tags:
                    self._tag_problems[tag].append(problem)
                if not tags:
                    self._un_tag_problems.append(problem)


    def create_readme_content(self):
        # tags ###
        table = ""
        total_number_of_problem = 0
        review_number_of_problem = 0
        for tag, problems in sorted(self._tag_problems.items()):
            table += ('### {}\n'.format(tag))
            table += ("| Id | Title  | Solution | Review (days ago)|\n")
            table += ("|----|-------|----------|------------------|\n")
            for problem in sorted(problems, key = lambda x: x['id']):
                solution_col = "".join(["[{solution}]({solution_link})".format(**s) for s in problem['solutions']] )
                line = "|{id}|[{name}]({url}) {tag_text}|{}|{diff}|\n".format(solution_col, **problem)
                table += line
                total_number_of_problem += 1
                review_number_of_problem += 1 if problem['need_review'] else 0
            table += '\n'

        table += '### {}\n'.format('Untagged')
        table += "| Id | Title | Solution |\n"
        table += "|----|-------|----------|\n"
        for problem in self._un_tag_problems:
            solution_col = "".join(["[{solution}]({solution_link})".format(**s) for s in problem['solutions']] )
            line = "|{id}|[{name}]({url})|{}|\n".format(solution_col, **problem)
            table += line
        table += '\n'

        with open(os.path.join(self._dest), 'w') as f:
            content = self._template.substitute({
                'total' : total_number_of_problem,
                'review': review_number_of_problem,
                'ratio' : int(100 - (review_number_of_problem/total_number_of_problem) * 100),
                'table' : table
            })
            f.write(content)


def main():
    parser = argparse.ArgumentParser()
    #parser.add_argument('-c', '--config', help='config file')
    parser.add_argument('-i', '--index', help='index of the probelms')
    parser.add_argument('-t', '--tags', nargs='*', help='tag list')
    parser.add_argument('-l', '--language', nargs='?', help='the language, default is python')
    parser.add_argument('-r', '--refresh', action="store_true", default=False, help='refresh')
    args = parser.parse_args()

    print(args)

    if args.index is not None:
        problem_index = int(args.index)
        web_parser = WebParser()
        problem = web_parser.get_problem(problem_index)

        if args.tags:
            problem.add_tags(args.tags)

        tmpl = TemplateCreator(PROBELM_DIR)
        language = args.language if args.language else None
        tmpl.create_template(problem, language)

        readme_content = ReadmeContent(PROBELM_DIR)
        readme_content.create_readme_content()

    elif args.refresh:
        print('---refresh-----')
        readme_content = ReadmeContent(PROBELM_DIR)
        readme_content.create_readme_content()
    


if __name__ == "__main__":
    main()
