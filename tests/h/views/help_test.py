# -*- coding: utf-8 -*-

import pytest
from pyramid import httpexceptions

from h.views import help


@pytest.mark.usefixtures("routes")
def test_welcome_page_redirects_to_new_url(pyramid_request):
    result = help.onboarding_page({}, pyramid_request)
    assert isinstance(result, httpexceptions.HTTPFound)


@pytest.mark.usefixtures("routes")
def test_help_page_returns_is_help_true(pyramid_request):
    result = help.help_page({}, pyramid_request)
    assert result["is_help"]


@pytest.mark.usefixtures("routes")
def test_custom_welcome_page(pyramid_request):
    result = help.custom_onboarding_page({}, pyramid_request)
    assert not result["is_help"]
    assert result["is_onboarding"]


@pytest.fixture
def routes(pyramid_config):
    pyramid_config.add_route("help", "/docs/help")
    pyramid_config.add_route("onboarding", "/welcome/")
    pyramid_config.add_route("custom_onboarding", "/welcome/{slug}")
    pyramid_config.add_route("embed", "/embed")
