from django.shortcuts import render

def home(request):
    artist_info = {
        'name': 'Vincent van Gogh',
        'bio': (
            'Vincent van Gogh was a Dutch post-impressionist painter '
            'who is among the most famous and influential figures in '
            'the history of Western art. He created about 2,100 artworks, '
            'including around 860 oil paintings.'
        ),
        'birth_date': '30 March 1853',
        'death_date': '29 July 1890',
    }
    return render(request, 'home.html', {'artist': artist_info})

def about(request):
    site_info = {
        'title': 'Demo Gallery Website',
        'description': (
            'Welcome to the demo version of a gallery website dedicated to the legendary '
            'artist Vincent van Gogh. Here, you can explore some of his most famous works '
            'and learn about their history and significance.'
        ),
    }
    return render(request, 'about.html', {'site': site_info})



def gallery(request):
    artworks = [
        {
            'title': 'Starry Night Over the Rhône',
            'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Starry_Night_Over_the_Rhone.jpg/774px-Starry_Night_Over_the_Rhone.jpg',
            'year': 1888
        },
        {
            'title': 'Wheatfield with Crows',
            'image': 'https://upload.wikimedia.org/wikipedia/commons/f/f3/Vincent_van_Gogh_%281853-1890%29_-_Wheat_Field_with_Crows_%281890%29.jpg',
            'year': 1890
        },
        {
            'title': 'Sunflowers',
            'image': 'https://www.whiteclouds.com/wp-content/uploads/2023/12/CW9132-sunflowers-by-vincent-van-gogh.jpg',
            'year': 1888
        }
    ]

    return render(request, 'gallery.html', {'artworks': artworks})
