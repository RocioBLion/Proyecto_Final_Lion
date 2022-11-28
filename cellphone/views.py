from django.contrib import messages
from django.shortcuts import render

from cellphone.models import Cellphone
from cellphone.forms import CellphoneForm

def create_cellphones(request):
    if request.method == "POST":
        cellphone_form = CellphoneForm(request.POST)
        print("-------------------------------------+++++++++++++++++")
        if cellphone_form.is_valid():
            data = cellphone_form.cleaned_data
            actual_objects = Cellphone.objects.filter(
                brand=data["brand"], model=data["model"], description=data["description"]
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"Cellphone {data['brand']} - {data['model']} - {data['description']} ya está creado",
                )
            else:
                cellphone = Cellphone(brand=data["brand"], model=data["model"],description=data["description"],)
                cellphone.save()
                messages.success(
                    request,
                    f"Cellphone {data['brand']} - {data['model']} - {data['description']}  creado exitosamente!",
                )

            return render(
                request=request,
                context={"cellphone": Cellphone.objects.all()},
                template_name="cellphone/cellphone_list.html",
            )

    cellphone_form = CellphoneForm(request.POST)
    context_dict = {"form": cellphone_form}
    return render(
        request=request,
        context=context_dict,
        template_name="cellphone/cellphone_form.html",
    )

def cellphones(request):
    return render(
        request=request,
        context={"accessories": Cellphone.objects.all()},
        template_name="accessorie/accessorie_list.html",
    )