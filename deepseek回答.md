Here’s how to externalize the hardcoded level & country-specific task data into your `jobs/chef.json`, along with the minimal HTML edits needed to pull that data from the JSON.

## 1. JSON additions – insert into `jobs/chef.json`

Add these two top-level keys alongside your existing data:

```json

```

## 2. HTML changes – replace two script blocks

**Remove** the entire `_baseTasksByLevel = { ... }` block (the big hardcoded object) and **replace** these two functions:

### Replace `getCountryTaskMods`:

```js
function getCountryTaskMods(country) {
    return (JOB_DATA.countryTaskMods && JOB_DATA.countryTaskMods[country]) 
        || JOB_DATA.countryTaskMods?.US 
        || { techAdoption: 1.0, laborCost: 1.0, aiSpeed: 1.0 };
}
```

### Replace `getTasksForLevelCountry`:

```js
function getTasksForLevelCountry(level, country) {
    const tasksByLevel = JOB_DATA.tasksByLevel || {};
    const base = (tasksByLevel[level] || tasksByLevel[0] || []).map(t => ({ ...t }));
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
```

That's it. Now all task data lives in the JSON, and you can edit levels, countries, and modifiers directly there without touching the HTML.