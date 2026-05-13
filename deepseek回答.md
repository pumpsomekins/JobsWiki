[chef.json]
```json
{
  "meta": {
    "job": "Chef / Cook",
    "slug": "chef",
    "incomeType": "salary",
    "incomeLabel": "Annual Salary",
    "calculatorInputs": ["annualSalary", "careerYears", "bonusRate"],
    "ltv_formula": "annualSalary × careerYears × (1 + bonusRate)",
    "automationThreat": "MID",
    "platformNote": "W2 employee, benefits included, unionized in some markets"
  },
  "industries": [
    { "id": "fb", "label": "Food & Beverage", "active": true },
    { "id": "hosp", "label": "Hospitality", "active": false },
    { "id": "qsr", "label": "QSR / Fast Food", "active": false },
    { "id": "fine", "label": "Fine Dining", "active": false },
    { "id": "cat", "label": "Catering", "active": false },
    { "id": "inst", "label": "Institutional", "active": false }
  ],
  "countries": {
    "US": {
      "name": "United States",
      "symbol": "$",
      "annualUSD": 56000,
      "annualLocal": 56000,
      "career": 30,
      "automationIdx": 37,
      "carName": "Toyota Camry",
      "carPriceUSD": 28000,
      "riskAge": 47,
      "startAge": 25,
      "localDisplay": "$56,000/yr (USD)",
      "flag": "🇺🇸",
      "riskLabel": "MID",
      "riskClass": "mid"
    },
    "UK": {
      "name": "United Kingdom",
      "symbol": "£",
      "annualUSD": 44000,
      "annualLocal": 35000,
      "career": 30,
      "automationIdx": 37,
      "carName": "Ford Focus",
      "carPriceUSD": 26000,
      "riskAge": 49,
      "startAge": 25,
      "localDisplay": "~£35K/yr (~$44K)",
      "flag": "🇬🇧",
      "riskLabel": "MID",
      "riskClass": "mid"
    },
    "AU": {
      "name": "Australia",
      "symbol": "A$",
      "annualUSD": 42000,
      "annualLocal": 65000,
      "career": 30,
      "automationIdx": 37,
      "carName": "Toyota RAV4",
      "carPriceUSD": 28000,
      "riskAge": 48,
      "startAge": 25,
      "localDisplay": "~A$65K/yr (~$42K)",
      "flag": "🇦🇺",
      "riskLabel": "MID",
      "riskClass": "mid"
    },
    "DE": {
      "name": "Germany",
      "symbol": "€",
      "annualUSD": 41000,
      "annualLocal": 38000,
      "career": 30,
      "automationIdx": 35,
      "carName": "VW Golf",
      "carPriceUSD": 30000,
      "riskAge": 50,
      "startAge": 25,
      "localDisplay": "~€38K/yr (~$41K)",
      "flag": "🇩🇪",
      "riskLabel": "SLOW",
      "riskClass": "slow"
    },
    "JP": {
      "name": "Japan",
      "symbol": "¥",
      "annualUSD": 28000,
      "annualLocal": 4200000,
      "career": 30,
      "automationIdx": 32,
      "carName": "Toyota Corolla",
      "carPriceUSD": 18000,
      "riskAge": 52,
      "startAge": 25,
      "localDisplay": "~¥4.2M/yr (~$28K)",
      "flag": "🇯🇵",
      "riskLabel": "SLOW",
      "riskClass": "slow"
    },
    "SG": {
      "name": "Singapore",
      "symbol": "S$",
      "annualUSD": 31000,
      "annualLocal": 42000,
      "career": 30,
      "automationIdx": 42,
      "carName": "Toyota Corolla*",
      "carPriceUSD": 88000,
      "riskAge": 46,
      "startAge": 25,
      "localDisplay": "~S$42K/yr (~$31K)",
      "flag": "🇸🇬",
      "riskLabel": "FAST",
      "riskClass": "fast"
    },
    "TW": {
      "name": "Taiwan",
      "symbol": "NT$",
      "annualUSD": 15000,
      "annualLocal": 480000,
      "career": 30,
      "automationIdx": 40,
      "carName": "Toyota Corolla",
      "carPriceUSD": 22000,
      "riskAge": 45,
      "startAge": 25,
      "localDisplay": "~NT$480K/yr (~$15K)",
      "flag": "🇹🇼",
      "riskLabel": "FAST",
      "riskClass": "fast"
    },
    "CN": {
      "name": "China",
      "symbol": "¥",
      "annualUSD": 12000,
      "annualLocal": 86000,
      "career": 30,
      "automationIdx": 44,
      "carName": "BYD Seagull",
      "carPriceUSD": 12000,
      "riskAge": 44,
      "startAge": 25,
      "localDisplay": "~¥86K/yr (~$12K)",
      "flag": "🇨🇳",
      "riskLabel": "FAST",
      "riskClass": "fast"
    }
  },
  "levels": [
    { "id": 0, "name": "Line Cook", "short": "Line", "yearsFrom": 0, "color": "#888888", "yearsLabel": "Entry · Yr 0" },
    { "id": 1, "name": "Chef de Partie", "short": "CDP", "yearsFrom": 2, "color": "#4f98a3", "yearsLabel": "≈ 2–3 yrs" },
    { "id": 2, "name": "Sous Chef", "short": "Sous", "yearsFrom": 5, "color": "#eab308", "yearsLabel": "≈ 5–6 yrs" },
    { "id": 3, "name": "Head Chef", "short": "Head", "yearsFrom": 8, "color": "#f97316", "yearsLabel": "≈ 8–11 yrs" },
    { "id": 4, "name": "Executive Chef", "short": "Exec", "yearsFrom": 16, "color": "#22c55e", "yearsLabel": "≈ 16–19 yrs" }
  ],
  "promotions": [
    { "from": "Line Cook", "to": "Chef de Partie", "years": "2–3 yrs", "tip": "Station mastery required" },
    { "from": "Chef de Partie", "to": "Sous Chef", "years": "2–3 yrs", "tip": "Performance + kitchen leadership" },
    { "from": "Sous Chef", "to": "Head Chef", "years": "3–5 yrs", "tip": "Menu creation + team management" },
    { "from": "Head Chef", "to": "Executive Chef", "years": "5–8 yrs", "tip": "Business acumen + reputation" }
  ],
  "levelUSD": {
    "US": [32000, 48000, 55000, 72000, 95000],
    "UK": [28000, 42000, 48000, 65000, 88000],
    "AU": [33000, 45000, 50000, 68000, 90000],
    "DE": [26000, 38000, 42000, 58000, 78000],
    "JP": [25000, 35000, 40000, 55000, 73000],
    "SG": [22000, 36000, 41000, 58000, 78000],
    "TW": [13000, 18000, 20000, 28000, 37000],
    "CN": [8000, 12000, 14000, 20000, 30000]
  },
  "levelLocal": {
    "US": ["$32K", "$48K", "$55K", "$72K", "$95K"],
    "UK": ["£22K", "£32K", "£37K", "£50K", "£68K"],
    "AU": ["A$45K", "A$62K", "A$70K", "A$95K", "A$125K"],
    "DE": ["€24K", "€35K", "€39K", "€54K", "€72K"],
    "JP": ["¥3.2M", "¥4.5M", "¥5.1M", "¥7.0M", "¥9.3M"],
    "SG": ["S$30K", "S$48K", "S$55K", "S$78K", "S$105K"],
    "TW": ["NT$380K", "NT$520K", "NT$580K", "NT$820K", "NT$1.1M"],
    "CN": ["¥50K", "¥72K", "¥85K", "¥120K", "¥180K"]
  },
  "languages": {
    "US": [{ "lang": "English", "level": "Essential", "score": 5 }, { "lang": "Spanish", "level": "Helpful", "score": 2 }],
    "UK": [{ "lang": "English", "level": "Essential", "score": 5 }],
    "AU": [{ "lang": "English", "level": "Essential", "score": 5 }],
    "DE": [{ "lang": "German", "level": "Essential", "score": 5 }, { "lang": "English", "level": "Helpful", "score": 2 }],
    "JP": [{ "lang": "Japanese", "level": "Essential", "score": 5 }, { "lang": "English", "level": "Senior Only", "score": 3 }],
    "SG": [{ "lang": "English", "level": "Essential", "score": 5 }, { "lang": "Mandarin", "level": "Helpful", "score": 2 }, { "lang": "Malay", "level": "Optional", "score": 1 }],
    "TW": [{ "lang": "Mandarin", "level": "Essential", "score": 5 }, { "lang": "Taiwanese", "level": "Helpful", "score": 2 }, { "lang": "English", "level": "Senior Only", "score": 3 }],
    "CN": [{ "lang": "Mandarin", "level": "Essential", "score": 5 }, { "lang": "Dialect", "level": "Regional", "score": 2 }, { "lang": "English", "level": "High-end Only", "score": 3 }]
  },
  "langScoreLabels": { "1": "Elementary", "2": "Limited Working", "3": "Professional Working", "4": "Full Professional", "5": "Native / Bilingual" },
  "cities": {
    "US": [
      { "city": "San Francisco", "region": "West", "salary": 72000, "cost": 105 },
      { "city": "New York", "region": "Northeast", "salary": 68000, "cost": 103 },
      { "city": "Boston", "region": "Northeast", "salary": 64000, "cost": 90 },
      { "city": "Seattle", "region": "West", "salary": 62000, "cost": 88 },
      { "city": "Los Angeles", "region": "West", "salary": 65000, "cost": 95 },
      { "city": "Chicago", "region": "Midwest", "salary": 58000, "cost": 80 },
      { "city": "Denver", "region": "Mountain", "salary": 55000, "cost": 78 },
      { "city": "Miami", "region": "South", "salary": 52000, "cost": 75 },
      { "city": "Dallas", "region": "South", "salary": 50000, "cost": 65 },
      { "city": "Phoenix", "region": "Southwest", "salary": 48000, "cost": 60 }
    ],
    "UK": [
      { "city": "London", "region": "England", "salary": 55000, "cost": 100 },
      { "city": "Edinburgh", "region": "Scotland", "salary": 44000, "cost": 75 },
      { "city": "Bristol", "region": "England", "salary": 43000, "cost": 73 },
      { "city": "Manchester", "region": "England", "salary": 42000, "cost": 72 },
      { "city": "Birmingham", "region": "England", "salary": 40000, "cost": 70 },
      { "city": "Leeds", "region": "England", "salary": 39000, "cost": 68 }
    ],
    "AU": [
      { "city": "Sydney", "region": "NSW", "salary": 88000, "cost": 100 },
      { "city": "Melbourne", "region": "VIC", "salary": 82000, "cost": 92 },
      { "city": "Canberra", "region": "ACT", "salary": 80000, "cost": 85 },
      { "city": "Perth", "region": "WA", "salary": 78000, "cost": 82 },
      { "city": "Brisbane", "region": "QLD", "salary": 75000, "cost": 80 },
      { "city": "Gold Coast", "region": "QLD", "salary": 70000, "cost": 75 },
      { "city": "Adelaide", "region": "SA", "salary": 68000, "cost": 72 }
    ],
    "DE": [
      { "city": "Munich", "region": "Bavaria", "salary": 72000, "cost": 100 },
      { "city": "Frankfurt", "region": "Hesse", "salary": 68000, "cost": 95 },
      { "city": "Stuttgart", "region": "Baden-W.", "salary": 66000, "cost": 88 },
      { "city": "Hamburg", "region": "Hamburg", "salary": 65000, "cost": 88 },
      { "city": "Düsseldorf", "region": "NRW", "salary": 60000, "cost": 82 },
      { "city": "Berlin", "region": "Berlin", "salary": 60000, "cost": 80 },
      { "city": "Cologne", "region": "NRW", "salary": 58000, "cost": 78 }
    ],
    "JP": [
      { "city": "Tokyo", "region": "Kanto", "salary": 68000, "cost": 100 },
      { "city": "Yokohama", "region": "Kanto", "salary": 62000, "cost": 90 },
      { "city": "Osaka", "region": "Kansai", "salary": 58000, "cost": 85 },
      { "city": "Kyoto", "region": "Kansai", "salary": 55000, "cost": 82 },
      { "city": "Nagoya", "region": "Chubu", "salary": 52000, "cost": 75 },
      { "city": "Fukuoka", "region": "Kyushu", "salary": 47000, "cost": 70 },
      { "city": "Sapporo", "region": "Hokkaido", "salary": 45000, "cost": 68 }
    ],
    "SG": [
      { "city": "Orchard", "region": "Central", "salary": 82000, "cost": 103 },
      { "city": "CBD / Marina", "region": "Central", "salary": 80000, "cost": 100 },
      { "city": "Tampines", "region": "East", "salary": 64000, "cost": 80 },
      { "city": "Jurong", "region": "West", "salary": 62000, "cost": 78 },
      { "city": "Woodlands", "region": "North", "salary": 60000, "cost": 72 }
    ],
    "TW": [
      { "city": "Taipei", "region": "Northern", "salary": 30000, "cost": 100 },
      { "city": "Hsinchu", "region": "Northern", "salary": 28000, "cost": 82 },
      { "city": "New Taipei", "region": "Northern", "salary": 27000, "cost": 88 },
      { "city": "Taichung", "region": "Central", "salary": 24000, "cost": 72 },
      { "city": "Kaohsiung", "region": "Southern", "salary": 23000, "cost": 68 },
      { "city": "Tainan", "region": "Southern", "salary": 22000, "cost": 65 },
      { "city": "Taitung", "region": "Eastern", "salary": 18000, "cost": 55 },
      { "city": "Hualien", "region": "Eastern", "salary": 17000, "cost": 52 }
    ],
    "CN": [
      { "city": "Shanghai", "region": "East", "salary": 30000, "cost": 105 },
      { "city": "Beijing", "region": "North", "salary": 28000, "cost": 100 },
      { "city": "Shenzhen", "region": "South", "salary": 28000, "cost": 98 },
      { "city": "Guangzhou", "region": "South", "salary": 24000, "cost": 85 },
      { "city": "Chengdu", "region": "Southwest", "salary": 18000, "cost": 65 },
      { "city": "Chongqing", "region": "Southwest", "salary": 17000, "cost": 60 },
      { "city": "Wuhan", "region": "Central", "salary": 16000, "cost": 58 },
      { "city": "Xi'an", "region": "Northwest", "salary": 14000, "cost": 52 }
    ]
  },
  "countryMeta": {
    "US": { "difficulty": 8, "restDays": 10, "hoursPerDay": 10.5, "splitShift": true, "bestLearnAge": "17–22", "bestEntryAge": "19–25", "cert": "ServSafe · CIA Degree Optional", "travel": "Low", "mobility": "High", "expression": "High" },
    "UK": { "difficulty": 8, "restDays": 15, "hoursPerDay": 10, "splitShift": true, "bestLearnAge": "16–21", "bestEntryAge": "18–24", "cert": "Level 2/3 Food Safety · NVQ", "travel": "Low", "mobility": "High", "expression": "High" },
    "AU": { "difficulty": 7, "restDays": 20, "hoursPerDay": 9.5, "splitShift": false, "bestLearnAge": "17–22", "bestEntryAge": "19–25", "cert": "SITXFSA006 · Certificate III Hospitality", "travel": "Low", "mobility": "High", "expression": "High" },
    "DE": { "difficulty": 7, "restDays": 25, "hoursPerDay": 9, "splitShift": false, "bestLearnAge": "16–20", "bestEntryAge": "18–23", "cert": "Ausbildung Koch (3 yrs IHK apprentice)", "travel": "Low", "mobility": "High", "expression": "Moderate" },
    "JP": { "difficulty": 9, "restDays": 8, "hoursPerDay": 11, "splitShift": true, "bestLearnAge": "18–23", "bestEntryAge": "20–26", "cert": "調理師免許 (National Cook License)", "travel": "Very Low", "mobility": "Extreme", "expression": "Moderate" },
    "SG": { "difficulty": 8, "restDays": 14, "hoursPerDay": 10.5, "splitShift": true, "bestLearnAge": "17–22", "bestEntryAge": "19–25", "cert": "WSQ Food Safety · ITE Pastry/Culinary", "travel": "Low", "mobility": "High", "expression": "High" },
    "TW": { "difficulty": 8, "restDays": 12, "hoursPerDay": 10, "splitShift": true, "bestLearnAge": "17–22", "bestEntryAge": "19–25", "cert": "廚師證照 Level 1–3 · 餐飲管理學位", "travel": "Low", "mobility": "High", "expression": "Moderate" },
    "CN": { "difficulty": 9, "restDays": 7, "hoursPerDay": 11.5, "splitShift": true, "bestLearnAge": "16–21", "bestEntryAge": "18–24", "cert": "中式烹飪師 (初/中/高級) · 廚師職業資格証", "travel": "Low", "mobility": "High", "expression": "High" }
  },
  "difficultyLabels": ["", "", "Very Easy", "Easy", "Below Avg", "Average", "Above Avg", "Hard", "Very Hard", "Brutal", "Extreme"],
  "insightCards": [
    { "id": "difficulty", "icon": "💪", "label": "Job Hardship", "valueKey": "difficulty", "valueTemplate": "{value}/10", "metaTemplate": "{difficultyLabel} · physically & mentally demanding", "colorMode": "gradient-bad" },
    { "id": "restDays", "icon": "🏖️", "label": "Annual Leave", "valueKey": "restDays", "valueTemplate": "{value} days", "metaTemplate": "{hoursPerDay}h avg work day · Split shifts {splitShiftLabel}", "colorMode": "gradient-good" },
    { "id": "bestLearnAge", "icon": "🎓", "label": "Best Learning Age", "valueKey": "bestLearnAge", "valueTemplate": "{value}", "metaTemplate": "Culinary school or apprenticeship entry window", "colorMode": "accent" },
    { "id": "bestEntryAge", "icon": "🚀", "label": "Best Entry Age", "valueKey": "bestEntryAge", "valueTemplate": "{value}", "metaTemplate": "Peak energy & fastest skill absorption period", "colorMode": "accent" },
    { "id": "travel", "icon": "✈️", "label": "Business Travel", "valueKey": "travel", "valueTemplate": "{value}", "metaTemplate": "Frequency of travel for events, sourcing, or multi-site management.", "colorMode": "accent" },
    { "id": "mobility", "icon": "🏃", "label": "Physical Mobility", "valueKey": "mobility", "valueTemplate": "{value}", "metaTemplate": "Level of constant movement, standing, and station transitions.", "colorMode": "accent" },
    { "id": "expression", "icon": "🗣️", "label": "Creative Self-Expression", "valueKey": "expression", "valueTemplate": "{value}", "metaTemplate": "Requirement to communicate vision, lead teams, and express creativity.", "colorMode": "accent" },
    { "id": "cert", "icon": "📜", "label": "Certifications Required", "valueKey": "cert", "valueTemplate": "{value}", "metaTemplate": "Varies by employer tier & establishment type", "spanFull": true, "colorMode": "neutral" }
  ],
  "extendedMeta": {
    "US": { "budget": "$450/mo", "hnwi": "Private Clubs · Resort Dining · Estate Chef Ladder", "startupReadiness": 68, "mbti": "ESTP · ISTJ · ENTJ", "uni": "Not required", "uniMeta": "Prestige helps less than Michelin-grade references.", "privateSchool": "Useful but debt-sensitive", "privateMeta": "Line experience still wins.", "schools": "CIA · Johnson & Wales · Kendall", "retire": "Corporate Dining Leadership, Instructor Roles, Private Chef.", "pivot": "Estate Chef, Kitchen Ops Consultant, Content/Demo Chef." },
    "UK": { "budget": "£260/mo", "hnwi": "Hotels · Members Clubs · Private Events", "startupReadiness": 54, "mbti": "ISTJ · ESTJ · ENTJ", "uni": "Optional", "uniMeta": "References and practical output dominate.", "privateSchool": "Helpful for placement", "privateMeta": "Apprenticeship kitchens carry more weight.", "schools": "Westminster Kingsway · Le Cordon Bleu London · UCB", "retire": "Hotel Training, F&B Management, Consultancy.", "pivot": "Members-Club Chef, Luxury Catering Lead, Compliance Trainer." },
    "AU": { "budget": "A$420/mo", "hnwi": "Resorts · Wine Regions · Premium Tourism", "startupReadiness": 72, "mbti": "ESTP · ENTJ · ISTJ", "uni": "Optional", "uniMeta": "TAFE and real kitchen output matter more.", "privateSchool": "Often practical", "privateMeta": "Live service volume is key.", "schools": "Le Cordon Bleu Melbourne · William Angliss · TAFE NSW", "retire": "Catering Operator, Venue Manager, Hospitality Trainer.", "pivot": "Private Dining Operator, Venue Consultant, Regional Trainer." },
    "DE": { "budget": "€220/mo", "hnwi": "Luxury Hotels · Old-money Dining · Cruise / Resort", "startupReadiness": 49, "mbti": "ISTJ · INTJ · ESTJ", "uni": "Usually not required", "uniMeta": "Formal training structure matters more.", "privateSchool": "Apprenticeship stronger", "privateMeta": "Apprenticeship route is more trusted.", "schools": "IHK tracks · Hotelfachschule Heidelberg · DHBW", "retire": "Training Kitchens, Hotel Operations, Procurement.", "pivot": "Food Safety Lead, Hotel Trainer, Procurement Specialist." },
    "JP": { "budget": "¥45,000/mo", "hnwi": "Omakase · Ryokan · Private Invitation Dining", "startupReadiness": 46, "mbti": "ISTJ · INTJ · ISFJ", "uni": "Not required", "uniMeta": "Lineage and master-apprentice credibility matter more.", "privateSchool": "Can help, lineage stronger", "privateMeta": "Hierarchy and apprenticeship quality remain stronger.", "schools": "Tsuji Culinary Institute · Hattori Nutrition College · Tokyo Seika", "retire": "Teaching, Quality Control, Supplier Advisory, Small-Format Dining.", "pivot": "Luxury Counter Chef, QA/Standards Lead, Craft Instructor." },
    "SG": { "budget": "S$420/mo", "hnwi": "Luxury Hotels · Expat Clients · Regional Events", "startupReadiness": 76, "mbti": "ENTJ · ESTJ · ESTP", "uni": "Useful but optional", "uniMeta": "Multilingual polish and operational discipline matter more.", "privateSchool": "Useful if placement-led", "privateMeta": "Brand-name hotel placement and language advantage.", "schools": "At-Sunrice · SHATEC · Temasek hospitality tracks", "retire": "Consulting, Regional Training, Private Dining.", "pivot": "Cloud-Kitchen Founder, Private Dining Operator, Regional Trainer." },
    "TW": { "budget": "NT$8,000/mo", "hnwi": "Private Banquets · Boutique Hospitality · Luxury Clubs", "startupReadiness": 57, "mbti": "ISTJ · ESTP · ENTJ", "uni": "Optional", "uniMeta": "Bilingual service quality and steady kitchen reputation.", "privateSchool": "Selective value", "privateMeta": "Consistent kitchen output remains strongest signal.", "schools": "國立高雄餐旅大學 · 景文科大餐飲系 · 實踐大學", "retire": "Banquet Operations, Culinary Teaching, Central Kitchen Roles.", "pivot": "Banquet Lead, Product Testing, Kitchen Standards Consultant." },
    "CN": { "budget": "¥1,800/mo", "hnwi": "Luxury Banquets · Private Rooms · Club Kitchens", "startupReadiness": 61, "mbti": "ISTJ · ESTP · ENTJ", "uni": "Not required", "uniMeta": "Apprenticeship pedigree and execution matter more.", "privateSchool": "Mixed value", "privateMeta": "Live kitchen references outrank tuition branding.", "schools": "Le Cordon Bleu Shanghai · SICA · Shanghai Business & Tourism", "retire": "Training Manager, Central Kitchen Leader, Private Chef.", "pivot": "Private Household Chef, SOP Consultant, Flavor/Product R&D." }
  },
  "startupLinks": {
    "US": [{ "label": "SBA Grants", "url": "https://www.sba.gov" }, { "label": "CloudKitchens", "url": "https://cloudkitchens.com" }],
    "UK": [{ "label": "Gov Business Support", "url": "https://www.gov.uk/business-finance-support" }, { "label": "Kitchen United", "url": "https://www.kitchenunited.com" }],
    "AU": [{ "label": "Business.gov.au", "url": "https://business.gov.au" }, { "label": "FoodStars", "url": "https://foodstars.com.au" }],
    "DE": [{ "label": "KfW Start-ups", "url": "https://www.kfw.de" }, { "label": "KitchenTown Berlin", "url": "https://www.kitchentown.de" }],
    "JP": [{ "label": "J-Net21", "url": "https://j-net21.smrj.go.jp" }, { "label": "Cloud Kitchen Japan", "url": "https://cloudkitchens.com/jp/" }],
    "SG": [{ "label": "Enterprise SG", "url": "https://www.enterprisesg.gov.sg" }, { "label": "Smart City Kitchens", "url": "https://smartcitykitchens.com" }],
    "TW": [{ "label": "SMEA Grants", "url": "https://www.smea.gov.tw" }, { "label": "Cloud Kitchen Taiwan", "url": "https://www.cloudkitchens.com.tw" }],
    "CN": [{ "label": "China Business Registry", "url": "http://www.gsxt.gov.cn" }, { "label": "Meituan Cloud Kitchen", "url": "https://kd.meituan.com" }]
  },
  "famousChefs": {
    "US": [{ "name": "Alan Wong", "netWorth": "$1.1B" }, { "name": "Wolfgang Puck", "netWorth": "$120M" }],
    "UK": [{ "name": "Gordon Ramsay", "netWorth": "$220M" }, { "name": "Jamie Oliver", "netWorth": "$200M" }],
    "AU": [{ "name": "Curtis Stone", "netWorth": "$25M" }, { "name": "Neil Perry", "netWorth": "$25M" }],
    "DE": [{ "name": "Tim Mälzer", "netWorth": "$10M" }, { "name": "Eckart Witzigmann", "netWorth": "$5M" }],
    "JP": [{ "name": "Nobu Matsuhisa", "netWorth": "$200M" }, { "name": "Masaharu Morimoto", "netWorth": "$18M" }],
    "SG": [{ "name": "Sam Leong", "netWorth": "$5M" }, { "name": "Janice Wong", "netWorth": "$3M" }],
    "TW": [{ "name": "André Chiang", "netWorth": "$10M" }, { "name": "Lanshu Chen", "netWorth": "$5M" }],
    "CN": [{ "name": "Da Dong", "netWorth": "$50M" }, { "name": "Wang Gang", "netWorth": "$2M" }]
  },
  "accessLinks": [
    { "title": "Training & Courses", "desc": "Online platforms and culinary schools." },
    { "title": "Certifications & Credentials", "desc": "Food safety, HACCP, Red Seal, and licensing." },
    { "title": "Job Search & Placement", "desc": "LinkedIn, Culinary Agents, hotel career pages." },
    { "title": "Freelance & Side Work", "desc": "Banquet staffing, private events, pop-ups." },
    { "title": "Your Portfolio & Referrals", "desc": "Link to your own portfolio and referral network." },
    { "title": "Find a Mentor", "desc": "Connect with a master chef or senior sifu." }
  ],
  "careerRecs": [
    [
      { "title": "Kitchen Quality Monitor", "match": "76%", "color": "var(--green)", "desc": "Inspect food prep standards and safety compliance.", "skills": ["Food Safety", "Temperature Control"] },
      { "title": "Catering Production Staff", "match": "71%", "color": "var(--yellow)", "desc": "Execute large-batch food production.", "skills": ["Station Management", "Speed"] },
      { "title": "Food Prep Trainer", "match": "65%", "color": "var(--orange)", "desc": "Onboard new kitchen staff.", "skills": ["Knife Skills", "Ingredient Handling"] }
    ],
    [
      { "title": "Recipe Testing Technician", "match": "83%", "color": "var(--green)", "desc": "Support R&D teams testing dishes.", "skills": ["Sensory Evaluation", "Mise en Place"] },
      { "title": "Catering Supervisor", "match": "78%", "color": "var(--yellow)", "desc": "Lead a team for events.", "skills": ["Team Coordination", "Quality Awareness"] },
      { "title": "Production Kitchen Lead", "match": "72%", "color": "var(--orange)", "desc": "Oversee batch production.", "skills": ["Station Leadership", "Time Management"] }
    ],
    [
      { "title": "Food Technologist (R&D)", "match": "88%", "color": "var(--green)", "desc": "Sensory evaluation and recipe scaling.", "skills": ["Recipe Development", "Quality Control"] },
      { "title": "Event Operations Manager", "match": "82%", "color": "var(--yellow)", "desc": "High-pressure coordination.", "skills": ["Staff Supervision", "Cost Management"] },
      { "title": "F&B Procurement Analyst", "match": "76%", "color": "var(--orange)", "desc": "Ingredient quality and yield management.", "skills": ["Inventory Control", "Supplier Knowledge"] }
    ],
    [
      { "title": "F&B Operations Manager", "match": "90%", "color": "var(--green)", "desc": "Oversee multi-venue operations.", "skills": ["Budget Control", "Team Management"] },
      { "title": "Event Operations Manager", "match": "85%", "color": "var(--yellow)", "desc": "Crisis management and event logistics.", "skills": ["Crisis Management", "Logistics"] },
      { "title": "F&B Procurement Specialist", "match": "80%", "color": "var(--orange)", "desc": "Supplier and ingredient quality.", "skills": ["Supply Chain", "Negotiation"] }
    ],
    [
      { "title": "F&B Director", "match": "93%", "color": "var(--green)", "desc": "Lead entire F&B strategy.", "skills": ["Strategic Planning", "Brand Building"] },
      { "title": "Food Innovation Consultant", "match": "88%", "color": "var(--yellow)", "desc": "Advise on menu trends and innovation.", "skills": ["Culinary Expertise", "Market Analysis"] },
      { "title": "Culinary Program Director", "match": "82%", "color": "var(--orange)", "desc": "Lead culinary school or training.", "skills": ["Training Design", "Leadership"] }
    ]
  ],
  "survivalStrategy": [
    "As a <strong>Line Cook</strong>, master speed, knife precision, and food safety — skills no robot fully replicates at your pace.",
    "As a <strong>Chef de Partie</strong>, double down on station mastery and specialty depth.",
    "As a <strong>Sous Chef</strong>, recipe development and people management are your armor.",
    "As a <strong>Head Chef</strong>, focus on menu creation, brand identity, and team culture.",
    "As an <strong>Executive Chef</strong>, leverage brand, vision, and business relationships."
  ],
  "hazards": [
    { "icon": "🔥", "name": "Burns & Scalds", "levelClass": "haz-5", "width": "100%", "desc": "Critical · open flame" },
    { "icon": "🌡️", "name": "Heat Exhaustion", "levelClass": "haz-5", "width": "100%", "desc": "Critical · 38–50°C kitchens" },
    { "icon": "🔪", "name": "Cuts & Lacerations", "levelClass": "haz-4", "width": "80%", "desc": "High · daily knife work" },
    { "icon": "💪", "name": "Musculoskeletal Strain", "levelClass": "haz-4", "width": "80%", "desc": "High · 8–12 hrs standing" },
    { "icon": "🧠", "name": "Mental Fatigue", "levelClass": "haz-4", "width": "75%", "desc": "High · burnout 40–60%" },
    { "icon": "🚿", "name": "Slip & Fall", "levelClass": "haz-3", "width": "55%", "desc": "Medium · wet floors" },
    { "icon": "⚗️", "name": "Chemical Exposure", "levelClass": "haz-3", "width": "50%", "desc": "Medium · cleaning agents" },
    { "icon": "👂", "name": "Noise Exposure", "levelClass": "haz-2", "width": "35%", "desc": "Low-Med · fans" },
    { "icon": "🫁", "name": "Smoke & Fumes", "levelClass": "haz-3", "width": "45%", "desc": "Medium · ventilation" }
  ],
  "filters": [
    { "id": "all", "label": "All", "class": "all", "active": true, "dot": false },
    { "id": "replaceable", "label": "Replaceable", "class": "gf", "active": false, "dot": true },
    { "id": "indanger", "label": "In-Danger", "class": "yf", "active": false, "dot": true },
    { "id": "intro", "label": "Intro", "class": "of", "active": false, "dot": true },
    { "id": "nothing", "label": "Nothing", "class": "rf", "active": false, "dot": true }
  ],
  "mbtiData": [
    { "type": "ESTP", "desc": "The Dynamo. Thrives in fast-paced, high-pressure environments." },
    { "type": "ENTJ", "desc": "The Commander. Natural leaders who manage complex brigades." },
    { "type": "ISFP", "desc": "The Artist. Passionate about culinary aesthetics." },
    { "type": "ESFJ", "desc": "The Provider. Fosters collaborative kitchen culture." },
    { "type": "INTJ", "desc": "The Architect. Strategic kitchen optimization thinkers." }
  ],
  "filialPietyCountries": ["CN", "TW", "SG", "JP"],
  "ltvMethodology": "BLS 2025 median salary × 30-year career horizon. AI Risk weighted.",
  "highestThreat": "Inventory & Ordering is the most vulnerable node.",
  "langPillClasses": {
    "Essential": "llp-essential",
    "Helpful": "llp-helpful",
    "Optional": "llp-optional",
    "Senior Only": "llp-senior",
    "High-end Only": "llp-senior",
    "Regional": "llp-helpful"
  },
  "networkCards": [
    { "title": "Recommended Majors", "value": "Culinary Arts & Hospitality Mgt", "meta": "Secondary: Food Science, Nutrition, or Business Administration." },
    { "title": "Target Courses", "value": "Kitchen Ops & Cost Control", "meta": "Also: Molecular Gastronomy, Sustainable Sourcing, Staff Leadership." },
    { "title": "Stretch Majors", "value": "F&B Tech & Innovation", "meta": "Transition into tech-enabled food systems." },
    { "title": "Key Connections", "value": "Michelin Execs & F&B Directors", "meta": "Build relationships with top-tier culinary executives.", "loginCTA": true }
  ],
  "version": "v2.4 · Apr 2026",
  "footnote": "* Data: Miso Robotics · BLS 2025 · JobForesight 2026 · ILO benchmarks"
}
```

