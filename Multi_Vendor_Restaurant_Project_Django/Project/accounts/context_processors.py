from vendor.models import Vendor
from django.conf import settings

# This is function used to allow all page can access information of vendor
def get_vendor(request):
    try:
        vendor = Vendor.objects.get(user = request.user)
    except:
        vendor = None
    return dict(vendor=vendor)

def get_google_api(request):
    return {'GOOGLE_API_KEY': settings.GOOGLE_API_KEY}