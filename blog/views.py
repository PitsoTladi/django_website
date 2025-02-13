from django.shortcuts import render,get_object_or_404
from datetime import date

post =[
    { 
        'slug' : 'ufc-311',
        'image' : 'islam_Makhachev.jpeg',
        'author' : 'sir Pitso Tladi',
        'date' : date(2025,10,2),
        'title' : 'ufc 311',
        'excerpt' : ' UFC 311 was more than combat; it was a meditation on struggle and triumph. Islam Makhachev defended his title with a first-round submission, proving his mastery once more...',
        'content': """
                UFC 311 was more than combat; it was a meditation on struggle and triumph. Islam Makhachev defended his title with a first-round submission,
               proving his mastery once more. Merab Dvalishvili outlasted Umar Nurmagomedov, etching his name deeper into the anals of  bantamweight history. 
               Jiri Prochazka, fueled by a fevered binge of martial arts films, dismantled Jamahal Hill in a cinematic display of technique and heart.
               Each bout was a verse in the poetry of human resilience—a reminder that beyond the blood and sweat, the octagon is where warriors seek not just victory,
                but transcendence.
        """
    },
        {
            "slug": "programming-is-fun",
            "image": "Mr_sigma.jpeg",
            "author": "Maximilian",
            "date": date(2022, 3, 10),
            "title": "Programming Is Great!",
            "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
            "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
            aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
            velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
            aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
            velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
            aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
            velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
            """
        },
        {
            "slug": "into-the-woods",
            "image": "Dominate.jpeg",
            "author": "Maximilian",
            "date": date(2020, 8, 5),
            "title": "Nature At Its Best",
            "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
            "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
            aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
            velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
            aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
            velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
            aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
            velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
            """
        },

               {
            "slug": "into-the-woods",
            "image": "Dominate.jpeg",
            "author": "Maximilian",
            "date": date(2020, 8, 5),
            "title": "Nature At Its Best",
            "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
            "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
            aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
            velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
            aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
            velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
            aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
            velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
            """
        },
]

def  get_date(post):
    return post['date']

# Create your views here.
def  landing_page(request):
   
    sorted_posts = sorted(post, key = get_date)
    latest_posts = sorted_posts[ -3: ]
    return render(request,'blog/index.html',  {
        'posts' : latest_posts,
        
    })

    

    

def  postsList(request):
   return render(request,'blog/all_posts.html',{
       'posts': post
       
       }
       )



def onePost(request,slug):
    thisPost = next((posts for posts in post if  posts['slug'] == slug ), None)
    return render(request,'blog/post-detail.html',{ 
        
        'one_post' : thisPost
        
        }
        )
