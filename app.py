from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
import os
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime, timezone
import base64
import random
import PyPDF2
import io
import re

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": [
    "http://localhost:5175",
    "http://localhost:5174",
    "http://localhost:5173",
    "https://resume-analysis-dash-3g0x.bolt.host",
    "https://edstack.netlify.app"
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

@app.route("/soon")
def soon():
    return render_template("soon.html")



##########################################################
#                 Logos & Companies List                 #
##########################################################

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
        "ltimindtree.com", "larsentoubro.com", "stripe.com", "ey.com",
        "kaleris.com", "seagate.com", "hsbc.com", "bt.com", "myntra.com",
        "microsoft.com", "infrrd.ai", "rtcamp.com", "infineon.com",
        "harmonicinc.com", "bakerhughes.com", "uber.com", "mindtickle.com",
        "kadel.in", "rippling.com", "qualcomm.com", "meta.com", "waymo.com",
        "youtube.com", "jpmorganchase.com", "google.com", "uberfreight.com",
        "rubrik.com", "walmart.com", "capgemini.com", "accenture.com",
        "hpe.com", "amazon.com", "oracle.com", "ltts.com", "hexaware.com",
        "birlasoft.com"
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
        },
        "coinbase":{
            "Role":"Software Engineer Intern",
            "Stipend":"₹1.75L L/M",
            "Loc": "Remote",
            "Batch":"2027 passout",
            "Logo":get_cached_logo("coinbase.com"),
            "Link": "https://www.coinbase.com/en-in/careers/positions/7294082"
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
            "Role": "Software Engineering and Product",
            "Stipend": "₹1.25L/M",
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
#                       Live Users                         #
############################################################

import random
import datetime
from zoneinfo import ZoneInfo  # Use built-in Python module for timezone
from flask import Flask, jsonify
from apscheduler.schedulers.background import BackgroundScheduler

# Initialize timezone IST using zoneinfo
IST = ZoneInfo("Asia/Kolkata")

# Initialize global variables
A = random.randint(200, 400)
B = A + random.choice([-3, -2, -1, 1, 2, 3])

def refresh_A():
    global A, B
    A = random.randint(200, 400)
    B = A + random.choice([-3, -2, -1, 1, 2, 3])
    # print(f"[A REFRESHED] A={A}, B={B}")

def refresh_B():
    global B
    B = A + random.choice([-3, -2, -1, 1, 2, 3])
    # print(f"[B REFRESHED] A={A}, B={B}")

scheduler = BackgroundScheduler(timezone=IST)

scheduler.add_job(refresh_B, 'interval', seconds=3, id='refresh_B_job')

now = datetime.datetime.now(IST)
next_midnight = (now + datetime.timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
scheduler.add_job(refresh_A, 'interval', hours=4, start_date=next_midnight, id='refresh_A_job')

scheduler.start()

@app.route('/liveUser', methods=['GET'])
def live_user():
    return jsonify({'A': A, 'B': B})


#############################################################
#                Resume Data From React                     #
#############################################################

TEXT = ""

@app.route('/upload-resume', methods=["POST","GET"])
def upload_resume():
    global TEXT
    TEXT = ""  # Reset TEXT before processing
    
    if 'resume' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['resume']

    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400

    if not file.filename.endswith('.pdf'):
        return jsonify({'error': 'Invalid file type. Please upload a PDF'}), 400

    try:
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(file.read()))
        
        for page in pdf_reader.pages:
            text = page.extract_text()
            if text:
                TEXT += text

        return jsonify({'text': TEXT, 'TEXT': TEXT}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

################################################################################
#                             AI Resume Analyse                                #
################################################################################

################################################################################
# SKILL TAXONOMY DEFINITION
################################################################################

SKILL_TAXONOMY = {
    'core_languages': {
        'skills': [
            'Python', 'Java', 'C++', 'C', 'Go', 'Rust', 
            'JavaScript', 'TypeScript', 'Kotlin', 'Swift', 
            'Ruby', 'PHP', 'Scala', 'Perl', 'R','LeetCode', 'Codeforces', 
            'CodeChef', 'HackerRank', 'AtCoder', 'GeeksforGeeks'
        ],
        'weight': 1.0
    },
    'web_backend': {
       'skills': [
           'Django', 'Flask', 'FastAPI', 'Spring Boot', 'Express.js', 'Node.js', '.NET', 'Rails',
            'Laravel', 'NestJS', 'Koa.js', 'Hapi.js', 'ASP.NET Core', 'Gin', 'Fiber', 
            'AdonisJS', 'Sails.js', 'Phoenix', 'Falcon', 'Bottle', 'CherryPy', 
            'Actix', 'Quarkus', 'Micronaut'],
        'weight': 0.9
    },
    'web_frontend': {
         'skills': ['React', 'Vue', 'Angular', 'Next.js', 'Nuxt.js', 'Svelte', 'SolidJS',
            'HTML', 'CSS', 'JavaScript', 'TypeScript',
            'Tailwind CSS', 'Aceternity UI', 'shadcn/ui', 'DaisyUI', 'Flowbite', 
            'Headless UI', 'Radix UI', 'Material Tailwind', 'HyperUI', 'Preline UI',
            'Bootstrap', 'Material UI', 'Chakra UI',
            'Framer Motion', 'GSAP', 'Redux', 'Zustand', 'Recoil', 'Jotai',
            'Vite', 'Webpack', 'Babel', 'ESLint',
            'Jest', 'Cypress', 'Playwright'],
        'weight': 0.85
    },
    'ml_frameworks': {
        'skills': ['TensorFlow', 'PyTorch', 'Keras', 'Scikit-learn', 
            'XGBoost', 'LightGBM', 'CatBoost', 'Pandas', 'NumPy', 'SciPy', 'Polars',
            'Matplotlib', 'Seaborn', 'Plotly', 'Bokeh', 'Streamlit', 'Gradio', 
            'Flask', 'FastAPI', 'MLflow', 'Kaggle', 'Weights & Biases (W&B)', 'DVC',
            'SVM', 'Random Forest', 'Decision Trees', 'Regression', 'Clustering',
            'Machine Learning', 'Deep Learning', 'AI', 'Data Science'],
        'weight': 1.2
    },
    'ml_specialized': {
        'skills': ['Transformers', 'Hugging Face', 'LangChain', 'LlamaIndex', 'BERT', 'GPT', 
            'T5', 'LLM Fine-tuning', 'NLP', 'spaCy', 'NLTK', 'TextBlob', 
            'Sentence Transformers', 'Vector Embeddings', 'Computer Vision', 'OpenCV', 
            'YOLO', 'Detectron2', 'MMDetection', 'MediaPipe', 'Image Segmentation', 
            'Object Detection', 'Stable Diffusion', 'Diffusers', 'CLIP', 'DALL·E', 
            'Whisper', 'TensorRT', 'ONNX', 'TorchServe', 
            'Hugging Face Inference API', 'OpenVINO'],
        'weight': 1.5
    },
    'data_engineering': {
        'skills': ['Apache Spark', 'Hadoop', 'Flink', 'Beam', 'Presto', 'Hive', 'Pig',
            'Kafka', 'RabbitMQ', 'Pulsar', 'Kinesis',
            'Airflow', 'Luigi', 'Prefect', 'Dagster', 'dbt',
            'Snowflake', 'Databricks', 'BigQuery', 'Redshift', 'Azure Synapse', 'ClickHouse',
            'Delta Lake', 'Iceberg', 'Hudi', 'NiFi', 'Talend',
            'PostgreSQL', 'MySQL', 'MongoDB', 'Cassandra', 'Elasticsearch',
            'AWS Glue', 'Google Dataflow', 'Azure Data Factory', 'Docker', 'Kubernetes'],
        'weight': 1.3
    },
    'databases': {
        'skills': ['PostgreSQL', 'MySQL', 'SQLite', 'MariaDB', 'OracleDB', 'SQL Server',
            'MongoDB', 'Cassandra', 'CouchDB', 'DynamoDB', 
            'Firebase Realtime DB', 'Firestore', 'Redis', 'Memcached',
            'Elasticsearch', 'OpenSearch', 'ClickHouse', 
            'InfluxDB', 'TimescaleDB', 'Prometheus', 
            'Neo4j', 'ArangoDB', 'JanusGraph', 'Amazon RDS', 'Aurora', 
            'Google Cloud Spanner', 'PlanetScale', 'Neon', 'Supabase', 
            'Prisma', 'SQLAlchemy', 'TypeORM'],
        'weight': 0.9
    },
    'cloud_platforms': {
         'skills': ['AWS', 'GCP', 'Azure', 'Oracle Cloud', 'IBM Cloud', 'DigitalOcean', 'Heroku', 'Vercel',
            'Docker', 'Kubernetes', 'Helm', 'OpenShift', 'Rancher',
            'Terraform', 'CloudFormation', 'Pulumi', 'Ansible',
            'Jenkins', 'GitHub Actions', 'GitLab CI/CD', 'CircleCI', 'Argo CD',
            'Prometheus', 'Grafana', 'ELK Stack', 'Datadog', 'New Relic', 'Splunk',
            'S3', 'EBS', 'Cloud SQL', 'BigQuery', 'DynamoDB', 'Azure Blob Storage',
            'AWS Lambda', 'Google Cloud Functions', 'Azure Functions', 'Cloud Run', 'FaaS'],
        'weight': 1.1
    },
    'devops': {
         'skills': ['CI/CD', 'Jenkins', 'GitHub Actions', 'GitLab CI/CD', 'CircleCI', 'Travis CI', 'Argo CD', 'Tekton',
            'Ansible', 'Terraform', 'Puppet', 'Chef', 'Pulumi', 'CloudFormation',
            'Docker', 'Kubernetes', 'Helm', 'OpenShift', 'Rancher', 'K3s', 'Nomad',
            'Prometheus', 'Grafana', 'ELK Stack', 'Datadog', 'New Relic', 'Splunk', 'Jaeger', 'OpenTelemetry',
            'Fluentd', 'Loki', 'Nagios', 'PagerDuty', 
            'Firebase Authentication', 'Clerk', 'Auth0', 'Supabase Auth', 'Okta', 'AWS Cognito'],
        'weight': 0.9
    },
    'basic_tools': {
        'skills': ['Git', 'Linux', 'Command Line', 'Bash', 'Terminal',
            'SQL', 'REST API', 'GraphQL', 'Postman', 'SQLite',
            'Vercel', 'Netlify', 'Render', 'Heroku', 'Firebase', 'Supabase', 
            'Power BI', 'Tableau', 'Google Data Studio', 
            'Unity', 'Android Studio', 'VS Code', 'IntelliJ IDEA', 'PyCharm', 'Eclipse',
            'Leadership', 'Communication', 'Teamwork', 'Problem Solving', 'Time Management', 'Critical Thinking',
            'IMO', 'KVPY', 'NSO', 'IEO', 'JEE Mains', 'IIT', 'NIT', 'Coding Contests',
            'Cryptography', 'Research Paper', 'Fellowship', 'Award', 'Patent', 
            'Docker', 'Slack', 'Notion', 'Trello', 'Figma', 'Canva', 'Markdown', 'LaTeX', 'Spreadsheet (Excel/Google Sheets)'],
        'weight': 0.5
    }
}

################################################################################
# ANALYSIS FUNCTIONS
################################################################################

def extract_skills_deep(TEXT):
    """Extract skills with context awareness"""
    found_skills = {}
    text_lower = TEXT.lower()

    for category, data in SKILL_TAXONOMY.items():
        for skill in data['skills']:
            if skill.lower() in text_lower:
                skill_contexts = [
                    f"using {skill.lower()}",
                    f"with {skill.lower()}",
                    f"{skill.lower()},",
                    f"{skill.lower()} and",
                    f"built.*{skill.lower()}",
                    f"developed.*{skill.lower()}",
                    f"implemented.*{skill.lower()}"
                ]

                has_context = any(re.search(pattern, text_lower) for pattern in skill_contexts)

                if has_context or category == 'core_languages':
                    if category not in found_skills:
                        found_skills[category] = []
                    found_skills[category].append(skill)

    return found_skills

def analyze_experience_depth(TEXT):
    """Analyze actual experience depth"""
    text_lower = TEXT.lower()
    experience_score = 0

    fulltime_patterns = [r'(\d+)\s*\+?\s*years?', r'(\d+)\s*-\s*(\d+)\s*years?']
    for pattern in fulltime_patterns:
        matches = re.findall(pattern, text_lower)
        for match in matches:
            if isinstance(match, tuple):
                experience_score += int(match[0]) * 15
            else:
                experience_score += int(match) * 15

    if 'intern' in text_lower:
        internship_count = text_lower.count('intern')
        experience_score += internship_count * 8

    senior_keywords = ['lead', 'senior', 'principal', 'architect', 'manager']
    if any(keyword in text_lower for keyword in senior_keywords):
        experience_score += 20

    impact_patterns = [
        r'(\d+)%\s*(increase|improvement|reduction|growth)',
        r'(\d+)\s*users',
        r'(\d+)k\+?\s*users',
        r'\$(\d+)k',
        r'saved.*\$(\d+)'
    ]

    impact_count = 0
    for pattern in impact_patterns:
        matches = re.findall(pattern, text_lower)
        impact_count += len(matches)

    experience_score += min(impact_count * 3, 15)
    return min(experience_score, 100)

def analyze_project_quality(TEXT):
    """Analyze project complexity and quality"""
    text_lower = TEXT.lower()
    quality_score = 0

    advanced_patterns = [
        'microservices', 'distributed system', 'event-driven', 'load balancing',
        'caching', 'rate limiting', 'scalable', 'high availability', 'fault tolerant',
        'ci/cd', 'pipeline', 'automation', 'orchestration','system design','monolithic'
    ]
    advanced_count = sum(1 for pattern in advanced_patterns if pattern in text_lower)
    quality_score += min(advanced_count * 5, 30)

    scale_patterns = [r'(\d+)k?\+?\s*users', r'(\d+)\s*million', r'scale']
    scale_mentions = sum(len(re.findall(pattern, text_lower)) for pattern in scale_patterns)
    quality_score += min(scale_mentions * 4, 20)

    production_keywords = ['deployed', 'production', 'live', 'production-grade']
    prod_count = sum(1 for keyword in production_keywords if keyword in text_lower)
    quality_score += min(prod_count * 5, 15)

    quality_keywords = ['testing', 'test coverage', 'unit test', 'integration test', 'monitoring']
    quality_mentions = sum(1 for keyword in quality_keywords if keyword in text_lower)
    quality_score += min(quality_mentions * 3, 10)

    return min(quality_score, 75)

def calculate_resume_score(TEXT, skills_data, experience_score, project_score):
    """Realistic resume scoring"""
    score = 0
    score += min(experience_score * 0.4, 40)
    score += min(project_score * 0.33, 25)

    total_weighted_skills = 0
    for category, skills in skills_data.items():
        weight = SKILL_TAXONOMY[category]['weight']
        total_weighted_skills += len(skills) * weight

    score += min(total_weighted_skills * 1.5, 20)

    has_contact = bool(re.search(r'[\w\.-]+@[\w\.-]+', TEXT))
    has_education = 'education' in TEXT.lower() or 'university' in TEXT.lower() or 'college' in TEXT.lower()
    has_clear_sections = len(re.findall(r'\n[A-Z][a-z]+\n', TEXT)) >= 3

    if has_contact:
        score += 5
    if has_education:
        score += 5
    if has_clear_sections:
        score += 5

    return round(min(score, 100), 1)

def calculate_ats_compatibility(TEXT, skills_data):
    """Strict ATS compatibility check"""
    score = 0

    special_chars = TEXT.count('|') + TEXT.count('_') + TEXT.count('*')
    if special_chars < 5:
        score += 15
    elif special_chars < 10:
        score += 10
    else:
        score += 5

    required_sections = ['experience', 'education', 'skills']
    section_count = sum(1 for section in required_sections if section in TEXT.lower())
    score += (section_count / len(required_sections)) * 20

    total_skills = sum(len(skills) for skills in skills_data.values())
    if total_skills >= 15:
        score += 25
    elif total_skills >= 10:
        score += 20
    elif total_skills >= 7:
        score += 15
    else:
        score += 10

    score += 15

    action_verbs = ['developed', 'built', 'designed', 'implemented', 'created',
                    'engineered', 'deployed', 'led', 'managed', 'optimized']
    verb_count = sum(1 for verb in action_verbs if verb in TEXT.lower())
    score += min(verb_count * 1.5, 10)

    return round(min(score, 100), 1)

def calculate_technical_compatibility(skills_data, domain):
    """Deep domain-specific technical assessment"""
    domain_requirements = {
        'ML Engineer': {
            'ml_frameworks': (3, 'critical'),
            'ml_specialized': (2, 'critical'),
            'core_languages': (2, 'required'),
            'cloud_platforms': (1, 'nice_to_have'),
            'data_engineering': (1, 'nice_to_have')
        },
        'Full Stack Developer': {
            'web_frontend': (2, 'critical'),
            'web_backend': (1, 'critical'),
            'databases': (1, 'required'),
            'core_languages': (2, 'required'),
            'devops': (1, 'nice_to_have')
        },
        'Data Scientist': {
            'ml_frameworks': (2, 'critical'),
            'data_engineering': (2, 'critical'),
            'core_languages': (1, 'required'),
            'databases': (1, 'required'),
            'cloud_platforms': (1, 'required')
        }
    }

    requirements = domain_requirements.get(domain, domain_requirements['Full Stack Developer'])

    total_score = 0
    max_score = 0
    category_scores = {}

    for category, (min_required, priority) in requirements.items():
        actual_count = len(skills_data.get(category, []))

        if priority == 'critical':
            weight = 30
            max_score += weight
            if actual_count >= min_required:
                total_score += weight
            elif actual_count > 0:
                total_score += (actual_count / min_required) * weight * 0.5

        elif priority == 'required':
            weight = 20
            max_score += weight
            if actual_count >= min_required:
                total_score += weight
            elif actual_count > 0:
                total_score += (actual_count / min_required) * weight * 0.6

        else:
            weight = 10
            max_score += weight
            if actual_count >= min_required:
                total_score += weight
            elif actual_count > 0:
                total_score += (actual_count / min_required) * weight * 0.7

        category_scores[category] = {
            'found': actual_count,
            'required': min_required,
            'priority': priority,
            'skills': skills_data.get(category, [])
        }

    overall_score = round((total_score / max_score * 100) if max_score > 0 else 0, 1)
    return overall_score, category_scores

def get_gaps_for_role(skills_data, role):
    """Identify skill gaps for specific roles"""
    gaps = []

    if role == 'ML Engineer':
        if len(skills_data.get('ml_specialized', [])) < 2:
            gaps.append("Learn advanced ML techniques (Transformers, BERT, etc.)")
        if 'cloud_platforms' not in skills_data or len(skills_data['cloud_platforms']) == 0:
            gaps.append("Gain cloud platform experience (AWS/GCP)")
        if len(skills_data.get('ml_frameworks', [])) < 2:
            gaps.append("Master multiple ML frameworks")

    elif role == 'Full Stack Developer':
        if len(skills_data.get('databases', [])) < 2:
            gaps.append("Learn both SQL and NoSQL databases")
        if 'devops' not in skills_data:
            gaps.append("Learn CI/CD and DevOps practices")
        if len(skills_data.get('web_frontend', [])) < 2:
            gaps.append("Expand frontend framework knowledge")
    
    elif role == 'Data Scientist':
        if len(skills_data.get('ml_frameworks', [])) < 2:
            gaps.append("Master more ML/stats frameworks (Scikit-learn, XGBoost)")
        if len(skills_data.get('data_engineering', [])) < 1:
            gaps.append("Learn data engineering tools (Spark, Airflow)")
        if 'cloud_platforms' not in skills_data or len(skills_data['cloud_platforms']) == 0:
            gaps.append("Gain cloud platform experience for scalable ML")

    return gaps[:3] if gaps else ["Continue building projects to gain depth"]

def recommend_job_profiles(skills_data, experience_score, project_score, TEXT):
    """Realistic job recommendations"""
    profiles = []
    text_lower = TEXT.lower()

    # ML/DS related skills count
    ml_skills = len(skills_data.get('ml_frameworks', [])) + len(skills_data.get('ml_specialized', []))
    
    # Enhanced ML keywords
    ml_keywords = ['machine learning', 'ml', 'ai', 'artificial intelligence', 'deep learning', 
                   'neural network', 'computer vision', 'nlp', 'natural language']
    ml_experience = any(keyword in text_lower for keyword in ml_keywords)
    
    # Data Science keywords
    ds_keywords = ['data science', 'data scientist', 'statistical', 'statistics', 'analytics', 
                   'predictive model', 'data analysis', 'data mining', 'regression', 'classification']
    ds_experience = any(keyword in text_lower for keyword in ds_keywords)

    # ML Engineer - RELAXED conditions
    if ml_skills >= 2 and ml_experience and experience_score >= 20:
        match_score = min(40 + ml_skills * 5 + (experience_score * 0.3) + (project_score * 0.2), 85)
        profiles.append({
            "job_title": "Machine Learning Engineer",
            "match_score": round(match_score, 1),
            "reason": f"Has {ml_skills} ML skills with relevant experience",
            "gaps": get_gaps_for_role(skills_data, 'ML Engineer')
        })

    # Data Scientist - NEW ADDITION
    if ml_skills >= 1 and (ds_experience or ml_experience) and experience_score >= 15:
        data_eng_skills = len(skills_data.get('data_engineering', []))
        match_score = min(45 + ml_skills * 4 + data_eng_skills * 3 + (experience_score * 0.25), 80)
        profiles.append({
            "job_title": "Data Scientist",
            "match_score": round(match_score, 1),
            "reason": f"Has {ml_skills} ML/stats skills and data analysis background",
            "gaps": get_gaps_for_role(skills_data, 'Data Scientist')
        })

    frontend_skills = len(skills_data.get('web_frontend', []))
    backend_skills = len(skills_data.get('web_backend', []))
    full_stack_complete = frontend_skills >= 2 and backend_skills >= 1

    if full_stack_complete:
        match_score = min(45 + (frontend_skills + backend_skills) * 4 + (project_score * 0.3), 82)
        profiles.append({
            "job_title": "Full Stack Developer",
            "match_score": round(match_score, 1),
            "reason": f"Frontend: {frontend_skills} skills, Backend: {backend_skills} skills",
            "gaps": get_gaps_for_role(skills_data, 'Full Stack Developer')
        })

    if backend_skills >= 1:
        match_score = min(50 + backend_skills * 5 + (project_score * 0.25), 78)
        profiles.append({
            "job_title": "Backend Developer",
            "match_score": round(match_score, 1),
            "reason": f"Has {backend_skills} backend framework(s)",
            "gaps": ["Add more backend frameworks", "Learn microservices architecture"]
        })

    # Data Analyst - FIXED logic
    basic_tools = skills_data.get('basic_tools', [])
    has_sql = 'sql' in text_lower or any('SQL' in str(skill) for skill in basic_tools)
    has_viz = any(tool in text_lower for tool in ['powerbi', 'tableau', 'power bi', 'tablue'])
    
    if (has_sql or has_viz or ml_skills >= 1) and ml_skills < 4:
        match_score = min(40 + (experience_score * 0.3) + ml_skills * 3, 70)
        profiles.append({
            "job_title": "Data Analyst",
            "match_score": round(match_score, 1),
            "reason": f"Has data analysis and visualization skills",
            "gaps": ["Learn advanced SQL", "Master data visualization tools", "Learn statistical analysis"]
        })

    total_skills = sum(len(skills) for skills in skills_data.values())
    if total_skills >= 5:
        match_score = min(45 + total_skills * 2 + (project_score * 0.25), 75)
        profiles.append({
            "job_title": "Software Engineer",
            "match_score": round(match_score, 1),
            "reason": f"Generalist with {total_skills} technical skills",
            "gaps": ["Specialize in a domain", "Deepen expertise in one area"]
        })

    return sorted(profiles, key=lambda x: x['match_score'], reverse=True)[:3]

def determine_candidate_level(resume_score, ats_score, tech_score, experience_score, TEXT):
    """Realistic candidate level assessment"""
    text_lower = TEXT.lower()
    weighted_score = (resume_score * 0.3 + ats_score * 0.2 + tech_score * 0.3 + experience_score * 0.2)

    has_fulltime = bool(re.search(r'\d+\s*\+?\s*years?', text_lower))
    has_senior_role = any(keyword in text_lower for keyword in ['lead', 'senior', 'principal', 'architect', 'manager'])
    internship_only = 'intern' in text_lower and not has_fulltime

    if has_senior_role and weighted_score >= 70 and experience_score >= 60:
        return "Senior", 88, "Top tier - ready for senior roles"
    elif has_fulltime and weighted_score >= 65 and experience_score >= 40:
        return "Mid-Level", 72, "Experienced professional with proven skills"
    elif weighted_score >= 55 and experience_score >= 25:
        return "Junior", 55, "Early career with solid foundation"
    elif internship_only and weighted_score >= 45:
        return "Entry-Level", 38, "Recent graduate/intern with potential"
    else:
        return "Beginner", 20, "Needs more experience and skill development"

################################################################################
# FLASK ROUTES
################################################################################

@app.route('/analyze', methods=['POST'])
def analyze_resume():
    """Main endpoint to analyze resume"""
    try:
        data = request.get_json()
        TEXT = data.get('resume_text', '')

        if not TEXT:
            return jsonify({"error": "No resume TEXT provided"}), 400

        # Run analysis
        skills_data = extract_skills_deep(TEXT)
        experience_score = analyze_experience_depth(TEXT)
        project_score = analyze_project_quality(TEXT)
        resume_score = calculate_resume_score(TEXT, skills_data, experience_score, project_score)
        ats_score = calculate_ats_compatibility(TEXT, skills_data)

        primary_domain = "ML Engineer" if len(skills_data.get('ml_frameworks', [])) >= 2 else "Full Stack Developer"
        tech_score, category_breakdown = calculate_technical_compatibility(skills_data, primary_domain)

        job_recommendations = recommend_job_profiles(skills_data, experience_score, project_score, TEXT)
        candidate_level, percentile, level_description = determine_candidate_level(
            resume_score, ats_score, tech_score, experience_score, TEXT
        )

        # Build output
        output = {
            "resume_score": {
                "score": resume_score,
                "max_score": 100,
                "grade": "A+" if resume_score >= 90 else "A" if resume_score >= 80 else "B" if resume_score >= 70 else "C" if resume_score >= 60 else "D",
                "breakdown": {
                    "experience_contribution": round(min(experience_score * 0.4, 40), 1),
                    "project_contribution": round(min(project_score * 0.33, 25), 1),
                    "skills_contribution": round(resume_score - min(experience_score * 0.4, 40) - min(project_score * 0.33, 25), 1)
                }
            },
            "ats_compatibility": {
                "score": ats_score,
                "max_score": 100,
                "rating": "Excellent" if ats_score >= 85 else "Good" if ats_score >= 70 else "Fair" if ats_score >= 55 else "Poor",
                "issues": [] if ats_score >= 70 else ["Improve keyword density", "Add more standard sections"]
            },
            "technical_skills_compatibility": {
                "overall_score": tech_score,
                "target_domain": primary_domain,
                "category_breakdown": category_breakdown,
                "total_skills_identified": sum(len(skills) for skills in skills_data.values()),
                "skills_by_category": {k: v for k, v in skills_data.items()}
            },
            "experience_analysis": {
                "score": experience_score,
                "project_quality_score": project_score,
                "has_professional_experience": experience_score >= 40,
                "experience_level": "Senior" if experience_score >= 70 else "Mid" if experience_score >= 40 else "Junior" if experience_score >= 20 else "Entry"
            },
            "recommended_job_profiles": job_recommendations,
            "candidate_level": {
                "level": candidate_level,
                "percentile": percentile,
                "description": level_description,
                "realistic_assessment": f"Based on {experience_score}/100 experience score and {tech_score}/100 technical compatibility"
            },
            "visualization_data": {
                "score_breakdown": {
                    "categories": ['Resume Quality', 'ATS Score', 'Technical Match', 'Experience Depth'],
                    "scores": [resume_score, ats_score, tech_score, experience_score],
                    "colors": ['#1e429f' if s >= 75 else '#1c64f2' if s >= 55 else '#93C5FD' for s in [resume_score, ats_score, tech_score, experience_score]],
                    "thresholds": {
                        "strong": 75,
                        "fair": 55
                    }
                },
                "competitive_positioning": {
                    "levels": [
                        {"name": "Senior", "label": "Senior", "percentile": 80, "color": "#004f3b"},
                        {"name": "Mid-Level", "label": "Mid-Level", "percentile": 70, "color": "#007a55"},
                        {"name": "Junior", "label": "Junior", "percentile": 60, "color": "#00bc7d"},
                        {"name": "Entry", "label": "Entry", "percentile": 40, "color": "#5ee9b5"},
                        {"name": "Beginner", "label": "Beginner", "percentile": 20, "color": "#5ee9b5"}
                    ],
                    "current_level": candidate_level,
                    "current_percentile": percentile
                },
                "summary_stats": {
                    "average_score": round((resume_score + ats_score + tech_score + experience_score) / 4, 1),
                    "top_skill_gap": job_recommendations[0]['gaps'][0] if job_recommendations and job_recommendations[0].get('gaps') and len(job_recommendations[0]['gaps']) > 0 else "N/A"
                }
            }
        }
        return jsonify(output), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/summary', methods=['POST'])
def get_summary():
    """Get condensed summary of analysis"""
    try:
        data = request.get_json()
        TEXT = data.get('resume_text', '')

        if not TEXT:
            return jsonify({"error": "No resume TEXT provided"}), 400

        # Run quick analysis
        skills_data = extract_skills_deep(TEXT)
        experience_score = analyze_experience_depth(TEXT)
        project_score = analyze_project_quality(TEXT)
        resume_score = calculate_resume_score(TEXT, skills_data, experience_score, project_score)
        ats_score = calculate_ats_compatibility(TEXT, skills_data)

        primary_domain = "ML Engineer" if len(skills_data.get('ml_frameworks', [])) >= 2 else "Full Stack Developer"
        tech_score, _ = calculate_technical_compatibility(skills_data, primary_domain)

        job_recommendations = recommend_job_profiles(skills_data, experience_score, project_score, TEXT)
        candidate_level, percentile, _ = determine_candidate_level(
            resume_score, ats_score, tech_score, experience_score, TEXT
        )

        summary_data = {
            "resume_quality": {
                "score": resume_score,
                "grade": "A+" if resume_score >= 90 else "A" if resume_score >= 80 else "B" if resume_score >= 70 else "C" if resume_score >= 60 else "D",
                "out_of": 100
            },
            "ats_compatibility": {
                "score": ats_score,
                "rating": "Excellent" if ats_score >= 85 else "Good" if ats_score >= 70 else "Fair" if ats_score >= 55 else "Poor",
                "out_of": 100
            },
            "technical_match": {
                "score": tech_score,
                "domain": primary_domain,
                "out_of": 100
            },
            "experience_depth": {
                "score": experience_score,
                "out_of": 100
            },
            "realistic_level": {
                "level": candidate_level,
                "percentile": percentile
            },
            "top_3_job_matches": [
                {
                    "rank": i,
                    "job_title": job['job_title'],
                    "match_score": job['match_score'],
                    "reason": job['reason'],
                    "skill_gaps": job.get('gaps', [])[:2]
                }
                for i, job in enumerate(job_recommendations[:3], 1)
            ]
        }

        return jsonify(summary_data), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500



if __name__ == '__main__':
    app.run(debug=False)
