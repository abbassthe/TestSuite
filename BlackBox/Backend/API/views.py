from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from API.models import test  # Import the generate_answer function
from API.models import doc  # Import the generate_answer function


from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_response(request):
  if request.method == 'POST':
    # Get the question from the request body
    code = request.POST.get('code')
    if not code:
      return JsonResponse({'error': 'Missing question parameter'}, status=400)

    # Call generate_answer and get the predicted answer
    test_out = test(code=code)
    doc_out= doc(code=code)

    print(test_out.values())
    #print(test_out.answer)
    #print(doc_out.answer)


    # Return the answer as JSON response
    return JsonResponse({'code': code, 'testing code': test_out.values(), 'docstring': doc_out.values()})
  else:
    return JsonResponse({'error': 'Only POST requests allowed'}, status=405)