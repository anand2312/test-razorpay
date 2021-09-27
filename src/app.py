import os

import razorpay

from dotenv import load_dotenv, find_dotenv
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

load_dotenv(find_dotenv())


app = FastAPI()
templates = Jinja2Templates(directory="templates")

auth = os.environ.get("KEY_ID"), os.environ.get("KEY_SECRET")
razorpay_client = razorpay.Client(auth=auth)


# example; use a database or something else.
products_prices = {
    "apple": 10,
    "orange": 12,
    "pear": 15
}


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/payment/process")
async def do_payment(request: Request, product: str = Form(...), qty: int = Form(...)):
    total_cost = products_prices[product] * qty * 100  # razorpay expects amount in currency sub units i.e paise
    data = {"amount": total_cost, "currency": "INR"}
    pay_response = razorpay_client.order.create(data=data)  # although the integration page passes these as kwargs, that leads to errors

    order_id = pay_response["id"]

    return templates.TemplateResponse("confirm.html", {"request": request, "amount": total_cost, "order_id": order_id})


@app.post("/payment/success")
async def finish_payment():
    return HTMLResponse("<h1>Payment successful</h1>")
