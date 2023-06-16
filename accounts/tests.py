from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client

# Create your tests here.
class AdminSiteTests(TestCase):
    """Test for custom admin"""

    def setUp(self):
        """Create user and client"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            first_name = 'Super',
            last_name = 'User',
            username = 'Super User',
            email='admin@example.com',
            password='test123',
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            first_name = 'Test',
            last_name = 'User',
            username='Test User',
            email = 'user@example.com',
            password='testpass123',
        )

    def test_user_list(self):
        """Test if user are listed on the page"""
        url = reverse('admin:accounts_account_changelist')
        result = self.client.get(url)

        self.assertContains(result, self.user.first_name)
        self.assertContains(result, self.user.last_name)
        self.assertContains(result, self.user.email)

    def test_edit_user_page(self):
        """Test edit the user page works"""
        url = reverse('admin:accounts_account_change', args = [self.user.id])
        result = self.client.get(url)
        self.assertEqual(result.status_code, 200)

    def test_create_user_page(self):
        """Test the create user page works"""
        url = reverse('admin:accounts_account_add')
        result = self.client.get(url)

        self.assertEqual(result.status_code, 200)
