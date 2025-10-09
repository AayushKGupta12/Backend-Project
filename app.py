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
    "https://edstack.netlify.app",
    "https://stackbit.vercel.app"
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
  "Tata Consultancy Services": {
    "Role": "Software Engineer / Ninja / Digital",
    "Stipend": "₹3L - ₹7L LPA",
    "Loc": "India",
    "Link": "https://www.tcs.com/careers",
    "Batch": "2025/26 passouts",
    "Logo": "https://img.logo.dev/tcs.com"
  },
  "Infosys": {
    "Role": "Systems Engineer / Power Programmer",
    "Stipend": "₹3.6L - ₹8L LPA",
    "Loc": "India",
    "Link": "https://www.infosys.com/careers",
    "Batch": "2025/26 passouts",
    "Logo": "https://img.logo.dev/infosys.com"
  },
  "Wipro": {
    "Role": "Project Engineer",
    "Stipend": "₹3.5L - ₹6.5L LPA",
    "Loc": "India",
    "Link": "https://careers.wipro.com",
    "Batch": "2025/26 passouts",
    "Logo": "https://img.logo.dev/wipro.com"
  },
  "HCLTech": {
    "Role": "Graduate Engineer Trainee",
    "Stipend": "₹3.5L - ₹7L LPA",
    "Loc": "India",
    "Link": "https://www.hcltech.com/careers/campus-hiring",
    "Batch": "2025/26 passouts",
    "Logo": "https://img.logo.dev/hcltech.com"
  },
  "Tech Mahindra": {
    "Role": "Associate Software Engineer",
    "Stipend": "₹3L - ₹6L LPA",
    "Loc": "India",
    "Link": "https://campusconnect.techmahindra.com/home",
    "Batch": "2025/26 passouts",
    "Logo": "https://img.logo.dev/techmahindra.com"
  },
  "LTIMindtree": {
    "Role": "Software Engineer, Graduate Trainee",
    "Stipend": "₹3.4L - ₹7.2L LPA",
    "Loc": "India",
    "Link": "https://www.ltimindtree.com/careers/",
    "Batch": "2025/26 passouts",
    "Logo": "https://img.logo.dev/ltimindtree.com"
  },
  "Larsen & Toubro": {
    "Role": "Graduate Engineer Trainee",
    "Stipend": "₹4L - ₹8L LPA",
    "Loc": "India",
    "Link": "https://www.larsentoubro.com/corporate/careers/campus-recruitment/",
    "Batch": "2025/26 passouts",
    "Logo": "https://img.logo.dev/larsentoubro.com"
  },
  "Stripe": {
    "Role": "Software Engineering New Grad",
    "Stipend": "₹10L - ₹15L LPA",
    "Loc": "Bengaluru",
    "Link": "https://stripe.com/careers",
    "Batch": "2026",
    "Logo": "https://img.logo.dev/stripe.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "EY": {
    "Role": "Data Scientist / Machine Learning Engineer",
    "Stipend": "₹15L - ₹16L LPA",
    "Loc": "Kolkata",
    "Link": "https://www.ey.com/en_in/careers",
    "Batch": "2026 to 2027",
    "Logo": "https://img.logo.dev/ey.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  }
}

    return jsonify(data)




@app.route('/company-news1')
def company_news1():

    data = {
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
    "Link": "https://seagatecareers.com",
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
  }
}

    return jsonify(data)

@app.route('/company-news2')
def company_news2():

    data = {
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
  "Kadel Labs": {
    "Role": "MERN Stack Developer Intern",
    "Stipend": "₹25K - ₹40K/month",
    "Loc": "Udaipur",
    "Link": "https://kadel.in/careers",
    "Batch": "2024 to 2025",
    "Logo": "https://img.logo.dev/kadel.in"
  },
  "Rippling": {
    "Role": "SDE (Frontend)",
    "Stipend": "₹66.5 LPA",
    "Loc": "",
    "Link": "https://ats.rippling.com/en-GB/rippling/jobs/fce552a3-bcae-4f35-b5ff-0143031a5640",
    "Batch": "2022/23/24 passouts",
    "Logo": "https://img.logo.dev/rippling.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
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
  }
}



    return jsonify(data)


