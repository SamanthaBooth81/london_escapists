"""Travel Destinations Views"""
from django.shortcuts import render, redirect, reverse
from django.utils.text import slugify
from .models import TravelDestinations
from .forms import AddDestinationForm


def all_destinations(request):
    """View to display all destinations in the TravelDestinations Model"""
    destinations_list = TravelDestinations.objects.filter(
        status=1).order_by('-created_on')
    template = 'all_destinations.html'
    paginate_by = 12
    context = {
        'destinations_list': destinations_list,
    }
    return render(request, template, context)


def add_destinations(request):
    """View to add new destination"""
    if not request.user.is_superuser:
        # Redirect back to homepage if not a superuser
        # messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    destination_form = AddDestinationForm()
    if request.method == 'POST':
        model = TravelDestinations()
        results = TravelDestinations.objects.filter(
            destination=request.POST.get('destination'))
        destination_form = AddDestinationForm(request.POST, request.FILES)

        if destination_form.is_valid():
            if results.count() > 0:
                return render(request, "add_destination.html",
                              {
                                  "destination_form": destination_form,
                              },
                              )
            else:
                destinations = destination_form.save(commit=False)
                # # Post on Stack Overflow in README for appending array
                # # to recipe model along with guidance from my mentor
                # destinations.destinaion = request.POST.getlist('ingredients')
                # recipe.instructions = request.POST.getlist('instructions')
                # recipe.author = request.user
                # https://idlecoding.com/creating-custom-slugs-in-django/
                # used to create custom slug
                destinations.slug = slugify('-'.join(
                    [destinations.destination]), allow_unicode=False)
                # messages.success(
                #     request, "Recipe submitted and waiting approval!")
                destinations.save()
                return redirect('home')
        else:
            # messages.error(request, 'Please complete all required fields')
            return render(request, "add_destination.html",
                          {
                              "destination_form": destination_form,
                          },
                          )
    else:
        return render(request, "add_destination.html",
                      {
                          "destination_form": destination_form,
                      },
                      )
