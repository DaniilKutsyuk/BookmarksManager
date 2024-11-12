from rest_framework.response import Response
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view
from .models import Bookmark
from .serializers import BookmarkSerializer
from .forms import BookmarkForm


def bookmark_list_view(request):
    bookmarks = Bookmark.objects.all()
    return render(request, 'bookmark_list.html', {'bookmarks': bookmarks})

@api_view(['GET'])
def bookmark_list_api_view(request):
    bookmarks = Bookmark.objects.all()
    serializer = BookmarkSerializer(bookmarks, many=True)
    return Response({'bookmarks': serializer.data})

def create_bookmark_view(request):
    if request.method == 'POST':
        form = BookmarkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bookmark_list')  # Redirects to the bookmark list after saving
        else:
            # If form is not valid, display errors on the page
            return render(request, 'create_bookmark.html', {'form': form})
    else:
        form = BookmarkForm()
    return render(request, 'create_bookmark.html', {'form': form})

@api_view(['POST'])
def create_bookmark_api_view(request):
    serializer = BookmarkSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Bookmark created successfully'}, status=201)
    return Response(serializer.errors, status=400)

def view_bookmark_view(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)
    return render(request, 'view_bookmark.html', {'bookmark': bookmark})

@api_view(['GET'])
def view_bookmark_api_view(request, pk):
    bookmark = Bookmark.objects.get(pk=pk)
    serializer = BookmarkSerializer(bookmark)
    return Response({'bookmark': serializer.data})

def update_bookmark_view(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)
    if request.method == 'POST':
        form = BookmarkForm(request.POST, instance=bookmark)
        if form.is_valid():
            form.save()
            return redirect('bookmark_list')
    else:
        form = BookmarkForm(instance=bookmark)
    return render(request, 'update_bookmark.html', {'form': form})

@api_view(['PUT'])
def update_bookmark_api_view(request, pk):
    bookmark = Bookmark.objects.get(pk=pk)
    serializer = BookmarkSerializer(bookmark, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Bookmark updated successfully'})
    return Response(serializer.errors, status=400)

def delete_bookmark_view(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)
    bookmark.delete()
    return redirect('bookmark_list')

@api_view(['DELETE'])
def delete_bookmark_api_view(request, pk):
    bookmark = Bookmark.objects.get(pk=pk)
    bookmark.delete()
    return Response({'message': 'Bookmark deleted successfully'}, status=204)
