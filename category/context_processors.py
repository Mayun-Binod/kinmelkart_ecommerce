from category.models import Category

def menu_links(request):
    links = Category.objects.all()  # Fetch all categories from the database
    return dict(links=links)  # Return them as a dictionary
