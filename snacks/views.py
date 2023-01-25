from django.views.generic import DetailView, ListView, TemplateView
from .models import Snack

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['snacks'] = [
            {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f1/2ChocolateChipCookies.jpg/500px-2ChocolateChipCookies.jpg",
                "title": "Cookie",
                "description": "A cookie (American English), or a biscuit (British English), is a baked or cooked snack or dessert that is typically small, flat and sweet.",
                "reference_url": "https://en.wikipedia.org/wiki/Cookie"
            },
            {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/Municipal_Market_of_S%C3%A3o_Paulo_city.jpg/880px-Municipal_Market_of_S%C3%A3o_Paulo_city.jpg",
                "title": "Fruit",
                "description": "fruit normally means the seed-associated fleshy structures (or produce) of plants that typically are sweet or sour and edible in the raw state, such as apples, bananas, grapes, lemons, oranges, and strawberries.",
                "reference_url": "https://en.wikipedia.org/wiki/Fruit"
            },
            {
                "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Granola%2C_yogurt%2C_fruit._%2816696981528%29.jpg/440px-Granola%2C_yogurt%2C_fruit._%2816696981528%29.jpg",
                "title": "Yogurt",
                "description": "Granola is a breakfast and snack food consisting of rolled oats, nuts, honey or other sweeteners such as brown sugar, and sometimes puffed rice, that is usually baked until crisp, toasted and golden brown.",
                "reference_url": "https://en.wikipedia.org/wiki/Granola"
            },
        ]
        return context

class SnackListView(ListView):
    template_name = 'snack_list.html'
    model = Snack

class SnackDetailView(DetailView):
    template_name = 'snack_detail.html'
    model = Snack
