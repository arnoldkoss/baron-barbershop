from django.shortcuts import render

# Your view logic here


def home_page(request):
    """
    View function for rendering the home page.

    This function renders the 'home_page.html'
    template and returns it as an HTTP response.
    It takes a request object as its parameter.
    """
    return render(request, 'home_page.html')
