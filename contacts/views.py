from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from .models import Person, ExtraDetail
from .forms import ContactForm, DeleteForm


def index(request):
    contacts = Person.objects.all()
    return render(request, 'index.html', {'contacts': contacts})


@require_http_methods(["GET", "POST"])
def new_contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            person = Person(first_name=data['first_name'],
                            last_name=data['last_name'],
                            phone_no=data['phone_no'],
                            address=data['address'],
                            email=data['email'])
            person.save()
            extra_detail = ExtraDetail(person=person,
                                       website=data['website'],
                                       notes=data['notes'],
                                       birthday=data['birthday'],
                                       relationship=data['relationship'])
            extra_detail.save()
            return redirect(reverse('index'))
        return render(request, 'new_contact.html', {'form': form})
    else:
        return render(request, 'new_contact.html', {'form': ContactForm})


@require_http_methods(["GET", "POST"])
def edit_contact(request, contact_id):
    person = Person.objects.get(pk=contact_id)
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            person.first_name = data['first_name']
            person.last_name = data['last_name']
            person.phone_no = data['phone_no']
            person.address = data['address']
            person.extradetail.website = data['website']
            person.extradetail.relationship = data['relationship']
            person.extradetail.notes = data['notes']
            person.extradetail.birthday = data['birthday']
            person.save()
            person.extradetail.save()
            messages.success(request, "Contact updated")
            return redirect(reverse('index'))
        return render(request, 'new_contact.html', {'form': form,
                                                    'contact': person})
    else:
        form = ContactForm(initial={'birthday': person.extradetail.birthday})
        return render(request, 'new_contact.html', {'form': form,
                                                    'contact': person})


@require_http_methods(["GET", "POST"])
def delete_contact(request, contact_id):
    contact = Person.objects.get(pk=contact_id)
    if request.method == "POST":
        form = DeleteForm(request.POST)
        if form.is_valid():
            contact.delete()
            messages.success(request, "Contact deleted")
            return redirect(reverse('index'))
        return render(request, 'new_contact.html', {'form': form})
    else:
        return render(request, 'delete_contact.html', {'contact': contact})


def display_contacts_for_character(request, character):
    contacts = Person.objects.filter(first_name__istartswith=character)
    return render(request, 'index.html', {'contacts': contacts})
