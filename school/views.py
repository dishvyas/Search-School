from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse
from school import models
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import ListAPIView

def get_school_queryset(self):
	queryset = [] 
	for q in queries:
		posts = SchoolPost.model.objects.all()

		for post in posts:
			queryset.append(post)

	return list(set(queryset))	