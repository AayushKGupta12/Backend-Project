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
  "Foundation AI": {
    "Role": "Associate Technical Support Engineer",
    "Stipend": "₹3L - ₹5L LPA",
    "Loc": "Hyderabad, Telangana, India",
    "Link": "https://www.foundation.ai/careers",
    "Batch": "2023 to 2025",
    "Logo": "https://img.logo.dev/foundation.ai?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Stripe": {
    "Role": "Software Engineering New Grad",
    "Stipend": "₹10L - ₹15L LPA",
    "Loc": "Bengaluru",
    "Link": "https://stripe.com/careers",
    "Batch": "2026",
    "Logo": "https://img.logo.dev/stripe.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Odoo": {
    "Role": "Software Developer Intern",
    "Stipend": "₹20K/month",
    "Loc": "Gandhinagar",
    "Link": "https://www.odoo.com/page/careers",
    "Batch": "2025 to 2026",
    "Logo": "https://img.logo.dev/odoo.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
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
  "Stripe": {
    "Role": "Software Engineering New Grad",
    "Stipend": "₹12L - ₹15L LPA",
    "Loc": "Bengaluru",
    "Link": "https://stripe.com/careers",
    "Batch": "2026",
    "Logo": "https://img.logo.dev/stripe.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
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
  "Mindtickle": {
    "Role": "Software Engineer Internship",
    "Stipend": "₹70,000/month",
    "Loc": "Pune, India",
    "Link": "https://www.linkedin.com/jobs/view/4305566133",
    "Batch": "2026/27 passout",
    "Logo": "https://img.logo.dev/mindtickle.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Sense": {
    "Role": "Software Engineering Internship",
    "Stipend": "₹50,000/month",
    "Loc": "India",
    "Link": "https://sensehr.sensehq.com/careers/jobs/175",
    "Batch": "2026/27 passouts",
    "Logo": "https://img.logo.dev/sensehq.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Rippling": {
    "Role": "SDE (Frontend)",
    "Stipend": "₹66.5 LPA",
    "Loc": "",
    "Link": "https://ats.rippling.com/en-GB/rippling/jobs/fce552a3-bcae-4f35-b5ff-0143031a5640",
    "Batch": "2022/23/24 passouts",
    "Logo": "https://img.logo.dev/rippling.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Acko": {
    "Role": "Analytics Internship",
    "Stipend": "Not specified",
    "Loc": "Bangalore",
    "Link": "https://docs.google.com/forms/u/0/d/e/1FAIpQLSdZiQ8KrHnsdvzJujqsXvPwoHapvpReh4wtXSImBcN1UYfGCg/viewform?usp=send_form&pli=1",
    "Batch": "2025/26 passouts",
    "Logo": "https://img.logo.dev/acko.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Qualcomm": {
    "Role": "Associate Engineer",
    "Stipend": "Not specified",
    "Loc": "Bangalore, Chennai",
    "Link": "https://careers.qualcomm.com/careers/job/446706882405",
    "Batch": "2026 passouts",
    "Logo": "https://img.logo.dev/qualcomm.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Meta": {
    "Role": "Multiple Software and Product Roles",
    "Stipend": "$110K-$200K",
    "Loc": "Bangalore",
    "Link": "https://www.metacareers.com/jobs?offices%5B0%5D=Bangalore%2C%20India&page=2",
    "Batch": "2022/23/24 passouts and before",
    "Logo": "https://img.logo.dev/meta.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Waymo": {
    "Role": "Multiple ML/AI Roles",
    "Stipend": "$190K-$340K US market",
    "Loc": "Bangalore",
    "Link": "https://careers.withwaymo.com/jobs/search?address%5B%5D=12.974%2C77.701",
    "Batch": "2021/22/23/24 passouts and before",
    "Logo": "https://img.logo.dev/waymo.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Youtube": {
    "Role": "Software Engineer",
    "Stipend": "Not specified",
    "Loc": "India",
    "Link": "https://www.google.com/about/careers/applications/jobs/results/109851367958291142-software-engineer/",
    "Batch": "2022/23/24 passouts",
    "Logo": "https://img.logo.dev/youtube.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "JFrog": {
    "Role": "Internship (Software)",
    "Stipend": "Not specified",
    "Loc": "India",
    "Link": "https://join.jfrog.com/job/7247322-intern/?gh_src=526d35e41us",
    "Batch": "2025/26 passouts",
    "Logo": "https://img.logo.dev/jfrog.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "JP Morgan Chase": {
    "Role": "SDE-1",
    "Stipend": "Not specified",
    "Loc": "Banglore",
    "Link": "https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210667642",
    "Batch": "2023/24 passouts",
    "Logo": "https://img.logo.dev/jpmorganchase.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Google Associate Product Manager": {
    "Role": "Associate Product Manager",
    "Stipend": "Not specified",
    "Loc": "India",
    "Link": "https://www.google.com/about/careers/applications/jobs/results/75038123993506502-associate-product-manager/",
    "Batch": "2025/26 passouts",
    "Logo": "https://img.logo.dev/google.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Google Software Engineer Uni Grad": {
    "Role": "Software Engineer - Uni Grad",
    "Stipend": "Not specified",
    "Loc": "India",
    "Link": "https://www.google.com/about/careers/applications/jobs/results/125611950166942406-software-engineer/",
    "Batch": "2026 passouts",
    "Logo": "https://img.logo.dev/google.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Google Application Engineering Internship": {
    "Role": "Application Engineering Internship - 6 Months",
    "Stipend": "Not specified",
    "Loc": "India",
    "Link": "https://www.google.com/about/careers/applications/jobs/results/88011077542912710-application-engineering-intern-winter-2026",
    "Batch": "2026 passouts",
    "Logo": "https://img.logo.dev/google.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Uber Freight": {
    "Role": "SDE",
    "Stipend": "Not specified",
    "Loc": "",
    "Link": "https://www.uberfreight.com/careers/?gh_jid=4750841008#opportunities",
    "Batch": "2022/23/24 passouts",
    "Logo": "https://img.logo.dev/uberfreight.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Rubrik": {
    "Role": "Software Engineer - Winter Intern",
    "Stipend": "₹1.5 Lakh",
    "Loc": "Gurugram",
    "Link": "https://www.rubrik.com/company/careers/departments/job.7208329.1929",
    "Batch": "2026 passouts",
    "Logo": "https://img.logo.dev/rubrik.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Walmart Global Tech": {
    "Role": "Internship",
    "Stipend": "₹1 Lakh/m intern stipend; 26 LPA FTE",
    "Loc": "",
    "Link": "https://yt.openinapp.co/lhdte",
    "Batch": "Not specified",
    "Logo": "https://img.logo.dev/walmart.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Mindtickle": {
    "Role": "Software Engineer Internship",
    "Stipend": "₹70,000/month",
    "Loc": "Pune, India",
    "Link": "https://www.linkedin.com/jobs/view/4305566133",
    "Batch": "2026/27 passout",
    "Logo": "https://img.logo.dev/mindtickle.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Sense": {
    "Role": "Software Engineering Internship",
    "Stipend": "₹50,000/month",
    "Loc": "India",
    "Link": "https://sensehr.sensehq.com/careers/jobs/175",
    "Batch": "2026/27 passouts",
    "Logo": "https://img.logo.dev/sensehq.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Acko": {
    "Role": "Analytics Internship",
    "Stipend": "₹30,000/month",
    "Loc": "Bangalore, India",
    "Link": "https://docs.google.com/forms/u/0/d/e/1FAIpQLSdZiQ8KrHnsdvzJujqsXvPwoHapvpReh4wtXSImBcN1UYfGCg/viewform?usp=send_form&pli=1",
    "Batch": "2025/26 passouts",
    "Logo": "https://img.logo.dev/acko.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Qualcomm": {
    "Role": "Associate Engineer",
    "Stipend": "₹60,000/month",
    "Loc": "Bangalore, India",
    "Link": "https://careers.qualcomm.com/careers/job/446706882405",
    "Batch": "2026 passouts",
    "Logo": "https://img.logo.dev/qualcomm.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Meta": {
    "Role": "Multiple Software Engineering and Product Roles",
    "Stipend": "₹1,00,000 - ₹1,25,000/month",
    "Loc": "Bangalore, India",
    "Link": "https://www.metacareers.com/jobs?offices%5B0%5D=Bangalore%2C%20India&page=2",
    "Batch": "2022/23/24 passouts and before",
    "Logo": "https://img.logo.dev/meta.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Waymo": {
    "Role": "Multiple ML/AI roles",
    "Stipend": "₹1,20,000 - ₹1,50,000/month",
    "Loc": "Bangalore, India",
    "Link": "https://careers.withwaymo.com/jobs/search?address%5B%5D=12.974%2C77.701",
    "Batch": "2021/22/23/24 passouts and before",
    "Logo": "https://img.logo.dev/waymo.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Youtube": {
    "Role": "Software Engineer",
    "Stipend": "₹90,000 - ₹1,10,000/month",
    "Loc": "India",
    "Link": "https://www.google.com/about/careers/applications/jobs/results/109851367958291142-software-engineer/",
    "Batch": "2022/23/24 passouts",
    "Logo": "https://img.logo.dev/youtube.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "JFrog": {
    "Role": "Software Internship",
    "Stipend": "₹40,000/month",
    "Loc": "Bangalore, India",
    "Link": "https://join.jfrog.com/job/7247322-intern/?gh_src=526d35e41us",
    "Batch": "2025/26 passouts",
    "Logo": "https://img.logo.dev/jfrog.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "JP Morgan Chase": {
    "Role": "SDE-1",
    "Stipend": "₹80,000/month",
    "Loc": "Multiple locations, India",
    "Link": "https://jpmc.fa.oraclecloud.com/hcmUI/CandidateExperience/en/sites/CX_1001/job/210667642",
    "Batch": "2023/24 passouts",
    "Logo": "https://img.logo.dev/jpmorganchase.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Microsoft SDE 1": {
    "Role": "SDE 1",
    "Stipend": "₹1,00,000/month",
    "Loc": "Remote",
    "Link": "https://jobs.careers.microsoft.com/global/en/job/1863345/Software-Engineer",
    "Batch": "2023/24 passouts",
    "Logo": "https://img.logo.dev/microsoft.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Walmart Global Tech": {
    "Role": "Internship",
    "Stipend": "₹1 Lakh/m intern stipend; Package 26 LPA FTE",
    "Loc": "India",
    "Link": "https://yt.openinapp.co/lhdte",
    "Batch": "Not specified",
    "Logo": "https://img.logo.dev/walmart.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Uber Freight": {
    "Role": "SDE",
    "Stipend": "₹80,000/month",
    "Loc": "India",
    "Link": "https://www.uberfreight.com/careers/?gh_jid=4750841008#opportunities",
    "Batch": "2022/23/24 passouts",
    "Logo": "https://img.logo.dev/uberfreight.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
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