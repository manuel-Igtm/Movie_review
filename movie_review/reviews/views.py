from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from .models import Review
from .serializers import ReviewSerializer
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets, filters
from rest_framework.response import Response
from rest_framework import status
 #from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class ReviewListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request,*args, **kwargs):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request,*args, **kwargs):
        serializer = ReviewSerializer(data= self.request.data)
        if serializer.is_valid():
            serializer.save(user = self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReviewDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk, user):
        try:
            return Review.objects.get(pk=pk, user=user)
        except Review.DoesNotExist:
            return None

    def get(self, request, pk,*args, **kwargs):
        review = Review.objects.filter(pk=pk).first()
        if not review:
            return Response({'error': 'Review not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # def patch(self, request, pk,*args, **kwargs):
    #     review = self.get_object(pk, request.user)
    #     if not review:
    #         return Response({'error': 'You can only update your own reviews'}, status=status.HTTP_403_FORBIDDEN)
    #     serializer = ReviewSerializer(review, data=request.data,partial = True)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, *args, **kwargs):
    # Attempt to filter the user's review by pk and the logged-in user
        review = Review.objects.filter(pk=pk, user=request.user).first()
        
        if not review:
            return Response(
                {'error': 'You can only update your own reviews'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        # Use the ReviewSerializer with partial update enabled
        serializer = ReviewSerializer(review, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk,*args, **kwargs):
        review = self.get_object(pk, request.user)
        if not review:
            return Response({'error': 'You can only delete your own reviews'}, status=status.HTTP_403_FORBIDDEN)
        review.delete()
        return Response({'message': 'Review deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class ReviewPagination(PageNumberPagination):
    page_size = 10  # Default page size
    page_size_query_param = 'size'  # Allow clients to set custom page size


# class ReviewViewSet(viewsets.ModelViewSet):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     pagination_class = ReviewPagination

#     # Add filtering, searching, and sorting
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#     filterset_fields = ['movie_title', 'rating']  # Filters for exact matches
#     search_fields = ['movie_title', 'review_content']  # Search for partial matches
#     ordering_fields = ['rating', 'created_at']  # Allow sorting by these fields
#     ordering = ['-created_at']  # Default ordering (most recent first)

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)