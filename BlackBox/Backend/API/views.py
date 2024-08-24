from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from API.models import generate_answer  # Import the generate_answer function

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_response(request):
  if request.method == 'POST':
    # Get the question from the request body
    question = request.POST.get('question')
    if not question:
      return JsonResponse({'error': 'Missing question parameter'}, status=400)

    # Call generate_answer and get the predicted answer
    pred = generate_answer(question=question)
    answer = pred.answer

    # Return the answer as JSON response
    return JsonResponse({'question': question, 'answer': answer})
  else:
    return JsonResponse({'error': 'Only POST requests allowed'}, status=405)