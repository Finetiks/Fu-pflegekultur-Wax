from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
sitemaps = {

}
urlpatterns = [
  path("", views.index, name="index"),
  path("gift-vouchers", views.gift_voucher, name="gift_voucher"),
  path("about", views.about, name="about"),
  path("contacts", views.contact, name="contacts")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
