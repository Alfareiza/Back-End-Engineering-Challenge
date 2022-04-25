from django.http import JsonResponse
from django.shortcuts import render, redirect

from xml_converter.forms import XmlForm
from xml_converter.resources import handle_xml_file


def upload_page(request):
    """
    Main view : It has a form for receiving a xml file.
    @param request:
    @return:
    """
    if request.method == 'POST':
        form = XmlForm(request.POST, request.FILES)
        if form.is_valid():
            # import pdb;  pdb.set_trace()
            file = request.FILES.get('file', False)
            if file.name.endswith('.xml'):
                xml_converted = handle_xml_file(file)
                return JsonResponse(xml_converted)
            else:
                return JsonResponse(status=400, data={'message': 'Only XML files are supported.'})
        else:
            return render(request, "upload_page.html", {'form': form}, status=400)

    form = XmlForm()
    return render(request, "upload_page.html", {'form': form})


def home(request):
    """
    If someones try to access home. It'll be redirected to the upload_page view.
    """
    return redirect(upload_page)
