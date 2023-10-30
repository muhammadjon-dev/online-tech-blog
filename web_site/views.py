from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post, Profile, Comment, Ip
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.views.generic.edit import FormMixin
from .utils import get_client_ip
from .forms import AddCommentForm, AddPostFrom
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


class HomePageView(ListView):
    model = Post
    template_name = 'web_site/index.html'
    context_object_name = 'data_list'

    def get_queryset(self, **kwargs):
        data_list = []
        posts = Post.objects.all().order_by('-id')
        for post in posts[:3]:
            user_profile = Profile.objects.get(user=post.author)
            commnet_count = Comment.objects.filter(post=post).count()
            data_list.append({
                'post': post,
                'user_image': user_profile.image_url,
                'comment_count': commnet_count
            })

        return data_list


class PostDetailView(FormMixin, DetailView):
    model = Post
    template_name = 'web_site/post.html'
    form_class = AddCommentForm

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        post = get_object_or_404(Post, id=self.kwargs['pk'])
        user_ip = get_client_ip(self.request)

        
        if Ip.objects.filter(ip=user_ip).exists():
            post.views.add(Ip.objects.get(ip=user_ip))
        else: 
            Ip.objects.create(ip=user_ip)
            post.views.add(Ip.objects.get(ip=user_ip))
            
        comments = Comment.objects.filter(post=post).order_by('-pk')
        comment_data = []
        for comment in comments:
            print(comment)
            user_image = Profile.objects.get(user=comment.name.id).image_url
            comment_data.append({
                'user_image': user_image,
                'comment': comment
            })

        like_info = post.likes.filter(id=self.request.user.id).exists()

        user_image = Profile.objects.get(user=post.author).image_url
        comment_count = comments.count()
        views_count = post.views_count()
        context["post"] = post
        context["comment_data"] = comment_data
        context["comment_count"] = comment_count
        context["views_count"] = views_count
        context["user_image"] = user_image
        context["liked"] = like_info
        return context


class PostsByCategory(ListView):
    model = Post
    # context_object_name = 'posts'
    template_name = 'web_site/post_list.html'
    paginate_by = 4

    def get_queryset(self):
        search_value = self.request.GET.get('search')
        post = Post.objects.filter(category=self.kwargs['pk'])
        if search_value:
            post = post.filter(Q(title__contains=search_value) | Q(content__contains=search_value))

        return post

    def get_context_data(self, *args, **kwargs):
        context = super(PostsByCategory, self).get_context_data(*args, **kwargs)
        post = self.get_queryset()


        for obj in post:
            obj.image_url = Profile.objects.get(user=obj.author).image_url
            obj.save()

        context['posts'] = post
        # user_image =
        # context['image_url'] = user_image
        return context



class AddCommentView(CreateView):
    model = Comment
    form_class = AddCommentForm

    def form_valid(self, form):
        post = Post.objects.get(pk=self.kwargs['pk'])
        body = form.cleaned_data['body']
        user = self.request.user
        comment = self.model(post=post, name=user, body=body)
        comment.save()

        return super(AddCommentView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post', kwargs={'pk': self.kwargs['pk']})


class LikeView(TemplateView):

    def get(self, request, *args, **kwargs):
        post_pk = self.kwargs['pk']
        post = Post.objects.get(pk=post_pk)
        if request.user.is_authenticated:
            if not post.likes.filter(id=request.user.id).exists():
                post.likes.add(request.user)
            else:
                post.likes.remove(request.user)
        return HttpResponseRedirect(reverse_lazy('post', kwargs={'pk': self.kwargs['pk']}))


class AddPostView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = AddPostFrom
    template_name = 'web_site/add_post.html'
    redirect_field_name = 'redirect_to'
    login_url = reverse_lazy('login')


class SearchView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'web_site/post_list.html'
    paginate_by = 4

    def get_queryset(self):
        value = self.request.GET['search']
        return self.model.objects.filter(Q(title__contains=value) | Q(content__contains=value))
