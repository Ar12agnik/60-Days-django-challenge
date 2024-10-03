from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Snippet
from snippets.serializer import SnippetSerializer


@api_view(['GET', 'POST'])
def snippet_list(request):
    """
    list all snippets or create a new one
    """
    if request.method == "GET":
        snippets = Snippet.objects.all()
        serelizer = SnippetSerializer(snippets, many=True)
        return Response(serelizer.data)
    elif request.method == "POST":
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'PUT', 'DELETE'])
def snippet_detail(request,pk):
    try:
        snippet = Snippet.objects.get(id=pk)
    except snippet.DoesnotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serelizer = SnippetSerializer(snippet)
        return Response(data=serelizer.data)
    elif request.method == 'PUT':
        data=request.data
        serelizer = SnippetSerializer(data=data)
        if serelizer.is_valid():
            serelizer.save()
            return Response(data=serelizer.data)
        else:
            return Response(data=serelizer.errors)
    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
        
        
