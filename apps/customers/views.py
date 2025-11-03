# apps/customers/views.py
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Customer
from .forms import CustomerForm
from django.urls import reverse_lazy

# Home page view for the customers app.
class CustomerHomeView(TemplateView):
    template_name = 'customers/customer_home.html'

# Create view for adding a new customer.
class CustomerCreateView(CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/customer_form.html'
    success_url = reverse_lazy('customers:home')

# List view for displaying all customers.
class CustomerListView(ListView):
    model = Customer
    template_name = 'customers/customer_list.html'
    context_object_name = 'customers'

# Detail view for displaying a single customer's details.
class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customers/customer_detail.html'
    context_object_name = 'customer'

# Update view for editing an existing customer.
class CustomerUpdateView(UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = 'customers/customer_form.html'
    success_url = reverse_lazy('customers:home')

# Delete view for removing a customer.
class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customers/customer_confirm_delete.html'
    success_url = reverse_lazy('customers:home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        next_url = self.request.GET.get('next', self.success_url)
        context['next_url'] = next_url
        return context