import json



with open("app/data/test.json", "r", encoding="utf-8") as f:
    tests = json.load(f)


def get_test(test_id):
    return tests.get(test_id)

def ask_question(test_id, current_index):
    test = get_test(test_id)
    if not test or current_index >= len(test["questions"]):
        return None
    return test["questions"][current_index]
    
