from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from home.models import UserProfile
from product.models import Category, Product, Comment, ProductForm, ProductFilesForm, Files
from user.forms import ProfileUpdateForm, UserUpdateForm


@login_required(login_url='/login')  # Check Login
def index(request):
    category = Category.objects.all()
    current_user = request.user

    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'category': category,
               'profile': profile}
    return render(request, "user_profile.html", context)


@login_required(login_url='/login')  # Check Login
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('/user')
    else:
        category = Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)

        context = {'category': category,
                   'user_form': user_form,
                   'profile_form': profile_form}
        return render(request, "user_update.html", context)



@login_required(login_url='/login')  # Check Login
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below. <br>' + str(form.errors))
            return HttpResponseRedirect('/user/password')
    else:
        category = Category.objects.all()
        form = PasswordChangeForm(request.user)
        return render(request, "change_password.html", {
            'category': category, 'form': form
        })




@login_required(login_url='/login')  # Check Login
def comments(request):
    category = Category.objects.all()
    current_user = request.user
    comments = Comment.objects.filter(user_id=current_user.id)
    context = {'category': category,
               'comments': comments}
    return render(request, "user_comments.html", context)


@login_required(login_url='/login')  # Check Login
def deletecomment(request, id):
    current_user = request.user
    Comment.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'Comment deleted!')
    return HttpResponseRedirect('/user/comments')



@login_required(login_url='/login')  # Check Login
def notes(request):
    category = Category.objects.all()

    current_user = request.user
    products = Product.objects.filter(user_id=current_user.id)
    form = ProductForm()
    context = {'category': category,
               'form': form,
               'products': products}
    return render(request, "user_products.html", context)



@login_required(login_url='/login')  # Check Login
def addnote(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = request.user
            data = Product()
            data.user_id = current_user.id
            data.title = form.cleaned_data['title']
            data.keywords = form.cleaned_data['keywords']
            data.description = form.cleaned_data['description']
            data.image = form.cleaned_data['image']
            data.category = form.cleaned_data['category']
            data.slug = form.cleaned_data['slug']
            data.detail = form.cleaned_data['detail']
            data.status = 'False'
            data.save()
            messages.success(request, "Your Note Insterted Successfully")
            return HttpResponseRedirect('/user/notes')
        else:
            messages.success(request, "Note Form Error" + str(form.errors))
            return HttpResponseRedirect('/user/addnote')
    else:
        category = Category.objects.all()
        form = ProductForm()
        context = {'form': form, 'category': category}
        return render(request, 'user_addnote.html', context)


@login_required(login_url='/login')  # Check Login
def noteedit(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Note Updated Successfully")
            return HttpResponseRedirect('/user/notes')
        else:
            messages.success(request, "Note Form Error" + str(form.errors))
            return HttpResponseRedirect('/user/noteedit' + str(id))
    else:
        category = Category.objects.all()
        form = ProductForm(instance=product)
        context = {'form': form, 'category': category}
        return render(request, 'user_addnote.html', context)


@login_required(login_url='/login')  # Check Login
def notedelete(request, id):
    current_user = request.user
    Product.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'Product deleted!')
    return HttpResponseRedirect('/user/notes')




@login_required(login_url='/login')  # Check Login
def noteaddimage(request, id):
    if request.method == 'POST':
        lasturl = request.META.get('HTTP_REFERER')
        form = ProductFilesForm(request.POST, request.FILES)
        if form.is_valid():
            data = Files()
            data.title = form.cleaned_data['title']
            data.note_id = id
            data.image = form.cleaned_data['image']
            data.save()
            messages.success(request, "Your image has been successfully uploaded")
            return HttpResponseRedirect(lasturl)
        else:
            messages.success(request, "Form Error" + str(form.errors))
            return HttpResponseRedirect(lasturl)
    else:
        product = Product.objects.get(id=id)
        images = Files.objects.filter(note_id=id)
        form = ProductFilesForm()
        context = {'form': form,
                   'product': product,
                   'images': images}
        return render(request, 'product_gallery.html', context)
