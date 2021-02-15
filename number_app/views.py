from django.shortcuts import redirect, render
import random

# python manage.py

def index(request):

    # if user guess is not empty
    if 'guess' in request.session and 'number' in request.session:

        print("Current user guess:")
        print(request.session['guess'])

        # User guess is greater than the random number
        if request.session['number'] < int(request.session['guess']):
            print("User Guess is greater than the number")

        # User guess is less than the random number
        elif request.session['number'] > int(request.session['guess']):
            print("User Guess is less than the number")

        # if user guess the number then generate a new random number
        elif request.session['number'] == int(request.session['guess']):
            # print(request.session['number'] + request.session['guess'])
            print("User guess the number!!!!!")
            request.session['number'] = random.randint(1, 100)
            print("New random number: ")
            print(request.session['number'])

    # print("The random number is: ")
    # print(request.session['number'])

    #Render page
    return render(request, 'index.html')


# Udpates the user guess number then redirect back to root
def update_guess(request):
    request.session['guess'] = request.POST['user_guess']
    #prints the current user guess
    print("User guess updated")
    print(request.session['guess'])

    return redirect('/')

def generate_number(request):
    print("Generating a new number")
    request.session['number'] = random.randint(1, 100)
    print("The random number is: ")
    print(request.session['number'])

    return redirect('/')


# Clear sessions and redirect to root
def clear(request):
    request.session.clear()
    print("Session was cleared")

    request.session['number'] = random.randint(1, 100)
    print("New random number generated:")
    print(request.session['number'])

    return redirect('/')


