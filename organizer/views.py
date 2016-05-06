# organizer.views

from django.shortcuts import get_object_or_404, render

from .models import Tag


def homepage(request):
	return render(request, 'organizer/tag_list.html', {'tag_list': Tag.objects.all()})


def tag_detail(request, slug):
	tag = get_object_or_404(Tag, slug__iexact = slug)
	return render(request, 'organizer/tag_detail.html', {'tag': tag})

	










# homepage original code
	# tag_list = Tag.objects.all()
	# template = loader.get_template('organizer/tag_list.html')
	# context = Context({'tag_list': tag_list})
	# output = template.render(context)
	# return HttpResponse(output)

	# return render_to_response('organizer/tag_list.html', {'tag_list': Tag.objects.all()})

# tag_detail original code
	# template = loader.get_template('organizer/tag_detail.html')
	# context = Context({'tag': tag})
	# return HttpResponse(template.render(context))

	# return render_to_response('organizer/tag_detail.html', {'tag': tag})