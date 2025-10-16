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
    "http://localhost:5173",
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




LOGO_CACHE = {}
LOGO_API_TOKEN = "pk_djKZ3gIOQqyja8btgxBpBA"

def fetch_logo(domain):
    """Fetch a single logo and return base64 encoded data or URL"""
    try:
        url = f"https://img.logo.dev/{domain}?token={LOGO_API_TOKEN}"
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            # Convert to base64 for caching
            img_base64 = base64.b64encode(response.content).decode('utf-8')
            return f"data:image/png;base64,{img_base64}"
        return url  # Fallback to URL if fetch fails
    except Exception as e:
        print(f"Error fetching logo for {domain}: {e}")
        return f"https://img.logo.dev/{domain}?token={LOGO_API_TOKEN}"

def initialize_logo_cache():
    """Fetch all logos at startup and cache them"""
    global LOGO_CACHE
    
    # Extract all unique domains from company data
    domains = [
        "tcs.com", "infosys.com", "wipro.com", "hcltech.com", "techmahindra.com",
        "ltimindtree.com", "larsentoubro.com", "stripe.com",
        "kaleris.com", "seagate.com", "hsbc.com", "bt.com", "myntra.com",
        "microsoft.com", "infrrd.ai", "rtcamp.com", "infineon.com",
        "harmonicinc.com", "bakerhughes.com", "uber.com", "mindtickle.com",
        "kadel.in", "rippling.com", "qualcomm.com", "meta.com", "waymo.com",
        "youtube.com", "jpmorganchase.com", "google.com", "uberfreight.com",
        "rubrik.com", "walmart.com", "capgemini.com", "accenture.com",
        "hpe.com", "amazon.com", "oracle.com", "ltts.com", "hexaware.com",
        "birlasoft.com","ey.com"
    ]
    
    print("Starting logo cache initialization...")
    for domain in domains:
        LOGO_CACHE[domain] = fetch_logo(domain)
        print(f"Cached logo for {domain}")
    
    print(f"Logo cache initialized with {len(LOGO_CACHE)} logos")

def get_cached_logo(domain):
    """Get logo from cache, fetch if not available"""
    if domain not in LOGO_CACHE:
        LOGO_CACHE[domain] = fetch_logo(domain)
    return LOGO_CACHE[domain]


@app.route('/hero')
def hero():
    data = {
        "Tata Consultancy Services": {
            "Logo": get_cached_logo("tcs.com")
        },
        "Infosys": {
            "Logo": get_cached_logo("infosys.com")
        },
        "EY": {
            "Logo": get_cached_logo("ey.com")
        },
        "HSBC": {
            "Logo": get_cached_logo("hsbc.com")
        },
        "Microsoft": {
            "Logo": get_cached_logo("microsoft.com")
        },
        "Uber": {
            "Logo": get_cached_logo("uber.com")
        },
        "Qualcomm": {
            "Logo": get_cached_logo("qualcomm.com")
        },
        "Meta": {
            "Logo": get_cached_logo("meta.com")
        },
        "JP Morgan Chase": {
            "Logo": get_cached_logo("jpmorganchase.com")
        },
        "Google": {
            "Logo": get_cached_logo("google.com")
        },
        "Rubrik": {
            "Logo": get_cached_logo("rubrik.com")
        },
        "Walmart Global Tech": {
            "Logo": get_cached_logo("walmart.com")
        },
        "Amazon": {
            "Logo": get_cached_logo("amazon.com")
        },
        "Oracle": {
            "Logo": get_cached_logo("oracle.com")
        },
        "Hewlett Packard Enterprise": {
            "Logo": get_cached_logo("hpe.com")
        },
        "Myntra": {
            "Logo": get_cached_logo("myntra.com")
        }
    }
    return jsonify(data)



