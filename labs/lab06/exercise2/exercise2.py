def match_specialists(candidates_list, project_requirements):
    skill_count = {}
    for name, skills in candidates_list:
        for skill in skills:
            if skill not in skill_count:
                skill_count[skill] = 0
            else:
                skill_count[skill] += 1

    rare_skill = set()
    skill, count = skill_count
    for skill in skill_count:
        if count < 3:
            rare_skill.add(skill)
    
    specialist = []
    for name, skills in candidates_list:
        missing_requirement = project_requirements - skills
        if missing_requirement == set():
            my