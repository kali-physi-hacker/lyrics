from django.shortcuts import render


def test(request):
    template = ""
    context = {}
    return render(request=request, template_name=template, context=context)
