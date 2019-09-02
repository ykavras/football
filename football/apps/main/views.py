from django.shortcuts import render


def main(request):
    payload = {
        'title': 'Futbolun Kalbi',
        'body_id': 'football'
    }
    return render(request, 'main.html', payload)


def about(request):
    payload = {
        'title': 'Hakkımızda',
        'body_id': 'about'
    }
    return render(request, 'about.html', payload)


def sss(request):
    payload = {
        'title': 'Sıkça Sorulan Sorular',
        'body_id': 'sss'
    }
    return render(request, 'sss.html', payload)
