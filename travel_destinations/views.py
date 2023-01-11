"""Travel Destinations Views"""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import View
from django.utils.text import slugify
from .models import Destinations
from .forms import AddDestinationForm


def all_destinations(request):
    """View to display all destinations in the Destinations Model"""
    destinations_list = Destinations.objects.filter(
        status=1).order_by('-created_on')
    top_dest = Destinations.objects.filter(top_destination=True)
    template = 'all_destinations.html'
    # paginate_by = 12
    context = {
        'destinations_list': destinations_list,
        'top_dest': top_dest,
    }
    return render(request, template, context)


class DestinationDetail(View):
    """View recipe details"""

    def get(self, request, slug, *args, **kwargs):
        """Function to get the recipe details"""
        queryset = Destinations.objects.filter(status=1)
        dest = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "destination_details.html",
            {
                "dest": dest,
            },
        )


def add_destinations(request):
    """View to add new destination"""
    if not request.user.is_superuser:
        # Redirect back to homepage if not a superuser
        # messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    destination_form = AddDestinationForm()
    if request.method == 'POST':
        model = Destinations()
        results = Destinations.objects.filter(
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
