# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                dcc.Dropdown(id='site-dropdown',
                                    options=[
                                        {'label': 'All Sites', 'value': 'ALL'},
                                        {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                                        {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'},
                                        {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                                        {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'}
                                    ],
                                    value='ALL',
                                    placeholder='Select a Launch Site here',
                                    searchable=True),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div([ ], id='success-pie-chart'),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                dcc.RangeSlider(id='payload-slider',
                                    min=0, max=10000, step=1000,
                                    marks={0: '0',
                                        1000: '1000',
                                        2000: '2000',
                                        3000: '3000',
                                        4000: '4000',
                                        5000: '5000',
                                        6000: '6000',
                                        7000: '7000',
                                        8000: '8000',
                                        9000: '9000',
                                        10000: '10000'},
                                    value=[min_payload, max_payload]),

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div([ ], id='success-payload-scatter-chart'),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(Output(component_id='success-pie-chart', component_property='children'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(site):

    if(site=='ALL'):
        pie_data = spacex_df.groupby(['Launch Site'])['class'].sum().reset_index(name ='No of Successes')
        pie_fig = px.pie(pie_data, values='No of Successes', 
            names='Launch Site', 
            title='Total Success Launches by Site')
        return dcc.Graph(figure=pie_fig)
    
    else:
        pie_data = spacex_df[spacex_df['Launch Site']==site]
        pie_data = pie_data.groupby(['class'])['class'].count().reset_index(name ='Count')
        pie_fig = px.pie(pie_data, values='Count', 
            names='class', 
            title='Success/Failure ratio of site -' + site)
        return dcc.Graph(figure=pie_fig)

# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
# Import required libraries
import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the airline data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")
max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                dcc.Dropdown(id='site-dropdown',
                                    options=[
                                        {'label': 'All Sites', 'value': 'ALL'},
                                        {'label': 'CCAFS LC-40', 'value': 'CCAFS LC-40'},
                                        {'label': 'CCAFS SLC-40', 'value': 'CCAFS SLC-40'},
                                        {'label': 'KSC LC-39A', 'value': 'KSC LC-39A'},
                                        {'label': 'VAFB SLC-4E', 'value': 'VAFB SLC-4E'}
                                    ],
                                    value='ALL',
                                    placeholder='Select a Launch Site here',
                                    searchable=True),
                                html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div([ ], id='success-pie-chart'),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                dcc.RangeSlider(id='payload-slider',
                                    min=0, max=10000, step=1000,
                                    marks={0: '0',
                                        1000: '1000',
                                        2000: '2000',
                                        3000: '3000',
                                        4000: '4000',
                                        5000: '5000',
                                        6000: '6000',
                                        7000: '7000',
                                        8000: '8000',
                                        9000: '9000',
                                        10000: '10000'},
                                    value=[min_payload, max_payload]),

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div([ ], id='success-payload-scatter-chart'),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(Output(component_id='success-pie-chart', component_property='children'),
              Input(component_id='site-dropdown', component_property='value'))
def get_pie_chart(site):

    if(site=='ALL'):
        pie_data = spacex_df.groupby(['Launch Site'])['class'].sum().reset_index(name ='No of Successes')
        pie_fig = px.pie(pie_data, values='No of Successes', 
            names='Launch Site', 
            title='Total Success Launches by Site')
        return dcc.Graph(figure=pie_fig)
    
    else:
        pie_data = spacex_df[spacex_df['Launch Site']==site]
        pie_data = pie_data.groupby(['class'])['class'].count().reset_index(name ='Count')
        pie_fig = px.pie(pie_data, values='Count', 
            names='class', 
            title='Success/Failure ratio of site -' + site)
        return dcc.Graph(figure=pie_fig)

# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(Output(component_id='success-payload-scatter-chart', component_property='children'),
              [Input(component_id='site-dropdown', component_property='value'), 
              Input(component_id="payload-slider", component_property="value")])
def get_scatter_chart(site, payload_range):

    if(site=='ALL'):
        scatter_data = spacex_df
        scatter_fig = px.scatter(
            scatter_data, 
            x="Payload Mass (kg)", 
            y="class", 
            color="Booster Version Category",
            title='Correlation between payload and success for all sites')
        return dcc.Graph(figure=scatter_fig)
    
    else:
        min = payload_range[0]
        max = payload_range[1]
        
        scatter_data = spacex_df.loc[
            (spacex_df['Launch Site']==site) & 
            (spacex_df['Payload Mass (kg)']>min) & 
            (spacex_df['Payload Mass (kg)']<max),
            ['Payload Mass (kg)', 'class', 
            'Booster Version Category']]

        scatter_fig = px.scatter(
            scatter_data, 
            x="Payload Mass (kg)", 
            y="class", 
            color="Booster Version Category",
            title='Correlation between payload and success for site - ' + site)
        return dcc.Graph(figure=scatter_fig)

# Run the app
if __name__ == '__main__':
    app.run_server()


# Run the app
if __name__ == '__main__':
    app.run_server()
