from flask import Flask
from utils import Candidate

candid = Candidate('candidate.json')
dict_ = candid.load_candidates_in_dict()
app = Flask(__name__)
print(dict_.values())

@app.route('/')
def index():
    """
    YOU GET THE MAIN PAGE
    """
    str_ = '<pre>'
    for i in dict_:
        str_ += f'Имя кандидата-{dict_[i]['name']}\nПозиция кандидата- {dict_[i]['position']}\nНавыки кандидата-{dict_[i]['skills']}\n\n'
    str_ += '</pre>'
    return str_


@app.route('/candidate/<x>')
def candidate(x):
    """
    YOU ENTER THE PARAMETR AND GET PERSON WITH THIS ID
    """
    dictionary = candid.get_data_from_x(x)
    picture = dictionary['picture']
    name = dictionary['name']
    position = dictionary['position']
    skills = dictionary['skills']
    return f"<img src={picture}></img><pre>{name}\n{position}\n{skills}\n\n</pre>"


@app.route('/skill/<skill>')
def skill_info(skill):
    """
    YOU ENTER THE PARAMETR AND GET PERSON WITH THESE SKILLS
    """
    str_ = '<pre>'
    for can_ in dict_.values():
        candidate1 = can_['skills'].split(', ')
        candidate1 = [x.lower() for x in candidate1]
        if skill in candidate1:
            str_ += f"{can_['name']}\n{can_['position']}\n{can_['skills']}\n\n"
    str_ += '</pre>'
    return str_


app.run()
