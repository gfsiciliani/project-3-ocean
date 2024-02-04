from flask import Flask, render_template, send_file, jsonify, request
from matplotlib.figure import Figure
from matplotlib import pyplot as plt
import seaborn as sns
from scipy import stats
import numpy as np
from io import BytesIO
import pandas as pd

app = Flask(__name__)
# Read JSON data and parse it
with open('charts/worldcarbon.json', 'r') as carbon_file:
    carbon_data = json.load(carbon_file)

with open('charts/globaltemptemp.json', 'r') as temp_file:
    temp_data = json.load(temp_file)

# Convert JSON data to Pandas DataFrame
carbon_df = pd.DataFrame(carbon_data)
temp_df = pd.DataFrame(temp_data)

# Define route to serve the first plot
@app.route('/plot1')
def plot1():
    # Create the scatter plot with line of best fit
    plt.figure(figsize=(12, 6))
    sns.regplot(data=carbon_df, x='Year', y='Annual CO₂ emissions', scatter=True, ci=None, line_kws={"color": "green"})

    # Get the regression coefficients
    slope, intercept, r_value, p_value, std_err = stats.linregress(carbon_df['Year'], carbon_df['Annual CO₂ emissions'])

    # Compute R-squared value
    r_squared = r_value ** 2

    # Set the title and labels
    plt.title(f'Global Annual CO2 Emissions with Line of Best Fit')
    plt.xlabel('Year')
    plt.ylabel('Annual CO2 emissions')

    # Display the r-squared value
    plt.text(0.4, 0.8, f'$R^2$: {r_squared:.5f}', transform=plt.gca().transAxes, fontsize=12, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

    # Show the plot
    plt.tight_layout()
    
    # Save the plot to a BytesIO object
    img_bytes = BytesIO()
    plt.savefig(img_bytes, format='png')
    img_bytes.seek(0)
    
    # Return the image file
    return send_file(img_bytes, mimetype='image/png')

# Define route to serve the second plot
@app.route('/plot2')
def plot2():
    # chart the lines of the temperature anomaly

    #create a polynomial line of best fit
    degree = 3  # You can change the degree of the polynomial
    coefficients = np.polyfit(temp_df['Year '], temp_df['Temperature Anomaly\n(deg C)'], degree)
    polynomial = np.poly1d(coefficients)

    # Generate points for the polynomial curve
    x_values = np.linspace(min(temp_df['Year ']), max(temp_df['Year ']), 100)
    y_values = polynomial(x_values)

    # Calculate the R-squared value
    residuals = temp_df['Temperature Anomaly\n(deg C)'] - polynomial(temp_df['Year '])
    ss_res = np.sum(residuals ** 2)
    ss_tot = np.sum((temp_df['Temperature Anomaly\n(deg C)'] - np.mean(temp_df['Temperature Anomaly\n(deg C)'])) ** 2)
    r_squared = 1 - (ss_res / ss_tot)

    # Plot the data and the exponential curve
    plt.figure(figsize=(12, 6))
    plt.scatter(temp_df['Year '], temp_df['Temperature Anomaly\n(deg C)'], label='Data')
    plt.plot(x_values, y_values, color='red', label='Polynomial Curve')

    # Set the title and labels
    plt.title('Global Annual Temperature Anomaly with Polynomial Curve Fit')
    plt.xlabel('Year')
    plt.ylabel('Annual Temperature Anomaly')
    plt.legend()

    # Display the R-squared value on the graph
    plt.text(0.4, 0.9, f'$R^2$: {r_squared:.5f}', transform=plt.gca().transAxes, fontsize=12, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

    # Show the plot
    plt.tight_layout()

    # Save the plot to a BytesIO object
    img_bytes = BytesIO()
    plt.savefig(img_bytes, format='png')
    img_bytes.seek(0)
    
    # Return the image file
    return send_file(img_bytes, mimetype='image/png')

@app.route('/plot3')
def plot3():
    #combine in some way the regression line for carbon emissions and the global temperature in the same figure
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # Plot 1: Global Annual CO2 Emissions with Line of Best Fit
    sns.regplot(data=carbon_df, x='Year', y='Annual CO₂ emissions', scatter=True, ci=None, line_kws={"color": "green"}, ax=axes[0])

    slope, intercept, r_value, p_value, std_err = stats.linregress(carbon_df['Year'], carbon_df['Annual CO₂ emissions'])
    r_squared = r_value ** 2

    axes[0].set_title('Global Annual CO2 Emissions with Line of Best Fit')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Annual CO2 emissions')
    axes[0].text(0.4, 0.8, f'$R^2$: {r_squared:.5f}', transform=axes[0].transAxes, fontsize=12, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

    # Plot 2: Global Annual Temperature Anomaly with Polynomial Curve Fit
    degree = 3
    coefficients = np.polyfit(temp_df['Year '], temp_df['Temperature Anomaly\n(deg C)'], degree)
    polynomial = np.poly1d(coefficients)

    x_values = np.linspace(min(temp_df['Year ']), max(temp_df['Year ']), 100)
    y_values = polynomial(x_values)

    residuals = temp_df['Temperature Anomaly\n(deg C)'] - polynomial(temp_df['Year '])
    ss_res = np.sum(residuals ** 2)
    ss_tot = np.sum((temp_df['Temperature Anomaly\n(deg C)'] - np.mean(temp_df['Temperature Anomaly\n(deg C)'])) ** 2)
    r_squared = 1 - (ss_res / ss_tot)

    axes[1].scatter(temp_df['Year '], temp_df['Temperature Anomaly\n(deg C)'])
    axes[1].plot(x_values, y_values, color='red')
    axes[1].axvline(x=1950, color='black', linestyle='--')  # Vertical line at x=1950
    axes[1].set_title('Global Annual Temperature Anomaly with Polynomial Curve Fit')
    axes[1].set_xlabel('Year')
    axes[1].set_ylabel('Annual Temperature Anomaly')
    axes[1].text(0.2, 0.6, f'$R^2$: {r_squared:.5f}', transform=axes[1].transAxes, fontsize=12, bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5'))

    plt.tight_layout()

    # Save the plot to a BytesIO object
    img_bytes = BytesIO()
    plt.savefig(img_bytes, format='png')
    img_bytes.seek(0)
    
    # Return the image file
    return send_file(img_bytes, mimetype='image/png')
    
if __name__ == '__main__':
    app.run