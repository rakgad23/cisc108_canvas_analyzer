"""
Project 4C
Canvas Analyzer
CISC108 Honors
Fall 2019

Access the Canvas Learning Management System and process learning analytics.

Edit this file to implement the project.
To test your current solution, run the `test_my_solution.py` file.
Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: YOUR NAME HERE
"""
__version__ = 7

import canvas_requests
import matplotlib.pyplot as plt
from datetime import datetime


# 1)
def print_user_info(user):
    print("Name:", user['name'])
    print("Title:", user['title'])
    print("Primary Email:", user['primary_email'])
    print("Bio:", user['bio'])
# 2)
def filter_available_courses(courses):
    valid = []
    for course in courses:
        if course['workflow_state'] == 'available':
            valid.append(course)
    return valid
# 3) filter_available_courses
def print_courses(courses):
    for course in courses:
        print("\t", course["id"], ":", course["name"])
# 4) print_courses
def get_course_ids(courses):
    ids = []
    for course in courses:
        ids.append(course['id'])
    return ids

# 5) get_course_ids
def choose_course(course_ids):
    PROMPT = "Choose a course from the list above:"
    chosen = None
    while chosen not in course_ids:
        chosen = int(input(PROMPT))
    return chosen
# 6) choose_course
def summarize_points(submissions):
    possible = 0
    score = 0
    for submission in submissions:
        if submission['score'] is not None:
            points_possible = submission['assignment']['points_possible']
            group_weight = submission['assignment']['group']['group_weight']
            possible += points_possible * group_weight
            score += submission['score'] * group_weight
    print("Points possible so far:", possible)
    print("Points obtained:", score)
    print("Current grade:", round(100 * score / possible))

# 7) summarize_points
def summarize_groups(submissions):
    group_score = {}
    group_points = {}
    for sub in submissions:
        if sub['score'] is not None:
            group_name = sub['assignment']['group']['name']
            if group_name not in group_score:
                group_score[group_name] = 0
                group_points[group_name] = 0
            group_score[group_name] += sub['score']
            group_points[group_name] += sub['assignment']['points_possible']
    for name in group_score:
        score, points = group_score[name], group_points[name]
        print("*", name, ":", round(100 * score / points))
# 8) summarize_groups
def plot_scores(submissions):
    percent_scores = []
    for s in submissions:
        if s['assignment']['points_possible'] and s['score'] != None:
            percent_score = 100 * s['score'] / s['assignment']['points_possible']
            percent_scores.append(percent_score)
    plt.hist(percent_scores)
    plt.title("Distribution of Grades")
    plt.xlabel("Grades")
    plt.ylabel("Number of Assignments")
    plt.show()
# 9) plot_scores

# 10) plot_grade_trends

# Keep any function tests inside this IF statement to ensure


# that your `test_my_solution.py` does not execute it.
if __name__ == "__main__":
    main('hermione')
    # main('ron')
    # main('harry')
    
    # https://community.canvaslms.com/docs/DOC-10806-4214724194
    # main('YOUR OWN CANVAS TOKEN (You know, if you want)')

def main()