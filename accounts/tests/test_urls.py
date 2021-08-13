from django.test import TestCase
from django.urls import reverse, resolve
from accounts.views import home, loginPage, logoutUser, userPage, accountSettings, products, registerPage, customer, createOrder, updateOrder, deleteOrder


# Run Test
class TestUrls(TestCase):

    # test home route
    def test_home_route_is_resolved(self):
        url = reverse('home')
        # assert that resolved url correspond to the correct view
        self.assertEquals(resolve(url).func, home)
        # assert that url correspond url name
        self.assertEquals(url, '/')

    # test if login url is resolved
    def test_login_url_is_resolved(self):
        url = reverse('login')
        # assert that resolved url correspond to the correct view
        self.assertEquals(resolve(url).func, loginPage)
        # assert that url correspond url name
        self.assertEquals(url, '/login/')
        # # assert status code of responses
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)

    # test logout url is resolved
    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        # assert that resolved url correspond to the correct view
        self.assertEquals(resolve(url).func, logoutUser)
        # assert that url correspond url name
        self.assertEquals(url, '/logout/')

    # test user url is resolved
    def test_user_url_is_resolved(self):
        url = reverse('user-page')
        # assert that resolved url correspond to the correct view
        self.assertEquals(resolve(url).func, userPage)
        # assert that url correspond url name
        self.assertEquals(url, '/user/')

    # test account url is resolved
    def test_account_url_is_resolved(self):
        url = reverse('account')
        # assert that resolved url correspond to the correct view
        self.assertEquals(resolve(url).func, accountSettings)
        # assert that url correspond url name
        self.assertEquals(url, '/account/')

    # test products url is resolved
    def test_products_url_is_resolved(self):
        url = reverse('products')
        # assert that resolved url correspond to the correct view
        self.assertEquals(resolve(url).func, products)
        # assert that url correspond url name
        self.assertEquals(url, '/products')

    # test register url is resolved
    def test_register_url_is_resolved(self):
        url = reverse('register')
        # assert that resolved url correspond to the correct view
        self.assertEquals(resolve(url).func, registerPage)
        # assert that url correspond url name
        self.assertEquals(url, '/register')

    # test customer url is resolved
    def test_customer_url_is_resolved(self):
        pk_test = '1'
        url = reverse('customer', args=pk_test)
        # assert that resolved url correspond to the correct view
        self.assertEquals(resolve(url).func, customer)
        # # assert that url correspond url name
        self.assertEquals(url, '/customer/1/')

    # test create_order url is resolved
    def test_create_order_url_is_resolved(self):
        pk = '1'
        url = reverse('create_order', args=pk)
        # assert that resolved url correspond to the correct view
        self.assertEquals(resolve(url).func, createOrder)
        # # assert that url correspond url name
        self.assertEquals(url, '/create_order/1')

    # test update_order url is resolved
    def test_update_order_url_is_resolved(self):
        pk = '1'
        url = reverse('update_order', args=pk)
        # assert that resolved url correspond to the correct view
        self.assertEquals(resolve(url).func, updateOrder)
        # # assert that url correspond url name
        self.assertEquals(url, '/update_order/1')

    # test delete_order url is resolved
    def test_delete_order_url_is_resolved(self):
        pk = '1'
        url = reverse('delete_order', args=pk)
        # assert that resolved url correspond to the correct view
        self.assertEquals(resolve(url).func, deleteOrder)
        # # assert that url correspond url name
        self.assertEquals(url, '/delete_order/1')