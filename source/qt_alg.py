import sqlite3

n = 0
con = sqlite3.connect("source/db/SubjectAkinator.db")
cur = con.cursor()
turns = 0

used = set()
questions_id = {i[0]: 0 for i in cur.execute("SELECT id FROM questions").fetchall()}
subjects_id = {i[0]: 0 for i in cur.execute("SELECT id FROM subjects").fetchall()}
choice_range = None
right_answers = None


def real_subj(name_subj):
    return True if len(cur.execute("SELECT name FROM subjects WHERE name = ?", (name_subj, )).fetchall()) \
        else False


def new_game():
    global turns, choice_range, right_answers, used, questions_id, subjects_id
    turns = 0
    choice_range = None
    right_answers = None
    used = set()
    questions_id = {i[0]: 0 for i in cur.execute("SELECT id FROM questions").fetchall()}
    subjects_id = {i[0]: 0 for i in cur.execute("SELECT id FROM subjects").fetchall()}


def question():
    global turns, choice_range, right_answers
    real_max = max(subjects_id.values())
    questions_priority = questions_id.copy()
    choice_range = set([ids for ids in subjects_id.keys() if subjects_id[ids] == real_max])

    if len(choice_range) == 1:
        return {'text': cur.execute(f"SELECT name FROM subjects WHERE id = {choice_range.pop()}").fetchone()[0],
                "is_question": False,
                'turns': turns}

    while True:
        turns += 1
        real_max = max(subjects_id.values())
        questions_priority = questions_id.copy()
        choice_range = set([ids for ids in subjects_id.keys() if subjects_id[ids] == real_max])

        while True:
            if turns != 1:
                for quest, subj in cur.execute("SELECT question_id, subject_id FROM question_to_subjects").fetchall():
                    if quest not in used:
                        if subj in choice_range:
                            questions_priority[quest] += 1
                best_question = sorted(questions_priority.keys(), key=lambda x: -questions_priority[x])[0]
            else:
                best_question = 34
            right_answers = set([i[0] for i in cur.execute(f"""SELECT subject_id FROM question_to_subjects
             WHERE question_id = {best_question}""").fetchall()])

            if best_question in used:
                choice_range = set([choice_range.pop()])
                break
            used.add(best_question)
            if choice_range - right_answers != set():
                break
            questions_priority = questions_id.copy()

        if len(choice_range) == 1:
            turns -= 1
            return {'text': cur.execute(f"SELECT name FROM subjects WHERE id = {choice_range.pop()}").fetchone()[0],
                    "is_question": False,
                    'turns': turns}

        return {"text": cur.execute(f"SELECT text FROM questions WHERE id = {best_question}").fetchone()[0],
                "is_question": True,
                'turns': turns}


def ans_yes():
    for key in subjects_id.keys():
        if key in right_answers:
            subjects_id[key] += 1
        else:
            subjects_id[key] -= 1


def ans_no():
    for key in subjects_id.keys():
        if key in right_answers:
            subjects_id[key] -= 1
        else:
            subjects_id[key] += 1


