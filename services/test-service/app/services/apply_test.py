from app.services.message import *
from app.schemas.result_test import *
from app.services.ia_engine import *

user_sessions = {}

def process_input(user_id, message:str, name: str)-> ScoreResponse:
    session = user_sessions.get(user_id)
    #--------------------------------------
    if not session:
        test = get_test(name)
        if not test: 
            return ScoreResponse( 
                status= "error",
                score= None,
                description="El test '{name}' no existe."
            )
        
        user_sessions[user_id]={
            "test" : name,
            "index" : 0,
            "answers" : []
        }
        
        q = ask_question(name, 0)

        options = "\n".join([f"{k}: {v}" for k, v in q["options"].items()])


        return ScoreResponse(
            status= "begin",
            score= None,
            description= f"Iniciando el test '{test['name']}'\n{q['text']}\n{options}"
        )
         #---------------------------------------

    try:
        answer = int(message)
        session["answers"].append(answer)
    
    except ValueError:
        return ScoreResponse(
            status= "error",
            score= None,
            description= "Ingreso un valor incorrecto por favor ingrese un valor del 0 al 3"
        )
    
    session["index"] += 1
    user_sessions[user_id] = session

    next_q = ask_question(session["test"], session["index"])
    if next_q:
        options = "\n".join([f"{k}: {v}" for k, v in next_q["options"].items()])
        return ScoreResponse(
            status= "continue",
            score= None,
            description= f"{next_q['text']}\n{options}"
        )
    else:
        score = sum(session["answers"])
        interpretacion = interpret_score(session["test"], score)
        del user_sessions[user_id]
        return ScoreResponse(
            status= "success",
            score= score,
            description= interpretacion
        )