```json
{
  "meta": {
    "job": "DoorDash Dasher (Delivery Driver)",
    "slug": "dasher",
    "incomeType": "piece_rate",
    "incomeLabel": "Piece Rate / Per-Delivery Earnings",
    "calculatorInputs": [
      "ratePerTask",
      "tasksPerHour",
      "hoursPerWeek",
      "weeksPerYear",
      "careerYears",
      "peakPayRate",
      "peakHoursPct",
      "inflationRate",
      "taxRate"
    ],
    "bonusApplicable": true,
    "bonusRange": [0.05, 0.40],
    "inflationSensitive": true,
    "ltv_formula": "ratePerTask × tasksPerHour × hoursPerWeek × weeksPerYear × careerYears × (1 + peakPayRate × peakHoursPct)",
    "automationThreat": "HIGH",
    "platformNote": "1099 independent contractor · No benefits · Earnings vary by market, time & tips"
  },
  "industries": [
    { "id": "gig", "label": "Gig Economy", "active": true },
    { "id": "logistics", "label": "Logistics", "active": false },
    { "id": "qsr", "label": "QSR / Fast Food", "active": false },
    { "id": "retail", "label": "Retail", "active": false }
  ],
  "countries": {
    "US": {
      "name": "United States",
      "symbol": "$",
      "annualUSD": 36000,
      "annualLocal": 36000,
      "career": 10,
      "automationIdx": 72,
      "carName": "Honda Civic",
      "carPriceUSD": 25000,
      "riskAge": 38,
      "startAge": 18,
      "localDisplay": "$36,000/yr (USD)",
      "flag": "🇺🇸",
      "riskLabel": "FAST",
      "riskClass": "fast"
    },
    "CA": {
      "name": "Canada",
      "symbol": "C$",
      "annualUSD": 32000,
      "annualLocal": 42500,
      "career": 12,
      "automationIdx": 68,
      "carName": "Toyota Corolla",
      "carPriceUSD": 22000,
      "riskAge": 40,
      "startAge": 18,
      "localDisplay": "~C$42.5K/yr (~$32K USD)",
      "flag": "🇨🇦",
      "riskLabel": "FAST",
      "riskClass": "fast"
    },
    "AU": {
      "name": "Australia",
      "symbol": "A$",
      "annualUSD": 34000,
      "annualLocal": 51000,
      "career": 12,
      "automationIdx": 65,
      "carName": "Toyota Corolla",
      "carPriceUSD": 24000,
      "riskAge": 42,
      "startAge": 18,
      "localDisplay": "~A$51K/yr (~$34K USD)",
      "flag": "🇦🇺",
      "riskLabel": "FAST",
      "riskClass": "fast"
    },
    "UK": {
      "name": "United Kingdom",
      "symbol": "£",
      "annualUSD": 28000,
      "annualLocal": 21000,
      "career": 12,
      "automationIdx": 70,
      "carName": "Ford Fiesta",
      "carPriceUSD": 20000,
      "riskAge": 40,
      "startAge": 18,
      "localDisplay": "~£21K/yr (~$28K USD)",
      "flag": "🇬🇧",
      "riskLabel": "FAST",
      "riskClass": "fast"
    },
    "DE": {
      "name": "Germany",
      "symbol": "€",
      "annualUSD": 24000,
      "annualLocal": 22000,
      "career": 15,
      "automationIdx": 62,
      "carName": "VW Golf",
      "carPriceUSD": 28000,
      "riskAge": 45,
      "startAge": 18,
      "localDisplay": "~€22K/yr (~$24K USD)",
      "flag": "🇩🇪",
      "riskLabel": "MID",
      "riskClass": "mid"
    },
    "JP": {
      "name": "Japan",
      "symbol": "¥",
      "annualUSD": 18000,
      "annualLocal": 2700000,
      "career": 15,
      "automationIdx": 55,
      "carName": "Honda N-BOX",
      "carPriceUSD": 14000,
      "riskAge": 48,
      "startAge": 18,
      "localDisplay": "~¥2.7M/yr (~$18K USD)",
      "flag": "🇯🇵",
      "riskLabel": "MID",
      "riskClass": "mid"
    },
    "SG": {
      "name": "Singapore",
      "symbol": "S$",
      "annualUSD": 22000,
      "annualLocal": 29500,
      "career": 12,
      "automationIdx": 75,
      "carName": "Honda Fit",
      "carPriceUSD": 70000,
      "riskAge": 38,
      "startAge": 18,
      "localDisplay": "~S$29.5K/yr (~$22K USD)",
      "flag": "🇸🇬",
      "riskLabel": "FAST",
      "riskClass": "fast"
    },
    "TW": {
      "name": "Taiwan",
      "symbol": "NT$",
      "annualUSD": 10000,
      "annualLocal": 320000,
      "career": 5,
      "automationIdx": 68,
      "carName": "Gogoro Scooter",
      "carPriceUSD": 3000,
      "riskAge": 32,
      "startAge": 18,
      "localDisplay": "~NT$320K/yr (~$10K USD)",
      "flag": "🇹🇼",
      "riskLabel": "FAST",
      "riskClass": "fast"
    },
    "CN": {
      "name": "China",
      "symbol": "¥",
      "annualUSD": 8000,
      "annualLocal": 58000,
      "career": 5,
      "automationIdx": 78,
      "carName": "Electric Scooter",
      "carPriceUSD": 800,
      "riskAge": 30,
      "startAge": 18,
      "localDisplay": "~¥58K/yr (~$8K USD)",
      "flag": "🇨🇳",
      "riskLabel": "FAST",
      "riskClass": "fast"
    }
  },
  "levels": [
    { "id": 0, "name": "Entry Dasher", "short": "Entry", "yearsFrom": 0, "color": "#888888", "yearsLabel": "Launch · Yr 0" },
    { "id": 1, "name": "Top Dasher", "short": "Top", "yearsFrom": 1, "color": "#4f98a3", "yearsLabel": "≈ 1 yr" },
    { "id": 2, "name": "Team Lead / Shift Coordinator", "short": "Lead", "yearsFrom": 3, "color": "#eab308", "yearsLabel": "≈ 3–4 yrs" },
    { "id": 3, "name": "Fleet Manager", "short": "Fleet", "yearsFrom": 5, "color": "#22c55e", "yearsLabel": "≈ 5+ yrs" }
  ],
  "promotions": [
    { "from": "Entry Dasher", "to": "Top Dasher", "years": "1 yr", "tip": "High acceptance rate & customer rating" },
    { "from": "Top Dasher", "to": "Team Lead / Shift Coordinator", "years": "≈ 2 yrs", "tip": "Leadership & peer training" },
    { "from": "Team Lead / Shift Coordinator", "to": "Fleet Manager", "years": "≈ 2+ yrs", "tip": "Ops/logistics management" }
  ],
  "levelUSD": {
    "US": [28000, 40000, 50000, 75000],
    "CA": [24000, 34000, 43000, 65000],
    "AU": [28000, 38000, 48000, 70000],
    "UK": [20000, 30000, 38000, 55000],
    "DE": [18000, 26000, 33000, 48000],
    "JP": [14000, 20000, 26000, 40000],
    "SG": [16000, 24000, 31000, 45000],
    "TW": [8000, 12000, 15000, 24000],
    "CN": [6000, 9000, 12000, 18000]
  },
  "levelLocal": {
    "US": ["$28K", "$40K", "$50K", "$75K"],
    "CA": ["C$32K", "C$45K", "C$57K", "C$86K"],
    "AU": ["A$43K", "A$58K", "A$74K", "A$106K"],
    "UK": ["£15K", "£22K", "£28K", "£40K"],
    "DE": ["€16.5K", "€24K", "€30K", "€44K"],
    "JP": ["¥2.1M", "¥3.0M", "¥3.9M", "¥6.0M"],
    "SG": ["S$21K", "S$32K", "S$41K", "S$60K"],
    "TW": ["NT$256K", "NT$384K", "NT$480K", "NT$768K"],
    "CN": ["¥43K", "¥65K", "¥87K", "¥130K"]
  },
  "languages": {
    "US": [{ "lang": "English", "level": "Essential", "score": 5 }, { "lang": "Spanish", "level": "Helpful", "score": 2 }],
    "CA": [{ "lang": "English", "level": "Essential", "score": 5 }, { "lang": "French", "level": "Helpful", "score": 2 }],
    "AU": [{ "lang": "English", "level": "Essential", "score": 5 }],
    "UK": [{ "lang": "English", "level": "Essential", "score": 5 }],
    "DE": [{ "lang": "German", "level": "Essential", "score": 5 }, { "lang": "English", "level": "Helpful", "score": 2 }],
    "JP": [{ "lang": "Japanese", "level": "Essential", "score": 5 }, { "lang": "English", "level": "Senior Only", "score": 3 }],
    "SG": [{ "lang": "English", "level": "Essential", "score": 5 }, { "lang": "Mandarin", "level": "Helpful", "score": 2 }, { "lang": "Malay", "level": "Optional", "score": 1 }],
    "TW": [{ "lang": "Mandarin", "level": "Essential", "score": 5 }, { "lang": "Taiwanese", "level": "Helpful", "score": 2 }, { "lang": "English", "level": "Optional", "score": 3 }],
    "CN": [{ "lang": "Mandarin", "level": "Essential", "score": 5 }, { "lang": "Dialect", "level": "Regional", "score": 2 }, { "lang": "English", "level": "High-end Only", "score": 3 }]
  },
  "langScoreLabels": { "1": "Elementary", "2": "Limited Working", "3": "Professional Working", "4": "Full Professional", "5": "Native / Bilingual" },
  "langPillClasses": {
    "Essential": "llp-essential",
    "Helpful": "llp-helpful",
    "Optional": "llp-optional",
    "Senior Only": "llp-senior",
    "High-end Only": "llp-senior",
    "Regional": "llp-helpful"
  },
  "cities": {
    "US": [
      { "city": "San Francisco", "region": "West", "salary": 42000, "cost": 105 },
      { "city": "New York", "region": "Northeast", "salary": 40000, "cost": 103 },
      { "city": "Seattle", "region": "West", "salary": 38000, "cost": 88 },
      { "city": "Los Angeles", "region": "West", "salary": 36000, "cost": 95 },
      { "city": "Chicago", "region": "Midwest", "salary": 34000, "cost": 80 },
      { "city": "Denver", "region": "Mountain", "salary": 33000, "cost": 78 },
      { "city": "Miami", "region": "South", "salary": 32000, "cost": 75 },
      { "city": "Austin", "region": "South", "salary": 31000, "cost": 68 },
      { "city": "Atlanta", "region": "South", "salary": 30000, "cost": 62 },
      { "city": "Phoenix", "region": "Southwest", "salary": 29000, "cost": 60 }
    ],
    "CA": [
      { "city": "Vancouver", "region": "BC", "salary": 38000, "cost": 100 },
      { "city": "Toronto", "region": "ON", "salary": 36000, "cost": 95 },
      { "city": "Calgary", "region": "AB", "salary": 33000, "cost": 78 },
      { "city": "Montreal", "region": "QC", "salary": 31000, "cost": 72 },
      { "city": "Edmonton", "region": "AB", "salary": 30000, "cost": 70 }
    ],
    "AU": [
      { "city": "Sydney", "region": "NSW", "salary": 40000, "cost": 100 },
      { "city": "Melbourne", "region": "VIC", "salary": 38000, "cost": 92 },
      { "city": "Brisbane", "region": "QLD", "salary": 35000, "cost": 80 },
      { "city": "Perth", "region": "WA", "salary": 34000, "cost": 82 },
      { "city": "Adelaide", "region": "SA", "salary": 32000, "cost": 72 }
    ],
    "UK": [
      { "city": "London", "region": "England", "salary": 32000, "cost": 100 },
      { "city": "Birmingham", "region": "England", "salary": 28000, "cost": 70 },
      { "city": "Manchester", "region": "England", "salary": 27000, "cost": 72 },
      { "city": "Edinburgh", "region": "Scotland", "salary": 26000, "cost": 75 },
      { "city": "Bristol", "region": "England", "salary": 25000, "cost": 73 }
    ],
    "DE": [
      { "city": "Munich", "region": "Bavaria", "salary": 28000, "cost": 100 },
      { "city": "Berlin", "region": "Berlin", "salary": 25000, "cost": 80 },
      { "city": "Frankfurt", "region": "Hesse", "salary": 26000, "cost": 95 },
      { "city": "Hamburg", "region": "Hamburg", "salary": 25000, "cost": 88 },
      { "city": "Cologne", "region": "NRW", "salary": 24000, "cost": 78 }
    ],
    "JP": [
      { "city": "Tokyo", "region": "Kanto", "salary": 22000, "cost": 100 },
      { "city": "Osaka", "region": "Kansai", "salary": 19000, "cost": 85 },
      { "city": "Nagoya", "region": "Chubu", "salary": 18000, "cost": 75 },
      { "city": "Fukuoka", "region": "Kyushu", "salary": 17000, "cost": 70 },
      { "city": "Sapporo", "region": "Hokkaido", "salary": 16000, "cost": 68 }
    ],
    "SG": [
      { "city": "Orchard", "region": "Central", "salary": 24000, "cost": 103 },
      { "city": "CBD / Marina", "region": "Central", "salary": 23000, "cost": 100 },
      { "city": "Tampines", "region": "East", "salary": 21000, "cost": 80 },
      { "city": "Jurong", "region": "West", "salary": 20000, "cost": 78 },
      { "city": "Woodlands", "region": "North", "salary": 19000, "cost": 72 }
    ],
    "TW": [
      { "city": "Taipei", "region": "Northern", "salary": 12000, "cost": 100 },
      { "city": "New Taipei", "region": "Northern", "salary": 11500, "cost": 88 },
      { "city": "Taichung", "region": "Central", "salary": 10500, "cost": 72 },
      { "city": "Kaohsiung", "region": "Southern", "salary": 10000, "cost": 68 },
      { "city": "Tainan", "region": "Southern", "salary": 9500, "cost": 65 }
    ],
    "CN": [
      { "city": "Shanghai", "region": "East", "salary": 10000, "cost": 105 },
      { "city": "Beijing", "region": "North", "salary": 9500, "cost": 100 },
      { "city": "Shenzhen", "region": "South", "salary": 9500, "cost": 98 },
      { "city": "Guangzhou", "region": "South", "salary": 8500, "cost": 85 },
      { "city": "Chengdu", "region": "Southwest", "salary": 7000, "cost": 65 }
    ]
  },
  "countryMeta": {
    "US": { "difficulty": 7, "restDays": 0, "hoursPerDay": 8, "splitShift": false, "bestLearnAge": "18–25", "bestEntryAge": "18", "cert": "Driver license · Background check", "travel": "Constant local", "mobility": "Extreme", "expression": "Low" },
    "CA": { "difficulty": 7, "restDays": 5, "hoursPerDay": 8, "splitShift": false, "bestLearnAge": "18–24", "bestEntryAge": "18", "cert": "Driver license · Insurance", "travel": "Constant local", "mobility": "Extreme", "expression": "Low" },
    "AU": { "difficulty": 6, "restDays": 10, "hoursPerDay": 7.5, "splitShift": false, "bestLearnAge": "18–25", "bestEntryAge": "18", "cert": "Driver license · ABN", "travel": "Constant local", "mobility": "Extreme", "expression": "Low" },
    "UK": { "difficulty": 7, "restDays": 5, "hoursPerDay": 8, "splitShift": false, "bestLearnAge": "18–24", "bestEntryAge": "18", "cert": "Driver license · Insurance · Delivery permit", "travel": "Constant local", "mobility": "Extreme", "expression": "Low" },
    "DE": { "difficulty": 6, "restDays": 15, "hoursPerDay": 7, "splitShift": false, "bestLearnAge": "18–26", "bestEntryAge": "18", "cert": "Führerschein · Gewerbeerlaubnis", "travel": "Constant local", "mobility": "High", "expression": "Low" },
    "JP": { "difficulty": 8, "restDays": 5, "hoursPerDay": 9, "splitShift": false, "bestLearnAge": "18–25", "bestEntryAge": "18", "cert": "運転免許証 · 特定原付", "travel": "Constant local", "mobility": "Extreme", "expression": "Low" },
    "SG": { "difficulty": 7, "restDays": 7, "hoursPerDay": 9, "splitShift": false, "bestLearnAge": "18–24", "bestEntryAge": "18", "cert": "Class 2B/3 license", "travel": "Constant local", "mobility": "Extreme", "expression": "Low" },
    "TW": { "difficulty": 5, "restDays": 7, "hoursPerDay": 8, "splitShift": false, "bestLearnAge": "18–24", "bestEntryAge": "18", "cert": "機車駕照", "travel": "Constant local", "mobility": "Extreme", "expression": "Low" },
    "CN": { "difficulty": 5, "restDays": 5, "hoursPerDay": 9, "splitShift": false, "bestLearnAge": "18–22", "bestEntryAge": "18", "cert": "电瓶车牌照 · 外卖员证", "travel": "Constant local", "mobility": "Extreme", "expression": "Low" }
  },
  "difficultyLabels": ["", "", "Very Easy", "Easy", "Below Avg", "Average", "Above Avg", "Hard", "Very Hard", "Brutal", "Extreme"],
  "insightCards": [
    { "id": "difficulty", "icon": "💪", "label": "Job Hardship", "valueKey": "difficulty", "valueTemplate": "{value}/10", "metaTemplate": "{difficultyLabel} · physically demanding road work", "colorMode": "gradient-bad" },
    { "id": "restDays", "icon": "🏖️", "label": "Annual Leave", "valueKey": "restDays", "valueTemplate": "{value} days", "metaTemplate": "{hoursPerDay}h avg work day · No paid leave (1099)", "colorMode": "gradient-good" },
    { "id": "bestLearnAge", "icon": "🎓", "label": "Best Entry Age", "valueKey": "bestLearnAge", "valueTemplate": "{value}", "metaTemplate": "Minimal entry barriers; low learning curve.", "colorMode": "accent" },
    { "id": "bestEntryAge", "icon": "🚀", "label": "Peak Physical Stamina", "valueKey": "bestEntryAge", "valueTemplate": "{value}", "metaTemplate": "Ideal onset for sustained physical output.", "colorMode": "accent" },
    { "id": "travel", "icon": "✈️", "label": "Business Travel", "valueKey": "travel", "valueTemplate": "{value}", "metaTemplate": "All work is local road-based travel.", "colorMode": "accent" },
    { "id": "mobility", "icon": "🏃", "label": "Physical Mobility", "valueKey": "mobility", "valueTemplate": "{value}", "metaTemplate": "Constant driving, walking, lifting, bending.", "colorMode": "accent" },
    { "id": "expression", "icon": "🗣️", "label": "Schedule Control", "valueKey": "expression", "valueTemplate": "{value}", "metaTemplate": "Minimal personal expression; moderate time autonomy.", "colorMode": "accent" },
    { "id": "cert", "icon": "📜", "label": "Certifications Required", "valueKey": "cert", "valueTemplate": "{value}", "metaTemplate": "Driver license, background check & smartphone", "spanFull": true, "colorMode": "neutral" }
  ],
  "extendedMeta": {
    "US": { "budget": "$250/mo", "hnwi": "Not applicable · 1099 gig", "startupReadiness": 35, "mbti": "ISTP · ESTP · ISTJ", "uni": "No", "uniMeta": "Degree irrelevant for this role.", "privateSchool": "No value", "privateMeta": "No schooling advantage.", "schools": "Not applicable", "retire": "Pivot to logistics/warehouse or trade skill.", "pivot": "Warehouse Associate, Truck Driver, Fleet Coordinator." },
    "CA": { "budget": "C$200/mo", "hnwi": "Not applicable", "startupReadiness": 32, "mbti": "ISTP · ESTP · ISTJ", "uni": "No", "uniMeta": "Degree irrelevant for this role.", "privateSchool": "No value", "privateMeta": "No schooling advantage.", "schools": "Not applicable", "retire": "Pivot to warehousing or ride-share.", "pivot": "Ride-share Driver, Courier, Logistics Assistant." },
    "AU": { "budget": "A$250/mo", "hnwi": "Not applicable", "startupReadiness": 40, "mbti": "ISTP · ESTP · ISTJ", "uni": "No", "uniMeta": "TAFE logistics cert optional.", "privateSchool": "No value", "privateMeta": "No schooling advantage.", "schools": "TAFE Logistics Programs", "retire": "Pivot to full-time transport/logistics.", "pivot": "Postal Worker, Freight Handler, Courier Supervisor." },
    "UK": { "budget": "£150/mo", "hnwi": "Not applicable", "startupReadiness": 30, "mbti": "ISTP · ESTP · ISTJ", "uni": "No", "uniMeta": "GCSE-level sufficient.", "privateSchool": "No value", "privateMeta": "No schooling advantage.", "schools": "Not applicable", "retire": "Pivot to delivery services or warehouse.", "pivot": "Royal Mail Worker, HGV Driver, Delivery Station Operator." },
    "DE": { "budget": "€150/mo", "hnwi": "Not applicable", "startupReadiness": 28, "mbti": "ISTJ · ISTP · ESTJ", "uni": "No", "uniMeta": "Ausbildung logistics optional.", "privateSchool": "No value", "privateMeta": "No schooling advantage.", "schools": "Speditionskaufmann Programs", "retire": "Pivot to warehouse or industry logistics.", "pivot": "Postbote, LKW-Fahrer, Lagerverwalter." },
    "JP": { "budget": "¥20,000/mo", "hnwi": "Not applicable", "startupReadiness": 22, "mbti": "ISTJ · ISFP · ISTP", "uni": "No", "uniMeta": "High-school diploma typical.", "privateSchool": "No value", "privateMeta": "No schooling advantage.", "schools": "Not applicable", "retire": "Pivot to taxi or light logistics.", "pivot": "Taxi Driver, Bicycle Courier, Warehouse Staff." },
    "SG": { "budget": "S$200/mo", "hnwi": "Not applicable", "startupReadiness": 30, "mbti": "ISTP · ESTP · ISTJ", "uni": "No", "uniMeta": "ITE logistics cert optional.", "privateSchool": "No value", "privateMeta": "No schooling advantage.", "schools": "ITE Work-Learn Tech Programs", "retire": "Pivot to delivery station or grab fleet.", "pivot": "Grab Driver, Warehouse Operator, Dispatch Coordinator." },
    "TW": { "budget": "NT$4,000/mo", "hnwi": "Not applicable", "startupReadiness": 25, "mbti": "ISTP · ESTP · ISTJ", "uni": "No", "uniMeta": "高中學歷即可.", "privateSchool": "No value", "privateMeta": "No schooling advantage.", "schools": "Not applicable", "retire": "Pivot to store clerk or scooter courier.", "pivot": "便利店店員, 快遞員, 倉儲人員." },
    "CN": { "budget": "¥800/mo", "hnwi": "Not applicable", "startupReadiness": 20, "mbti": "ISTP · ESTP · ISTJ", "uni": "No", "uniMeta": "初中以上学历.", "privateSchool": "No value", "privateMeta": "No schooling advantage.", "schools": "Not applicable", "retire": "Pivot to factory or ride-share.", "pivot": "工厂普工, 网约车司机, 快递员." }
  },
  "startupLinks": {
    "US": [{ "label": "Dasher Gear", "url": "https://dasher.doordash.com" }, { "label": "Gridwise Analytics", "url": "https://gridwise.io" }],
    "CA": [{ "label": "Dasher Canada", "url": "https://dasher.doordash.com/en-ca" }, { "label": "SkipTheDishes", "url": "https://www.skipthedishes.com" }],
    "AU": [{ "label": "Menulog", "url": "https://www.menulog.com.au" }, { "label": "Uber Eats Aus", "url": "https://www.ubereats.com/au" }],
    "UK": [{ "label": "Deliveroo Riders", "url": "https://deliveroo.co.uk/riders" }, { "label": "Just Eat Courier", "url": "https://www.just-eat.co.uk/courier" }],
    "DE": [{ "label": "Lieferando Fahrer", "url": "https://www.lieferando.de/fahrer" }, { "label": "Wolt Partners DE", "url": "https://wolt.com/en/deu" }],
    "JP": [{ "label": "Uber Eats JP", "url": "https://www.ubereats.com/jp" }, { "label": "出前館", "url": "https://demae-can.com" }],
    "SG": [{ "label": "GrabExpress", "url": "https://www.grab.com/sg" }, { "label": "foodpanda riders", "url": "https://www.foodpanda.sg" }],
    "TW": [{ "label": "Uber Eats TW", "url": "https://www.ubereats.com/tw" }, { "label": "foodpanda TW", "url": "https://www.foodpanda.com.tw" }],
    "CN": [{ "label": "美团骑手", "url": "https://peisong.meituan.com" }, { "label": "饿了么骑手", "url": "https://h5.ele.me" }]
  },
  "careerRecs": [
    [
      { "title": "Warehouse Associate", "match": "72%", "color": "var(--yellow)", "desc": "Amazon/UPS fulfillment center roles.", "skills": ["Physical Stamina", "Punctuality"] },
      { "title": "Ride-Share Driver", "match": "68%", "color": "var(--orange)", "desc": "Uber/Lyft pax driver.", "skills": ["Navigation", "Customer Service"] },
      { "title": "Scooter Charger", "match": "55%", "color": "var(--orange)", "desc": "Lime/Bird field ops.", "skills": ["Flexible Schedule", "Route Planning"] }
    ],
    [
      { "title": "Fleet Dispatcher", "match": "80%", "color": "var(--green)", "desc": "Coordinate delivery fleets.", "skills": ["Communication", "Multi-tasking"] },
      { "title": "Logistics Coordinator", "match": "75%", "color": "var(--yellow)", "desc": "Plan delivery routes & schedules.", "skills": ["Route Optimization", "Computer Literacy"] },
      { "title": "Field Trainer", "match": "70%", "color": "var(--yellow)", "desc": "Onboard new dashers.", "skills": ["Teaching", "Patience"] }
    ],
    [
      { "title": "Operations Supervisor", "match": "85%", "color": "var(--green)", "desc": "Manage shift & dasher performance.", "skills": ["People Management", "Problem Solving"] },
      { "title": "E-Commerce Delivery Partner", "match": "78%", "color": "var(--yellow)", "desc": "Contract with Amazon Flex / GoPuff.", "skills": ["Reliability", "Vehicle Maintenance"] },
      { "title": "Fleet Coordinator", "match": "75%", "color": "var(--yellow)", "desc": "Oversee multiple gig fleets.", "skills": ["Scheduling", "Data Analysis"] }
    ],
    [
      { "title": "Fleet Manager", "match": "92%", "color": "var(--green)", "desc": "Head of fleet ops for a region.", "skills": ["Leadership", "P&L Management"] },
      { "title": "Last-Mile Logistics Manager", "match": "88%", "color": "var(--yellow)", "desc": "End-to-end station delivery ops.", "skills": ["Process Improvement", "Team Building"] },
      { "title": "Independent Contractor", "match": "82%", "color": "var(--orange)", "desc": "Run your own fleet subscription.", "skills": ["Entrepreneurship", "Fleet Leasing"] }
    ]
  ],
  "survivalStrategy": [
    "As an <strong>Entry Dasher</strong>, cherry-pick high-tip zones and use multi-app strategy to maximize hourly earnings.",
    "As a <strong>Top Dasher</strong>, leverage dash-pass priority and schedule flexibility to lock in profitable blocks.",
    "As a <strong>Team Lead</strong>, build peer-to-peer training skills and demonstrate operations leadership.",
    "As a <strong>Shift Coordinator</strong>, master dispatch logic and conflict resolution between drivers and restaurant partners.",
    "As a <strong>Fleet Manager</strong>, focus on automation trends (drones, bots) and up-skill into logistics management software."
  ],
  "hazards": [
    { "icon": "🚗", "name": "Road Traffic Accidents", "levelClass": "haz-5", "width": "100%", "desc": "Critical · primary fatality risk" },
    { "icon": "💪", "name": "Musculoskeletal Strain", "levelClass": "haz-4", "width": "80%", "desc": "High · lifting, bending & prolonged sitting" },
    { "icon": "🧠", "name": "Mental Fatigue & Distraction", "levelClass": "haz-4", "width": "75%", "desc": "High · app-driven constant alerting & multi-tasking" },
    { "icon": "🌧️", "name": "Weather Exposure", "levelClass": "haz-4", "width": "70%", "desc": "High · rain, cold, heat extremes" },
    { "icon": "🦮", "name": "Dog Bites & Encounters", "levelClass": "haz-3", "width": "50%", "desc": "Medium · suburban/rural drop-offs" },
    { "icon": "🔪", "name": "Personal Security & Assault", "levelClass": "haz-3", "width": "40%", "desc": "Medium · late-night deliveries" },
    { "icon": "📉", "name": "Income Insecurity", "levelClass": "haz-5", "width": "95%", "desc": "Critical · no wage floor, tip dependent" },
    { "icon": "🚲", "name": "Fall from Bike/E-Scooter", "levelClass": "haz-4", "width": "65%", "desc": "High · common in urban bike/scooter dashers" }
  ],
  "filters": [
    { "id": "all", "label": "All", "class": "all", "active": true, "dot": false },
    { "id": "replaceable", "label": "Replaceable", "class": "gf", "active": false, "dot": true },
    { "id": "indanger", "label": "In-Danger", "class": "yf", "active": false, "dot": true },
    { "id": "intro", "label": "Intro", "class": "of", "active": false, "dot": true },
    { "id": "nothing", "label": "Nothing", "class": "rf", "active": false, "dot": true }
  ],
  "tasksByLevel": {
    "0": [
      { "action": "Accept Orders & Navigate", "human": "Scan incoming offers; decline low-pay orders; navigate to restaurant using GPS.", "ai": "AI auto-accepts profitable orders based on learned preferences; route optimized in real time.", "timePct": 30, "ratio": 85, "ratioColor": "var(--red)", "eta": "~1 yr", "etaClass": "eta-soon", "status": "replaceable", "statusClass": "b-replaceable", "statusLabel": "Replaceable", "costRatio": 8.0 },
      { "action": "Wait & Pick Up", "human": "Stand in queue; verify order items; place in thermal bag; confirm pickup.", "ai": "Geofenced lockers & robot-arm pickups eliminate waiting; drone docking stations.", "timePct": 25, "ratio": 65, "ratioColor": "var(--orange)", "eta": "2–4 yrs", "etaClass": "eta-mid", "status": "indanger", "statusClass": "b-indanger", "statusLabel": "In-Danger", "costRatio": 4.0 },
      { "action": "Driving / Scooter Operation", "human": "Operate vehicle through traffic; find parking; handle complex urban situations.", "ai": "Autonomous delivery robots (Starship, Nuro) and sidewalk bots navigate fixed routes.", "timePct": 25, "ratio": 45, "ratioColor": "var(--yellow)", "eta": "3–6 yrs", "etaClass": "eta-mid", "status": "intro", "statusClass": "b-intro", "statusLabel": "Intro", "costRatio": 2.5 },
      { "action": "Drop Off & Handoff", "human": "Locate customer address; climb stairs; hand off or leave at door; take photo.", "ai": "Drone drop (Wing, Zipline) for single homes; lobby bots for apartments.", "timePct": 15, "ratio": 25, "ratioColor": "var(--green)", "eta": "5–8 yrs", "etaClass": "eta-far", "status": "intro", "statusClass": "b-intro", "statusLabel": "Intro", "costRatio": 1.2 },
      { "action": "Document & Report Issues", "human": "Report closed restaurants, wrong addresses, rude customers via app.", "ai": "Automated fraud detection & real-time issue flagging using camera & GPS.", "timePct": 5, "ratio": 90, "ratioColor": "var(--red)", "eta": "~1.5 yrs", "etaClass": "eta-soon", "status": "replaceable", "statusClass": "b-replaceable", "statusLabel": "Replaceable", "costRatio": 9.0 }
    ],
    "1": [
      { "action": "Priority Order Selection", "human": "Prioritize high-value catering/large orders; schedule Dash time for peak pay.", "ai": "Smart batch algorithms group deliveries automatically; human just drives.", "timePct": 25, "ratio": 80, "ratioColor": "var(--red)", "eta": "~1 yr", "etaClass": "eta-soon", "status": "replaceable", "statusClass": "b-replaceable", "statusLabel": "Replaceable", "costRatio": 7.0 },
      { "action": "Advanced Navigation & Multi-apping", "human": "Run dual app strategy (DD + UE) seamlessly; manage double-batch deliveries.", "ai": "Consolidator apps automate cross-platform optimization; AI handles batching.", "timePct": 20, "ratio": 70, "ratioColor": "var(--orange)", "eta": "2–3 yrs", "etaClass": "eta-mid", "status": "indanger", "statusClass": "b-indanger", "statusLabel": "In-Danger", "costRatio": 5.0 },
      { "action": "Customer Service & Conflict Resolution", "human": "Handle missing items, spilled drinks, address confusion in real time.", "ai": "AI chat & voice bots handle 80% of post-delivery complaints; credits auto-issued.", "timePct": 15, "ratio": 50, "ratioColor": "var(--yellow)", "eta": "3–5 yrs", "etaClass": "eta-mid", "status": "intro", "statusClass": "b-intro", "statusLabel": "Intro", "costRatio": 3.0 },
      { "action": "Vehicle Maintenance Tracking", "human": "Monitor oil changes, tire pressure, brake wear; schedule personal auto repair.", "ai": "IoT car sensors (SyncUP, Zubie) auto-log maintenance and predict failures.", "timePct": 10, "ratio": 60, "ratioColor": "var(--orange)", "eta": "2–4 yrs", "etaClass": "eta-mid", "status": "indanger", "statusClass": "b-indanger", "statusLabel": "In-Danger", "costRatio": 4.5 },
      { "action": "On-boarding & Shadowing", "human": "Show new dashers the ropes; share parking tips and restaurant shortcuts.", "ai": "AR/VR onboarding simulations replace ride-alongs; gamified training bots.", "timePct": 10, "ratio": 40, "ratioColor": "var(--yellow)", "eta": "3–5 yrs", "etaClass": "eta-far", "status": "intro", "statusClass": "b-intro", "statusLabel": "Intro", "costRatio": 2.0 },
      { "action": "Tax & Earnings Tracking", "human": "Log miles manually; track expenses for 1099 filing.", "ai": "Everlance / Stride auto-track; AI tax prep integrations standard.", "timePct": 20, "ratio": 95, "ratioColor": "var(--red)", "eta": "~1 yr", "etaClass": "eta-soon", "status": "replaceable", "statusClass": "b-replaceable", "statusLabel": "Replaceable", "costRatio": 10.0 }
    ],
    "2": [
      { "action": "Team Scheduling & Break Management", "human": "Coordinate shift swaps, manage coverage for peak demand, approve breaks.", "ai": "AI auto-schedules based on demand curves & driver availability; human edits only.", "timePct": 25, "ratio": 30, "ratioColor": "var(--yellow)", "eta": "3–5 yrs", "etaClass": "eta-far", "status": "intro", "statusClass": "b-intro", "statusLabel": "Intro", "costRatio": 1.8 },
      { "action": "Live Dispatch & Rerouting", "human": "Manually override dispatches for VIP orders or traffic emergencies.", "ai": "Predictive dispatch fully handles rerouting; edge-case escalations only.", "timePct": 20, "ratio": 55, "ratioColor": "var(--orange)", "eta": "2–4 yrs", "etaClass": "eta-mid", "status": "indanger", "statusClass": "b-indanger", "statusLabel": "In-Danger", "costRatio": 3.5 },
      { "action": "Driver Performance Reviews", "human": "Monitor acceptance rate, completion rate, and rating; enforce policies.", "ai": "Automated KPI dashboards & warnings; AI demotes/enables Top Dasher status.", "timePct": 15, "ratio": 75, "ratioColor": "var(--red)", "eta": "~2 yrs", "etaClass": "eta-soon", "status": "replaceable", "statusClass": "b-replaceable", "statusLabel": "Replaceable", "costRatio": 6.0 },
      { "action": "Restaurant Partnership Liaison", "human": "Visit merchants; resolve packaging issues & wait-time complaints.", "ai": "Tablet-based auto-error reporting; chatbots handle simple merchant issues.", "timePct": 15, "ratio": 25, "ratioColor": "var(--green)", "eta": "5–8 yrs", "etaClass": "eta-far", "status": "intro", "statusClass": "b-intro", "statusLabel": "Intro", "costRatio": 1.0 },
      { "action": "Quality Audits", "human": "Random bag checks; temperature compliance; thermal bag integrity.", "ai": "IoT thermal sensors + camera CV confirm bag status; automated audit logs.", "timePct": 10, "ratio": 60, "ratioColor": "var(--orange)", "eta": "2–3 yrs", "etaClass": "eta-mid", "status": "indanger", "statusClass": "b-indanger", "statusLabel": "In-Danger", "costRatio": 4.0 },
      { "action": "Accident/Incident Reporting", "human": "File first report; manage insurance claims; driver care follow-up.", "ai": "Auto-collision detection & claim initiation; human just verifies insurance data.", "timePct": 15, "ratio": 80, "ratioColor": "var(--red)", "eta": "~1.5 yrs", "etaClass": "eta-soon", "status": "replaceable", "statusClass": "b-replaceable", "statusLabel": "Replaceable", "costRatio": 7.5 }
    ],
    "3": [
      { "action": "Fleet Operations Strategy", "human": "P&L for delivery zones; expansion planning; headcount forecasting.", "ai": "AI forecasting tools run Monte Carlo simulations; human makes strategic decisions.", "timePct": 25, "ratio": 15, "ratioColor": "var(--green)", "eta": "8+ yrs", "etaClass": "eta-prot", "status": "nothing", "statusClass": "b-none", "statusLabel": "Nothing", "costRatio": 0.15 },
      { "action": "Vendor Management (Car Rentals, Fuel)", "human": "Negotiate fleet leases; fuel card partnerships; maintenance contracts.", "ai": "Automated RFP bidding & contract analysis; human finalize relationships.", "timePct": 15, "ratio": 25, "ratioColor": "var(--yellow)", "eta": "5–7 yrs", "etaClass": "eta-far", "status": "intro", "statusClass": "b-intro", "statusLabel": "Intro", "costRatio": 1.5 },
      { "action": "Government & Compliance", "human": "Manage 1099 vs W-2 classification; AB5/Prop22 lobbying; safety audits.", "ai": "Legal AI drafts compliance docs; strategic lobbying & negotiation fully human.", "timePct": 15, "ratio": 5, "ratioColor": "var(--green)", "eta": "10+ yrs", "etaClass": "eta-prot", "status": "nothing", "statusClass": "b-none", "statusLabel": "Nothing", "costRatio": 0.1 },
      { "action": "Team Culture & Retention", "human": "Build driver loyalty; recognition programs; career pathing.", "ai": "Gamification bots manage rewards; human touch needed for genuine culture.", "timePct": 15, "ratio": 10, "ratioColor": "var(--green)", "eta": "10+ yrs", "etaClass": "eta-prot", "status": "nothing", "statusClass": "b-none", "statusLabel": "Nothing", "costRatio": 0.2 },
      { "action": "Budgeting & Finance", "human": "Monthly operating budget; zone profitability analysis; CapEx for EV/bot fleet.", "ai": "AI dashboards automate budget tracking & variance analysis; strategic calls remain human.", "timePct": 20, "ratio": 45, "ratioColor": "var(--yellow)", "eta": "5–7 yrs", "etaClass": "eta-far", "status": "intro", "statusClass": "b-intro", "statusLabel": "Intro", "costRatio": 2.5 },
      { "action": "Automation Pilot Management", "human": "Oversee drone/bot testing zones; coordinate with local regulators; scale rollout.", "ai": "AI manages bot fleet logistics autonomously; human defines adoption pace & zone boundaries.", "timePct": 10, "ratio": 20, "ratioColor": "var(--green)", "eta": "6–10 yrs", "etaClass": "eta-far", "status": "nothing", "statusClass": "b-none", "statusLabel": "Nothing", "costRatio": 0.5 }
    ]
  },
  "countryTaskMods": {
    "US": { "techAdoption": 1.0, "laborCost": 1.0, "aiSpeed": 1.0 },
    "CA": { "techAdoption": 0.9, "laborCost": 0.85, "aiSpeed": 0.9 },
    "AU": { "techAdoption": 0.85, "laborCost": 0.9, "aiSpeed": 0.85 },
    "UK": { "techAdoption": 0.92, "laborCost": 0.8, "aiSpeed": 0.95 },
    "DE": { "techAdoption": 0.75, "laborCost": 0.8, "aiSpeed": 0.7 },
    "JP": { "techAdoption": 0.8, "laborCost": 0.7, "aiSpeed": 0.75 },
    "SG": { "techAdoption": 1.1, "laborCost": 0.95, "aiSpeed": 1.1 },
    "TW": { "techAdoption": 0.9, "laborCost": 0.5, "aiSpeed": 0.85 },
    "CN": { "techAdoption": 1.05, "laborCost": 0.35, "aiSpeed": 1.0 }
  },
  "networkCards": [
    { "title": "Recommended Majors", "value": "Logistics & Supply Chain Mgt", "meta": "Secondary: Business Admin, Operations Research." },
    { "title": "Target Courses", "value": "Last-Mile Ops & Fleet Tech", "meta": "Also: Gig Economy Law, Data Analytics, Urban Planning." },
    { "title": "Stretch Majors", "value": "Autonomous Systems & Drones", "meta": "Transition into emerging last-mile robot/drone industry." },
    { "title": "Key Connections", "value": "Fleet & Logistics Directors", "meta": "Build relationships with 3PL and gig economy leaders.", "loginCTA": true }
  ],
  "famousChefs": {
    "US": [{ "name": "Tony Xu (DoorDash)", "netWorth": "$1.5B" }],
    "CA": [{ "name": "Apoorva Mehta (Instacart)", "netWorth": "$1.2B" }],
    "AU": [{ "name": "Matt Barrie (Freelancer)", "netWorth": "$350M" }],
    "UK": [{ "name": "Will Shu (Deliveroo)", "netWorth": "$400M" }],
    "DE": [{ "name": "Miki Kuusi (Wolt)", "netWorth": "$1B" }],
    "JP": [{ "name": "Shintaro Yamada (Mercari)", "netWorth": "$2B" }],
    "SG": [{ "name": "Anthony Tan (Grab)", "netWorth": "$790M" }],
    "TW": [{ "name": "Jamie Lin (AppWorks)", "netWorth": "$150M" }],
    "CN": [{ "name": "王兴 (美团)", "netWorth": "$8.5B" }]
  },
  "accessLinks": [
    { "title": "Sign Up as Dasher", "desc": "Register on DoorDash, Uber Eats, Grubhub." },
    { "title": "Driver Supplies & Gear", "desc": "Thermal bags, phone mounts, dash cams." },
    { "title": "Tax Prep for 1099", "desc": "Everlance, Stride, Keeper Tax platform links." },
    { "title": "Rental Cars for Gigs", "desc": "HyreCar, Lyft Express Drive, Avis for dashers." },
    { "title": "Community Forums", "desc": "r/doordash_drivers, UberPeople, local FB groups." },
    { "title": "Find a Mentor", "desc": "Connect with a Fleet Manager or high-earning Top Dasher." }
  ],
  "mbtiData": [
    { "type": "ISTP", "desc": "The Tinkerer. Enjoys hands-on, independent work; navigating traffic & problem-solving." },
    { "type": "ESTP", "desc": "The Dynamo. Thrives in fast-paced, unpredictable street-level entrepreneurship." },
    { "type": "ISTJ", "desc": "The Inspector. Reliable, rule-abiding; perfect for structured scheduling and high acceptance rates." },
    { "type": "ISFP", "desc": "The Adventurer. Flexible, low-commitment lifestyle; prefers working alone with a personal touch." },
    { "type": "ENTJ", "desc": "The Commander. Naturally moves from driving into fleet management & operations leadership." }
  ],
  "filialPietyCountries": ["CN", "TW", "SG", "JP"],
  "ltvMethodology": "BLS 2025 median piece-rate earnings × 10-yr career horizon. AI Risk weighted by delivery automation maturity.",
  "highestThreat": "Order acceptance & routing is the most automatable node.",
  "version": "v1.0 May 2026",
  "footnote": "* Data: BLS 2025 · DoorDash Earnings Report 2024 · JobForesight 2026"
}
```