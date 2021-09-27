# Testing Razorpay

Testing out the Razorpay payment gateway interface, by using it's Python SDK along with FastAPI.

## Steps
[The razorpay standard web integration](https://razorpay.com/docs/payment-gateway/web-integration/standard/) page explains the process pretty well.

1. Gather user info needed and ascertain amount of transaction
2. Place order to razorpay (the function `client.order.create` had some inconsistencies with the example on the page, see src)
3. Use the `order_id` returned by step 2 to lead to checkout page
3. Done!


You should ideally also keep track of order IDs by yourself on the server side, but that isn't covered here.

## Project test
Clone the repository, `cd` into it

Download test API keys from your razorpay dashboard and add them to a `.env` file with the keys `KEY_ID` and `KEY_SECRET`

Run `poetry install`

Run `poetry run uvicorn app:app --reload`
