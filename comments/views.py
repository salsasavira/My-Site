from django.shortcuts import render
from .models import Comment


# Create your views here.
def comment_list(request):
    comments = Comment.objects.filter(post=1) # sama spt di html post.text, artinya mengambil text dari post. post adalah foreign key di comments

    title = "Developer" # mengganti title tidak dari file htmlnya
    total = comments.count()

    return render(request, 'comments/comment_list.html', {'comments': comments, 'title': 'Developer', 'total' : total}) #pada {'comments' : comments} = {'a' : b} = b itu yang ada di for dalam file html