@app.route('/company-news')
def company_news():
    data = {
        "Tata Consultancy Services": {
            "Role": "Software Engineer / Ninja / Digital",
            "Stipend": "₹3L - ₹7L LPA",
            "Loc": "India",
            "Link": "https://www.tcs.com/careers/india/entry-level",
            "Batch": "2025/26 passouts",
            "Logo": get_cached_logo("tcs.com")
        },
        "Infosys": {
            "Role": "Wintern Internship",
            "Stipend": "Merit Based",
            "Loc": "India",
            "Link": "https://www.infosys.com/careers/internships.html",
            "Batch": "2025/26 passouts",
            "Logo": get_cached_logo("infosys.com")
        },
        "Wipro": {
            "Role": "Project Engineer",
            "Stipend": "₹3.5L - ₹6.5L LPA",
            "Loc": "India",
            "Link": "https://careers.wipro.com/search/?q=&locationsearch=India&searchResultView=LIST&markerViewed=&carouselIndex=&facetFilters=%7B%22custRMKMappingPicklist%22%3A%5B%22Engineering%22%2C%22Data+Analytics%22%5D%7D&pageNumber=0",
            "Batch": "2025/26 passouts",
            "Logo": get_cached_logo("wipro.com")
        },
        "Tech Mahindra": {
            "Role": "Associate Software Engineer",
            "Stipend": "₹3L - ₹6L LPA",
            "Loc": "India",
            "Link": "https://campusconnect.techmahindra.com/home",
            "Batch": "2025/26 passouts",
            "Logo": get_cached_logo("techmahindra.com")
        },
        "LTIMindtree": {
            "Role": "Ad Trafficker Ad Ops",
            "Stipend": "₹3.4L - ₹7.2L LPA",
            "Loc": "Mumbai",
            "Link": "https://ltimindtree.ripplehire.com/candidate/?token=xviyQvbnyYZdGtozXoNm&lang=en&source=CAREERSITE#detail/job/794405",
            "Batch": "2025/26 passouts",
            "Logo": get_cached_logo("ltimindtree.com")
        },
        "Larsen & Toubro": {
            "Role": "Graduate Engineer Trainee",
            "Stipend": "₹4L - ₹8L LPA",
            "Loc": "India",
            "Link": "https://www.larsentoubro.com/corporate/careers/campus-recruitment/",
            "Batch": "2025/26 passouts",
            "Logo": get_cached_logo("larsentoubro.com")
        },
        "Stripe": {
            "Role": "50+ Opening Multiple Roles",
            "Stipend": "₹10L - ₹65L LPA",
            "Loc": "Bengaluru",
            "Link": "https://stripe.com/jobs/search?office_locations=Asia+Pacific--Bengaluru",
            "Batch": "2026",
            "Logo": get_cached_logo("stripe.com")
        },
        "EY": {
            "Role": "Data Scientist / Machine Learning Engineer",
            "Stipend": "₹15L - ₹16L LPA",
            "Loc": "Kolkata",
            "Link": "https://eyglobal.yello.co/job_boards/c1riT--B2O-KySgYWsZO1Q?locale=en",
            "Batch": "2026 to 2027",
            "Logo": get_cached_logo("ey.com")
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
            "Link": "https://kaleris.wd501.myworkdayjobs.com/kaleris_careers?locations=39a74440c4f910011fdea6685c650000",
            "Batch": "2024 to 2025",
            "Logo": get_cached_logo("kaleris.com")
        },
        "Seagate": {
            "Role": "Automation Intern",
            "Stipend": "₹37K - ₹53K/month",
            "Loc": "Pune",
            "Link": "https://seagatecareers.com/search/?createNewAlert=false&q=&locationsearch=India&optionsFacetsDD_country=&optionsFacetsDD_dept=&optionsFacetsDD_customfield1=&optionsFacetsDD_lang=",
            "Batch": "2024 to 2026",
            "Logo": get_cached_logo("seagate.com")
        },
        "HSBC": {
            "Role": "Summer Intern",
            "Stipend": "₹25K - ₹33K/month",
            "Loc": "Mumbai",
            "Link": "https://www.hsbc.com/careers",
            "Batch": "2024 to 2025",
            "Logo": get_cached_logo("hsbc.com")
        },
        "BT Group": {
            "Role": "Associate Engineer",
            "Stipend": "₹4L - ₹64L LPA",
            "Loc": "Bengaluru",
            "Link": "https://jobs.bt.com/search/?createNewAlert=false&q=&locationsearch=india&optionsFacetsDD_brand=&optionsFacetsDD_customfield3=",
            "Batch": "2023 to 2025",
            "Logo": get_cached_logo("bt.com")
        },
        "Microsoft": {
            "Role": "Software Engineering Intern",
            "Stipend": "₹67K - ₹1L/month",
            "Loc": "Multiple across India",
            "Link": "https://jobs.careers.microsoft.com/global/en/search?lc=India&et=Full-Time&l=en_us&pg=1&pgSz=20&o=Relevance&flt=true",
            "Batch": "2026 to 2027",
            "Logo": get_cached_logo("microsoft.com")
        },
        "Infrrd": {
            "Role": "Trainee Software Development Engineer",
            "Stipend": "₹6L - ₹9L LPA",
            "Loc": "Bangalore",
            "Link": "https://www.infrrd.ai/open-positions",
            "Batch": "2026",
            "Logo": get_cached_logo("infrrd.ai")
        },
        "rtCamp": {
            "Role": "Associate React Engineer",
            "Stipend": "Probation ₹25K/month, 2 Lakh/m FTE",
            "Loc": "Remote",
            "Link": "https://careers.rtcamp.com/",
            "Batch": "2025 to 2026",
            "Logo": get_cached_logo("rtcamp.com")
        },
        "Infineon Technologies": {
            "Role": "Engineer Applications",
            "Stipend": "₹6L - ₹10L LPA",
            "Loc": "Bangalore",
            "Link": "https://jobs.infineon.com/careers?start=0&location=india&pid=563808966965058&sort_by=distance&filter_include_remote=0",
            "Batch": "2023 to 2025",
            "Logo": get_cached_logo("infineon.com")
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
            "Link": "https://careers.harmonicinc.com/apply-now/",
            "Batch": "2024 to 2025",
            "Logo": get_cached_logo("harmonicinc.com")
        },
        "Baker Hughes": {
            "Role": "Summer Intern",
            "Stipend": "₹25K - ₹33K/month",
            "Loc": "Mumbai & Bangalore",
            "Link": "https://careers.bakerhughes.com/global/en/job/R153161/Summer-Internships-2026-India",
            "Batch": "2026 to 2028",
            "Logo": get_cached_logo("bakerhughes.com")
        },
        "Rippling": {
            "Role": "SDE (Frontend)",
            "Stipend": "₹66.5 LPA",
            "Loc": "",
            "Link": "https://ats.rippling.com/en-GB/rippling/jobs/fce552a3-bcae-4f35-b5ff-0143031a5640",
            "Batch": "2022/23/24 passouts",
            "Logo": get_cached_logo("rippling.com")
        },
        "Qualcomm": {
            "Role": "Associate Engineer",
            "Stipend": "₹60,000/month",
            "Loc": "Bangalore, India",
            "Link": "https://careers.qualcomm.com/careers/job/446706882405",
            "Batch": "2026 passouts",
            "Logo": get_cached_logo("qualcomm.com")
        },
        "Meta": {
            "Role": "Multiple Software Engineering and Product Roles",
            "Stipend": "₹1,00,000 - ₹1,25,000/month",
            "Loc": "Bangalore, India",
            "Link": "https://www.metacareers.com/jobs?offices[0]=Bangalore%2C%20India&sort_by_new=true",
            "Batch": "2022/23/24 passouts and before",
            "Logo": get_cached_logo("meta.com")
        },
        "Waymo": {
            "Role": "Multiple ML/AI roles",
            "Stipend": "₹1,20,000 - ₹1,50,000/month",
            "Loc": "Bangalore, India",
            "Link": "https://careers.withwaymo.com/jobs/search?address%5B%5D=12.974%2C77.701",
            "Batch": "2021/22/23/24 passouts and before",
            "Logo": get_cached_logo("waymo.com")
        }
    }
    return jsonify(data)


