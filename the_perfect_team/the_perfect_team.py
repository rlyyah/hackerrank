def differentTeams(skills):
    skills_dir = {}
    team_amount = 0
    create_team = False
    team_string = 'pcmbz'
    for letter in skills:
        if letter in team_string:
            if letter not in skills_dir:
                skills_dir[letter] = 1
            else:
                skills_dir[letter] += 1
    if len(skills_dir) == 5:
        create_team = True
    while create_team:
        team_amount += 1
        for elements in skills_dir:
            skills_dir[elements] -= 1
            if skills_dir[elements] == 0:
                create_team = False
    return team_amount       
            
print(differentTeams('sdadasdasdasdasdaspcmbzpcmbzasdasdasd'))
