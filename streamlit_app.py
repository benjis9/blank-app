import streamlit as st
import streamlit.components.v1 as components

def render_html_table(data):
    html = """
    <style>
    table { width: 100%; border-collapse: collapse; margin-top: 20px; }
    th, td { border: 1px solid #ccc; padding: 8px; text-align: center; }
    th { background-color: #f8f8f8; }
    td.score-1 { background-color: #d4edda; }
    td.score-0_5 { background-color: #fff3cd; }
    td.score-0 { background-color: #f8d7da; }
    </style>
    <table>
        <tr>
            <th rowspan="2">#</th>
            <th colspan="2">Team</th>
            <th colspan="2">Business Model</th>
            <th colspan="2">Traction</th>
        </tr>
        <tr>
            <th>Score</th><th>Rationale</th>
            <th>Score</th><th>Rationale</th>
            <th>Score</th><th>Rationale</th>
        </tr>
    """
    for i in range(1, 5):
        row = data[str(i)]
        def score_class(score):
            return f"score-{str(score).replace('.', '_')}"  # Generate class based on score value

        html += f"""
        <tr>
            <td>{i}</td>
            <td class='{score_class(row['Team']['score'])}'>{row['Team']['score']}</td>
            <td>{row['Team']['rationale']}</td>
            <td class='{score_class(row['Business Model']['score'])}'>{row['Business Model']['score']}</td>
            <td>{row['Business Model']['rationale']}</td>
            <td class='{score_class(row['Traction']['score'])}'>{row['Traction']['score']}</td>
            <td>{row['Traction']['rationale']}</td>
        </tr>
        """
    html += "</table>"
    
    # Use st.components.v1.html() to render larger HTML content
    components.html(html, height=2400)  # Adjust the height as necessary

# Test data structure (mock data)
test_data = {
  "1": {
    "Team": {
      "score": 1,
      "rationale": "The founding team consists of three experienced co-founders with complementary skill sets, including a strong advisory board. All founders have worked in the tech space for over 10 years and have prior startup experience."
    },
    "Business Model": {
      "score": 1,
      "rationale": "The business operates a B2B SaaS model, which is highly scalable. There are clear opportunities for expanding the product offering and upselling additional services to current customers."
    },
    "Traction": {
      "score": 1,
      "rationale": "The company has 1,000 paying customers and shows strong month-over-month revenue growth of 20%. Retention rates are high with 85% of customers renewing their subscriptions after one year."
    }
  },
  "2": {
    "Team": {
      "score": 0.5,
      "rationale": "The team has a founder with relevant experience, but lacks a strong co-founder or advisory board. The founder has a background in finance but limited experience in the core industry of e-commerce."
    },
    "Business Model": {
      "score": 0.5,
      "rationale": "The business model is somewhat scalable but faces challenges due to high capital expenditure for infrastructure. It has some room for product expansion but the growth may be limited by operational costs."
    },
    "Traction": {
      "score": 0.5,
      "rationale": "The business has a small user base, and while there has been steady growth, the customer retention rate is only 60%. There is limited data on repeat purchases or long-term engagement."
    }
  },
  "3": {
    "Team": {
      "score": 0,
      "rationale": "The team consists of a solo founder with minimal industry experience. The founder has no prior startup experience and lacks an advisory board or experienced co-founders."
    },
    "Business Model": {
      "score": 0,
      "rationale": "The business model is not scalable and requires significant capital investment. The company relies heavily on physical inventory and logistics, which makes expansion costly and difficult."
    },
    "Traction": {
      "score": 0,
      "rationale": "The company has no paying customers and is still in the early stages of product development. There are no metrics or KPIs indicating significant growth or market interest."
    }
  },
  "4": {
    "Team": {
      "score": 1,
      "rationale": "The founding team consists of two highly experienced entrepreneurs who previously built a successful startup. They have complementary skills, with one focusing on technology and the other on business development."
    },
    "Business Model": {
      "score": 1,
      "rationale": "The business model is highly scalable with a strong B2B component. There are clear opportunities for product expansion, and the business is well-positioned to take advantage of growing demand in its target market."
    },
    "Traction": {
      "score": 0.5,
      "rationale": "The company has some initial customers, but growth has been slow. The customer base is still in the early stages, and there is limited data to indicate strong retention or engagement. However, the company is seeing steady growth in revenue."
    }
  }
}



st.text("what's going on?")
# Call the function to display the table with the test data
render_html_table(test_data)