@app.route('/company-news3')
def company_news3():
    data = {
      "Microsoft": {
        "Role": "Software Engineer",
        "Stipend": "₹22 LPA average",
        "Loc": "Bangalore, India",
        "Batch": "2025 onwards",
        "Link": "https://jobs.careers.microsoft.com/us/en/job/1849735/Software-Engineer",
        "Logo": "https://img.logo.dev/microsoft.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
      },
      "Dolby": {
        "Role": "Research Intern",
        "Stipend": "₹1.5 L/month",
        "Loc": "Bangalore",
        "Batch": "2027, 2028 PHD grads",
        "Link": "https://jobs.dolby.com/careers/job/30262513?domain=dolby.com&",
        "Logo": "https://img.logo.dev/dolby.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
      },
      "IG Tech": {
        "Role": "Frontend Development Intern",
        "Stipend": "₹30,000",
        "Loc": "Not specified",
        "Batch": "Not specified",
        "Link": "https://docs.google.com/forms/d/16OiiJjygdHHHqbdwwVOHLExFyeJDi9UtvVvIcZd0VRY/viewform?edit_requested=true",
        "Logo": "https://img.logo.dev/igtech.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
      },
      "Thermo Fisher Scientific": {
        "Role": "Engineer I, Software",
        "Stipend": "Not specified",
        "Loc": "India",
        "Batch": "2026 onwards",
        "Link": "https://jobs.thermofisher.com/global/en/job/R-01329697/Engineer-I-Software?rx_ch=jobpost&rx_id=9719795a-a91d-11f0-9efd-b3409657a5f1&rx_job=R-01329697&rx_medium=post&rx_paid=0&rx_r=none",
        "Logo": "https://img.logo.dev/thermofisher.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
      },
      "Nike": {
        "Role": "Software Engineer I",
        "Stipend": "Not specified",
        "Loc": "Bangalore",
        "Batch": "2025 onwards",
        "Link": "https://careers.nike.com/software-engineer-i-itc/job/R-71708",
        "Logo": "https://img.logo.dev/nike.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
      },
      "American Express": {
        "Role": "Software Engineer I",
        "Stipend": "Not specified",
        "Loc": "Chennai",
        "Batch": "2025 grads",
        "Link": "https://aexp.eightfold.ai/careers/job/30486244?hl=en&domain=aexp.com",
        "Logo": "https://img.logo.dev/aexp.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
      },
      "Blueyonder": {
        "Role": "Software Engineer",
        "Stipend": "Not specified",
        "Loc": "India",
        "Batch": "2026 onwards",
        "Link": "https://careers.blueyonder.com/us/en/job/BYPBYXUS253097EXTERNALENUS/Software-engineer",
        "Logo": "https://img.logo.dev/blueyonder.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
      },
      "Docusign": {
        "Role": "Software Engineer",
        "Stipend": "Not specified",
        "Loc": "India",
        "Batch": "2026 onwards",
        "Link": "https://careers.docusign.com/jobs/26738?lang=en-us&iis=Job+board",
        "Logo": "https://img.logo.dev/docusign.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
      },
      "Wells Fargo": {
        "Role": "Software Engineer",
        "Stipend": "Not specified",
        "Loc": "India",
        "Batch": "2026 onwards",
        "Link": "https://www.wellsfargojobs.com/en/jobs/r-495099/software-engineer/?jClickId=295291e2-66d1-44d6-a336-3189b6259586",
        "Logo": "https://img.logo.dev/wellsfargo.com?token=pk_djKZ3gIOQqyja8btgxBpBA"
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
            "Logo": get_cached_logo("capgemini.com")
        },
        "Accenture": {
            "Role": "Software Engineering Associate",
            "Stipend": "₹4L - ₹6.5L LPA",
            "Loc": "India",
            "Link": "https://www.accenture.com/in-en/careers",
            "Batch": "2025/26 passouts",
            "Logo": get_cached_logo("accenture.com")
        },
        "Hewlett Packard Enterprise": {
            "Role": "DevOps/Cloud Engineer",
            "Stipend": "₹5.5L - ₹8L LPA",
            "Loc": "India (Multiple cities)",
            "Link": "https://careers.hpe.com",
            "Batch": "2025/26 passouts",
            "Logo": get_cached_logo("hpe.com")
        },
        "Google": {
            "Role": "Software Engineer/AI Engineer",
            "Stipend": "₹20L - ₹40L LPA",
            "Loc": "Bangalore/Hyderabad",
            "Link": "https://careers.google.com",
            "Batch": "2025/26 passouts",
            "Logo": get_cached_logo("google.com")
        },
        "Amazon": {
            "Role": "Software Development Engineer",
            "Stipend": "₹28L - ₹30L LPA",
            "Loc": "Pan India",
            "Link": "https://www.amazon.jobs/en/",
            "Batch": "2025/26 passouts",
            "Logo": get_cached_logo("amazon.com")
        },
        "Oracle": {
            "Role": "Software Engineer",
            "Stipend": "₹7L - ₹14L LPA",
            "Loc": "Bangalore/Gurgaon/Hyderabad",
            "Link": "https://www.oracle.com/in/careers/",
            "Batch": "2025/26 passouts",
            "Logo": get_cached_logo("oracle.com")
        },
        "LTTS": {
            "Role": "Graduate Engineer Trainee",
            "Stipend": "₹3.5L - ₹5.5L LPA",
            "Loc": "India",
            "Link": "https://www.ltts.com/careers",
            "Batch": "2025/26 passouts",
            "Logo": get_cached_logo("ltts.com")
        },
        "Hexaware": {
            "Role": "Trainee/Graduate Engineer",
            "Stipend": "₹3.5L - ₹5L LPA",
            "Loc": "India",
            "Link": "https://www.hexaware.com/careers/",
            "Batch": "2025/26 passouts",
            "Logo": get_cached_logo("hexaware.com")
        },
        "Birlasoft": {
            "Role": "Trainee",
            "Stipend": "₹3.5L - ₹5L LPA",
            "Loc": "India",
            "Link": "https://www.birlasoft.com/careers",
            "Batch": "2025/26 passouts",
            "Logo": get_cached_logo("birlasoft.com")
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
