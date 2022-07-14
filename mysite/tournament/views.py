from datetime import datetime
from unicodedata import name
from venv import create
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from .models import MyUser
from django.contrib.auth.models import User
from .models import Tournament, Player, PlayersInTournament
from .forms import TournamentForm, PlayerForm, UpdateTournamentForm
from django.contrib.auth.decorators import login_required

def format_input_date(date):

    output=[None]*3
    output[0]=int(date[0:4])
    output[1]=int(date[5:7])
    output[2]=int(date[9:10])
    try:
        output.append(int(date[11:13]))
    except:
        pass
    try:
        output.append(int(date[14:16]))
    except:
        pass
    return output

def base_view(request):
    return render(request, 'tournament/base_view.html')
def login_view(request):
    if request.method == "POST":
        password=request.POST.get('password')
        name=request.POST.get('name')
        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home_view')
        else:
            messages.success(request, ("There Was An Error Logging In, Try Again..."))	
            return redirect('/login_view')
        
    else:
        return render(request, 'tournament/login_view.html', {})	

def home_view(request):
    return render(request, 'tournament/home_view.html')

def register_view(request):
    if request.method == "POST":
        password_=request.POST.get('password')
        email_=request.POST.get('email')
        name_=request.POST.get('name')
        birth_date_=request.POST.get('birth_date')
        if not ( User.objects.filter(username=name).exists() and MyUser.objects.filter(username=name).exists() ):
            try:
                new_user=User.objects.create_user(username=name_, password=password_)
                new_myuser=MyUser.objects.create(email=email_, name=name_, birth_date=birth_date_)
                new_myuser.save()
                messages.info(request, 'You have registered')
                return redirect('/home_view')
            except:
                messages.info(request, 'This name is used, try again')
                return redirect('/home_view')
        else:
            messages.info(request, 'This name is used')
            return redirect('/home_view')

    else:
        return render(request, 'tournament/register_view.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('/home_view')

@login_required
def create_tournament(request):

    context ={}

    form = TournamentForm(request.POST or None)
    if form.is_valid():
        form.instance.creator=request.user
        form.save() 
        messages.info(request, 'You created a tournament')
        return redirect('/home_view')
         
    context['form']= form
    return render(request, "tournament/create_tournament.html", context)  

@login_required
def create_player(request):
    context={}
    form = PlayerForm(request.POST or None)
    if form.is_valid():
        messages.info(request, 'You created a player')
        form.save()
        return redirect('/home_view')
    context['form']= form
    return render(request, "tournament/create_tournament.html", context)  

@login_required
def tournament_my_table_view(request):
    query_results= Tournament.objects.filter(creator=request.user)
    
    tournaments={
        "tournament":query_results
    }
    return render(request, "tournament/tournament_my_table_view.html", tournaments) 

def tournament_table_view(request):
    tournaments={}
    if request.method == "POST" and request.user.is_authenticated == 1:
        start_date=request.POST.get('start_date')
        end_date_from_post=request.POST.get('end_date')
        try:
            s_date=format_input_date(start_date)
            e_date=format_input_date(end_date_from_post) 
            start = datetime(*s_date)
            end = datetime(*e_date)
            if end>=datetime.now() or  end < start:
                messages.info(request, 'Wrong date input')
                return redirect('/home_view')
        
            query_results= Tournament.objects.filter(begin_date__range=[start, end]).exclude(end_date= None)
            tournaments={
             "tournament":query_results
            } 
        except:
            messages.info(request, 'Wrong date input or none tournaments to show')
    else:
        if request.user.is_authenticated == 0:
            query_results= Tournament.objects.filter(end_date = None).filter(begin_date__lte=datetime.today())
            tournaments={
            "tournament":query_results
         }
    print(tournaments)
    return render(request, "tournament/tournament_table_view.html", tournaments) 

@login_required
def tournament_view(request, id):
    obj = Tournament.objects.get(pk=id)
    query_results=Player.objects.filter()
    player_in_tournamets= PlayersInTournament.objects.filter(tournament=obj)
    
    result={
        "tournament":obj,
        "player":query_results,
        "player_in_tournamets":player_in_tournamets
    }

    return render(request, "tournament/tournament_view.html", result)

@login_required
def delete_tournament_view(request, id):
    context ={}
    obj = get_object_or_404(Tournament, id = id)
    if request.method =="POST":
        obj.delete()
        return redirect('/home_view')

@login_required
def update_tournament_view(request, pk):
    obj = Tournament.objects.get(id = pk)
    form = UpdateTournamentForm(instance=obj)
    if request.method =="GET":
        form = UpdateTournamentForm(request.GET, instance=obj)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            url = "/tournament/"+str(pk)
            return redirect(url)
    context = {"form":form}
    return render(request, "tournament/update_view.html", context)

@login_required
def add_player(request, pk, id):
    x = Tournament.objects.get(id = id)
    y = Player.objects.get(id = pk)
    obj=PlayersInTournament(tournament = x , player = y)
    player_in_tournamets= PlayersInTournament.objects.filter(tournament=x)
    print(x.max_number_of_player)
    print( player_in_tournamets.count())
    print(x.max_number_of_player >= player_in_tournamets.count())
    if x.max_number_of_player > player_in_tournamets.count() and x.end_date == None:
        try:
            obj.save()
        except:
            messages.info(request, 'This players in already in this tournament')
        url = "/tournament/"+str(id)
        return redirect(url)
    else:
        messages.info(request, 'This tournament has enough players or this tournaments is over')
        url = "/tournament/"+str(id)
        return redirect(url)

@login_required  
def delete_player_from_tournament(request, pk, id):

    obj=PlayersInTournament.objects.get(tournament = id , player = pk)
    if request.method =="POST":
        obj.delete()
        url = "/tournament/"+str(id)
        return redirect(url)

