from .models import Category
from django.templatetags.static import static

def categories(request):
    cats = Category.objects.all()
    Category_menu = []

    for c in cats:
        icon = static(
            f'img/categories/{c.slug}.svg'
        )

        Category_menu.append({
            'name': c.name,
            'slug': c.slug,
            'url': c.get_abcolute_url(),
            'icon': icon,
        })

    POPULAR_SLUGS = ['fruits','vegetables','drinks']

    popular_categories = [c for c in Category_menu if c['slug'] in POPULAR_SLUGS
                          ]
    return{
        'categories': cats,
        'category_menu': Category_menu,
        'popular_categories': popular_categories,
    }