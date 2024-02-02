from flask import Flask, render_template, send_file
from matplotlib.figure import Figure
from io import BytesIO

app = Flask(__name__)

# Define route to serve the first plot
@app.route('/plot1')
def plot1():
    # Generate the plot
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.regplot(data=carbon_filter2, x='Year', y='Annual CO₂ emissions', scatter=True, ci=None, line_kws={"color": "green"}, ax=ax)
    
    # Add annotations, titles, etc.
    
    # Save the plot to a BytesIO object
    img_bytes = BytesIO()
    fig.savefig(img_bytes, format='png')
    img_bytes.seek(0)
    
    # Return the image file
    return send_file(img_bytes, mimetype='image/png')

# Define route to serve the second plot
@app.route('/plot2')
def plot2():
    # Similar implementation for the second plot
    
# Define route to serve JSON data
@app.route('/data')
def data():
    # Fetch and return data as JSON
    
if __name__ == '__main__':
    app.run(debug=True)