import pytest
#import requests
import allure

class TestCreateBooking(object):

    @pytest.mark.positive
    @allure.title("verify the create booking status and booking ID shouldn't be null")
    @allure.description("create a booking from payload and verify the status is 200 and ID shouldn't be null")
    def test_create_booking_positive(self):
        pass
