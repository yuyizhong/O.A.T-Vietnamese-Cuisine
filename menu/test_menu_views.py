from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import MenuItem, Category


class MenuAppTests(TestCase):
    """
    Test cases for menu app as logged in user
    """
    def setUp(self):
        """ Test Setup """
        self.category = Category.objects.create(name='Test Category')
        # Create menu contents
        self.menu_item = MenuItem.objects.create(
            name='Test Menu Item',
            description='Test description',
            price=9.99,
            category=self.category
        )
        # Create superuser/staff
        self.user = User.objects.create_superuser(
            username='admin',
            password='adminpassword',
            email='admin@example.com'
        )

    def test_menu_list_view(self):
        """
        Test menu-list accessability, template render to any users
        """
        url = reverse('menu-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu/menu_list.html')

    def test_add_menu_view(self):
        """
        Test add_menu_view access to staff user only
        with correct template render
        """
        self.client.force_login(self.user)
        url = reverse('add-menu')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu/add_menu.html')

    def test_edit_menu_view(self):

        """
        Test edit_menu_view access to staff user only
        with correct template render
        """
        self.client.force_login(self.user)
        url = reverse('edit-menu', args=[self.menu_item.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'menu/edit_menu.html')

    def test_hide_menu_view(self):
        """
        Test hind/unhide_menu function to staff user only
        """
        self.client.force_login(self.user)
        url = reverse('hide-menu', args=[self.menu_item.id])
        response = self.client.get(url)
        # Expecting a redirect
        self.assertEqual(response.status_code, 302)

    def test_delete_menu_view(self):
        """
        Test delete_menu function to staff user only
        """
        self.client.force_login(self.user)
        url = reverse('delete-menu', args=[self.menu_item.id])
        response = self.client.get(url)
        # Expecting a redirect
        self.assertEqual(response.status_code, 302)
