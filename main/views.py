from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Profile, Comment
from .forms import UserForm, ProfileUpdate, UserUpdate, CommentForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.db.models import Q


def home(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'home.html', context)


def search(request):
    if request.method == 'POST':
        srch = request.POST['srh']

        if srch:
            match = Post.objects.filter(
            Q(title__icontains=srch) |
            Q(content__icontains=srch) |
            Q(author__username__icontains=srch)|
            Q(image__icontains=srch)|
            Q(date_posted__icontains=srch)
        )
            if match:
                return render(request, 'search.html', {'sr': match})

        else:
            return HttpResponseRedirect('/search/')
    context = {'posts': Post.objects.all()}
    return render(request, 'search.html', context)

def like_view(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))

def dislike_view(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    disliked = False
    if post.dislikes.filter(id=request.user.id).exists():
        post.dislikes.remove(request.user)
        disliked = False
    else:
        post.dislikes.add(request.user)
        disliked = True
    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'register.html', {'form':form})

def add_comment(request, id):
    post = get_object_or_404(Post, id=id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return HttpResponseRedirect(reverse('post_detail', args=[str(id)]))
            
    else:
        comment_form = CommentForm()

    return render(request, 'add_comment.html', {'post': post,
                                           'comment_form': comment_form})



def profile(request):
    if request.method == 'POST':
        u_form = UserUpdate(request.POST, instance=request.user)
        p_form = ProfileUpdate(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdate(instance=request.user)
        p_form = ProfileUpdate(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'profile.html', context)

class PostList(ListView):
    model               = Post
    template_name       = 'home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

class UserPostList(ListView):
    model = Post
    template_name = 'user_posts.html' 
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get(('username')))
        return Post.objects.filter(author=user).order_by('-date_posted')



class PostDetail(DetailView):
    model               = Post
    
    def get_context_data(self, *args, **kwargs):
        posts = Post.objects.all()
        context = super(PostDetail, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        total_dislikes = stuff.total_dislikes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        disliked = False
        if stuff.dislikes.filter(id=self.request.user.id).exists():
            disliked = True

        context['posts'] = posts
        context["total_likes"] = total_likes
        context["total_dislikes"] = total_dislikes
        context["liked"] = liked
        context["disliked"] = disliked
        return context


class PostUpdate(UpdateView):
    model               = Post
    template_name       = 'post_form.html'
    fields              = ['title', 'content', 'image']

class PostCreate(CreateView):
    model               = Post
    template_name       = 'post_form.html'
    fields              = ['title', 'content', 'image']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDelete(DeleteView):
    model               = Post
    success_url         = '/home/'

