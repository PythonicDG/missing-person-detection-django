def navbar_context(request):
    app_pages = {
        "dashboard",
        "report_missing",
        "report_found",
        "view_found",
        "my_reports",
        "view_report",
        "profile",
        "update_profile",
        "inbox",
        "open_chat",
    }

    url_name = None
    if hasattr(request, "resolver_match") and request.resolver_match:
        url_name = request.resolver_match.url_name

    return {
        "show_app_nav": request.user.is_authenticated and url_name in app_pages
    }
