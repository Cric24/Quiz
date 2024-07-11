from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Quiz data (expanded example)
quiz_data = [
    {
        'category': 'General Knowledge',
        'question': 'What is the capital of Australia?',
        'options': ['Sydney', 'Melbourne', 'Canberra', 'Brisbane'],
        'correct_answer': 'Canberra',
        'explanation': 'Canberra is the capital city of Australia.'
    },
    {
        'category': 'Science',
        'question': 'What is the atomic number of Carbon?',
        'options': ['6', '7', '8', '9'],
        'correct_answer': '6',
        'explanation': 'The atomic number of Carbon is 6.'
    },
    {
        'category': 'History',
        'question': 'Who was the first President of the United States?',
        'options': ['Thomas Jefferson', 'George Washington', 'John Adams', 'James Madison'],
        'correct_answer': 'George Washington',
        'explanation': 'George Washington was the first President of the United States.'
    },
    {
        'category': 'Sports',
        'question': 'Which country won the FIFA World Cup in 2018?',
        'options': ['Brazil', 'France', 'Germany', 'Spain'],
        'correct_answer': 'France',
        'explanation': 'France won the FIFA World Cup in 2018.'
    },
    {
        'category': 'Technology',
        'question': 'Who is the CEO of Tesla Motors?',
        'options': ['Jeff Bezos', 'Elon Musk', 'Tim Cook', 'Satya Nadella'],
        'correct_answer': 'Elon Musk',
        'explanation': 'Elon Musk is the CEO of Tesla Motors.'
    },
    {
        'category': 'Geography',
        'question': 'Which is the longest river in the world?',
        'options': ['Amazon River', 'Nile River', 'Yangtze River', 'Mississippi River'],
        'correct_answer': 'Nile River',
        'explanation': 'The Nile River is the longest river in the world.'
    },
    {
        'category': 'Movies',
        'question': 'Who played the role of Neo in the movie "The Matrix"?',
        'options': ['Keanu Reeves', 'Leonardo DiCaprio', 'Tom Cruise', 'Brad Pitt'],
        'correct_answer': 'Keanu Reeves',
        'explanation': 'Keanu Reeves played the role of Neo in "The Matrix".'
    },
    {
        'category': 'Music',
        'question': 'Which band performed the song "Bohemian Rhapsody"?',
        'options': ['The Beatles', 'Queen', 'Led Zeppelin', 'Rolling Stones'],
        'correct_answer': 'Queen',
        'explanation': 'The band Queen performed the song "Bohemian Rhapsody".'
    },
    {
        'category': 'Literature',
        'question': 'Who wrote the novel "To Kill a Mockingbird"?',
        'options': ['Harper Lee', 'John Steinbeck', 'F. Scott Fitzgerald', 'Mark Twain'],
        'correct_answer': 'Harper Lee',
        'explanation': 'Harper Lee wrote the novel "To Kill a Mockingbird".'
    },
    {
        'category': 'Mathematics',
        'question': 'What is the value of π (pi) to two decimal places?',
        'options': ['3.12', '3.14', '3.16', '3.18'],
        'correct_answer': '3.14',
        'explanation': 'The value of π (pi) to two decimal places is 3.14.'
    },
]

# Shuffle quiz data for random order
random.shuffle(quiz_data)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        # Initialize score and feedback lists
        score = 0
        feedback = []
        # Check answers and provide feedback
        for question in quiz_data:
            user_answer = request.form.get(question['question'])
            if user_answer == question['correct_answer']:
                score += 1
                feedback.append({'question': question['question'], 'answer': user_answer, 'correct': True, 'explanation': question['explanation']})
            else:
                feedback.append({'question': question['question'], 'answer': user_answer, 'correct': False, 'explanation': question['explanation']})
        return render_template('result.html', score=score, total=len(quiz_data), feedback=feedback)

    return render_template('quiz.html', quiz_data=quiz_data)

if __name__ == '__main__':
    app.run(debug=True)
