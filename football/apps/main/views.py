from django.shortcuts import render


def main(request):
    payload = {
        'title': 'Heart of football',
        'body_id': 'football'
    }
    return render(request, 'main.html', payload)
