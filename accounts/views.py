from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model, login, logout, authenticate

User = get_user_model()

# Create your views here.
def signup(request):
    if request.method == "POST":
        """Traiter le formulaire: ici si la requete est de type post
        on reccupere  les informtion de formulaire 
        et on creye l'utlisateur, on le connect sur notre site et on le dirige vers page l'index
        """
        username = request.POST.get("username")
        password = request.POST.get("password")
        user  = User.objects.create_user(username=username,
                                        password=password)
        login(request, user)
        return redirect('index')
    return render(request, 'accounts/signup.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('index')
    return render(request, 'accounts/login.html')
    

def logout_user(request):
    logout(request)
    return redirect('index')