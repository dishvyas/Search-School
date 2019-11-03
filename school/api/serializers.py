from rest_framework import serializers

from school.models import SchoolPost
# block|cluster|schoolid|schoolname|category|gender|medium_of_inst|address|area|pincode|landmark|identification1|busroutes

class SchoolPostSerializer(serializers.ModelSerializer):

	class Meta:
		model = SchoolPost
		fields = ['block', 'schoolid', 'schoolname', 'category', 'gender', 'medium_of_inst', 'address', 'area', 'pincode', 'landmark', 'busroutes']


	





