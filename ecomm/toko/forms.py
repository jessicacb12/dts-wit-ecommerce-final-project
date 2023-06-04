from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

from .models import PILIHAN_LABEL, PILIHAN_KATEGORI, PILIHAN_PEMBAYARAN

class CheckoutForm(forms.Form):
    alamat_1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Alamat Anda', 'class': 'textinput form-control'}))
    alamat_2 = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Apartement, Rumah, atau yang lain (opsional)', 'class': 'textinput form-control'}))
    negara = CountryField(blank_label='(Pilih Negara)').formfield(widget=CountrySelectWidget(attrs={'class': 'countryselectwidget form-select'}))
    kode_pos = forms.CharField(widget=forms.TextInput(attrs={'class': 'textinput form-outline', 'placeholder': 'Kode Pos'}))
    simpan_info_alamat = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    opsi_pembayaran = forms.ChoiceField(widget=forms.RadioSelect(), choices=PILIHAN_PEMBAYARAN)

class AddProductForm(forms.Form):
    nama_produk = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'textinput form-control'}
        ),
        max_length=100
    )
    harga = forms.FloatField()
    deskripsi = forms.Textarea(
        attrs={'class': 'textinput form-control'}
    )
    gambar = forms.ImageField()
    label = forms.ChoiceField(widget=forms.CheckboxInput(), choices=PILIHAN_LABEL)
    kategori = forms.ChoiceField(widget=forms.CheckboxInput(), choices=PILIHAN_KATEGORI)