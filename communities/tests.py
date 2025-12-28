from rest_framework.test import APITestCase
from accounts.models import CustomUser
from .models import Community
from django.urls import reverse
from django.utils import timezone

class CommunityViewTests(APITestCase):

    def test_new_user_cannot_create_community(self):

        user = CustomUser.objects.create_user(
            email="newuser@email.com",
            password="userpassword"
        )
        user.date_joined = timezone.now() - timezone.timedelta(days=5)
        user.save()

        self.client.force_authenticate(user=user)

        response = self.client.post(
            reverse("community_list"),
            {
                "community_name": "hohoho",
                "description": "santa and his one horse sleigh",
            },
            format='json'
        )

        self.assertEqual(response.status_code, 403)
        self.assertIn(
            "You must be a member for at least 30 days to create a community.",
            str(response.data)
        )

        self.assertFalse(
            Community.objects.filter(community_name="hohoho").exists()
        )



