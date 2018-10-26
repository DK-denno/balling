from django.shortcuts import render,redirect
from .forms import SignUpForm
from django.contrib.auth import login,authenticate
from .models import Profile,Message,Fixtures,Teams
from .forms import ProfileForm,ChangeLeagueForm,MessageForm
# Create your views here.


def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,email=email,password=password)
            user.save()
            profile = Profile(user=user)
            profile.save()
            login(request,user)
            return redirect('index')
        else:
            print('error')
    else:
        form = SignUpForm()
        return render(request,'signup.html',{"form":form})




def index(request):
    message_form = MessageForm()
    if request.method == 'POST':
        message_form = MessageForm(request.POST)
        if message_form.is_valid():
            messaging = message_form.save(commit=False)
            messaging.user = request.user
            messaging.league = request.user.profile.league
            messaging.save()
            return redirect('/')
    messages = Message.objects.filter(league=request.user.profile.league)
    if request.user.league == None:
        message = 'PLEASE CLICK ON THE PROFILES OPTION AND CHOOSE YOUR TEAM AND LEAGUE'
        return render(request,'index.html',{"habari":message,"message_form":message_form})
    return render(request,'index.html',{"messages":messages,"form":message_form})

def profile(request):
    form = ProfileForm()
    changeLeague = ChangeLeagueForm()
    print(request.user.profile.dp)
    if request.method == 'POST':
        changeLeague = ChangeLeagueForm(request.POST,instance=request.user.profile)
        form = ProfileForm(request.POST,request.FILES,instance=request.user.profile)
        if form.is_valid():
            form.save()       
        if changeLeague.is_valid():
                changeLeague.save()  
    return render(request,'profile/profile.html',{"form":form,"changeLeague":changeLeague})

    
def team(request):
    team = Teams.objects.get(name=request.user.profile.team.name)
    profile = Profile.objects.filter(team=team)
    fixtures = Fixtures.objects.filter(league=request.user.profile.league)
    return render(request,'fixtures.html',{"fixtures":fixtures, "players":profile, "team":team})

