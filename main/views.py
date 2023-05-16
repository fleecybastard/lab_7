from django.views.generic import ListView, CreateView, DeleteView, DetailView
from django.urls import reverse_lazy

from main.models import AirLine, AirCraft
from main.filters import AirCraftFilter


class AirLineListView(ListView):
    model = AirLine
    template_name = 'main/airline_list.html'
    context_object_name = 'airline_list'


class AirLineDetailView(DetailView):
    model = AirLine
    context_object_name = 'airline'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        airline = context_data[self.context_object_name]
        context_data['aircrafts'] = AirCraft.objects.filter(airline=airline)
        return context_data


class AirLineDeleteView(DeleteView):
    model = AirLine
    context_object_name = 'airline'
    success_url = reverse_lazy('airline-list')
    template_name = 'main/airline_delete.html'


class AirLineCreateView(CreateView):
    model = AirLine
    fields = ['name']
    success_url = reverse_lazy('airline-list')
    template_name = 'main/airline_create.html'


class AirCraftCreateView(CreateView):
    model = AirCraft
    fields = ['model', 'capacity', 'payload', 'flight_distance', 'fuel_per_hour']
    template_name = 'main/aircraft_create.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['pk'] = self.kwargs['pk']
        return context_data

    def form_valid(self, form):
        form.instance.airline = AirLine.objects.get(id=self.kwargs['pk'])
        return super(AirCraftCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('airline-detail', kwargs={'pk': self.kwargs['pk']})


class AirCraftDeleteView(DeleteView):
    model = AirCraft
    context_object_name = 'aircraft'
    template_name = 'main/aircraft_delete.html'

    def form_valid(self, form):
        self.airline_pk = self.object.airline.id
        return super(AirCraftDeleteView, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('airline-detail', kwargs={'pk': self.airline_pk})


class AirLineFilterView(DetailView):
    model = AirLine
    context_object_name = 'airline'
    template_name = 'main/airline_filter.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        airline = context_data[self.context_object_name]
        air_crafts_filter = AirCraftFilter(self.request.GET,
                                                   queryset=AirCraft.objects.filter(airline_id=airline.id))

        context_data['aircrafts'] = air_crafts_filter.qs
        context_data['form'] = air_crafts_filter.form
        return context_data



