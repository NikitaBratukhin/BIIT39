from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.views import View
from blogs.models import Category, Blog, Comment
from django.utils import timezone
from .forms import CKEditorForm
class ManageBlog(View):
    def get(self, request):
        blogs = Blog.objects.filter(is_active=True, creator=request.user)
        return render(request, "management/blog.html", {"blogs": blogs})


class ManageCategory(View):
    def get(self, request):
        categories = Category.objects.filter(is_active=True)
        return render(request, "management/category.html", {"categories": categories})


class CreateBlog(View):
    def get(self, request):
        form = CKEditorForm()
        categories = Category.objects.filter(is_active=True)
        return render(request, "management/create_blog.html", {"form": form, "categories": categories})

    def post(self, request):
        data = request.POST
        title = data.get("title")
        desc = data.get("desc")
        content = data.get("content")
        thumbnail = request.FILES.get("thumbnail")
        categories = data.getlist("categories")
        status = data.get("status")

        if not (title and desc and content and thumbnail and categories and status):
            messages.info(request,
                          "Заголовок, описание, контент, изображение, категории или статус не могут быть пустыми")
            return redirect("manage:create_blog")

        try:
            status = bool(int(status))
        except:
            messages.info(request, "Что-то не так со статусом")
            return redirect("manage:create_blog")

        blog = Blog(
            title=title,
            desc=desc,
            content=content,
            creator=request.user,
            thumbnail=thumbnail,
            is_published=status
        )
        blog.save()
        for id in categories:
            try:
                c = Category.objects.get(id=int(id))
                blog.categories.add(c)
            except Exception as e:
                pass

        blog.save()
        messages.success(request, "Мероприятие создано")

        return redirect("manage:create_blog")


class CreateCategory(View):
    def get(self, request):
        return render(request, "management/create_category.html")

    def post(self, request):
        data = request.POST
        category = data.get("category")
        desc = data.get("desc")

        c = Category.objects.filter(category=category).first()
        if c is not None:
            messages.warning(request, "Категория уже существует")
        else:
            c = Category(
                category=category,
                desc=desc
            )
            c.save()
            messages.success(request, "Категория создана")
        return redirect("manage:create_category")


class EditBlog(View):
    def get(self, request, id):
        blog = Blog.objects.filter(id=id, creator=request.user).first()
        if blog is None:
            messages.info(request, "Мероприятие не существует")
            return redirect("manage:blog")
        categories = Category.objects.all()
        form = CKEditorForm({"content": blog.content})
        return render(request, "management/edit_blog.html", {"blog": blog, "categories": categories, "form": form})

    def post(self, request, id=None):
        data = request.POST
        id = data.get("id")
        blog = Blog.objects.filter(is_active=True, creator=request.user, id=id).first()
        if blog is None:
            messages.info(request, "Мероприятие не существует")
            return redirect("manage:blog")

        title = data.get("title")
        desc = data.get("desc")
        content = data.get("content")
        status = data.get("status")
        thumbnail = request.FILES.get("thumbnail")
        categories = data.getlist("categories")

        blog.title = title
        blog.desc = desc
        blog.content = content
        if thumbnail:
            blog.thumbnail = thumbnail

        try:
            status = int(status)
            if not blog.is_published and status:
                blog.published_on = timezone.now()
            blog.is_published = bool(status)
        except:
            messages.info(request, "Ошибка при обновлении статуса")

        blog.categories.set([])
        for id in categories:
            try:
                c = Category.objects.get(id=int(id))
                blog.categories.add(c)
            except Exception as e:
                pass

        blog.save()
        messages.success(request, "Изменения сохранены")

        return redirect("manage:blog")


class DeleteBlog(View):
    def get(self, request, id):
        blog = Blog.objects.filter(id=id, creator=request.user).first()
        if blog is None:
            messages.warning(request, "Мероприятие не существует")
        else:
            blog.is_active = False
            blog.save()
            messages.info(request, "Мероприятие удалено")

        return redirect("manage:blog")


class EditCategory(View):
    def get(self, request, id):
        category = get_object_or_404(Category, id=id, is_active=True)
        return render(request, "management/edit_category.html", {"category": category})

    def post(self, request, id):
        c = Category.objects.filter(id=id, is_active=True).first()
        data = request.POST
        category, desc = data.get("category"), data.get("desc")
        if not ((category and desc) or c):
            messages.warning(request, "Категория или описание не могут быть пустыми. Или категория не существует")
            return redirect("manage:category")
        c.category = category
        c.desc = desc
        c.save()
        messages.success(request, "Изменения сохранены")
        return redirect("manage:category")


class DeleteCategory(View):
    def get(self, request, id):
        category = get_object_or_404(Category, id=id)
        category.is_active = False
        category.save()
        messages.info(request, "Категория удалена")
        return redirect("manage:category")


class ManageComment(View):
    def get(self, request):
        comments = Comment.objects.filter(is_active=True, blog__in=Blog.objects.filter(creator=request.user))
        return render(request, "management/comment.html", {"comments": comments})


class DeleteComment(View):
    def get(self, request, id):
        comment = get_object_or_404(Comment.objects.filter(id=id, is_active=True))
        if comment.blog.creator.username != request.user.username:
            messages.warning(request, "Вы не являетесь автором этого мероприятия")
            return redirect("manage:comment")
        comment.is_active = False
        comment.save()
        messages.success(request, "Комментарий удален")
        return redirect("manage:comment")