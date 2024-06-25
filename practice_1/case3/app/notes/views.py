from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserRegistrationForm
from django.views.generic import ListView
from .models import Note
from .models import Note
from .forms import NoteForm

def index(request):
    notes = []
    if request.user.is_authenticated:
        notes = Note.objects.filter(user=request.user)

    return render(request, 'index.html', {'notes': notes})

def features(request):
    return render(request, 'features.html')

def contacts(request):
    return render(request, 'contacts.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.user = request.user
            new_note.save()

            return redirect('index')
    else:
        form = NoteForm()

    return render(request, 'notes/note_create.html', {'form': form})


def note_view(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)

    return render(request, 'notes/note_view.html', {'note': note})

def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)
    note.delete()

    return redirect('index')