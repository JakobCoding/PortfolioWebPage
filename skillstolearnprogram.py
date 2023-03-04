skills = {'python':1, 'ruby':2, 'bash':4, 'git':8, 'html':16, 'tdd':32, 'css':64, 'javascript':128}

input_skills = list(set(input("Enter your skills, seprated by space: ").lower().split()))

def check_score(input_skills, avail_skills=skills):
    i. score = 0
for i in input_skills:
    score += avail_skills[i]
    
check_score()

def improve_skills(skills_to_learn, avail_skills=skills):
    for i in skills_to_learn:
        print(f"{i} will import you score by {avail_skills[i]}")
        

print(f"Your score is: {check_score(input_skills)}")

skills_to_learn = list(set(input("Enter your skills you want to learn, seprated by space:").lower().split()))

improve_skills(skills_to_learn)