@app.route('/company-news3')
def company_news3():

    data = {
  "Youtube": {
    "Role": "Software Engineer",
    "Stipend": "₹90,000 - ₹1,10,000/month",
    "Loc": "India",
    "Link": "https://www.google.com/about/careers/applications/jobs/results/109851367958291142-software-engineer/",
    "Batch": "2022/23/24 passouts",
    "Logo": "https://img.logo.dev/youtube.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "JP Morgan Chase": {
    "Role": "SDE-1",
    "Stipend": "₹80,000/month",
    "Loc": "Multiple locations, India",
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
    "Loc": "India",
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
    "Loc": "India",
    "Link": "https://yt.openinapp.co/lhdte",
    "Batch": "Not specified",
    "Logo": "https://img.logo.dev/walmart.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Microsoft SDE 1": {
    "Role": "SDE 1",
    "Stipend": "₹1,00,000/month",
    "Loc": "Remote",
    "Link": "https://jobs.careers.microsoft.com/global/en/job/1863345/Software-Engineer",
    "Batch": "2023/24 passouts",
    "Logo": "https://img.logo.dev/microsoft.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  }
}

    return jsonify(data)


@app.route('/company-news4')
def company_news4():

    data = {
  "Capgemini": {
    "Role": "Software Engineer/Consultant",
    "Stipend": "₹3.8L - ₹6.5L LPA",
    "Loc": "India",
    "Link": "https://www.capgemini.com/in-en/careers/",
    "Batch": "2025/26 passouts",
    "Logo": "https://img.logo.dev/capgemini.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Accenture": {
    "Role": "Software Engineering Associate",
    "Stipend": "₹4L - ₹6.5L LPA",
    "Loc": "India",
    "Link": "https://www.accenture.com/in-en/careers",
    "Batch": "2025/26 passouts",
    "Logo": "https://img.logo.dev/accenture.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Hewlett Packard Enterprise": {
    "Role": "DevOps/Cloud Engineer",
    "Stipend": "₹5.5L - ₹8L LPA",
    "Loc": "India (Multiple cities)",
    "Link": "https://careers.hpe.com",
    "Batch": "2025/26 passouts",
    "Logo": "https://img.logo.dev/hpe.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Google": {
    "Role": "Software Engineer/AI Engineer",
    "Stipend": "₹20L - ₹40L LPA",
    "Loc": "Bangalore/Hyderabad",
    "Link": "https://careers.google.com",
    "Batch": "2025/26 passouts",
    "Logo": "https://img.logo.dev/google.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Amazon": {
    "Role": "Software Development Engineer",
    "Stipend": "₹28L - ₹30L LPA",
    "Loc": "Pan India",
    "Link": "https://www.amazon.jobs/en/",
    "Batch": "2025/26 passouts",
    "Logo": "https://img.logo.dev/amazon.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Oracle": {
    "Role": "Software Engineer",
    "Stipend": "₹7L - ₹14L LPA",
    "Loc": "Bangalore/Gurgaon/Hyderabad",
    "Link": "https://www.oracle.com/in/careers/",
    "Batch": "2025/26 passouts",
    "Logo": "https://img.logo.dev/oracle.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "LTTS": {
    "Role": "Graduate Engineer Trainee",
    "Stipend": "₹3.5L - ₹5.5L LPA",
    "Loc": "India",
    "Link": "https://www.ltts.com/careers",
    "Batch": "2025/26 passouts",
    "Logo": "https://img.logo.dev/ltts.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Hexaware": {
    "Role": "Trainee/Graduate Engineer",
    "Stipend": "₹3.5L - ₹5L LPA",
    "Loc": "India",
    "Link": "https://www.hexaware.com/careers/",
    "Batch": "2025/26 passouts",
    "Logo": "https://img.logo.dev/hexaware.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
  },
  "Birlasoft": {
    "Role": "Trainee",
    "Stipend": "₹3.5L - ₹5L LPA",
    "Loc": "India",
    "Link": "https://www.birlasoft.com/careers",
    "Batch": "2025/26 passouts",
    "Logo": "https://img.logo.dev/birlasoft.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
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
