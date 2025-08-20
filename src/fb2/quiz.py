question = [
    {
        "question": "What does Michaelis-Menten kinetics describe?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "The rate of enzyme-catalyzed reactions", "correct": True, "feedback": "Correct!"},
            {
                "answer": "The binding of substrates to enzymes",
                "correct": False,
                "feedback": "Incorrect. This is related but not what Michaelis-Menten kinetics describes.",
            },
            {
                "answer": "The effect of pH on enzyme activity",
                "correct": False,
                "feedback": "Incorrect. This is a different aspect of enzyme behavior.",
            },
        ],
    },
    {
        "question": "What is the primary assumption of Michaelis-Menten kinetics?",
        "type": "multiple_choice",
        "answers": [
            {"answer": "Enzymes form a complex with substrates", "correct": True, "feedback": "Correct!"},
            {"answer": "Substrate concentration is much higher than enzyme concentration", "correct": False, "feedback": "Incorrect. This is a condition for the model but not the primary assumption."},
            {"answer": "The reaction is at equilibrium", "correct": False, "feedback": "Incorrect. Michaelis-Menten kinetics applies to non-equilibrium conditions."},
        ],
    },

    {"question": "What is required to fit a function with Python?",
     "type": "many_choice",
     "answers": [
         {"answer": "A dataset with input-output pairs", "correct": True, "feedback": "Correct!"},
         {"answer": "A function definition of the underlying model", "correct": True, "feedback": "Correct!"},
         {"answer": "An initial guess of the model parameters", "correct": True, "feedback": "Correct!"},
         {"answer": "A difficult optimization problem", "correct": False, "feedback": "Incorrect. While fitting can be challenging, it's not strictly a requirement."}
     ]
    }
]

def get_quiz():
    from jupyterquiz import display_quiz
    return display_quiz(question)
