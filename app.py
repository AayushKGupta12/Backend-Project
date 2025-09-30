from flask import Flask, jsonify, render_template
from flask_cors import CORS
import requests
import os
from mistralai import Mistral
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import requests
from datetime import datetime, timezone

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": [
    "http://localhost:5175",
    "http://localhost:5174",
    "http://localhost:5173"
]}})


@app.route('/')
def blogs():
    return("Succefully Rendered")

@app.route('/contact')
def contact():
  return render_template("contact.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/service')
def service():
    return render_template("service.html")




@app.route('/company-news')
def company_news():


    data = {
  "Stripe": {
    "Role": "Software Engineering New Grad",
    "Stipend": "₹12L - ₹15L LPA",
    "Loc": "Bengaluru",
    "Link": "https://stripe.com/careers",
    "Batch": "2026",
    "Logo": "https://img.logo.dev/stripe.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Stripe Intern": {
    "Role": "Software Engineer Intern",
    "Stipend": "₹92K - ₹1L/month",
    "Loc": "Bengaluru",
    "Link": "https://stripe.com/careers",
    "Batch": "2026 to 2027",
    "Logo": "https://img.logo.dev/stripe.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "EY": {
    "Role": "Data Scientist / Machine Learning Engineer",
    "Stipend": "₹15L - ₹16L LPA",
    "Loc": "Kolkata",
    "Link": "https://www.ey.com/en_in/careers",
    "Batch": "2026 to 2027",
    "Logo": "https://img.logo.dev/ey.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Kaleris": {
    "Role": "Associate Software Engineer Intern",
    "Stipend": "₹25K - ₹42K/month",
    "Loc": "Chennai",
    "Link": "https://kaleris.com/company/careers/",
    "Batch": "2024 to 2025",
    "Logo": "https://img.logo.dev/kaleris.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Seagate": {
    "Role": "Automation Intern",
    "Stipend": "₹17K - ₹33K/month",
    "Loc": "Pune",
    "Link": "https://www.seagate.com/careers",
    "Batch": "2024 to 2026",
    "Logo": "https://img.logo.dev/seagate.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "HSBC": {
    "Role": "Summer Intern",
    "Stipend": "₹25K - ₹33K/month",
    "Loc": "Mumbai",
    "Link": "https://www.hsbc.com/careers",
    "Batch": "2024 to 2025",
    "Logo": "https://img.logo.dev/hsbc.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "BT Group": {
    "Role": "Associate Engineer",
    "Stipend": "₹4L - ₹6L LPA",
    "Loc": "Bengaluru",
    "Link": "https://www.bt.com/careers",
    "Batch": "2023 to 2025",
    "Logo": "https://img.logo.dev/bt.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Philips": {
    "Role": "Apprentice",
    "Stipend": "₹2L - ₹3L LPA",
    "Loc": "Pune",
    "Link": "https://www.philips.com/a-w/careers.html",
    "Batch": "2025",
    "Logo": "https://img.logo.dev/philips.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Myntra": {
    "Role": "Software Development Engineer Intern",
    "Stipend": "₹70,000/month",
    "Loc": "Bangalore",
    "Link": "https://www.myntra.com/careers",
    "Batch": "2026",
    "Logo": "https://img.logo.dev/myntra.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Microsoft": {
    "Role": "Software Engineering Intern",
    "Stipend": "₹67K - ₹1L/month",
    "Loc": "Multiple across India",
    "Link": "https://careers.microsoft.com/",
    "Batch": "2026 to 2027",
    "Logo": "https://img.logo.dev/microsoft.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Infrrd": {
    "Role": "Trainee Software Development Engineer",
    "Stipend": "₹6L - ₹9L LPA",
    "Loc": "Bangalore",
    "Link": "https://www.infrrd.ai/careers",
    "Batch": "2026",
    "Logo": "https://img.logo.dev/infrrd.ai?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "rtCamp": {
    "Role": "Associate React Engineer",
    "Stipend": "Probation ₹25K/month, 2 Lakh/m FTE",
    "Loc": "Remote",
    "Link": "https://rtcamp.com/careers/",
    "Batch": "2025 to 2026",
    "Logo": "https://img.logo.dev/rtcamp.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Infineon Technologies": {
    "Role": "Engineer Applications",
    "Stipend": "₹6L - ₹10L LPA",
    "Loc": "Bangalore",
    "Link": "https://www.infineon.com/cms/en/careers/",
    "Batch": "2023 to 2025",
    "Logo": "https://img.logo.dev/infineon.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Harmonic": {
    "Role": "Associate QA Engineer",
    "Stipend": "₹4L - ₹6L LPA",
    "Loc": "Bangalore",
    "Link": "https://careers.harmonicinc.com/",
    "Batch": "2024 to 2025",
    "Logo": "https://img.logo.dev/harmonicinc.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Baker Hughes": {
    "Role": "Summer Intern",
    "Stipend": "₹25K - ₹33K/month",
    "Loc": "Mumbai & Bangalore",
    "Link": "https://careers.bakerhughes.com/",
    "Batch": "2026 to 2028",
    "Logo": "https://img.logo.dev/bakerhughes.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Uber": {
    "Role": "Data Science Intern",
    "Stipend": "₹50K - ₹1L/month",
    "Loc": "Bangalore",
    "Link": "https://www.uber.com/global/en/careers/",
    "Batch": "2026",
    "Logo": "https://img.logo.dev/uber.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Autodesk": {
    "Role": "Software Dev Engineer",
    "Stipend": "₹8–12 LPA",
    "Loc": "Bengaluru, India",
    "Link": "https://www.autodesk.com/careers/overview",
    "Date_of_publish": "29 September 2025",
    "Batch": "2023, 2024, 2025",
    "Logo": "https://img.logo.dev/autodesk.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Verto": {
    "Role": "Associate Software Engineer",
    "Stipend": "₹5–10 LPA",
    "Loc": "Pune, India",
    "Link": "https://www.vertofx.com/About-Us/Company/Careers/",
    "Date_of_publish": "29 September 2025",
    "Batch": "2024, 2025",
    "Logo": "https://img.logo.dev/vertofx.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Fortrea_Web": {
    "Role": "Website Designer",
    "Stipend": "₹3–5 LPA",
    "Loc": "Bangalore, India",
    "Link": "https://careers.fortrea.com/",
    "Date_of_publish": "29 September 2025",
    "Batch": "2023, 2024, 2025",
    "Logo": "https://img.logo.dev/fortrea.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Fortrea_SEO": {
    "Role": "SEO Apprentice",
    "Stipend": "₹3–4 LPA",
    "Loc": "Bangalore, India",
    "Link": "https://careers.fortrea.com/",
    "Date_of_publish": "30 September 2025",
    "Batch": "2023, 2024, 2025",
    "Logo": "https://img.logo.dev/fortrea.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Newfold Digital": {
    "Role": "AI Engineer Intern",
    "Stipend": "₹25,000–42,000/month",
    "Loc": "Mumbai, India",
    "Link": "https://www.newfold.com/careers",
    "Date_of_publish": "30 September 2025",
    "Batch": "2023, 2024, 2025",
    "Logo": "https://img.logo.dev/newfold.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Teradata": {
    "Role": "Software Engineer",
    "Stipend": "₹6–10 LPA",
    "Loc": "Hyderabad, India",
    "Link": "https://careers.teradata.com/jobs/219278/software-engineer",
    "Date_of_publish": "30 September 2025",
    "Batch": "2022, 2023, 2024, 2025",
    "Logo": "https://img.logo.dev/teradata.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "v4C.ai": {
    "Role": "Software Engineer",
    "Stipend": "₹5.2 LPA",
    "Loc": "Remote, India",
    "Link": "https://www.v4c.ai/careers",
    "Date_of_publish": "30 September 2025",
    "Batch": "2024, 2025",
    "Logo": "https://img.logo.dev/v4c.ai?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "ShareChat": {
    "Role": "SDE Intern",
    "Stipend": "₹50,000/month",
    "Loc": "Bangalore, India",
    "Link": "https://sharechat.com/careers",
    "Date_of_publish": "30 September 2025",
    "Batch": "2025, 2026",
    "Logo": "https://img.logo.dev/sharechat.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  }
}

    return jsonify(data)


@app.route("/soon")
def soon():
    return render_template("soon.html")


################# News Stack ###############################

API_BLOG = "pub_727ab1d20b1946d9b9e44b6b298ab23a"
CACHE = {
    "latest-news": None,
    "tech": None,
    "health": None,
    "business": None,
    "sports":None,
    "science":None,
    "stock":None,
    "updated_at": None
}

def fetch_and_cache():
    global CACHE
    try:
        news_url = f"https://newsdata.io/api/1/latest?apikey={API_BLOG}&q=IT%20sector%20Jobs%20opening"
        tech_url = f"https://newsdata.io/api/1/latest?apikey={API_BLOG}&country=in&language=en&category=technology&timezone=Asia/Kolkata"
        health_url = f"https://newsdata.io/api/1/latest?apikey={API_BLOG}&country=in&language=en&category=health&timezone=Asia/Kolkata"
        business_url = f"https://newsdata.io/api/1/latest?apikey={API_BLOG}&country=in&language=en&category=business&timezone=Asia/Kolkata"
        sports_url = f"https://newsdata.io/api/1/latest?apikey={API_BLOG}&q=cricket&country=in&language=en&category=sports&timezone=Asia/Kolkata"
        science_url = f"https://newsdata.io/api/1/latest?apikey={API_BLOG}&category=science&country=in&language=en&timezone=Asia/Kolkata"
        stock_url = f"https://newsdata.io/api/1/latest?apikey={API_BLOG}&q=BSE&country=in&language=en&timezone=Asia/Kolkata"

        CACHE["latest-news"] = requests.get(news_url).json()
        CACHE["tech"] = requests.get(tech_url).json()
        CACHE["health"] = requests.get(health_url).json()
        CACHE["business"] = requests.get(business_url).json()
        CACHE["sports"] = requests.get(sports_url).json()
        CACHE["science"] = requests.get(science_url).json()
        CACHE["stock"] = requests.get(stock_url).json()
        CACHE["updated_at"] = datetime.now(timezone.utc)
    except Exception as e:
        print(f"Cache Error: {e}")

fetch_and_cache()  # Initial cache fill

scheduler = BackgroundScheduler()
trigger = CronTrigger(minute=0, timezone='Asia/Kolkata')  # Top of every UTC hour
scheduler.add_job(fetch_and_cache, trigger)
scheduler.start()


@app.route("/latest-news")
def latest_news():
    print(CACHE["updated_at"])
    return jsonify(CACHE["latest-news"])

@app.route("/tech")
def tech_news():
    print(CACHE["updated_at"])
    return jsonify(CACHE["tech"])

@app.route("/health")
def health():
    print(CACHE["updated_at"])
    return jsonify(CACHE["health"])

@app.route("/sports")
def sports():
    print(CACHE["updated_at"])
    return jsonify(CACHE["sports"])

@app.route("/science")
def science():
    print(CACHE["updated_at"])
    return jsonify(CACHE["science"])

@app.route("/stock")
def stock():
    print(CACHE["updated_at"])
    return jsonify(CACHE["stock"])

@app.route("/business")
def business():
    print(CACHE["updated_at"])
    return jsonify(CACHE["business"])

############################################################


if __name__ == '__main__':
    app.run(debug=False)