[chef.html]
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cook Lifecycle – Chef</title>
    <link href="https://api.fontshare.com/v2/css?f[]=satoshi@400,500,700,900&f[]=cabinet-grotesk@800&display=swap" rel="stylesheet">
    <style>
        *,
        *::before,
        *::after {
            box-sizing: border-box;
            margin: 0;
            padding: 0
        }
        :root {
            --bg: #0e0e0e;
            --surface: #161616;
            --surface-2: #1c1c1c;
            --surface-3: #222;
            --border: #2a2a2a;
            --border-hi: #363636;
            --text: #e2e2e2;
            --text-muted: #aaa;
            --text-faint: #666;
            --green: #22c55e;
            --yellow: #eab308;
            --orange: #f97316;
            --red: #ef4444;
            --accent: #4f98a3;
            --accent-hover: #60b8c4;
            --font-body: 'Satoshi', 'Inter', sans-serif;
            --font-display: 'Cabinet Grotesk', 'Satoshi', sans-serif;
            --ease: cubic-bezier(0.16, 1, 0.3, 1);
            --radius-sm: 4px;
            --radius-md: 8px;
            --radius-lg: 12px;
            --human-cost: #f97316;
            --ai-cost: #22c55e;
        }
        html {
            -webkit-font-smoothing: antialiased;
            scroll-behavior: smooth
        }
        body {
            background: var(--bg);
            color: var(--text);
            font-family: var(--font-body);
            font-size: 16px;
            line-height: 1.6;
            min-height: 100dvh
        }
        button {
            cursor: pointer;
            border: none;
            background: none;
            font: inherit
        }
        body::before {
            content: '';
            position: fixed;
            inset: 0;
            background: repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(0, 0, 0, .05) 2px, rgba(0, 0, 0, .05) 4px);
            pointer-events: none;
            z-index: 0
        }
        .page {
            position: relative;
            z-index: 1;
            max-width: 1200px;
            margin: 0 auto;
            padding: 36px 24px 80px
        }
        @media(max-width:768px) {
            .page {
                padding: 20px 14px 60px
            }
        }
        .industry-row {
            display: flex;
            align-items: center;
            gap: 8px;
            flex-wrap: wrap;
            margin-bottom: 14px
        }
        .industry-pill {
            display: inline-flex;
            align-items: center;
            gap: 5px;
            padding: 4px 11px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 600;
            letter-spacing: .04em;
            border: 1px solid var(--border-hi);
            color: var(--text-faint);
            cursor: pointer;
            transition: all .18s var(--ease);
            white-space: nowrap
        }
        .industry-pill:hover {
            color: var(--text-muted);
            border-color: var(--text-faint)
        }
        .industry-pill.active {
            color: #fff;
            border-color: transparent;
            background: var(--surface-3)
        }
        .industry-pill .ind-dot {
            width: 5px;
            height: 5px;
            border-radius: 50%;
            background: currentColor;
            flex-shrink: 0;
            opacity: .7
        }
        .header {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            gap: 16px;
            margin-bottom: 28px;
        }
        .header-top-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
            width: 100%;
            gap: 16px;
            flex-wrap: wrap;
        }
        @media(max-width:600px) {
            .header-top-row {
                justify-content: flex-start;
            }
        }
        .header-tag {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            font-size: 12px;
            font-weight: 700;
            letter-spacing: .12em;
            text-transform: uppercase;
            color: var(--accent);
            background: color-mix(in oklch, var(--accent) 12%, transparent);
            border: 1px solid color-mix(in oklch, var(--accent) 30%, transparent);
            padding: 4px 10px;
            border-radius: 4px;
            margin-bottom: 10px
        }
        .header-tag .live-dot {
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background: var(--accent);
            animation: pulse 2s ease-in-out infinite
        }
        @keyframes pulse {
            0%,
            100% {
                opacity: 1
            }
            50% {
                opacity: .35
            }
        }
        .page-title {
            font-family: var(--font-display);
            font-size: clamp(22px, 4vw, 32px);
            font-weight: 800;
            color: #fff;
            line-height: 1.1;
            letter-spacing: -.01em;
        }
        .page-subtitle {
            font-size: 13px;
            color: var(--text-muted)
        }
        .page-subtitle span {
            color: var(--accent);
            font-size: 12px;
            font-family: monospace
        }
        .header-right {
            display: flex;
            align-items: center;
            gap: 10px;
            flex-shrink: 0;
            flex-wrap: wrap;
        }
        .btn-subscribe {
            display: inline-flex;
            align-items: center;
            gap: 7px;
            padding: 9px 18px;
            border-radius: var(--radius-md);
            font-size: 14px;
            font-weight: 700;
            letter-spacing: .02em;
            background: var(--accent);
            color: #fff;
            transition: background .18s var(--ease), transform .15s, box-shadow .18s var(--ease)
        }
        .btn-subscribe:hover {
            background: var(--accent-hover);
            transform: translateY(-1px);
            box-shadow: 0 6px 24px color-mix(in oklch, var(--accent) 35%, transparent)
        }
        .btn-subscribe svg {
            width: 14px;
            height: 14px
        }
        .country-section {
            margin-bottom: 20px
        }
        .country-label {
            font-size: 12px;
            font-weight: 700;
            letter-spacing: .1em;
            text-transform: uppercase;
            color: var(--text-faint);
            margin-bottom: 10px
        }
        .country-tabs {
            display: flex;
            gap: 6px;
            flex-wrap: wrap
        }
        .ctab {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 7px 13px;
            border-radius: var(--radius-md);
            border: 1px solid var(--border-hi);
            font-size: 13px;
            font-weight: 600;
            color: var(--text-muted);
            cursor: pointer;
            transition: all .18s var(--ease);
            white-space: nowrap;
            position: relative
        }
        .ctab:hover {
            border-color: var(--text-faint);
            color: var(--text)
        }
        .ctab.active {
            background: var(--surface-2);
            border-color: var(--accent);
            color: #fff
        }
        .ctab.active::after {
            content: '';
            position: absolute;
            bottom: -7px;
            left: 50%;
            transform: translateX(-50%);
            width: 4px;
            height: 4px;
            border-radius: 50%;
            background: var(--accent)
        }
        .ctab .flag {
            font-size: 14px;
            line-height: 1
        }
        .ctab .cname {
            font-size: 12px
        }
        .ctab .crisk {
            font-size: 12px;
            padding: 1px 5px;
            border-radius: 3px;
            font-weight: 700;
            margin-left: 2px
        }
        .crisk.fast {
            background: color-mix(in oklch, var(--red) 18%, transparent);
            color: var(--red);
            border: 1px solid color-mix(in oklch, var(--red) 30%, transparent)
        }
        .crisk.mid {
            background: color-mix(in oklch, var(--yellow) 14%, transparent);
            color: var(--yellow);
            border: 1px solid color-mix(in oklch, var(--yellow) 25%, transparent)
        }
        .crisk.slow {
            background: color-mix(in oklch, var(--green) 14%, transparent);
            color: var(--green);
            border: 1px solid color-mix(in oklch, var(--green) 25%, transparent)
        }
        .ltv-section {
            margin-bottom: 12px
        }
        .section-label {
            font-size: 12px;
            font-weight: 700;
            letter-spacing: .12em;
            text-transform: uppercase;
            color: var(--text-faint);
            margin-bottom: 14px
        }
        .ltv-grid {
            display: grid;
            grid-template-columns: repeat(5, 1fr);
            gap: 10px;
            margin-bottom: 12px
        }
        @media(max-width:1000px) {
            .ltv-grid {
                grid-template-columns: repeat(3, 1fr)
            }
        }
        @media(max-width:600px) {
            .ltv-grid {
                grid-template-columns: repeat(2, 1fr)
            }
        }
        .ltv-card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            padding: 16px 18px 14px;
            position: relative;
            overflow: hidden;
            transition: border-color .2s, box-shadow .2s var(--ease)
        }
        .ltv-card:hover {
            border-color: var(--border-hi);
            box-shadow: 0 8px 28px rgba(0, 0, 0, .35)
        }
        .ltv-card::after {
            content: '';
            position: absolute;
            inset: 0;
            background: radial-gradient(circle at 50% 0%, var(--glow, transparent) 0%, transparent 70%);
            pointer-events: none;
            opacity: .5
        }
        .ltv-card.c-total {
            --glow: color-mix(in oklch, var(--accent) 15%, transparent)
        }
        .ltv-card.c-safe {
            --glow: color-mix(in oklch, var(--green) 12%, transparent)
        }
        .ltv-card.c-risk {
            --glow: color-mix(in oklch, var(--red) 12%, transparent)
        }
        .ltv-card.c-idx {
            --glow: color-mix(in oklch, var(--yellow) 12%, transparent)
        }
        .ltv-card.c-age {
            --glow: color-mix(in oklch, var(--orange) 12%, transparent)
        }
        .ltv-lbl {
            font-size: 12px;
            font-weight: 700;
            letter-spacing: .08em;
            text-transform: uppercase;
            color: var(--text-muted);
            margin-bottom: 8px
        }
        .ltv-val {
            font-family: var(--font-display);
            font-size: clamp(20px, 2.5vw, 28px);
            font-weight: 800;
            letter-spacing: -.02em;
            line-height: 1;
            margin-bottom: 4px
        }
        .cl-total {
            color: #fff
        }
        .cl-safe {
            color: var(--green)
        }
        .cl-risk {
            color: var(--red)
        }
        .cl-idx {
            color: var(--yellow)
        }
        .cl-age {
            color: var(--orange)
        }
        .ltv-meta {
            font-size: 12px;
            color: var(--text-muted);
            line-height: 1.4
        }
        .ltv-bar {
            height: 3px;
            background: var(--border);
            border-radius: 2px;
            margin-top: 10px;
            overflow: hidden
        }
        .ltv-bar-fill {
            height: 100%;
            border-radius: 2px;
            transition: width 1.4s var(--ease)
        }
        .age-timeline {
            display: flex;
            align-items: center;
            gap: 6px;
            margin-top: 8px
        }
        .age-seg {
            height: 4px;
            border-radius: 2px;
            transition: width .8s var(--ease)
        }
        .age-seg.safe-seg {
            background: var(--green);
            flex: 1
        }
        .age-seg.risk-seg {
            background: var(--orange);
            flex-shrink: 0
        }
        .age-pins {
            display: flex;
            justify-content: space-between;
            margin-top: 3px
        }
        .age-pin {
            font-size: 11px;
            color: var(--text-muted)
        }
        .age-pin.risk-pin {
            color: var(--orange);
            font-weight: 700
        }
        .ltv-chart-wrap {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            padding: 18px 22px;
            margin-bottom: 12px
        }
        .car-viz {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            padding: 20px 22px;
            margin-bottom: 12px;
        }
        .car-viz-header {
            display: flex;
            align-items: baseline;
            gap: 10px;
            margin-bottom: 4px;
            flex-wrap: wrap
        }
        .car-viz-eq {
            font-size: 12px;
            font-weight: 700;
            letter-spacing: .1em;
            text-transform: uppercase;
            color: var(--text-faint)
        }
        .car-viz-val {
            font-family: var(--font-display);
            font-size: clamp(18px, 3vw, 26px);
            font-weight: 800;
            color: #fff;
            transition: all .3s var(--ease)
        }
        .car-viz-val span {
            color: var(--accent)
        }
        .car-viz-sub {
            font-size: 12px;
            color: var(--text-faint);
            margin-bottom: 16px
        }
        .car-grid {
            display: flex;
            flex-wrap: wrap;
            gap: 5px;
            margin-bottom: 10px;
            min-height: 60px
        }
        .car-icon {
            width: 38px;
            height: 22px;
            flex-shrink: 0;
            transition: opacity .3s var(--ease), transform .3s var(--ease)
        }
        .car-icon.safe-car {
            color: var(--green);
            opacity: .85
        }
        .car-icon.risk-car {
            color: var(--red);
            opacity: .55
        }
        .car-legend {
            display: flex;
            gap: 16px;
            flex-wrap: wrap
        }
        .car-legend-item {
            display: flex;
            align-items: center;
            gap: 6px;
            font-size: 12px;
            color: var(--text-muted)
        }
        .car-legend-swatch {
            width: 24px;
            height: 10px;
            border-radius: 2px
        }
        .car-legend-swatch.safe {
            background: color-mix(in oklch, var(--green) 35%, transparent);
            border: 1px solid var(--green)
        }
        .car-legend-swatch.risk {
            background: color-mix(in oklch, var(--red) 25%, transparent);
            border: 1px solid var(--red)
        }
        .filters-row {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
            margin-bottom: 14px;
            flex-wrap: wrap
        }
        .filters-left {
            display: flex;
            align-items: center;
            gap: 7px;
            flex-wrap: wrap
        }
        .filter-pill {
            display: inline-flex;
            align-items: center;
            gap: 5px;
            padding: 5px 11px;
            border-radius: 4px;
            border: 1px solid var(--border-hi);
            font-size: 12px;
            font-weight: 600;
            letter-spacing: .04em;
            color: var(--text-muted);
            cursor: pointer;
            transition: all .15s var(--ease)
        }
        .filter-pill.active,
        .filter-pill:hover {
            color: #fff;
            border-color: transparent
        }
        .filter-pill.all.active {
            background: #fff2;
            color: #fff
        }
        .filter-pill.gf.active {
            background: color-mix(in oklch, var(--red) 22%, transparent);
            border-color: var(--red);
            color: var(--red)
        }
        .filter-pill.yf.active {
            background: color-mix(in oklch, var(--orange) 18%, transparent);
            border-color: var(--orange);
            color: var(--orange)
        }
        .filter-pill.of.active {
            background: color-mix(in oklch, var(--yellow) 18%, transparent);
            border-color: var(--yellow);
            color: var(--yellow)
        }
        .filter-pill.rf.active {
            background: color-mix(in oklch, var(--green) 16%, transparent);
            border-color: var(--green);
            color: var(--green)
        }
        .filter-pill .dot {
            width: 5px;
            height: 5px;
            border-radius: 50%;
            background: currentColor
        }
        .table-wrap {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            overflow: hidden
        }
        .table-scroll {
            overflow-x: auto
        }
        table {
            width: 100%;
            border-collapse: collapse;
            min-width: 780px
        }
        thead {
            background: var(--surface-2)
        }
        th {
            padding: 11px 12px;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: .08em;
            text-transform: uppercase;
            color: var(--text-faint);
            border-bottom: 1px solid var(--border);
            white-space: nowrap
        }
        th:not(:last-child) {
            border-right: 1px solid var(--border)
        }
        td {
            padding: 11px 12px;
            border-bottom: 1px solid var(--border);
            vertical-align: middle
        }
        td:not(:last-child) {
            border-right: 1px solid var(--border)
        }
        tr:last-child td {
            border-bottom: none
        }
        tbody tr {
            transition: background .15s var(--ease)
        }
        tbody tr:hover {
            background: var(--surface-2)
        }
        tbody tr.hidden-row {
            display: none
        }
        .col-action {
            font-weight: 600;
            font-size: 14px;
            color: #fff;
            white-space: nowrap
        }
        .col-action .time-pct {
            display: block;
            font-size: 11px;
            font-weight: 500;
            color: var(--text-faint);
            letter-spacing: .03em;
            margin-top: 3px;
            white-space: nowrap
        }
        .col-action .time-pct strong {
            color: var(--text-muted);
            font-weight: 700
        }
        .col-human,
        .col-ai {
            font-size: 13px;
            max-width: 200px
        }
        .col-human {
            color: var(--text)
        }
        .col-ai {
            color: #9ecde8
        }
        .bar-wrap {
            display: flex;
            flex-direction: column;
            gap: 4px;
            min-width: 100px
        }
        .bar-track {
            width: 100%;
            background: var(--border);
            border-radius: 2px;
            height: 5px;
            overflow: hidden
        }
        .bar-fill {
            height: 100%;
            border-radius: 2px;
            transition: width 1.2s var(--ease)
        }
        .bar-lbl {
            font-size: 12px;
            color: var(--text);
            display: flex;
            justify-content: space-between
        }
        .bar-lbl span:last-child {
            font-weight: 700;
            color: var(--text)
        }
        .cost-ratio-wrap {
            display: flex;
            flex-direction: column;
            gap: 4px;
            min-width: 110px
        }
        .cost-ratio-bar {
            display: flex;
            height: 8px;
            border-radius: 4px;
            overflow: hidden;
            background: var(--border)
        }
        .cost-ratio-human {
            background: var(--human-cost);
            transition: flex .6s var(--ease);
            opacity: .8
        }
        .cost-ratio-ai {
            background: var(--ai-cost);
            transition: flex .6s var(--ease);
            opacity: .8
        }
        .cost-ratio-lbl {
            font-size: 11px;
            color: var(--text-muted);
            display: flex;
            justify-content: space-between;
            gap: 4px
        }
        .cost-ratio-lbl .cr-human {
            color: var(--human-cost);
            font-weight: 700
        }
        .cost-ratio-lbl .cr-ai {
            color: var(--ai-cost);
            font-weight: 700
        }
        .cost-ratio-lbl .cr-sep {
            color: var(--text-faint)
        }
        .eta-badge {
            font-size: 12px;
            color: var(--text-muted);
            white-space: nowrap
        }
        .eta-soon {
            color: var(--red)
        }
        .eta-mid {
            color: var(--orange)
        }
        .eta-far {
            color: var(--yellow)
        }
        .eta-prot {
            color: var(--green)
        }
        .status-badge {
            display: inline-flex;
            align-items: center;
            gap: 4px;
            padding: 3px 9px;
            border-radius: 3px;
            font-size: 11px;
            font-weight: 700;
            letter-spacing: .06em;
            text-transform: uppercase;
            white-space: nowrap
        }
        .status-badge .dot {
            width: 5px;
            height: 5px;
            border-radius: 50%;
            background: currentColor;
            flex-shrink: 0
        }
        .b-replaceable {
            background: color-mix(in oklch, var(--red) 16%, transparent);
            color: var(--red);
            border: 1px solid color-mix(in oklch, var(--red) 30%, transparent)
        }
        .b-indanger {
            background: color-mix(in oklch, var(--orange) 13%, transparent);
            color: var(--orange);
            border: 1px solid color-mix(in oklch, var(--orange) 25%, transparent)
        }
        .b-intro {
            background: color-mix(in oklch, var(--yellow) 14%, transparent);
            color: var(--yellow);
            border: 1px solid color-mix(in oklch, var(--yellow) 28%, transparent)
        }
        .b-none {
            background: color-mix(in oklch, var(--green) 13%, transparent);
            color: var(--green);
            border: 1px solid color-mix(in oklch, var(--green) 25%, transparent)
        }
        .summary-row {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
            margin-top: 12px
        }
        @media(max-width:640px) {
            .summary-row {
                grid-template-columns: 1fr
            }
        }
        .summary-card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 14px 16px;
            font-size: 13px;
            color: var(--text-muted)
        }
        .summary-card strong {
            color: var(--text);
            display: block;
            font-size: 14px;
            font-weight: 700;
            margin-bottom: 3px
        }
        .footnote {
            margin-top: 12px;
            font-size: 12px;
            color: var(--text-faint);
            text-align: right
        }
        .time-sum-badge {
            display: inline-flex;
            align-items: center;
            gap: 4px;
            font-size: 11px;
            color: var(--text-faint);
            margin-top: 2px;
            letter-spacing: .04em
        }
        .time-sum-badge .ts-check {
            color: var(--green);
            font-weight: 700
        }
        .modal-overlay {
            position: fixed;
            inset: 0;
            background: rgba(0, 0, 0, .75);
            backdrop-filter: blur(6px);
            z-index: 100;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
            opacity: 0;
            pointer-events: none;
            transition: opacity .25s var(--ease)
        }
        .modal-overlay.open {
            opacity: 1;
            pointer-events: all
        }
        .modal {
            background: var(--surface-2);
            border: 1px solid var(--border-hi);
            border-radius: var(--radius-lg);
            padding: 30px;
            max-width: 420px;
            width: 100%;
            transform: translateY(14px) scale(.97);
            transition: transform .28s var(--ease);
            position: relative
        }
        .modal-overlay.open .modal {
            transform: none
        }
        .modal-close {
            position: absolute;
            top: 12px;
            right: 12px;
            width: 28px;
            height: 28px;
            border-radius: 4px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--text-muted);
            transition: background .15s, color .15s
        }
        .modal-close:hover {
            background: var(--border);
            color: var(--text)
        }
        .modal-icon {
            width: 42px;
            height: 42px;
            background: color-mix(in oklch, var(--accent) 16%, transparent);
            border: 1px solid color-mix(in oklch, var(--accent) 32%, transparent);
            border-radius: var(--radius-md);
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--accent);
            margin-bottom: 14px
        }
        .modal-title {
            font-family: var(--font-display);
            font-size: 19px;
            font-weight: 800;
            color: #fff;
            margin-bottom: 5px;
            letter-spacing: -.01em
        }
        .modal-desc {
            font-size: 13px;
            color: var(--text-muted);
            margin-bottom: 22px;
            line-height: 1.6
        }
        .modal-desc strong {
            color: var(--text)
        }
        .input-group {
            display: flex;
            gap: 7px;
            margin-bottom: 12px
        }
        .modal-input {
            flex: 1;
            background: var(--surface);
            border: 1px solid var(--border-hi);
            border-radius: var(--radius-md);
            padding: 9px 13px;
            color: var(--text);
            font: inherit;
            font-size: 14px;
            outline: none;
            transition: border-color .18s
        }
        .modal-input::placeholder {
            color: var(--text-faint)
        }
        .modal-input:focus {
            border-color: var(--accent)
        }
        .btn-confirm {
            display: inline-flex;
            align-items: center;
            gap: 5px;
            padding: 9px 16px;
            border-radius: var(--radius-md);
            background: var(--accent);
            color: #fff;
            font: inherit;
            font-size: 14px;
            font-weight: 700;
            cursor: pointer;
            border: none;
            white-space: nowrap;
            transition: background .18s var(--ease), transform .15s
        }
        .btn-confirm:hover {
            background: var(--accent-hover);
            transform: translateY(-1px)
        }
        .modal-tags {
            display: flex;
            gap: 6px;
            flex-wrap: wrap;
            margin-top: 4px
        }
        .modal-tag {
            display: inline-flex;
            align-items: center;
            gap: 4px;
            padding: 5px 9px;
            border: 1px solid var(--border-hi);
            border-radius: 4px;
            font-size: 12px;
            color: var(--text-muted);
            cursor: pointer;
            transition: all .15s
        }
        .modal-tag:hover,
        .modal-tag.sel {
            border-color: var(--accent);
            color: var(--accent);
            background: color-mix(in oklch, var(--accent) 10%, transparent)
        }
        .modal-success {
            text-align: center;
            padding: 14px 0;
            display: none
        }
        .modal-success .check {
            width: 48px;
            height: 48px;
            border-radius: 50%;
            background: color-mix(in oklch, var(--green) 16%, transparent);
            border: 1px solid var(--green);
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--green);
            margin: 0 auto 12px;
            font-size: 22px
        }
        .modal-success h3 {
            color: #fff;
            font-size: 16px;
            font-weight: 700;
            margin-bottom: 5px
        }
        .modal-success p {
            font-size: 13px;
            color: var(--text-muted)
        }
        .toast {
            position: fixed;
            bottom: 22px;
            right: 22px;
            background: var(--surface-2);
            border: 1px solid var(--border-hi);
            border-radius: var(--radius-md);
            padding: 11px 15px;
            font-size: 13px;
            color: var(--text);
            display: flex;
            align-items: center;
            gap: 9px;
            z-index: 200;
            box-shadow: 0 8px 32px rgba(0, 0, 0, .5);
            transform: translateY(18px);
            opacity: 0;
            transition: all .28s var(--ease)
        }
        .toast.show {
            transform: none;
            opacity: 1
        }
        .toast-dot {
            width: 7px;
            height: 7px;
            border-radius: 50%;
            background: var(--green);
            flex-shrink: 0;
            animation: pulse 2s infinite
        }
        .ltv-fade {
            animation: fadeIn .4s var(--ease)
        }
        @keyframes fadeIn {
            from {
                opacity: .2;
                transform: translateY(4px)
            }
            to {
                opacity: 1;
                transform: none
            }
        }
        .level-section {
            margin-bottom: 20px
        }
        .level-tabs {
            display: flex;
            align-items: center;
            gap: 0;
            flex-wrap: wrap
        }
        .ltab {
            position: relative;
            display: inline-flex;
            flex-direction: column;
            align-items: center;
            gap: 3px;
            padding: 9px 16px;
            border: 1px solid var(--border-hi);
            font-size: 13px;
            font-weight: 700;
            color: var(--text-muted);
            cursor: pointer;
            transition: all .18s var(--ease);
            background: var(--surface);
            white-space: nowrap;
            margin-right: -1px
        }
        .ltab:first-child {
            border-radius: var(--radius-md) 0 0 var(--radius-md)
        }
        .ltab:last-child {
            border-radius: 0 var(--radius-md) var(--radius-md) 0;
            margin-right: 0
        }
        .ltab:hover {
            color: var(--text);
            background: var(--surface-2);
            z-index: 1
        }
        .ltab.active {
            background: var(--surface-2);
            border-color: var(--accent);
            color: #fff;
            z-index: 2
        }
        .ltab .lyears {
            font-size: 11px;
            font-weight: 500;
            color: var(--text-faint);
            letter-spacing: .04em
        }
        .ltab.active .lyears {
            color: var(--accent)
        }
        .ltab .lpct {
            font-size: 11px;
            font-weight: 700;
            color: var(--accent);
            letter-spacing: .03em;
            background: color-mix(in oklch, var(--accent) 12%, transparent);
            border: 1px solid color-mix(in oklch, var(--accent) 25%, transparent);
            padding: 1px 5px;
            border-radius: 3px;
            margin-top: 1px
        }
        .ltab.active .lpct {
            background: color-mix(in oklch, var(--accent) 20%, transparent)
        }
        .ltab .lcolor-dot {
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background: var(--ldot, var(--text-faint));
            margin-bottom: 2px
        }
        .income-chart-wrap {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            padding: 20px 22px;
            margin-bottom: 12px
        }
        .income-chart-header {
            display: flex;
            align-items: baseline;
            justify-content: space-between;
            margin-bottom: 14px;
            flex-wrap: wrap;
            gap: 8px
        }
        .income-chart-title {
            font-size: 12px;
            font-weight: 700;
            letter-spacing: .1em;
            text-transform: uppercase;
            color: var(--text-faint)
        }
        .income-chart-note {
            font-size: 12px;
            color: var(--text-faint)
        }
        #incomeSVG {
            width: 100%;
            overflow: visible;
            display: block
        }
        .level-legend {
            display: flex;
            gap: 14px;
            flex-wrap: wrap;
            margin-top: 10px
        }
        .level-legend-item {
            display: flex;
            align-items: center;
            gap: 5px;
            font-size: 12px;
            color: var(--text)
        }
        .level-legend-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            flex-shrink: 0
        }
        .promo-section {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            padding: 18px 22px;
            margin-bottom: 12px
        }
        .promo-flow {
            display: flex;
            align-items: center;
            gap: 0;
            overflow-x: auto;
            padding: 4px 0
        }
        .promo-node {
            display: flex;
            flex-direction: column;
            align-items: center;
            min-width: 100px;
            gap: 5px
        }
        .promo-circle {
            width: 46px;
            height: 46px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 12px;
            font-weight: 800;
            letter-spacing: .02em;
            text-align: center;
            border: 2px solid;
            line-height: 1.2
        }
        .promo-label {
            font-size: 12px;
            font-weight: 600;
            color: var(--text-muted);
            text-align: center;
            max-width: 90px;
            line-height: 1.3
        }
        .promo-salary {
            font-size: 12px;
            color: var(--text-faint);
            text-align: center;
            font-weight: 700
        }
        .promo-arrow {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 2px;
            padding: 0 4px;
            min-width: 52px
        }
        .promo-arrow-line {
            width: 100%;
            height: 1px;
            background: var(--border-hi);
            position: relative
        }
        .promo-arrow-line::after {
            content: '▶';
            position: absolute;
            right: -5px;
            top: -5px;
            font-size: 12px;
            color: var(--text-faint)
        }
        .promo-arrow-years {
            font-size: 11px;
            color: var(--accent);
            font-weight: 700;
            white-space: nowrap;
            text-align: center
        }
        .promo-arrow-sub {
            font-size: 11px;
            color: var(--text-muted);
            white-space: nowrap
        }
        .insights-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
            margin-bottom: 12px
        }
        @media(max-width:768px) {
            .insights-grid {
                grid-template-columns: repeat(2, 1fr)
            }
        }
        @media(max-width:480px) {
            .insights-grid {
                grid-template-columns: 1fr
            }
        }
        .insight-card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            padding: 16px 18px;
            position: relative;
            overflow: hidden;
            transition: border-color .2s
        }
        .insight-card:hover {
            border-color: var(--border-hi)
        }
        .insight-icon {
            font-size: 22px;
            margin-bottom: 8px;
            display: block
        }
        .insight-label {
            font-size: 12px;
            font-weight: 700;
            letter-spacing: .08em;
            text-transform: uppercase;
            color: var(--text-muted);
            margin-bottom: 4px
        }
        .insight-value {
            font-family: var(--font-display);
            font-size: clamp(16px, 2vw, 22px);
            font-weight: 800;
            color: #fff;
            line-height: 1;
            margin-bottom: 4px
        }
        .insight-meta {
            font-size: 12px;
            color: var(--text-muted);
            line-height: 1.4
        }
        .difficulty-bar {
            display: flex;
            gap: 3px;
            margin-top: 8px
        }
        .diff-pip {
            width: 14px;
            height: 6px;
            border-radius: 2px;
            background: var(--border)
        }
        .diff-pip.filled-low {
            background: var(--green)
        }
        .diff-pip.filled-mid {
            background: var(--yellow)
        }
        .diff-pip.filled-high {
            background: var(--orange)
        }
        .diff-pip.filled-max {
            background: var(--red)
        }
        .hazards-section {
            margin-bottom: 12px
        }
        .hazards-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 8px
        }
        @media(max-width:600px) {
            .hazards-grid {
                grid-template-columns: repeat(2, 1fr)
            }
        }
        .hazard-card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            padding: 12px 14px;
            display: flex;
            align-items: center;
            gap: 10px
        }
        .hazard-icon {
            font-size: 20px;
            flex-shrink: 0
        }
        .hazard-info {
            flex: 1;
            min-width: 0
        }
        .hazard-name {
            font-size: 12px;
            font-weight: 700;
            color: var(--text);
            margin-bottom: 4px
        }
        .hazard-bar-track {
            width: 100%;
            height: 4px;
            background: var(--border);
            border-radius: 2px;
            overflow: hidden
        }
        .hazard-bar-fill {
            height: 100%;
            border-radius: 2px
        }
        .hazard-level {
            font-size: 11px;
            color: var(--text-muted);
            margin-top: 3px
        }
        .haz-1 {
            background: var(--green)
        }
        .haz-2 {
            background: color-mix(in oklch, var(--green) 60%, var(--yellow))
        }
        .haz-3 {
            background: var(--yellow)
        }
        .haz-4 {
            background: var(--orange)
        }
        .haz-5 {
            background: var(--red)
        }
        .lang-section {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            padding: 18px 22px;
            margin-bottom: 12px
        }
        .lang-list {
            display: flex;
            flex-direction: column;
            gap: 10px
        }
        .lang-row {
            display: flex;
            align-items: center;
            gap: 12px
        }
        .lang-name {
            font-size: 14px;
            font-weight: 700;
            color: #fff;
            min-width: 90px
        }
        .lang-level-pill {
            display: inline-flex;
            align-items: center;
            padding: 3px 9px;
            border-radius: 3px;
            font-size: 12px;
            font-weight: 700;
            letter-spacing: .05em;
            white-space: nowrap
        }
        .llp-essential {
            background: color-mix(in oklch, var(--red) 14%, transparent);
            color: var(--red);
            border: 1px solid color-mix(in oklch, var(--red) 28%, transparent)
        }
        .llp-helpful {
            background: color-mix(in oklch, var(--yellow) 12%, transparent);
            color: var(--yellow);
            border: 1px solid color-mix(in oklch, var(--yellow) 22%, transparent)
        }
        .llp-optional {
            background: color-mix(in oklch, var(--green) 12%, transparent);
            color: var(--green);
            border: 1px solid color-mix(in oklch, var(--green) 22%, transparent)
        }
        .llp-senior {
            background: color-mix(in oklch, var(--accent) 12%, transparent);
            color: var(--accent);
            border: 1px solid color-mix(in oklch, var(--accent) 22%, transparent)
        }
        .lang-bar-wrap {
            flex: 1;
            max-width: 180px
        }
        .lang-bar-track {
            width: 100%;
            height: 4px;
            background: var(--border);
            border-radius: 2px;
            overflow: hidden
        }
        .lang-bar-fill {
            height: 100%;
            border-radius: 2px;
            background: var(--accent)
        }
        .heatmap-section {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            padding: 18px 22px;
            margin-bottom: 12px
        }
        .heatmap-header {
            display: flex;
            align-items: baseline;
            justify-content: space-between;
            margin-bottom: 14px;
            flex-wrap: wrap;
            gap: 8px
        }
        .heatmap-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(130px, 1fr));
            gap: 8px
        }
        .city-card {
            border-radius: var(--radius-md);
            padding: 12px 14px;
            position: relative;
            overflow: hidden;
            cursor: default;
            transition: transform .15s var(--ease), box-shadow .15s
        }
        .city-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0, 0, 0, .4)
        }
        .city-name {
            font-size: 13px;
            font-weight: 700;
            color: #fff;
            margin-bottom: 2px
        }
        .city-region {
            font-size: 11px;
            color: rgba(255, 255, 255, .5);
            margin-bottom: 6px;
            text-transform: uppercase;
            letter-spacing: .06em
        }
        .city-salary {
            font-size: 14px;
            font-weight: 800;
            color: #fff;
            font-family: var(--font-display)
        }
        .city-cost {
            font-size: 11px;
            color: rgba(255, 255, 255, .55);
            margin-top: 2px
        }
        .heatmap-scale {
            display: flex;
            align-items: center;
            gap: 8px;
            margin-top: 10px;
            flex-wrap: wrap
        }
        .heatmap-scale-bar {
            display: flex;
            height: 6px;
            border-radius: 3px;
            overflow: hidden;
            flex: 1;
            max-width: 200px
        }
        .hs-low {
            background: var(--red);
            flex: 1
        }
        .hs-mid {
            background: var(--yellow);
            flex: 1
        }
        .hs-high {
            background: var(--green);
            flex: 1
        }
        .heatmap-scale-labels {
            display: flex;
            justify-content: space-between;
            width: 100%;
            max-width: 200px;
            font-size: 11px;
            color: var(--text-faint)
        }
        .extended-section {
            margin-bottom: 12px
        }
        .extended-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
            margin-bottom: 12px
        }
        @media(max-width:768px) {
            .extended-grid {
                grid-template-columns: repeat(2, 1fr)
            }
        }
        @media(max-width:480px) {
            .extended-grid {
                grid-template-columns: 1fr
            }
        }
        .link-grid-extended {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px
        }
        @media(max-width:900px) {
            .link-grid-extended {
                grid-template-columns: repeat(2, 1fr)
            }
        }
        @media(max-width:560px) {
            .link-grid-extended {
                grid-template-columns: 1fr
            }
        }
        .link-card,
        .note-card,
        .insight-card,
        .ltv-card,
        .summary-card,
        .ctab,
        .ltab,
        .filter-pill,
        .industry-pill,
        .modal-tag {
            transition: border-color 0.2s var(--ease), transform 0.2s var(--ease), box-shadow 0.2s var(--ease), background-color 0.2s var(--ease);
        }
        .link-card:hover,
        .note-card:hover,
        .insight-card:hover,
        .ltv-card:hover,
        .summary-card:hover,
        .ctab:hover,
        .ltab:hover,
        .filter-pill:hover:not(.active),
        .industry-pill:hover:not(.active),
        .modal-tag:hover:not(.sel) {
            border-color: var(--border-hi);
            transform: translateY(-2px);
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
        }
        .link-card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            padding: 14px 16px
        }
        .link-card-title {
            font-size: 13px;
            font-weight: 700;
            color: #fff;
            margin-bottom: 4px
        }
        .link-card-desc {
            font-size: 12px;
            color: var(--text-muted);
            line-height: 1.5
        }
        .note-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
            margin-bottom: 12px
        }
        @media(max-width:900px) {
            .note-grid {
                grid-template-columns: repeat(2, 1fr)
            }
        }
        @media(max-width:560px) {
            .note-grid {
                grid-template-columns: 1fr
            }
        }
        .note-card {
            background: var(--surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            padding: 16px 18px;
            position: relative;
            overflow: hidden
        }
        .note-title {
            font-size: 12px;
            font-weight: 700;
            letter-spacing: .08em;
            text-transform: uppercase;
            color: var(--text-muted);
            margin-bottom: 6px
        }
        .note-value {
            font-family: var(--font-display);
            font-size: 16px;
            font-weight: 800;
            color: #fff;
            line-height: 1.2;
            margin-bottom: 6px
        }
        .note-meta {
            font-size: 12px;
            color: var(--text-muted);
            line-height: 1.55
        }
        .sec-divider {
            height: 1px;
            background: var(--border);
            margin: 20px 0
        }
        .theme-toggle {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 8px 14px;
            border-radius: var(--radius-md);
            border: 1px solid var(--border-hi);
            background: var(--surface);
            color: var(--text-muted);
            font-size: 13px;
            font-weight: 700;
            cursor: pointer;
            transition: all .18s var(--ease);
            letter-spacing: .04em
        }
        .theme-toggle:hover {
            border-color: var(--accent);
            color: var(--text)
        }
        .theme-toggle .th-icon {
            font-size: 16px;
            line-height: 1
        }
        .btn-ghost {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 8px 14px;
            border-radius: var(--radius-md);
            border: 1px solid var(--border-hi);
            background: var(--surface);
            color: var(--text-muted);
            font-size: 13px;
            font-weight: 700;
            cursor: pointer;
            transition: all .18s var(--ease);
            letter-spacing: .04em
        }
        .btn-ghost:hover {
            border-color: var(--accent);
            color: var(--text)
        }
        .btn-login {
            display: inline-flex;
            align-items: center;
            gap: 7px;
            padding: 9px 18px;
            border-radius: var(--radius-md);
            font-size: 14px;
            font-weight: 700;
            letter-spacing: .02em;
            background: var(--surface-3);
            color: #fff;
            border: 1px solid var(--border-hi);
            transition: all .18s var(--ease);
            cursor: pointer
        }
        .btn-login:hover {
            background: var(--surface-2);
            border-color: var(--text-muted)
        }
        html[data-theme="light"] {
            --bg: #f4f4f5;
            --surface: #ffffff;
            --surface-2: #f0f0f0;
            --surface-3: #e8e8e8;
            --border: #e0e0e0;
            --border-hi: #cccccc;
            --text: #111111;
            --text-muted: #444444;
            --text-faint: #777777;
            --green: #16a34a;
            --yellow: #ca8a04;
            --orange: #ea580c;
            --red: #dc2626;
            --accent: #2a7b8a;
            --accent-hover: #1e6474;
            --human-cost: #ea580c;
            --ai-cost: #16a34a;
        }
        html[data-theme="light"] body {
            color: var(--text)
        }
        html[data-theme="light"] body::before {
            background: repeating-linear-gradient(0deg, transparent, transparent 2px, rgba(0, 0, 0, .02) 2px, rgba(0, 0, 0, .02) 4px)
        }
        html[data-theme="light"] .page-title {
            color: #111
        }
        html[data-theme="light"] .col-action {
            color: #111
        }
        html[data-theme="light"] thead {
            background: var(--surface-2)
        }
        html[data-theme="light"] .modal {
            background: var(--surface)
        }
        html[data-theme="light"] .modal-title {
            color: #111
        }
        html[data-theme="light"] .car-viz-val {
            color: #111
        }
        html[data-theme="light"] .insight-value {
            color: #111
        }
        html[data-theme="light"] .note-value {
            color: #111
        }
        html[data-theme="light"] .ltv-val.cl-total {
            color: #111
        }
        html[data-theme="light"] .city-name {
            color: #111
        }
        html[data-theme="light"] .city-salary {
            color: #111
        }
        html[data-theme="light"] .promo-label {
            color: var(--text-muted)
        }
        html[data-theme="light"] .table-wrap {
            background: var(--surface)
        }
        html[data-theme="light"] tbody tr:hover {
            background: var(--surface-2)
        }
        html[data-theme="light"] .summary-card strong {
            color: #111
        }
        html[data-theme="light"] .modal-input {
            background: var(--surface-2);
            color: #111
        }
        html[data-theme="light"] .lang-name {
            color: #111
        }
        .main-tabs-nav {
            display: flex;
            gap: 0;
            border-bottom: 1px solid var(--border);
            margin-bottom: 20px;
            margin-top: 4px;
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
            scrollbar-width: none;
        }
        .main-tabs-nav::-webkit-scrollbar {
            display: none;
        }
        .mtab {
            display: inline-flex;
            align-items: center;
            gap: 7px;
            padding: 10px 18px;
            font-size: 13px;
            font-weight: 700;
            color: var(--text-muted);
            border: none;
            background: none;
            cursor: pointer;
            white-space: nowrap;
            border-bottom: 2px solid transparent;
            margin-bottom: -1px;
            letter-spacing: .01em;
            transition: color .18s var(--ease), border-color .18s var(--ease);
            flex-shrink: 0;
        }
        .mtab:hover {
            color: var(--text);
        }
        .mtab.active {
            color: #fff;
            border-bottom-color: var(--accent);
        }
        .mtab .mtab-icon {
            font-size: 15px;
            line-height: 1;
        }
        .mtab .mtab-badge {
            font-size: 11px;
            font-weight: 700;
            padding: 1px 6px;
            border-radius: 99px;
            background: color-mix(in oklch, var(--accent) 18%, transparent);
            color: var(--accent);
            border: 1px solid color-mix(in oklch, var(--accent) 30%, transparent);
        }
        .tab-panel {
            display: none;
        }
        .tab-panel.active {
            display: block;
        }
        .home-country-pill {
            display: inline-flex;
            align-items: center;
            gap: 0;
            border: 1px solid color-mix(in oklch, var(--accent) 30%, transparent);
            background: color-mix(in oklch, var(--accent) 12%, transparent);
            border-radius: 6px;
            overflow: visible;
            position: relative;
            margin-bottom: 0;
        }
        .home-part {
            display: inline-flex;
            align-items: center;
            gap: 6px;
            font-size: 12px;
            font-weight: 700;
            letter-spacing: .12em;
            text-transform: uppercase;
            color: var(--accent);
            padding: 4px 10px;
            text-decoration: none;
            border-radius: 5px 0 0 5px;
            transition: background .15s;
            cursor: pointer;
        }
        .home-part:hover {
            background: color-mix(in oklch, var(--accent) 22%, transparent);
        }
        .home-part .live-dot {
            width: 6px;
            height: 6px;
            border-radius: 50%;
            background: var(--accent);
            animation: pulse 2s ease-in-out infinite;
            flex-shrink: 0;
        }
        .country-sep {
            width: 1px;
            height: 20px;
            background: color-mix(in oklch, var(--accent) 35%, transparent);
            flex-shrink: 0;
        }
        .country-part {
            display: inline-flex;
            align-items: center;
            gap: 3px;
            font-size: 12px;
            font-weight: 700;
            letter-spacing: .12em;
            text-transform: uppercase;
            color: var(--accent);
            padding: 4px 10px;
            border: none;
            background: none;
            cursor: pointer;
            border-radius: 0 5px 5px 0;
            transition: background .15s;
        }
        .country-part:hover {
            background: color-mix(in oklch, var(--accent) 22%, transparent);
        }
        .country-dropdown {
            display: none;
            position: absolute;
            top: calc(100% + 6px);
            left: 0;
            z-index: 9999;
            background: var(--surface-2);
            border: 1px solid var(--border-hi);
            border-radius: 8px;
            min-width: 220px;
            box-shadow: 0 8px 28px rgba(0, 0, 0, .4);
            overflow: hidden;
        }
        .country-dropdown.open {
            display: block;
        }
        .cdd-header {
            font-size: 10px;
            font-weight: 700;
            letter-spacing: .1em;
            text-transform: uppercase;
            color: var(--text-faint);
            padding: 8px 12px 6px;
            border-bottom: 1px solid var(--border);
        }
        .cdd-item {
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 8px 12px;
            cursor: pointer;
            transition: background .14s;
            border: none;
            background: none;
            width: 100%;
            text-align: left;
            color: var(--text);
            font-size: 13px;
            font-weight: 500;
        }
        .cdd-item:hover {
            background: var(--surface);
        }
        .cdd-item.active {
            background: color-mix(in oklch, var(--accent) 15%, transparent);
            color: var(--accent);
        }
        .cdd-flag {
            font-size: 16px;
        }
        .cdd-name {
            flex: 1;
        }
        .cdd-risk {
            font-size: 10px;
            font-weight: 700;
            letter-spacing: .08em;
            padding: 2px 6px;
            border-radius: 4px;
        }
        .cdd-risk.fast {
            background: color-mix(in oklch, #ef4444 20%, transparent);
            color: #ef4444;
        }
        .cdd-risk.mid {
            background: color-mix(in oklch, #f97316 20%, transparent);
            color: #f97316;
        }
        .cdd-risk.slow {
            background: color-mix(in oklch, #22c55e 20%, transparent);
            color: #22c55e;
        }
        #home-blank-page {
            display: none;
            position: fixed;
            inset: 0;
            background: var(--bg);
            z-index: 10000;
            align-items: center;
            justify-content: center;
            flex-direction: column;
            gap: 12px;
        }
        #home-blank-page.visible {
            display: flex;
        }
        #home-blank-page .home-back-hint {
            font-size: 12px;
            color: var(--text-faint);
            letter-spacing: .08em;
            text-transform: uppercase;
            cursor: pointer;
        }
        #home-blank-page .home-back-hint:hover {
            color: var(--accent);
        }
    </style>
