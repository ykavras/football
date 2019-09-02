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


def privacy(request):
    payload = {
        'title': 'Gizlilik',
        'body_id': 'privacy'
    }
    return render(request, 'privacy.html', payload)


def contact(request):
    payload = {
        'title': 'İletişim',
        'body_id': 'contact'
    }
    return render(request, 'contact.html', payload)
