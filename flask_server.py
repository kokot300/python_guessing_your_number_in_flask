#!/usr/bin/python3

from flask import Flask, render_template, request
import game as g

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def root():
    '''
    flask server that can guess number you pick in max 10 attempts.
    :return: rendered html template
    '''
    if request.method == 'GET':
        game_return = g.game()
        my_guess = int(game_return[0])
        min = int(game_return[1])
        max = int(game_return[2])
        return render_template('form.html', my_guess=my_guess, min=min, max=max)
    elif request.method == 'POST':
        min = request.form.get('min')
        max = request.form.get('max')
        answer = request.form.get('answer')
        print(min, max, answer)
        if answer == None:
            answer = min
        game_return = g.game(int(answer), int(min), int(max))
        print(game_return)
        if game_return == 'wygrałem!':
            msg = game_return
            return render_template('form.html', msg=msg, my_guess=500, min=0, max=1000)
        my_guess = int(game_return[0])
        min = int(game_return[1])
        max = int(game_return[2])
        msg = ''
        return render_template('form.html', my_guess=my_guess, msg=msg, min=min, max=max)
    else:
        return "oh no, you've broken my server. get out of here!"


if __name__ == '__main__':
    app.run()
