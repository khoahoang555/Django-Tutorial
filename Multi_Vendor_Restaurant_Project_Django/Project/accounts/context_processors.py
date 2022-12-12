from vendor.models import Vendor

# This is function used to allow all page can access information of vendor
def get_vendor(request):
    try:
        vendor = Vendor.objects.get(user = request.user)
    except:
        vendor = None
    return dict(vendor=vendor)