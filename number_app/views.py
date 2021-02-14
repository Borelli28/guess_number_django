from django.shortcuts import render
import random


def index(request):
    #Create a rand numer between 1 - 100
    the_number = random.randint(1, 100)
    print("The cpu generated number is: " + str(the_number))

    # Save the random number in sessions
    request.session['number'] = the_number
    print(request.session['key'])

    # If a guess number already exist then
    if 'guess' in request.session:
        print("Guess exists")
        print(request.session['guess'])
        # if there a new guess inputted by user then update 'guess'
        if request.session['guess'] != request.POST['user_guess']:
            print("There is a new user guess so 'guess' is being updated in session")
            request.session['guess'] = request.POST['user_guess']
            print(request.session['guess'])


    # Else if guess does not exist create one
    else:
        request.session['guess'] = request.POST['user_guess']
        print(request.session['guess'])

    #Render page
    return render(request, 'index.html')
