blog1 = 'he is so awesome'
blog2 = 'cars are very cool'
blog3 = 'hey look at my cat'

# this is args


def blog_posts(regular_args, *args):
    print(regular_args)
    for post in args:
        print(post)


blog_posts('here is my blog :', blog1, blog2, blog3)

# this is kwargs


def blog_post2(**kwargs):
    for title, post in kwargs.items():
        print(title, post)


blog_post2(
blog1 ='he is so awesome',
blog2 ='cars are very cool',
blog3 ='hey look at my cat'

)
