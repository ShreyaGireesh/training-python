from django.http import HttpResponseRedirect

class CustomErrorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("✅ CustomErrorMiddleware is executing!")
        try:
            response = self.get_response(request)
            # 🚨 Manually raise an exception to test middleware behavior
            raise ValueError("Test exception inside middleware")  
        except Exception as e:
            print(f"⚠️ Exception caught in middleware: {e}")  # Log the error
            return self.handle_exception(request)

    def handle_exception(self, request):
        print("🔄 Redirecting to external error page...")
        return HttpResponseRedirect("http://127.0.0.1:5500/frontend/error.html")
