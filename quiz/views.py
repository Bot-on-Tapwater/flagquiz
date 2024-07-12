# quiz/views.py

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils import timezone
from .models import Country, UserScore
import random
import requests
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'quiz/home.html')

def quiz(request):
    countries = list(Country.objects.all())
    questions = []

    for country in countries:
        choices = random.sample(countries, 4)
        if country not in choices:
            choices[random.randint(0, 3)] = country
        random.shuffle(choices)
        question = {
            'question': {"answer": country.name, "flag_url": country.flag_url},
            'choices': [choice.name for choice in choices]
        }
        questions.append(question)

    random.shuffle(questions)
    return JsonResponse({'questions': questions})

# def answer(request):
#     selected_country = request.POST.get('choice')
#     correct_country = request.POST.get('correct')
    
#     if selected_country == correct_country:
#         request.session['score'] += 1

#     elapsed_time = timezone.now().timestamp() - request.session['start_time']
    
#     if elapsed_time >= 300:  # 5 minutes
#         return redirect('results')

#     return redirect('quiz')
@csrf_exempt
def create_score(request):
    username = request.POST.get('username')
    score = request.POST.get('score')
    # UserScore.objects.create(username=username, score=score)

    # Create an instance of the UserScore model
    user_score = UserScore(username=username, score=score)

    # Save the instance to the database
    user_score.save()

    return JsonResponse(user_score.to_dict())

def results(request):
    try:
        results = UserScore.objects.all().order_by('-score')
        return JsonResponse([score.to_dict() for score in results], safe=False)
    except Exception as e:
        return {"error": str(e)}

def get_countries_and_flags(request):
    url = 'https://restcountries.com/v3.1/all'
    response = requests.get(url)
    if response.status_code == 200:
        countries = response.json()
        country_data = []
        for country in countries:
            country_name = country.get('name', {}).get('common')
            flag_url = country.get('flags', {}).get('png')
            if country_name and flag_url:
                # Create or update the Country record
                Country.objects.update_or_create(
                    name=country_name,
                    defaults={'flag_url': flag_url}
                )
                country_data.append({
                    'name': country_name,
                    'flag': flag_url
                })
        return JsonResponse(country_data, safe=False)
    else:
        return JsonResponse({'error': 'Failed to fetch data'}, status=response.status_code)

