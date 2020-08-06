from django.shortcuts import render, redirect
from django.utils import timezone
from django.conf import settings
from django.contrib import messages
from .forms import QuoteFormForFrontend


def quote_view(request):
    if request.method == 'POST':
        form = QuoteFormForFrontend(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Request successful! You will be contacted by one of our agents within the hour. Thank you!')
            return redirect('get-a-quote')

    else:
        form = QuoteFormForFrontend()

    context = {
        'form': form
    }

    return render(request, "getQuote/get-a-quote.html", context)
