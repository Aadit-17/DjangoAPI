from django.shortcuts import render
from joblib import load
# Create your views here.

model = load('./UsageModels/model.joblib')


def predictor(request):
    if request.method == 'POST':
        input1 = request.POST['input1']
        input2 = request.POST['input2']
        input3 = request.POST['input3']
        input4 = request.POST['input4']
        y_pred = model.predict([[input1, input2, input3, input4]])
        if y_pred[0] == 0:
            output = 'Class 1'
        elif y_pred[0] == 1:
            output = 'Class 2'
        else:
            output = 'Class 3'
        return render(request, 'base.html', {'result': output})
    return render(request, 'base.html')
