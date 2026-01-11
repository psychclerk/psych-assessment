# 🧠 PG Psychiatry Assessment Framework

A comprehensive psychiatric symptom assessment educational app for postgraduate medical students, built with Streamlit.

## Overview

This interactive educational tool provides detailed assessment frameworks for 80 psychiatric symptoms across 11 clinical categories. Each symptom includes structured content on assessment, differential diagnosis, management approaches, and clinical teaching pearls.

## Features

- **80 Psychiatric Symptoms** organized into 11 clinical categories
- **Structured Assessment Framework** for each symptom
- **Differential Diagnosis** with primary psychiatric disorders, secondary mimics, and red flags
- **Evidence-Based Management** including biological, psychological, and social interventions
- **Faculty Pearls** with key clinical insights and teaching points
- **Easy Navigation** via sidebar categories and symptom selection
- **Sequential Navigation** within categories using Previous/Next buttons
- **Professional Medical Education UI** optimized for learning

## Categories

1. **Mood & Affect Presentations** (12 symptoms)
   - Persistent Sadness, Loss of Interest, Feeling Hopeless/Worthless, Crying Spells, Fatigue/Low Energy, Excessive Happiness, Irritability, Increased Activity, Decreased Need for Sleep, Grandiosity, Mood Cycling, Rapid Mood Swings

2. **Anxiety & Fear Presentations** (8 symptoms)
   - Excessive Worry, Panic Attacks, Palpitations/Breathlessness, Fear of Dying/Losing Control, Avoidance Behavior, Phobic Fear, Obsessions, Compulsions

3. **Thought Disturbances** (7 symptoms)
   - Hearing Voices, Delusions, Disorganized Speech, Suspiciousness, Flight of Ideas, Tangentiality, Thought Blocking

4. **Behavioral Disturbances** (6 symptoms)
   - Aggression/Violence, Disinhibition, Social Withdrawal, Self-Neglect, Wandering Behavior, Impulsivity

5. **Cognitive & Memory Presentations** (8 symptoms)
   - Poor Concentration, Memory Loss, Confusion/Disorientation, Difficulty with Complex Tasks, Slowed Thinking, Racing Thoughts, Distraction/Distractibility, Indecision

6. **Sleep, Appetite & Somatic Presentations** (11 symptoms)
   - Insomnia, Hypersomnia, Nightmares, Appetite Changes, Weight Changes, Nausea/Vomiting, Abdominal Pain, Headache, Chest Pain

7. **Substance Use & Intoxication** (8 symptoms)
   - Alcohol Intoxication/Withdrawal, Cannabis Effects, Stimulant Intoxication, Opioid Intoxication, Sedative Intoxication, Hallucinogen Effects, Withdrawal Syndromes

8. **Trauma & Dissociation** (6 symptoms)
   - Flashbacks, PTSD Nightmares, Hypervigilance, Emotional Numbing, Depersonalization, Derealization

9. **Sexual & Gender Presentations** (6 symptoms)
   - Decreased Sexual Interest, Sexual Dysfunction, Compulsive Sexual Behavior, Gender Dysphoria, Sexual Orientation Confusion, Paraphilic Interest

10. **Attention, Impulse Control & Development** (7 symptoms)
    - Inattention, Hyperactivity, Poor Impulse Control, Developmental Delay, Learning Difficulty, Regressive Behavior, Tics/Stereotyped Movements

11. **Miscellaneous Presentations** (5 symptoms)
    - Excessive Crying/Emotional Lability, Emotional Numbness, Apathy/Lack of Motivation, Suicidal Ideation/Behavior, Self-Harm/Non-suicidal Self-Injury

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Setup

1. Clone or download this repository:
```bash
git clone <repository-url>
cd psych-assessment
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Usage

1. **Select a Category** from the sidebar dropdown
2. **Choose a Symptom** from the symptom list
3. **Explore Content** by expanding sections:
   - **Assessment**: Core symptom clarification, syndrome screening, ruling out mimics, psychosocial context, and risk assessment
   - **Differential Diagnosis**: Primary psychiatric disorders, secondary mimics, and red flags
   - **Management**: Immediate priorities, biological/psychological/social interventions, and follow-up monitoring
   - **Faculty Pearls**: Key clinical insights highlighted at the bottom

4. **Navigate** within a category using Previous/Next buttons
5. Use **Expand/Collapse** to focus on specific sections

## Project Structure

```
psych-assessment/
├── app.py                    # Main Streamlit application
├── data/
│   └── symptoms.json         # All 80 symptoms with clinical content
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── .gitignore               # Git ignore rules
```

## Data Format

Symptom data is stored in `data/symptoms.json` with the following structure:

```json
{
  "Category Name": {
    "Symptom Name": {
      "assessment": {
        "clarify_core": "Questions to clarify the symptom...",
        "screen_for_syndrome": "Key associated features...",
        "rule_out_mimics": "Medical, substance, medication causes...",
        "psychosocial_context": "Stressors, support systems...",
        "risk_assessment": "Safety concerns..."
      },
      "differential_diagnosis": {
        "primary_psychiatric": "Main psychiatric disorders...",
        "secondary_mimics": "Medical/substance causes...",
        "red_flags": "Features pointing to specific diagnoses..."
      },
      "management": {
        "immediate_priorities": "Safety, crisis intervention...",
        "biological_interventions": "Medications, investigations...",
        "psychological_interventions": "Therapies, psychoeducation...",
        "social_interventions": "Psychosocial support...",
        "follow_up_monitoring": "Monitoring schedule..."
      },
      "faculty_pearls": [
        "Clinical insight 1...",
        "Clinical insight 2..."
      ]
    }
  }
}
```

## Customization

### Adding New Symptoms

1. Edit `data/symptoms.json`
2. Add symptom to the appropriate category following the structure above
3. Restart the Streamlit app to see changes

### Modifying Content

Simply edit the relevant sections in `data/symptoms.json`. The app will reflect changes automatically on refresh.

## Technical Details

- **Framework**: Streamlit 1.28+
- **Data Format**: JSON
- **No Authentication**: Public access for educational use
- **No Data Persistence**: All data is stored in JSON files
- **Responsive Design**: Works on desktop, tablet, and mobile devices

## Educational Use

This tool is designed for:
- Postgraduate medical students
- Psychiatry residents
- Mental health professionals in training
- Medical educators

The content is evidence-based and appropriate for PG-level medical education.

## Development

### Running the Data Generator

To regenerate the symptoms data:

```bash
python3 create_symptoms.py
```

This will create/update `data/symptoms.json` with all 80 symptoms.

## Contributing

Contributions are welcome! Areas for enhancement:
- Adding more detailed clinical content
- Including case examples
- Adding assessment tools/ scales
- Multilingual support
- Additional categories

## License

Educational use only. Please refer to your institution's guidelines for clinical practice.

## Acknowledgments

This educational tool was developed to support psychiatry education and training. Content is based on established psychiatric assessment principles and evidence-based practices.

## Contact

For questions, issues, or suggestions, please contact the development team.

---

**Note**: This is an educational tool and should not replace clinical judgment or formal psychiatric training. Always consult current clinical guidelines and your institution's protocols.
