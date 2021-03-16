# -*- coding: utf-8 -*-
"""
Developed for generate test scenarios in Gherkin automated from Activities Diagram in plantuml.
"""

def read_diagram(diagram_name):
    f = open(diagram_name, "rt", encoding="utf-8")
    diagram = (f.read())
    f.close()
    return (diagram)


def split_lines(text_diagram):
    return text_diagram.split('\n')


def remove_syntax_tags(text_diagram):
    # Remove plantUML syntax tags from file
    tags = ['@startuml', 'floating note',
            'end note', 'start', 'end', '@enduml']

    for tag in tags:

        if tag in text_diagram:
            text_diagram.remove(tag)

    return (text_diagram)


def remove_feature_tittle(feature, text_diagram):
    for i in text_diagram:

        if i == feature:
            text_diagram.remove(feature)

    return (text_diagram)


def check_conditionals(text_diagram):
    scenarios_dict = {}
    main_key = ''

    for i in text_diagram:

        if i.startswith('if'):
            scenario_key = i
            print(scenario_key)
            #scenario_key = i.replace('if', '')
            #scenario_key = scenario_key.replace('then', '')
            scenarios_dict[scenario_key] = []
            # Setting main key to dict(conditional reason).
            main_key = scenario_key.replace('(yes)', '')

        elif i.startswith('else') or i.startswith('elseif'):
            scenario_key = i
            print(scenario_key)
            scenario_key = i.replace('else', main_key)
            scenario_key = scenario_key.replace('then', '')
            scenarios_dict[scenario_key] = []
        scenarios_dict[scenario_key].append(i)

    print(scenarios_dict)
    return


# Generate Gherkin Scenario Functions

def get_feature_name(text_diagram):
    tag = 'floating note'

    for i in range(len(text_diagram)):

        if text_diagram[i] == tag:
            feature_name = text_diagram[i+1]

    return (feature_name)


def generate_feature(tittle):
    f = open("scenarios1.txt", "w", encoding='utf-8')
    f.write("Feature: "+tittle)
    f.close()
