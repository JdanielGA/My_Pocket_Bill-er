# apps/customers/views.py
from django.db.models import Q
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Customer
from .forms import CustomerForm
from django.urls import reverse_lazy

# Home page view for the customers app.
class CustomerHomeView(ListView):
    model = Customer
    template_name = 'customers/customer_home.html'
    context_object_name = 'customers'

    # Functions to search customers by name, email or customer ID.
    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q', None)
        if search_query:
            queryset = queryset.filter(
                Q(first_name__icontains=search_query) |
                Q(last_name__icontains=search_query) |
                Q(email__icontains=search_query) |
                Q(customer_id__icontains=search_query)
            )
        else:
            queryset = queryset.order_by('-created_at')[:5]

        return queryset
    
    # Get context data for the home page.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_customers'] = Customer.objects.count()
        context['recent_customers'] = Customer.objects.all().order_by('-created_at')[:5]
        return context

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