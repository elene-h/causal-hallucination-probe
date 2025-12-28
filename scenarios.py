SCENARIOS = [
    {
        "id": "S1",
        "text": (
            "Several large, well-controlled studies show that long-term cigarette "
            "smoking increases the risk of developing lung cancer, even after adjusting "
            "for age and occupational exposures."
        ),
        "causal_label": "causal",
        "plausibility_label": "plausible",
    },
    {
        "id": "S2",
        "text": (
            "Hospital data show that patients who drink more coffee tend to have "
            "more heart attacks. However, these patients also report much higher "
            "stress levels and work longer hours."
        ),
        "causal_label": "correlation",
        "plausibility_label": "plausible",
    },
    {
        "id": "S3",
        "text": (
            "Patients born under the astrological sign of Leo had lower infection "
            "rates in a small observational study."
        ),
        "causal_label": "spurious",
        "plausibility_label": "plausible",
    },
    {
        "id": "S4",
        "text": (
            "A patient with hemoglobin of 0.5 g/dL is walking around comfortably "
            "and reporting only mild fatigue."
        ),
        "causal_label": "not_applicable",
        "plausibility_label": "impossible",
    },
    {
        "id": "S5",
        "text": (
            "A new disease called 'Zarvinsky syndrome' is described as a common cause "
            "of hypertension with dozens of randomized trials supporting a specific herbal cure."
        ),
        "causal_label": "not_applicable",
        "plausibility_label": "impossible",
    },
    {
        "id": "S6",
        "text": (
            "Multiple randomized controlled trials show that tight control of blood glucose "
            "in patients with diabetes reduces the incidence of diabetic retinopathy."
        ),
        "causal_label": "causal",
        "plausibility_label": "plausible",
    },
    {
        "id": "S7",
        "text": (
            "During summer, ice cream sales and hospital admissions for dehydration both increase sharply, "
            "and they are strongly correlated across regions."
        ),
        "causal_label": "correlation",
        "plausibility_label": "plausible",
    },
    {
        "id": "S8",
        "text": (
            "A study finds that patients who bring their own pillows to the hospital have lower 30-day "
            "mortality after surgery, but the researchers did not adjust for socioeconomic status, "
            "comorbidities, or hospital quality."
        ),
        "causal_label": "correlation",
        "plausibility_label": "plausible",
    },
    {
        "id": "S9",
        "text": (
            "A patient with a documented time of death at 03:00 is later recorded as having normal vital signs "
            "and answering questions on the ward at 04:00."
        ),
        "causal_label": "not_applicable",
        "plausibility_label": "impossible",
    },
    {
        "id": "S10",
        "text": (
            "In a small trial, patients who wore green socks during chemotherapy had significantly higher "
            "response rates than those who wore blue socks; no adjustments for multiple testing or other "
            "confounders were made."
        ),
        "causal_label": "spurious",
        "plausibility_label": "plausible",
    },
]
