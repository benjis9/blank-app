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
    for i in range(1, 4):
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
    components.html(html, height=600)  # Adjust the height as necessary

# Test data structure (mock data)
test_data = {
    '1': {'Team': {'score': 1, 'rationale': 'Strong team with experienced leadership.'},
          'Business Model': {'score': 0.5, 'rationale': 'Model has potential, but unclear revenue model.'},
          'Traction': {'score': 0, 'rationale': 'Limited traction, few users engaged.'}},
    '2': {'Team': {'score': 0.5, 'rationale': 'Some experience, but lack of depth in the market.'},
          'Business Model': {'score': 1, 'rationale': 'Clear revenue model, scalable business.'},
          'Traction': {'score': 0.5, 'rationale': 'Some growth, but not enough to sustain long-term.'}},
    '3': {'Team': {'score': 0, 'rationale': 'Inexperienced team with limited industry knowledge.'},
          'Business Model': {'score': 0, 'rationale': 'Business model is unclear, lacks clarity.'},
          'Traction': {'score': 1, 'rationale': 'Strong traction with growing customer base and partnerships.'}}
}

# Call the function to display the table with the test data
render_html_table(test_data)