</head>
<body>
    <svg style="display:none" xmlns="http://www.w3.org/2000/svg">
        <symbol id="car" viewBox="0 0 38 22">
            <rect x="1" y="8" width="36" height="9" rx="2" fill="currentColor" opacity=".9" />
            <path d="M8 8 L13 3 H25 L30 8 Z" fill="currentColor" />
            <circle cx="10" cy="19" r="3" fill="currentColor" />
            <circle cx="28" cy="19" r="3" fill="currentColor" />
            <rect x="13.5" y="3.5" width="4" height="4" rx=".7" fill="rgba(0,0,0,.35)" />
            <rect x="18.5" y="3.5" width="4" height="4" rx=".7" fill="rgba(0,0,0,.35)" />
        </symbol>
    </svg>
    <div class="modal-overlay" id="modalOverlay" role="dialog" aria-modal="true">
        <div class="modal">
            <button class="modal-close" id="modalClose" aria-label="Close"><svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M18 6 6 18M6 6l12 12" /></svg></button>
            <div id="modalForm">
                <div class="modal-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9" /><path d="M13.73 21a2 2 0 0 1-3.46 0" /></svg></div>
                <div class="modal-title">Subscribe to AI Threat Alerts</div>
                <div class="modal-desc">Get notified when automation risk changes for <strong>Chef / Cook</strong> roles.</div>
                <div class="input-group"><input class="modal-input" id="emailInput" type="email" placeholder="your@email.com" autocomplete="email"><button class="btn-confirm" id="confirmBtn"><svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12" /></svg>Subscribe</button></div>
                <div style="font-size: 12px;color:var(--text-faint);margin-bottom:12px">Select alert types:</div>
                <div class="modal-tags" id="modalTags"><span class="modal-tag sel" data-val="status">📊 Status Changes</span><span class="modal-tag sel" data-val="ltv">💰 LTV Updates</span><span class="modal-tag" data-val="weekly">📅 Weekly Digest</span><span class="modal-tag" data-val="break">⚡ Tech Breakthroughs</span></div>
            </div>
            <div class="modal-success" id="modalSuccess"><div class="check">✓</div><h3>You're subscribed!</h3><p>We'll alert you when Chef/Cook automation landscape changes.</p></div>
        </div>
    </div>
    <div class="toast" id="toast"><span class="toast-dot"></span><span id="toastMsg">Subscribed successfully</span></div>
    <div class="page">
        <header class="header">
            <div class="header-top-row">
                <div class="home-country-pill" id="homeCountryPill"><a class="home-part" id="homePart" href="#"><span class="live-dot"></span> HOME</a><span class="country-sep"></span><button class="country-part" id="countryToggleBtn" aria-haspopup="listbox">(<span id="countryPillLabel">US</span>)&#9660;</button><div class="country-dropdown" id="countryDropdown" role="listbox" aria-label="Select country by risk"></div></div>
                <div class="header-right">
                    <button class="btn-ghost">Upload Resume</button><button class="btn-ghost">Enter MBTI</button><button class="btn-login">Login</button>
                    <button class="theme-toggle" id="themeToggle" title="Toggle light/dark mode"><span class="th-icon">☀️</span><span id="themeLabel">Light</span></button>
                    <button class="btn-subscribe" id="openModal"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9" /><path d="M13.73 21a2 2 0 0 1-3.46 0" /></svg>Subscribe</button>
                </div>
            </div>
            <h1 class="page-title">Cook Lifecycle</h1>
        </header>
        <div class="level-section"><div class="section-label">Career Level — Click to compare salary, LTV &amp; insights</div><div class="level-tabs" id="levelTabs"></div></div>
        <nav class="main-tabs-nav" role="tablist" id="mainTabsNav">
            <button class="mtab active" role="tab" data-tab="tab-ltv"><span class="mtab-icon">💰</span>LTV &amp; Salary</button>
            <button class="mtab" role="tab" data-tab="tab-career"><span class="mtab-icon">📈</span>Job Path &amp; Insights</button>
            <button class="mtab" role="tab" data-tab="tab-risk"><span class="mtab-icon">🤖</span>Job Workflow &amp; AI/Robotic Risks</button>
            <button class="mtab" role="tab" data-tab="tab-hazards"><span class="mtab-icon">⚠️</span>Job Hazards</button>
            <button class="mtab" role="tab" data-tab="tab-profile"><span class="mtab-icon">🧠</span>MBTI &amp; Fit</button>
            <button class="mtab" role="tab" data-tab="tab-network"><span class="mtab-icon">🎓</span>Education &amp; Network</button>
        </nav>
        <div class="tab-panel active" id="tab-ltv">
            <div class="section-label">Job Lifetime Value Analysis</div>
            <div class="ltv-grid" id="ltvKpiGrid"></div>
            <div class="car-viz" id="carVizWrap"></div>
            <div class="income-chart-wrap" id="incomeChartWrap"></div>
            <div class="section-label">Income HeatMap</div>
            <div class="heatmap-section" id="heatmapSection"></div>
        </div>
        <div class="tab-panel" id="tab-career">
            <div class="section-label" style="margin-bottom:14px">Career Path</div>
            <div class="promo-section" style="margin-bottom:12px" id="promoSectionWrap"></div>
            <div class="section-label" style="margin-bottom:14px">Career Profile Insights</div>
            <div class="insights-grid" id="insightsGrid"></div>
        </div>
        <div class="tab-panel" id="tab-risk">
            <div class="section-label" style="margin-bottom:14px">Current Career Level Workflow &amp; Risks</div>
            <div class="filters-row" id="filtersRow"></div>
            <div class="table-wrap" id="tableWrap"></div>
            <div class="summary-row" id="summaryRow"></div>
        </div>
        <div class="tab-panel" id="tab-hazards"><div class="hazards-section" id="hazardsSection"></div></div>
        <div class="tab-panel" id="tab-profile">
            <div class="extended-section" id="extraInsightsSection"></div>
            <div class="extended-section" id="accessSection"></div>
            <div class="extended-section" id="careerNotesSection"></div>
            <div class="extended-section" id="careerRecsSection"></div>
        </div>
        <div class="tab-panel" id="tab-network">
            <div class="extended-section" id="networkSection"></div>
            <div class="lang-section" id="langSection"></div>
        </div>
        <div class="footnote"><span id="footnoteText"></span></div>
    </div>
    <div id="home-blank-page"><h2 style="color:var(--text);font-family:var(--font-display);font-weight:800;font-size:24px">🏠 Home</h2><p style="color:var(--text-muted);font-size:14px">Welcome back. Select a career path to continue.</p><span class="home-back-hint" id="homeBackBtn">← Back to Cook Lifecycle</span></div>
    <script>
        // ── fetch job data from external JSON ──
        let JOB_DATA;
        let D;
        fetch('./jobs/chef.json')
            .then(r => r.json())
            .then(d => {
                JOB_DATA = d;
                D = JOB_DATA;
                initAll();
            });

        // ─── Level & Country specific tasks ───
        const _baseTasksByLevel = {
            0: [{ action: 'Food Preparation (Mise en Place)', human: 'Wash, peel, chop vegetables; portion proteins; measure dry goods per station specs.',
                    ai: 'Suzumo robotic vegetable cutters & automated portioning systems handle bulk prep.',
                    timePct: 35, ratio: 75, ratioColor: 'var(--red)', eta: '~2 yrs', etaClass: 'eta-soon',
                    status: 'replaceable', statusClass: 'b-replaceable', statusLabel: 'Replaceable',
                    costRatio: 6.0 },
                { action: 'Basic Cooking & Station Support', human: 'Operate grill/fryer/sauté under chef direction; monitor temps; flip & stir continuously.',
                    ai: 'Miso Robotics Flippy arm with thermal vision automates grilling & frying sequences.',
                    timePct: 28, ratio: 58, ratioColor: 'var(--orange)', eta: '3–5 yrs', etaClass: 'eta-mid',
                    status: 'indanger', statusClass: 'b-indanger', statusLabel: 'In-Danger',
                costRatio: 3.5 },
                { action: 'Cleaning & Sanitation', human: 'Scrub stations, sanitize surfaces, wash dishes, empty grease traps between services.',
                    ai: 'Autonomous floor scrubbers & UV-C sanitizing robots reduce manual cleaning load.',
                    timePct: 20, ratio: 45, ratioColor: 'var(--yellow)', eta: '5–7 yrs',
                    etaClass: 'eta-far', status: 'intro', statusClass: 'b-intro', statusLabel: 'Intro',
                    costRatio: 4.0 },
                { action: 'Plating Support & Garnishing', human: 'Assemble basic plates per spec; add garnishes; ensure consistent portion presentation.',
                    ai: 'Dexterous plating robots emerging but struggle with artistic nuance & sauce drizzling.',
                    timePct: 10, ratio: 12, ratioColor: 'var(--green)', eta: '10+ yrs',
                    etaClass: 'eta-prot', status: 'nothing', statusClass: 'b-none', statusLabel: 'Nothing',
                    costRatio: 0.4 },
                { action: 'Inventory Assistance', human: 'Check low-stock items; report shortages to Chef de Partie; rotate FIFO stock.',
                    ai: 'RFID & AI camera systems auto-track inventory levels in real time.',
                    timePct: 7, ratio: 85, ratioColor: 'var(--red)', eta: '~1.5 yrs',
                etaClass: 'eta-soon', status: 'replaceable', statusClass: 'b-replaceable',
                    statusLabel: 'Replaceable', costRatio: 7.5 },
            ],
            1: [{ action: 'Station Cooking & Management', human: 'Own a station (sauté, pastry, grill); execute dishes to spec; manage timing & flow.',
                    ai: 'AI-assisted cooktops with recipe-guided temp control; robotic stir & flip functions.',
                    timePct: 35, ratio: 50, ratioColor: 'var(--orange)', eta: '4–6 yrs', etaClass: 'eta-mid',
                    status: 'indanger', statusClass: 'b-indanger', statusLabel: 'In-Danger',
                costRatio: 2.8 },
                { action: 'Advanced Food Preparation', human: 'Butcher fish/meat; prepare complex sauces & emulsions; oversee junior prep cooks.',
                    ai: 'Automated butchery systems & precision dispensers for sauces; still needs human QC.',
                    timePct: 22, ratio: 40, ratioColor: 'var(--yellow)', eta: '5–8 yrs',
                etaClass: 'eta-far', status: 'intro', statusClass: 'b-intro', statusLabel: 'Intro',
                    costRatio: 3.2 },
                { action: 'Quality Control & Tasting', human: 'Taste every batch; adjust seasoning; ensure consistency across covers; reject subpar output.',
                    ai: 'Electronic noses & computer vision grade food; cannot replicate subjective taste nuance.',
                    timePct: 15, ratio: 10, ratioColor: 'var(--green)', eta: '10+ yrs',
                etaClass: 'eta-prot', status: 'nothing', statusClass: 'b-none', statusLabel: 'Nothing',
                    costRatio: 0.3 },
                { action: 'Mentoring Junior Staff', human: 'Coach Line Cooks on knife skills, timing, and station protocols; demonstrate techniques.',
                    ai: 'VR/AR training modules supplement but cannot replace hands-on human mentorship.',
                    timePct: 12, ratio: 8, ratioColor: 'var(--green)', eta: '10+ yrs',
                etaClass: 'eta-prot', status: 'nothing', statusClass: 'b-none', statusLabel: 'Nothing',
                    costRatio: 0.2 },
                { action: 'Inventory & Ordering', human: 'Track station inventory; place supplier orders; manage par levels & reduce waste.',
                    ai: 'MarketMan / BlueCart AI predictive analytics for automated ordering.',
                    timePct: 16, ratio: 82, ratioColor: 'var(--red)', eta: '~2 yrs', etaClass: 'eta-soon',
                    status: 'replaceable', statusClass: 'b-replaceable', statusLabel: 'Replaceable',
                    costRatio: 6.5 },
            ],
            2: [{ action: 'Team Supervision & Scheduling', human: 'Manage brigade shifts; resolve conflicts; ensure coverage; maintain morale & discipline.',
                    ai: 'AI scheduling tools optimize shifts; human leadership & conflict resolution irreplaceable.',
                    timePct: 25, ratio: 15, ratioColor: 'var(--green)', eta: '10+ yrs',
                etaClass: 'eta-prot', status: 'nothing', statusClass: 'b-none', statusLabel: 'Nothing',
                    costRatio: 0.15 },
                { action: 'Quality Control & Expediting', human: 'Oversee every plate leaving the pass; ensure consistency; call orders; manage pace.',
                    ai: 'Computer vision checks plate composition; cannot judge nuanced flavor or artistic merit.',
                    timePct: 22, ratio: 18, ratioColor: 'var(--green)', eta: '10+ yrs',
                etaClass: 'eta-prot', status: 'nothing', statusClass: 'b-none', statusLabel: 'Nothing',
                    costRatio: 0.25 },
                { action: 'Inventory & Cost Management', human: 'Manage kitchen-wide ordering; negotiate with suppliers; track food cost percentages.',
                    ai: 'AI procurement platforms automate ordering & cost analysis with high accuracy.',
                    timePct: 20, ratio: 78, ratioColor: 'var(--red)', eta: '~2.5 yrs',
                etaClass: 'eta-soon', status: 'replaceable', statusClass: 'b-replaceable',
                    statusLabel: 'Replaceable', costRatio: 5.5 },
                { action: 'Recipe Testing & Menu Support', human: 'Collaborate with Head Chef on new dishes; test recipes; document procedures.',
                    ai: 'Generative AI suggests flavor pairings; human sensory validation still essential.',
                    timePct: 18, ratio: 30, ratioColor: 'var(--yellow)', eta: '6–9 yrs',
                etaClass: 'eta-far', status: 'intro', statusClass: 'b-intro', statusLabel: 'Intro',
                    costRatio: 1.8 },
                { action: 'Station Coverage (Peak Service)', human: 'Jump onto stations during rushes; demonstrate technique; fill gaps in brigade.',
                    ai: 'Limited robotic coverage; cannot adapt to dynamic rush conditions with human dexterity.',
                    timePct: 15, ratio: 22, ratioColor: 'var(--green)', eta: '8+ yrs',
                etaClass: 'eta-prot', status: 'nothing', statusClass: 'b-none', statusLabel: 'Nothing',
                    costRatio: 0.35 },
            ],
            3: [{ action: 'Menu Planning & Creation', human: 'Design seasonal menus; create signature dishes; balance flavor, cost & presentation.',
                    ai: 'AI generates molecular flavor combinations; lacks cultural intuition & creative vision.',
                    timePct: 25, ratio: 25, ratioColor: 'var(--yellow)', eta: '7–10 yrs',
                etaClass: 'eta-far', status: 'intro', statusClass: 'b-intro', statusLabel: 'Intro',
                    costRatio: 1.5 },
                { action: 'Team Management & Development', human: 'Hire, train, promote brigade members; build kitchen culture; performance reviews.',
                    ai: 'No AI equivalent for human leadership, mentorship & cultural development.',
                    timePct: 25, ratio: 5, ratioColor: 'var(--green)', eta: '10+ yrs',
                etaClass: 'eta-prot', status: 'nothing', statusClass: 'b-none', statusLabel: 'Nothing',
                    costRatio: 0.1 },
                { action: 'Vendor Relations & Sourcing', human: 'Build relationships with farmers, fishmongers, specialty suppliers; negotiate contracts.',
                    ai: 'Digital marketplaces streamline ordering; relationship-based sourcing remains human.',
                    timePct: 15, ratio: 20, ratioColor: 'var(--green)', eta: '10+ yrs',
                etaClass: 'eta-prot', status: 'nothing', statusClass: 'b-none', statusLabel: 'Nothing',
                    costRatio: 0.3 },
                { action: 'Quality Control Oversight', human: 'Set quality standards; audit stations; ensure consistency across all shifts.',
                    ai: 'Sensors and cameras assist; final judgment requires human sensory expertise.',
                    timePct: 15, ratio: 12, ratioColor: 'var(--green)', eta: '10+ yrs',
                etaClass: 'eta-prot', status: 'nothing', statusClass: 'b-none', statusLabel: 'Nothing',
                    costRatio: 0.2 },
                { action: 'Administrative & Financial', human: 'Manage P&L; food cost analysis; report to ownership; handle compliance paperwork.',
                    ai: 'AI-powered restaurant management platforms automate much of P&L tracking.',
                    timePct: 20, ratio: 65, ratioColor: 'var(--orange)', eta: '3–4 yrs',
                etaClass: 'eta-mid', status: 'indanger', statusClass: 'b-indanger',
                statusLabel: 'In-Danger', costRatio: 4.0 },
            ],
            4: [{ action: 'Strategic Planning & Vision', human: 'Define culinary direction; multi-outlet strategy; brand positioning; expansion planning.',
                    ai: 'AI provides data insights; strategic vision and brand storytelling remain uniquely human.',
                    timePct: 25, ratio: 8, ratioColor: 'var(--green)', eta: '10+ yrs',
                etaClass: 'eta-prot', status: 'nothing', statusClass: 'b-none', statusLabel: 'Nothing',
                    costRatio: 0.12 },
                { action: 'Brand & Business Development', human: 'Media appearances; cookbook deals; consulting; build personal & restaurant brand equity.',
                    ai: 'No AI equivalent for personal brand building & authentic media presence.',
                    timePct: 20, ratio: 3, ratioColor: 'var(--green)', eta: '10+ yrs',
                etaClass: 'eta-prot', status: 'nothing', statusClass: 'b-none', statusLabel: 'Nothing',
                    costRatio: 0.08 },
                { action: 'Executive Leadership', human: 'Lead all kitchen operations; mentor Head Chefs; represent culinary vision to stakeholders.',
                    ai: 'Leadership, inspiration & organizational culture are fundamentally human domains.',
                    timePct: 22, ratio: 2, ratioColor: 'var(--green)', eta: '10+ yrs',
                etaClass: 'eta-prot', status: 'nothing', statusClass: 'b-none', statusLabel: 'Nothing',
                    costRatio: 0.05 },
                { action: 'Vendor & Partner Relations', human: 'Cultivate high-level supplier partnerships; secure exclusives; negotiate multi-unit deals.',
                    ai: 'CRM & procurement AI assist; relationship trust & exclusivity require human touch.',
                    timePct: 15, ratio: 15, ratioColor: 'var(--green)', eta: '10+ yrs',
                etaClass: 'eta-prot', status: 'nothing', statusClass: 'b-none', statusLabel: 'Nothing',
                    costRatio: 0.2 },
                { action: 'Menu Innovation & R&D', human: 'Pioneer new techniques; lead culinary R&D; create signature concepts across outlets.',
                    ai: 'AI supports flavor analysis; true culinary innovation needs human creativity & instinct.',
                    timePct: 10, ratio: 20, ratioColor: 'var(--yellow)', eta: '8–12 yrs',
                etaClass: 'eta-far', status: 'intro', statusClass: 'b-intro', statusLabel: 'Intro',
                    costRatio: 1.2 },
                { action: 'Financial Oversight', human: 'Multi-venue P&L review; capital allocation; investor reporting; long-term financial strategy.',
                    ai: 'AI dashboards automate reporting; strategic financial decisions remain human-led.',
                    timePct: 8, ratio: 50, ratioColor: 'var(--orange)', eta: '4–5 yrs',
                etaClass: 'eta-mid', status: 'indanger', statusClass: 'b-indanger',
                statusLabel: 'In-Danger', costRatio: 3.0 },
            ],
        };

        // Country-specific modifiers for task data
        function getCountryTaskMods(country) {
            const mods = {
                US: { techAdoption: 1.0, laborCost: 1.0, aiSpeed: 1.0 },
                UK: { techAdoption: 0.9, laborCost: 0.85, aiSpeed: 0.9 },
                AU: { techAdoption: 0.85, laborCost: 0.9, aiSpeed: 0.85 },
                DE: { techAdoption: 0.75, laborCost: 0.8, aiSpeed: 0.7 },
                JP: { techAdoption: 0.8, laborCost: 0.7, aiSpeed: 0.75 },
                SG: { techAdoption: 1.1, laborCost: 0.95, aiSpeed: 1.1 },
                TW: { techAdoption: 0.9, laborCost: 0.5, aiSpeed: 0.85 },
                CN: { techAdoption: 1.05, laborCost: 0.35, aiSpeed: 1.0 },
            };
            return mods[country] || mods.US;
        }

        function getTasksForLevelCountry(level, country) {
            const base = (_baseTasksByLevel[level] || _baseTasksByLevel[0]).map(t => ({ ...t }));
            const mod = getCountryTaskMods(country);
            base.forEach(t => {
                const origRatio = t.ratio;
                t.ratio = Math.min(95, Math.round(origRatio * mod.techAdoption));
                t.costRatio = parseFloat((t.costRatio * mod.laborCost / Math.max(0.3, mod.aiSpeed)).toFixed(2));
                if (t.etaClass === 'eta-soon' && mod.aiSpeed < 0.9) t.eta = '~2.5 yrs';
                if (t.etaClass === 'eta-mid' && mod.aiSpeed > 1.0) t.eta = '2–4 yrs';
                if (t.ratio >= 70) t.ratioColor = 'var(--red)';
                else if (t.ratio >= 40) t.ratioColor = 'var(--orange)';
                else if (t.ratio >= 25) t.ratioColor = 'var(--yellow)';
                else t.ratioColor = 'var(--green)';
            });
            return base;
        }

        let currentCountry = 'US';
        let currentLevel = 0;
        const selectedMBTI = { type: 'ESTP', desc: 'The Dynamo. Thrives in fast-paced, high-pressure environments.' }; // placeholder from original D

        function fmt(n, c) { const sym = (JOB_DATA.countries[c] || JOB_DATA.countries.US).symbol || '$'; return sym + n.toLocaleString('en-US'); }
        function fmtK(n, c) { const sym = (JOB_DATA.countries[c] || JOB_DATA.countries.US).symbol || '$'; return n >= 1000000 ? sym + (n / 1000000).toFixed(2) + 'M' : fmt(n, c); }

        function calcLTV(c) { const ltv = c.annualUSD * c.career; const safe = Math.round(ltv * (1 - c.automationIdx / 100)); const risk = ltv - safe; const carCount = Math.round(ltv / c.carPriceUSD); const safeCarCount = Math.round(safe / c.carPriceUSD); const riskCarCount = carCount - safeCarCount; const safeYears = c.riskAge - c.startAge; const totalWorkYears = 55 - c.startAge; return { ltv, safe, risk, carCount, safeCarCount, riskCarCount, safeYears, totalWorkYears }; }

        function buildCarGrid(safeCount, riskCount) { const grid = document.getElementById('carGrid'); if (!grid) return; const total = safeCount + riskCount;
            grid.innerHTML = ''; for (let i = 0; i < total; i++) { const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
                svg.setAttribute('width', '38'); svg.setAttribute('height', '22'); svg.setAttribute('viewBox', '0 0 38 22'); svg.setAttribute('role', 'img'); svg.setAttribute('aria-label', i < safeCount ? 'Safe earnings car' : 'At-risk earnings car');
                svg.classList.add('car-icon', i < safeCount ? 'safe-car' : 'risk-car'); svg.style.opacity = '0'; svg.style.transform = 'scale(.7)'; const use = document.createElementNS('http://www.w3.org/2000/svg', 'use');
                use.setAttribute('href', '#car'); svg.appendChild(use); grid.appendChild(svg); const delay = i * 28;
                setTimeout(() => { svg.style.transition = `opacity .25s ${delay}ms, transform .3s ${delay}ms`; svg.style.opacity = ''; svg.style.transform = ''; }, 60); } }
        const riskOrder = { fast: 0, mid: 1, slow: 2 };

        function renderCountryDropdown() { const dd = document.getElementById('countryDropdown'); if (!dd) return; const sorted = Object.entries(JOB_DATA.countries).sort(([, a], [, b]) => riskOrder[a.riskClass] - riskOrder[b.riskClass]);
            dd.innerHTML = `<div class="cdd-header">&#9660; Risk: Highest to Lowest</div>` + sorted.map(([code, c]) => `
                <button class="cdd-item${code===currentCountry?' active':''}" data-country="${code}"><span class="cdd-flag">${c.flag}</span><span class="cdd-name">${c.name}</span><span class="cdd-risk ${c.riskClass}">${c.riskLabel}</span></button>`).join(''); }

        function renderLevelTabs() { const container = document.getElementById('levelTabs'); if (!container) return; const maxSal = JOB_DATA.levelUSD[currentCountry] ? JOB_DATA.levelUSD[currentCountry][JOB_DATA.levels.length - 1] : JOB_DATA.levelUSD.US[JOB_DATA.levels.length - 1];
            container.innerHTML = JOB_DATA.levels.map((lvl, i) => { const salaries = JOB_DATA.levelUSD[currentCountry] || JOB_DATA.levelUSD.US; const pct = Math.round(salaries[i] / maxSal * 100); const pctText = i === JOB_DATA.levels.length - 1 ? 'Peak LTV' : pct + '% of peak LTV'; return `
              <button class="ltab${i===currentLevel?' active':''}" data-level="${i}" style="--ldot:${lvl.color}"><span class="lcolor-dot"></span>${lvl.name}<span class="lyears">${lvl.yearsLabel}</span><span class="lpct">${pctText}</span></button>`; }).join(''); }

        function renderLTVKpiCards(countryCode, levelIndex, animate = true) { const grid = document.getElementById('ltvKpiGrid'); if (!grid) return; const c = JOB_DATA.countries[countryCode] || JOB_DATA.countries.US; const salaries = JOB_DATA.levelUSD[countryCode] || JOB_DATA.levelUSD.US; const salariesLocal = JOB_DATA.levelLocal[countryCode] || JOB_DATA.levelLocal.US; const annualUSD = salaries[levelIndex]; const careerYrs = c.career; const ltv = annualUSD * careerYrs; const maxUSD = salaries[JOB_DATA.levels.length - 1]; const peakLTV = maxUSD * careerYrs; const ltvPct = Math.round((ltv / peakLTV) * 100); const safe = Math.round(ltv * (1 - c.automationIdx / 100)); const risk = ltv - safe; const lvlName = JOB_DATA.levels[levelIndex].name; const d = calcLTV(c); const totalSpan = 55 - c.startAge; const safeSpan = d.safeYears; const riskSpan = totalSpan - safeSpan;
            grid.innerHTML = `
            <div class="ltv-card c-total"><div class="ltv-lbl">Career LTV</div><div class="ltv-val cl-total">${c.symbol}${ltv.toLocaleString('en-US')}</div><div class="ltv-meta">${careerYrs} yrs · ${salariesLocal[levelIndex]}/yr at ${lvlName}</div><div class="ltv-bar"><div class="ltv-bar-fill" style="width:${ltvPct}%;background:var(--accent)"></div></div></div>
            <div class="ltv-card c-safe"><div class="ltv-lbl">Human-Safe LTV</div><div class="ltv-val cl-safe">${c.symbol}${safe.toLocaleString('en-US')}</div><div class="ltv-meta">AI cannot replicate (${100-c.automationIdx}%)</div><div class="ltv-bar"><div class="ltv-bar-fill" style="width:${100-c.automationIdx}%;background:var(--green)"></div></div></div>
            <div class="ltv-card c-risk"><div class="ltv-lbl">At-Risk LTV</div><div class="ltv-val cl-risk">${c.symbol}${risk.toLocaleString('en-US')}</div><div class="ltv-meta">Threatened by AI (${c.automationIdx}%)</div><div class="ltv-bar"><div class="ltv-bar-fill" style="width:${c.automationIdx}%;background:var(--red)"></div></div></div>
            <div class="ltv-card c-idx"><div class="ltv-lbl">Automation Index</div><div class="ltv-val cl-idx">${c.automationIdx}%</div><div class="ltv-meta">Weighted across task nodes</div><div class="ltv-bar"><div class="ltv-bar-fill" style="width:${c.automationIdx}%;background:var(--yellow)"></div></div></div>
            <div class="ltv-card c-age"><div class="ltv-lbl">Peak Risk Age</div><div class="ltv-val cl-age">${c.riskAge}</div><div class="ltv-meta">Safe window: ${c.startAge} → ${c.riskAge} (${safeSpan} yrs)</div><div class="age-timeline"><div class="age-seg safe-seg" style="flex:${safeSpan}"></div><div class="age-seg risk-seg" style="flex:${riskSpan}"></div></div><div class="age-pins"><span class="age-pin">${c.startAge}</span><span class="age-pin risk-pin">${c.riskAge} ⚠</span><span class="age-pin">55</span></div></div>`; }

        function renderCarViz(countryCode, levelIndex) { const wrap = document.getElementById('carVizWrap'); if (!wrap) return; const c = JOB_DATA.countries[countryCode] || JOB_DATA.countries.US; const salaries = JOB_DATA.levelUSD[countryCode] || JOB_DATA.levelUSD.US; const ltv = salaries[levelIndex] * c.career; const safe = Math.round(ltv * (1 - c.automationIdx / 100)); const risk = ltv - safe; const carCount = Math.round(ltv / c.carPriceUSD); const safeCarCount = Math.round(safe / c.carPriceUSD); const riskCarCount = carCount - safeCarCount; const sgNote = countryCode === 'SG' ? ' *COE-inclusive price applies' : '';
            wrap.innerHTML = `
            <div class="car-viz-header"><span class="car-viz-eq">Career LTV Equals</span><span class="car-viz-val"><span>${carCount}</span> <span style="color:var(--text-muted)">${c.carName}${carCount===1?'':'s'}</span></span></div>
            <div class="car-viz-sub">Based on $${c.carPriceUSD.toLocaleString('en-US')} (USD)/unit${sgNote} · 🟢 Safe · 🔴 At-risk</div>
            <div class="car-grid" id="carGrid" aria-label="Car visualization"></div>
            <div class="car-legend"><div class="car-legend-item"><div class="car-legend-swatch safe"></div><span>${safeCarCount} cars = Human-Safe LTV</span></div><div class="car-legend-item"><div class="car-legend-swatch risk"></div><span>${riskCarCount} cars = At-Risk LTV</span></div></div>`;
            buildCarGrid(safeCarCount, riskCarCount); }

        function buildIncomePoints(country) { const salaries = JOB_DATA.levelUSD[country] || JOB_DATA.levelUSD.US; const transitions = JOB_DATA.levels.map(l => l.yearsFrom); const pts = []; for (let yr = 0; yr <= 30; yr++) { let lvl = 0; for (let i = transitions.length - 1; i >= 0; i--) { if (yr >= transitions[i]) { lvl = i; break; } } const nextTrans = transitions[lvl + 1] || 30; const frac = lvl < 4 ? (yr - transitions[lvl]) / (nextTrans - transitions[lvl]) : 1; const baseSal = salaries[lvl]; const nextSal = lvl < 4 ? salaries[lvl + 1] : salaries[4] * 1.15; const sal = baseSal + (nextSal - baseSal) * frac * 0.4;
            pts.push({ yr, sal, lvl }); } return pts; }

        function renderIncomeChart(country) { const wrap = document.getElementById('incomeChartWrap'); if (!wrap) return; const pts = buildIncomePoints(country); const TOTAL_YRS = 30; const W = 900, H = 240, padL = 55, padR = 30, padT = 24, padB = 38; const cW = W - padL - padR, cH = H - padT - padB; const maxSal = Math.max(...pts.map(p => p.sal)) * 1.12; const minSal = pts[0].sal * 0.75; const xOf = yr => padL + (yr / TOTAL_YRS) * cW; const yOf = sal => padT + cH - ((sal - minSal) / (maxSal - minSal)) * cH; let inner = ''; for (let g = 0; g <= 4; g++) { const y = padT + (g / 4) * cH; const val = Math.round(maxSal - (g / 4) * (maxSal - minSal));
            inner += `<line x1="${padL}" y1="${y}" x2="${W-padR}" y2="${y}" stroke="#222" stroke-width="1"/><text x="${padL-5}" y="${y+4}" text-anchor="end" fill="#555" font-size="10">${val>=1000?'$'+(val/1000).toFixed(0)+'K':val}</text>`; } [0,5,10,15,20,25,30].forEach(yr => { inner += `<text x="${xOf(yr)}" y="${H-5}" text-anchor="middle" fill="#555" font-size="10">Yr ${yr}</text>`; });
            inner += `<line x1="${xOf(30)}" y1="${padT}" x2="${xOf(30)}" y2="${H-padB}" stroke="#555" stroke-width="1.5" stroke-dasharray="4,3"/>`;
            let d = '';
            pts.forEach((p, i) => { d += (i === 0 ? 'M' : 'L') + xOf(p.yr).toFixed(1) + ',' + yOf(p.sal).toFixed(1); });
            inner += `<path d="${d}" fill="none" stroke="url(#careerGrad)" stroke-width="2.5"/>`; const lvlStart = JOB_DATA.levels[currentLevel].yearsFrom; const currentSal = pts.find(p => p.yr === lvlStart)?.sal || (JOB_DATA.levelUSD[country] || JOB_DATA.levelUSD.US)[currentLevel]; const projX1 = xOf(lvlStart), projX2 = xOf(30), projY = yOf(currentSal);
            inner += `<line x1="${projX1}" y1="${projY}" x2="${projX2}" y2="${projY}" stroke="#ef4444" stroke-width="2" stroke-dasharray="4,3" opacity="0.8"/>`;
            const transYears = [...JOB_DATA.levels.map(l => l.yearsFrom), 30];
            transYears.forEach(yr => { const p = pts.find(pp => pp.yr === yr); if (!p) return; const col = JOB_DATA.levels[p.lvl].color;
                inner += `<circle cx="${xOf(p.yr)}" cy="${yOf(p.sal)}" r="5" fill="${col}" stroke="#0e0e0e" stroke-width="2"/>`; });
            const lvlColor = JOB_DATA.levels[currentLevel].color; const lvlEnd = currentLevel < 4 ? JOB_DATA.levels[currentLevel + 1].yearsFrom : 30; const rx1 = xOf(lvlStart), rx2 = xOf(lvlEnd); const defs = `<defs><linearGradient id="careerGrad" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="#4f98a3"/><stop offset="60%" stop-color="#eab308"/><stop offset="100%" stop-color="#22c55e"/></linearGradient></defs><rect x="${rx1}" y="${padT}" width="${rx2-rx1}" height="${cH}" fill="${lvlColor}" opacity="0.07" rx="2"/>`;
            wrap.innerHTML = `
            <div class="income-chart-header"><span class="income-chart-title">Annual Income Curve — ${JOB_DATA.countries[country]?.name||country}</span><span class="income-chart-note">Colored dots mark level transitions</span></div>
            <svg id="incomeSVG" height="${H}" viewBox="0 0 ${W} ${H}" preserveAspectRatio="none">${defs}${inner}</svg>
            <div class="level-legend">${JOB_DATA.levels.map(l=>`<div class="level-legend-item"><div class="level-legend-dot" style="background:${l.color}"></div>${l.name}</div>`).join('')}<div class="level-legend-item" style="margin-left:10px;border-left:1px solid #333;padding-left:10px"><svg width="18" height="8"><line x1="0" y1="4" x2="18" y2="4" stroke="#ef4444" stroke-width="2" stroke-dasharray="4,3"/></svg><span style="color:var(--red)">Current → Career End</span></div></div>`; }

        function renderPromoFlow(country) { const wrap = document.getElementById('promoSectionWrap'); if (!wrap) return; const salaries = JOB_DATA.levelLocal[country] || JOB_DATA.levelLocal.US; let html = '<div class="section-label" style="margin-bottom:16px">Typical Promotion Timeline</div><div class="promo-flow">';
            JOB_DATA.levels.forEach((lvl, i) => { const isActive = i === currentLevel;
            html += `<div class="promo-node"><div class="promo-circle" style="border-color:${lvl.color};background:${isActive?lvl.color+'22':'transparent'};color:${lvl.color}"><span style="font-size:11px;text-align:center;padding:2px">${lvl.short}</span></div><div class="promo-label" style="color:${isActive?lvl.color:'var(--text)'}">${lvl.name}</div><div class="promo-salary" style="color:${isActive?'#fff':'var(--text-muted)'}">${salaries[i]}</div></div>`; if (i < JOB_DATA.levels.length - 1) { const tr = JOB_DATA.promotions[i];
                html += `<div class="promo-arrow"><div class="promo-arrow-line"></div><div class="promo-arrow-years">${tr.years}</div><div class="promo-arrow-sub">${tr.tip}</div></div>`; } });
            html += '</div>';
            wrap.innerHTML = html; }

        function renderDifficultyBar(difficulty) { const bars = Array(10).fill(0).map((_, i) => { const filled = i < difficulty; let fillClass = 'diff-pip'; if (filled) { if (difficulty <= 3) fillClass += ' filled-low'; else if (difficulty <= 5) fillClass += ' filled-mid'; else if (difficulty <= 7) fillClass += ' filled-high'; else fillClass += ' filled-max'; } return `<div class="${fillClass}"></div>`; }).join(''); return `<div class="difficulty-bar">${bars}</div>`; }

        function renderInsights(country) { const section = document.getElementById('insightsGrid'); if (!section) return; const meta = JOB_DATA.countryMeta[country] || JOB_DATA.countryMeta.US; const gradientMinsMaxs = {};
            JOB_DATA.insightCards.forEach(card => { if (card.colorMode && card.colorMode.startsWith('gradient')) { const key = card.valueKey; if (!gradientMinsMaxs[key]) { let min = Infinity, max = -Infinity; for (const c in JOB_DATA.countryMeta) { const val = JOB_DATA.countryMeta[c][key]; if (typeof val === 'number') { if (val < min) min = val; if (val > max) max = val; } }
                    gradientMinsMaxs[key] = { min, max }; } } });
            section.className = 'insights-grid';
            section.innerHTML = JOB_DATA.insightCards.map(card => { const rawValue = meta[card.valueKey]; const displayValue = card.valueTemplate.replace('{value}', rawValue); let metaText = card.metaTemplate; if (card.id === 'difficulty') { const diffLabel = JOB_DATA.difficultyLabels[meta.difficulty] || '';
                    metaText = metaText.replace('{difficultyLabel}', diffLabel); } if (card.id === 'restDays') { metaText = metaText.replace('{hoursPerDay}', meta.hoursPerDay).replace('{splitShiftLabel}', meta.splitShift ? 'common' : 'rare'); } let valueStyle = ''; const mode = card.colorMode || ''; if (mode === 'accent') { valueStyle = 'color: var(--accent)'; } else if (mode.startsWith('gradient')) { const key = card.valueKey; const mm = gradientMinsMaxs[key]; if (mm && mm.max !== mm.min) { const val = parseFloat(rawValue); let hue; if (mode === 'gradient-bad') { hue = 120 * (mm.max - val) / (mm.max - mm.min); } else { hue = 120 * (val - mm.min) / (mm.max - mm.min); } hue = Math.max(0, Math.min(120, Math.round(hue)));
                    valueStyle = `color: hsl(${hue}, 100%, 50%)`; } else { valueStyle = 'color: hsl(120, 100%, 50%)'; } } return `<div class="insight-card"${card.spanFull?' style="grid-column:span 2"':''}><span class="insight-icon">${card.icon}</span><div class="insight-label">${card.label}</div><div class="insight-value"${valueStyle?` style="${valueStyle}"`:''}>${displayValue}</div><div class="insight-meta">${metaText}</div>${card.id==='difficulty'?renderDifficultyBar(meta.difficulty):''}</div>`; }).join(''); }

        function renderLang(country) { const section = document.getElementById('langSection'); if (!section) return; const langs = JOB_DATA.languages[country] || []; const pillClass = JOB_DATA.langPillClasses;
            section.innerHTML = `
            <div class="section-label" style="margin-bottom:12px">Language Requirements — ${JOB_DATA.countries[country]?.name||country}</div>
            <div class="lang-list">${langs.map(l=>`<div class="lang-row"><div class="lang-name">${l.lang}</div><span class="lang-level-pill ${pillClass[l.level]||'llp-optional'}">${l.level}</span><div class="lang-bar-wrap"><div class="lang-bar-track"><div class="lang-bar-fill" style="width:${l.score*20}%"></div></div></div><div style="font-size:12px;color:var(--text-muted);min-width:120px">${JOB_DATA.langScoreLabels[l.score]||l.score+'/5'}</div></div>`).join('')}</div>`; }

        function renderHeatmap(country) { const section = document.getElementById('heatmapSection'); if (!section) return; const cities = JOB_DATA.cities[country] || []; if (!cities.length) { section.innerHTML = '<div style="font-size:13px;color:var(--text-faint);padding:18px">No city data</div>'; return; } const sorted = [...cities].sort((a, b) => b.salary - a.salary); const maxS = sorted[0].salary, minS = sorted[sorted.length - 1].salary; const cards = sorted.map(c => { const pct = (c.salary - minS) / (maxS - minS || 1); let bg; if (pct < 0.5) { const t = pct * 2; bg = `rgba(${Math.round(239+(234-239)*t)},${Math.round(68+(179-68)*t)},${Math.round(68+(8-68)*t)},0.25)`; } else { const t = (pct - 0.5) * 2; bg = `rgba(${Math.round(234+(34-234)*t)},${Math.round(179+(197-179)*t)},${Math.round(8+(94-8)*t)},0.25)`; } const brd = pct < 0.33 ? 'var(--red)' : pct < 0.66 ? 'var(--yellow)' : 'var(--green)'; const salK = c.salary >= 1000 ? (c.salary / 1000).toFixed(0) + 'K' : c.salary; return `<div class="city-card" style="background:${bg};border:1px solid ${brd}"><div class="city-name">${c.city}</div><div class="city-region">${c.region}</div><div class="city-salary">$${salK}</div><div class="city-cost">Cost Index: ${c.cost}</div></div>`; }).join('');
            section.innerHTML = `
            <div class="heatmap-header"><span class="section-label" style="margin-bottom:0">City Income Heatmap — ${JOB_DATA.countries[country]?.name||country}</span><span style="font-size:12px;color:var(--text-muted)">Avg. cook salary (USD equiv.)</span></div>
            <div class="heatmap-grid">${cards}</div>
            <div class="heatmap-scale"><div class="heatmap-scale-bar"><div class="hs-low"></div><div class="hs-mid"></div><div class="hs-high"></div></div><span style="font-size:11px;color:var(--text-muted)">Low → High income</span></div>`; }

        function renderHazards() { const section = document.getElementById('hazardsSection'); if (!section) return;
            section.innerHTML = `<div class="section-label">Work Hazards</div><div class="hazards-grid">${JOB_DATA.hazards.map(h=>`<div class="hazard-card"><span class="hazard-icon">${h.icon}</span><div class="hazard-info"><div class="hazard-name">${h.name}</div><div class="hazard-bar-track"><div class="hazard-bar-fill ${h.levelClass}" style="width:${h.width}"></div></div><div class="hazard-level">${h.desc}</div></div></div>`).join('')}</div>`; }

        function renderExtraInsights(country) { const section = document.getElementById('extraInsightsSection'); if (!section) return; const meta = JOB_DATA.extendedMeta[country] || JOB_DATA.extendedMeta.US; const links = JOB_DATA.startupLinks[country] || []; const linksHtml = links.map(l => `<a href="${l.url}" target="_blank" style="color:var(--accent);text-decoration:none;font-size:12px;display:block;margin-top:4px">→ ${l.label}</a>`).join(''); const baseStartup = meta.startupReadiness; const multipliers = [0, 5, 15, 25, 40]; const dynamicStartup = Math.min(95, baseStartup + multipliers[currentLevel]); const startupColor = dynamicStartup >= 70 ? 'var(--green)' : dynamicStartup >= 40 ? 'var(--yellow)' : 'var(--red)';
            section.innerHTML = `
            <div class="section-label">Career Economics and Fit</div><div class="extended-grid">
              <div class="insight-card"><span class="insight-icon">💸</span><div class="insight-label">Relationship Budget</div><div class="insight-value" style="color:var(--accent)">${meta.budget}</div><div class="insight-meta">Monthly social/dating spend at this level.</div></div>
              <div class="insight-card" id="startupCard" style="cursor:pointer"><span class="insight-icon">🚀</span><div class="insight-label">Startup Readiness</div><div class="insight-value" style="color:${startupColor}">${dynamicStartup}%</div><div class="insight-meta">Market support for pivots.</div><div id="startupLinks" style="display:block;margin-top:8px;border-top:1px solid var(--border);padding-top:8px">${linksHtml}</div><div id="startupToggle" style="font-size:11px;color:var(--accent);margin-top:8px;text-decoration:underline">Click to hide</div></div>
              <div class="insight-card"><span class="insight-icon">🧑‍💼</span><div class="insight-label">High Net Worth Client Access</div><div class="insight-value" style="font-size:14px;color:var(--text)">${meta.hnwi}</div><div class="insight-meta">Best environments for high-net-worth diners.</div></div>
            </div>`; }

        function renderAccessLinks() { const section = document.getElementById('accessSection'); if (!section) return;
            section.innerHTML = `<div class="section-label">Pathways &amp; Access Points</div><div class="link-grid-extended">${JOB_DATA.accessLinks.map(item=>`<div class="link-card"><div class="link-card-title">${item.title}</div><div class="link-card-desc">${item.desc}</div></div>`).join('')}</div>`; }

        function renderCareerNotes(country) { const section = document.getElementById('careerNotesSection'); if (!section) return; const meta = JOB_DATA.extendedMeta[country] || JOB_DATA.extendedMeta.US; let retireMetaText = "Late-career exit options."; if (JOB_DATA.filialPietyCountries.includes(country)) { retireMetaText += " Includes parental care planning."; }
            section.innerHTML = `
            <div class="section-label">MBTI Fit, Skill Pivots &amp; Retirement</div><div class="note-grid">
              <div class="note-card"><div class="note-title">MBTI fit: ${selectedMBTI.type}</div><div class="note-value" style="font-size:14px;color:var(--accent)">Highly Compatible</div><div class="note-meta">${selectedMBTI.desc}<br><br><div style="background:color-mix(in oklch,var(--accent) 10%,transparent);border:1px dashed var(--accent);padding:8px;border-radius:4px;margin-top:4px"><div style="color:var(--accent);font-weight:700;font-size:12px">Log in to see your MBTI fit.</div></div></div></div>
              <div class="note-card"><div class="note-title">Skill Pivot</div><div class="note-value" style="font-size:14px">${meta.pivot}</div><div class="note-meta"><div style="background:color-mix(in oklch,var(--accent) 10%,transparent);border:1px dashed var(--accent);padding:8px;border-radius:4px;margin-top:4px"><div style="color:var(--accent);font-weight:700;font-size:12px">Login for personalized matches.</div></div></div></div>
              <div class="note-card"><div class="note-title">Retirement Planning</div><div class="note-value" style="font-size:14px">${meta.retire}</div><div class="note-meta">${retireMetaText}</div></div>
            </div>`; }

        function renderCareerRecs(level) { const section = document.getElementById('careerRecsSection'); if (!section) return; const recs = JOB_DATA.careerRecs[level] || JOB_DATA.careerRecs[0];
            section.innerHTML = `<div class="section-label">Career Recommendations</div><div class="note-grid">${recs.map(r=>`<div class="note-card"><div class="note-title">${r.title}</div><div class="note-value" style="font-size:14px;color:${r.color}">${r.match} Match</div><div class="note-meta">${r.desc}<br><br><strong>Skills:</strong> ${r.skills.join(', ')}.</div></div>`).join('')}</div>`; }

        function renderNetworkSection(country) { const section = document.getElementById('networkSection'); if (!section) return; const meta = JOB_DATA.extendedMeta[country] || JOB_DATA.extendedMeta.US; const chefs = JOB_DATA.famousChefs[country] || JOB_DATA.famousChefs.US; const chefsHtml = chefs.map(c => `<strong>${c.name}</strong> (${c.netWorth})`).join(', '); const networkCardsHtml = JOB_DATA.networkCards.map(card => `<div class="note-card"><div class="note-title">${card.title}</div><div class="note-value" style="font-size:14px">${card.value}</div><div class="note-meta">${card.meta}${card.loginCTA?`<br><br><div style="background:color-mix(in oklch,var(--accent) 10%,transparent);border:1px dashed var(--accent);padding:8px;border-radius:4px;margin-top:4px"><div style="color:var(--accent);font-weight:700;font-size:12px">Login to unlock personalized connections.</div></div>`:''}</div></div>`).join('');
            section.innerHTML = `
            <div class="section-label">Education &amp; Networking Strategy</div><div class="note-grid">
              <div class="note-card"><div class="note-title">Prestige University</div><div class="note-value">${meta.uni}</div><div class="note-meta">${meta.uniMeta}</div></div>
              <div class="note-card"><div class="note-title">Private Schooling</div><div class="note-value">${meta.privateSchool}</div><div class="note-meta">${meta.privateMeta}<br><br><div style="background:color-mix(in oklch,var(--accent) 10%,transparent);border:1px dashed var(--accent);padding:8px;border-radius:4px;margin-top:4px"><div style="color:var(--accent);font-weight:700;font-size:12px">Login for personalized ROI analysis.</div></div></div></div>
              <div class="note-card"><div class="note-title">Recommended Schools</div><div class="note-value" style="font-size:14px">${meta.schools}</div><div class="note-meta"><div style="background:color-mix(in oklch,var(--accent) 10%,transparent);border:1px dashed var(--accent);padding:8px;border-radius:4px;margin-top:4px"><div style="color:var(--accent);font-weight:700;font-size:12px">Login for personalized school match.</div></div></div></div>
              ${networkCardsHtml}
              <div class="note-card" style="grid-column:span 2"><div class="note-title">Hall of Fame — ${JOB_DATA.countries[country]?.name||country}</div><div class="note-value" style="font-size:14px">${chefsHtml}</div><div class="note-meta">These chefs scaled via brand, media, and multi-venue empires.</div></div>
            </div>`; }

        function renderFiltersAndTable() {
            const filtersRow = document.getElementById('filtersRow'); const tableWrap = document.getElementById('tableWrap'); if (!filtersRow || !tableWrap) return;
            const tasks = getTasksForLevelCountry(currentLevel, currentCountry); const timeSum = tasks.reduce((s, t) => s + t.timePct, 0);
            filtersRow.innerHTML = `
            <div class="filters-left" role="group">
              ${JOB_DATA.filters.map(f=>`<button class="filter-pill ${f.class}${f.active?' active':''}" data-filter="${f.id}">${f.dot?'<span class="dot"></span> ':''}${f.label}${f.id==='all'?` <span style="opacity:.5;font-size:12px">${tasks.length}</span>`:''}</button>`).join('')}
            </div>
            <div style="font-size:12px;color:var(--text-faint);display:flex;align-items:center;gap:6px">${JOB_DATA.version} · <span class="time-sum-badge"><span class="ts-check">✓</span> ${timeSum}% workflow</span></div>`;
            tableWrap.innerHTML = `
            <div class="table-scroll"><table aria-label="Job automation workflow">
              <thead><tr><th>Action</th><th>Human Workflow</th><th>AI / Bot Workflow</th><th>Automation Ratio</th><th>Cost Ratio</th><th style="text-align:center">ETA</th><th style="text-align:center">Status</th></tr></thead>
              <tbody>${tasks.map(t=>{
                const humanPct = (t.costRatio / (1 + t.costRatio) * 100).toFixed(0);
                const aiPct = (1 / (1 + t.costRatio) * 100).toFixed(0);
                const ratioDisplay = t.costRatio >= 1 ? `${t.costRatio.toFixed(1)}:1` : `1:${(1 / t.costRatio).toFixed(1)}`;
                const humanLabel = 'Human'; const aiLabel = 'AI';
                return `
                <tr data-status="${t.status}">
                  <td class="col-action">${t.action}<span class="time-pct">⏱ <strong>${t.timePct}%</strong> of daily workflow</span></td>
                  <td class="col-human">${t.human}</td>
                  <td class="col-ai">${t.ai}</td>
                  <td><div class="bar-wrap"><div class="bar-track"><div class="bar-fill" style="width:${t.ratio}%;background:${t.ratioColor}"></div></div><div class="bar-lbl"><span>Automated</span><span>${t.ratio}%</span></div></div></td>
                  <td><div class="cost-ratio-wrap"><div class="cost-ratio-bar"><div class="cost-ratio-human" style="flex:${humanPct}"></div><div class="cost-ratio-ai" style="flex:${aiPct}"></div></div><div class="cost-ratio-lbl"><span class="cr-human">${humanLabel}</span><span class="cr-sep">${ratioDisplay}</span><span class="cr-ai">${aiLabel}</span></div></div></td>
                  <td style="text-align:center"><span class="eta-badge ${t.etaClass}">${t.eta}</span></td>
                  <td style="text-align:center"><span class="status-badge ${t.statusClass}"><span class="dot"></span>${t.statusLabel}</span></td>
                </tr>`;}).join('')}
              </tbody>
            </table></div>`;
        }

        function renderSummary(level) { const row = document.getElementById('summaryRow'); if (!row) return; const tasks = getTasksForLevelCountry(currentLevel, currentCountry); const maxRiskTask = tasks.reduce((max, t) => t.ratio > max.ratio ? t : max, tasks[0]); const maxCostTask = tasks.reduce((max, t) => t.costRatio > max.costRatio ? t : max, tasks[0]);
            row.innerHTML = `
            <div class="summary-card"><strong>Survival Strategy</strong> ${JOB_DATA.survivalStrategy[level]||JOB_DATA.survivalStrategy[0]}</div>
            <div class="summary-card"><strong>Highest Threat</strong>${maxRiskTask.action} — ${maxRiskTask.ratio}% automatable (${maxRiskTask.statusLabel})</div>
            <div class="summary-card"><strong>Best Cost Ratio</strong>${maxCostTask.action} — Human costs <strong>${maxCostTask.costRatio.toFixed(1)}x</strong> more than AI/robot</div>`; }

        function renderAll(countryCode, levelIndex, animate = true) {
            renderLTVKpiCards(countryCode, levelIndex, animate); renderCarViz(countryCode, levelIndex); renderIncomeChart(countryCode); renderPromoFlow(countryCode); renderInsights(countryCode); renderLang(countryCode); renderHeatmap(countryCode); renderExtraInsights(countryCode); renderCareerNotes(countryCode); renderCareerRecs(levelIndex); renderNetworkSection(countryCode); renderFiltersAndTable(); renderSummary(levelIndex);
            if (animate) { const sec = document.querySelector('.ltv-section'); if (sec) { sec.classList.remove('ltv-fade'); void sec.offsetWidth; sec.classList.add('ltv-fade'); } }
        }

        function initAll() {
            renderCountryDropdown(); renderLevelTabs(); renderHazards(); renderAccessLinks(); renderAll(currentCountry, currentLevel, false);
            const footnoteEl = document.getElementById('footnoteText'); if (footnoteEl) footnoteEl.textContent = JOB_DATA.footnote;
        }

        document.getElementById('countryDropdown')?.addEventListener('click', e => { const item = e.target.closest('.cdd-item'); if (!item) return;
            currentCountry = item.dataset.country; document.querySelectorAll('.cdd-item').forEach(i => i.classList.remove('active')); item.classList.add('active'); const lbl = document.getElementById('countryPillLabel'); if (lbl) lbl.textContent = currentCountry;
            document.getElementById('countryDropdown')?.classList.remove('open'); renderAll(currentCountry, currentLevel, true); });
        document.getElementById('countryToggleBtn')?.addEventListener('click', e => { e.stopPropagation(); renderCountryDropdown(); document.getElementById('countryDropdown')?.classList.toggle('open'); });
        document.addEventListener('click', () => { document.getElementById('countryDropdown')?.classList.remove('open'); });
        document.getElementById('homePart')?.addEventListener('click', e => { e.preventDefault(); document.getElementById('home-blank-page')?.classList.add('visible'); });
        document.getElementById('homeBackBtn')?.addEventListener('click', () => { document.getElementById('home-blank-page')?.classList.remove('visible'); });
        document.getElementById('levelTabs')?.addEventListener('click', e => { const tab = e.target.closest('.ltab'); if (!tab) return;
            document.querySelectorAll('.ltab').forEach(t => t.classList.remove('active')); tab.classList.add('active'); currentLevel = parseInt(tab.dataset.level) || 0; renderAll(currentCountry, currentLevel, true); });
        document.getElementById('filtersRow')?.addEventListener('click', e => { const pill = e.target.closest('.filter-pill'); if (!pill) return;
            document.querySelectorAll('.filter-pill').forEach(p => p.classList.remove('active')); pill.classList.add('active'); const f = pill.dataset.filter;
            document.querySelectorAll('tbody tr').forEach(r => { r.classList.toggle('hidden-row', f !== 'all' && r.dataset.status !== f); }); });
        const overlay = document.getElementById('modalOverlay');
        document.getElementById('openModal')?.addEventListener('click', () => overlay.classList.add('open'));
        document.getElementById('modalClose')?.addEventListener('click', () => overlay.classList.remove('open'));
        overlay?.addEventListener('click', e => { if (e.target === overlay) overlay.classList.remove('open'); });
        document.addEventListener('keydown', e => { if (e.key === 'Escape') overlay.classList.remove('open'); });
        document.querySelectorAll('.modal-tag').forEach(t => t.addEventListener('click', () => t.classList.toggle('sel')));
        document.getElementById('confirmBtn')?.addEventListener('click', () => { const email = document.getElementById('emailInput').value.trim(); if (!email || !email.includes('@')) { const inp = document.getElementById('emailInput'); inp.style.borderColor = 'var(--red)'; inp.focus(); setTimeout(() => inp.style.borderColor = '', 1200); return; }
            document.getElementById('modalForm').style.display = 'none'; document.getElementById('modalSuccess').style.display = 'block'; setTimeout(() => overlay.classList.remove('open'), 2200);
            setTimeout(() => { document.getElementById('modalForm').style.display = 'block'; document.getElementById('modalSuccess').style.display = 'none'; document.getElementById('emailInput').value = ''; }, 2800); const toast = document.getElementById('toast'); document.getElementById('toastMsg').textContent = 'Subscribed · alerts enabled'; toast.classList.add('show'); setTimeout(() => toast.classList.remove('show'), 3200); });
        (function() { const btn = document.getElementById('themeToggle'); const lbl = document.getElementById('themeLabel'); if (!btn) return; let dark = true;
            btn.addEventListener('click', () => { dark = !dark; if (dark) { document.documentElement.removeAttribute('data-theme'); btn.querySelector('.th-icon').textContent = '☀️'; lbl.textContent = 'Light'; } else { document.documentElement.setAttribute('data-theme', 'light'); btn.querySelector('.th-icon').textContent = '🌙'; lbl.textContent = 'Dark'; } }); })();
        // initAll is now called after fetch success
        (function() { const nav = document.getElementById('mainTabsNav'); if (!nav) return;
            nav.addEventListener('click', function(e) { const btn = e.target.closest('.mtab'); if (!btn) return; const target = btn.dataset.tab;
                nav.querySelectorAll('.mtab').forEach(b => b.classList.toggle('active', b === btn));
                document.querySelectorAll('.tab-panel').forEach(p => p.classList.toggle('active', p.id === target)); if (target === 'tab-risk') { renderFiltersAndTable(); renderSummary(currentLevel); } }); })();
    </script>
</body>
</html>
```