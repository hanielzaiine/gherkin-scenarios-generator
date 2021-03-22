# -*- coding: utf-8 -*-
"""
DEVELOP
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
            'end note', 'start', 'end','endif','@enduml']

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
    '''
    This function checks whether the diagram has conditionals, and groups the flow paths
    In the structure: {conditional:scenario}
    '''
    scenarios_dict = {}
    main_key = ''

    for i in text_diagram:

        if i.startswith('if'):
            scenario_key = clean_scenario_name(i)
            scenarios_dict[scenario_key] = []
            # Setting main key to dict(conditional reason).
            main_key = scenario_key

        elif i.startswith('else') or i.startswith('elseif'):
            scenario_key = main_key+clean_scenario_name(i)
            scenarios_dict[scenario_key] = []
        scenarios_dict[scenario_key].append(i)

    return scenarios_dict

def clean_scenario_name(scenario_string):
    tags = ['(', ')', 'if', 'then', 'yes', 'else', 'elseif']

    for tag in tags:

        if tag in scenario_string:
            scenario_string = scenario_string.replace(tag,'')

    return (scenario_string)

# Generate Gherkin Scenario Functions

def get_feature_name(text_diagram):
    tag = 'floating note'

    for i in range(len(text_diagram)):

        if text_diagram[i] == tag:
            feature_name = text_diagram[i+1]

    return (feature_name)


def generate_feature(tittle, scenarios_dict):
    f = open("scenarios1.txt", "w", encoding='utf-8')
    f.write("Feature: "+tittle+'\n')
    for key in scenarios_dict.keys():
        f.write(key)
        for scenario in scenarios_dict[key]:
            f.write(scenario)
            f.write('\n')
    f.close()
