from django.shortcuts import render
import csv


def inflation_view(request):
    template_name = 'inflation.html'
    with open('inflation_russia.csv', newline='') as csvfile:
        reader = list(csv.reader(csvfile, delimiter=';'))

    for row in reader:
        count = 0
        for value in row:
            if not value:
                row[count] = '-'
            count += 1

    context = {
        'data_inflation': reader,
    }

    return render(request, template_name,
                  context)
