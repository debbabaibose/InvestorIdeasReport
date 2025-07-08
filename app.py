import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import streamlit 
from plotly.subplots import make_subplots

import streamlit as st
import pandas as pd
import plotly.express as px

import pandas as pd
import numpy as np

import ast


# Using object notation

import warnings
warnings.filterwarnings("ignore")



# Read the data based on selected option
report_options = st.sidebar.radio('Choose Report', ('Cost vs Portfolio value','Annualised ROI', 'Annualised ROI with Investment' , 'Compound Return' , 'User Buys on Every Report Date' , 'Daywise Absolute Return'))

try:

    if report_options == 'Cost vs Portfolio value':
        import streamlit as st
        import pandas as pd
        import plotly.graph_objects as go
        
        # Read the data
        df = pd.read_csv('Annualised ROI/July07_2025/compound_return_s2f.csv')
        cumulative_investment = df['Investment'].tolist()
        final_graph_list1 = df['Gain_amount'].tolist()
        # Create traces
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['Date'], y=cumulative_investment, mode='lines', name='cumulative_investment'))
        fig.add_trace(go.Scatter(x=df['Date'], y=final_graph_list1, mode='lines', name='return_amount'))
        
        # Customize the layout
        fig.update_layout(
            autosize=True,
            height=1000,
            width = 1000
        )
        
        fig.update_yaxes(automargin=True)
        
        # Display the graph in Streamlit
        st.plotly_chart(fig)
    
    
    
    
    if report_options == 'Annualised ROI':
        mode = st.sidebar.radio('Choose Support mode', ('Support 2 from', 'Support 2 to', 'Support 1 from', 'Support 1 to'))
    
        if mode == 'Support 2 from':
            df = pd.read_csv('Annualised ROI/July07_2025/compound_return_s2f.csv')
        if mode == 'Support 2 to':
            df = pd.read_csv('Annualised ROI/July07_2025/compound_return_s2t.csv')
         
        if mode == 'Support 1 from':
            df = pd.read_csv('Annualised ROI/July07_2025/compound_return_s1f.csv')    
         
        if mode == 'Support 1 to':
            df = pd.read_csv('Annualised ROI/July07_2025/compound_return_s1t.csv')
        
        # Apply CSS styling to position the buttons in the top-right corner
        # Add CSS styling to adjust the button positioning
        st.markdown(
            """
            <style>
            .stButton button {
                margin-right: 10px;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        # Create a container to hold the buttons
        button_container = st.container()
        
        # Add the buttons to the container
        with button_container:
            col1, col2 = st.columns(2)
            plot_button = col1.button("Graph")
            st.write("")
            table_button = col2.button("Data")
        
        fig = px.line(df, x='Date', y='Gain', labels={'x': 'Date', 'y': 'ROI'})
    
        # Customize the layout
        fig.update_layout(
            autosize=True,
            height=800,
            margin=dict(l=40, r=40, t=40, b=40),
        )
        
        # Create an empty placeholder for the content
        content_placeholder = st.empty()
        if plot_button:
            
            
        
            # Display the graph in Streamlit
            content_placeholder.plotly_chart(fig)
            
        if table_button:
            
            df = df[['Date','Investment','Gain','Avg_duration','Compound_Return']]
            content_placeholder.dataframe(df)
            
        else:
            # Display the graph in Streamlit
            content_placeholder.plotly_chart(fig)
            
    
    
    if report_options == 'Annualised ROI with Investment':
        mode = st.sidebar.radio('Choose Support mode', ('Support 2 from', 'Support 2 to', 'Support 1 from', 'Support 1 to'))
        
        if mode == 'Support 2 from':
            # Read the data
            df = pd.read_csv('Annualised ROI/July07_2025/compound_return_s2f.csv')
        if mode == 'Support 2 to':
            df = pd.read_csv('Annualised ROI/July07_2025/compound_return_s2t.csv')
         
        if mode == 'Support 1 from':
            df = pd.read_csv('Annualised ROI/July07_2025/compound_return_s1f.csv')    
         
        if mode == 'Support 1 to':
            df = pd.read_csv('Annualised ROI/July07_2025/compound_return_s1t.csv')    
            
            
        investment_list= df['DailyInvestment'].tolist()
        
        # Create subplots and mention plot grid size
        fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.03,
                            subplot_titles=('Absolute Return', 'Investment'), row_width=[0.2, 0.7])
        
        # Plot the absolute return on the first row
        fig.add_trace(go.Scatter(x=df['Date'], y=df['Gain'], mode='lines', name='return_amount'), row=1, col=1)
        
        # Bar trace for investment on the second row without legend
        fig.add_trace(go.Bar(x=df['Date'], y=investment_list, showlegend=False), row=2, col=1)
        
        # Customize the layout
        fig.update_layout(
            autosize=True,
            height=1000,
        )
        
        fig.update_yaxes(automargin=True)
        
        
        # Apply CSS styling to position the buttons in the top-right corner
        # Add CSS styling to adjust the button positioning
        st.markdown(
            """
            <style>
            .stButton button {
                margin-right: 10px;
            }
            </style>
            """,
            unsafe_allow_html=True
        )
        # Create a container to hold the buttons
        button_container = st.container()
        
        # Add the buttons to the container
        with button_container:
            col1, col2 = st.columns(2)
            plot_button = col1.button("Graph")
            st.write("")
            table_button = col2.button("Data")
        
        # Create an empty placeholder for the content
        content_placeholder = st.empty()
    
        
        if plot_button:
            content_placeholder.plotly_chart(fig)
            
        if table_button:
            df = df[['Date','Investment','Gain','Avg_duration','Compound_Return']]
            content_placeholder.dataframe(df)
            
        else:
            # Display the graph in Streamlit
            content_placeholder.plotly_chart(fig)
        
        
        
    
        
    if report_options == 'Compound Return':
        mode = st.sidebar.radio('Choose Support mode' , (['Support 2 from', 'Nifty50','NiftyMidCap50','NiftySmallCap50' , 'Compare']))
        
        if mode !='Compare':
        
            if mode == 'Support 2 from':
                
                # Read the data
                df = pd.read_csv('Annualised ROI/July07_2025/compound_return_s2f.csv')
                
            if mode == 'Nifty50':
                # Read the data
                df = pd.read_csv('Annualised ROI/July07_2025/Compound_Return_Nifty50.csv')
            
            if mode == 'NiftyMidCap50':
                # Read the data
                df = pd.read_csv('Annualised ROI/July07_2025/Compound_Return_NiftyMidcap50.csv')
                  
            if mode == 'NiftySmallCap50':
                # Read the data
                df = pd.read_csv('Annualised ROI/July07_2025/Compound_Return_NiftySmallcap50.csv')
              
            
            
            
            # Slice the DataFrame to select rows starting from index 140 onwards
            df_sliced = df[140:]
            
            # Create the line graph
            fig = px.line(x=df_sliced['Date'], y=df_sliced['Compound_Return'], labels={'x':'Date', 'y':'ROI'})
            
            # Customize the layout
            fig.update_layout(
                autosize=True,
                height=1000,
            )
            
            fig.update_yaxes(automargin=True)
            
            # Apply CSS styling to position the buttons in the top-right corner
            # Add CSS styling to adjust the button positioning
            st.markdown(
                """
                <style>
                .stButton button {
                    margin-right: 10px;
                }
                </style>
                """,
                unsafe_allow_html=True
            )
            # Create a container to hold the buttons
            button_container = st.container()
            
            # Add the buttons to the container
            with button_container:
                col1, col2 = st.columns(2)
                plot_button = col1.button("Graph")
                st.write("")
                table_button = col2.button("Data")
            
            # Create an empty placeholder for the content
            content_placeholder = st.empty()
    
            
            if plot_button:
                content_placeholder.plotly_chart(fig)
                
            if table_button:
                df = df[['Date','Investment','Gain','Avg_duration','Compound_Return']]
                content_placeholder.dataframe(df)
                
            else:
                # Display the graph in Streamlit
                content_placeholder.plotly_chart(fig)
        
        
        
        if mode == 'Compare':
        # Read the data
            df_s2f = pd.read_csv('Annualised ROI/July07_2025/compound_return_s2f.csv')
            df_nifty50 = pd.read_csv('Annualised ROI/July07_2025/Compound_Return_Nifty50.csv')
            df_nifty_midcap50 = pd.read_csv('Annualised ROI/July07_2025/Compound_Return_NiftyMidcap50.csv')
            df_nifty_smallcap50 = pd.read_csv('Annualised ROI/July07_2025/Compound_Return_NiftySmallcap50.csv')
            
            # Set default options
            selected_options = ['Support 2 from','Nifty50']
            
            # Display the checkboxes for selecting options
            selected_options = st.sidebar.multiselect('Select Options', ['Nifty50', 'NiftyMidCap50', 'NiftySmallCap50', 'Support 2 from'], default=selected_options)
            
            if selected_options:
                fig = make_subplots(rows=len(selected_options), cols=1, subplot_titles=selected_options, shared_xaxes=True)
            
                # Counter for row index
                row = 1
            
                # Plot the selected options
                if 'Support 2 from' in selected_options:
                    df_s2f = df_s2f[140:]
                    fig.add_trace(go.Scatter(x=df_s2f['Date'], y=df_s2f['Compound_Return'], name='Support 2 from'), row=row, col=1)
                    row += 1
            
                if 'Nifty50' in selected_options:
                    df_nifty50 = df_nifty50[140:]
                    fig.add_trace(go.Scatter(x=df_nifty50['Date'], y=df_nifty50['Compound_Return'], name='Nifty50'), row=row, col=1)
                    row += 1
            
                if 'NiftyMidCap50' in selected_options:
                    # Read the data and plot NiftyMidCap50
                    df_nifty_midcap50 = df_nifty_midcap50[140:]
                    fig.add_trace(go.Scatter(x=df_nifty_midcap50['Date'], y=df_nifty_midcap50['Compound_Return'], name='NiftyMidcap50'), row=row, col=1)
                    row += 1
                    
            
                if 'NiftySmallCap50' in selected_options:
                    # Read the data and plot NiftySmallCap50
                    df_nifty_smallcap50 = df_nifty_smallcap50[140:]
                    fig.add_trace(go.Scatter(x=df_nifty_smallcap50['Date'], y=df_nifty_smallcap50['Compound_Return'], name='NiftySmallcap50'), row=row, col=1)
                    row += 1
            
                # Update the layout
                fig.update_layout(height=800)
            
                # Display the graph in Streamlit
                st.plotly_chart(fig)
            else:
                st.info("Please select at least one option.")
                
                
                
        
    if report_options == 'User Buys on Every Report Date':
        
        
        #df = pd.read_csv('C:/Users/user-41305506/StreamlitProject - InvestorIdeas/Annualised ROI/compound_return_userbuysoneveryreportdate_31052023.csv')
        
        mode = st.sidebar.radio('Choose report type' , (['Annualised ROI' ,'Annualised ROI with Investment','Compound Return']))
        
        
        if mode == 'Annualised ROI':
            
            df = pd.read_csv('Annualised ROI/July07_2025/compound_return_userbuysoneveryreportdate.csv')
            
            
            fig = px.line(df, x='Date', y='Gain', labels={'x': 'Date', 'y': 'ROI'})
    
            # Customize the layout
            fig.update_layout(
                autosize=True,
                height=800,
                margin=dict(l=40, r=40, t=40, b=40),
            )
    
            # Apply CSS styling to position the buttons in the top-right corner
            # Add CSS styling to adjust the button positioning
            st.markdown(
                """
                <style>
                .stButton button {
                    margin-right: 10px;
                }
                </style>
                """,
                unsafe_allow_html=True
            )
            # Create a container to hold the buttons
            button_container = st.container()
            
            # Add the buttons to the container
            with button_container:
                col1, col2 = st.columns(2)
                plot_button = col1.button("Graph")
                st.write("")
                table_button = col2.button("Data")
            
            # Create an empty placeholder for the content
            content_placeholder = st.empty()
    
            
            if plot_button:
                content_placeholder.plotly_chart(fig)
                
            if table_button:
                df = df[['Date','Investment','Gain','Avg_duration','Compound_Return']]
                content_placeholder.dataframe(df)
                
            else:
                # Display the graph in Streamlit
                content_placeholder.plotly_chart(fig)
            
            
        if mode == 'Annualised ROI with Investment':
            
            df = pd.read_csv('Annualised ROI/July07_2025/compound_return_userbuysoneveryreportdate.csv')
            
            
            investment_list= df['DailyInvestment'].tolist()
            
            # Create subplots and mention plot grid size
            fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.03,
                                subplot_titles=('Absolute Return', 'Investment'), row_width=[0.2, 0.7])
            
            # Plot the absolute return on the first row
            fig.add_trace(go.Scatter(x=df['Date'], y=df['Gain'], mode='lines', name='return_amount'), row=1, col=1)
            
            # Bar trace for investment on the second row without legend
            fig.add_trace(go.Bar(x=df['Date'], y=investment_list, showlegend=False), row=2, col=1)
            
            # Customize the layout
            fig.update_layout(
                autosize=True,
                height=1000,
            )
            
            fig.update_yaxes(automargin=True)
            
            # Apply CSS styling to position the buttons in the top-right corner
            # Add CSS styling to adjust the button positioning
            st.markdown(
                """
                <style>
                .stButton button {
                    margin-right: 10px;
                }
                </style>
                """,
                unsafe_allow_html=True
            )
            # Create a container to hold the buttons
            button_container = st.container()
            
            # Add the buttons to the container
            with button_container:
                col1, col2 = st.columns(2)
                plot_button = col1.button("Graph")
                st.write("")
                table_button = col2.button("Data")
            
            # Create an empty placeholder for the content
            content_placeholder = st.empty()
    
            
            if plot_button:
                content_placeholder.plotly_chart(fig)
                
            if table_button:
                df = df[['Date','Investment','Gain','Avg_duration','Compound_Return']]
                content_placeholder.dataframe(df)
                
            else:
                # Display the graph in Streamlit
                content_placeholder.plotly_chart(fig)
            
            
            
        if mode == 'Compound Return':
            
            df = pd.read_csv('Annualised ROI/July07_2025/compound_return_userbuysoneveryreportdate.csv')
            
            
            # Slice the DataFrame to select rows starting from index 140 onwards
            df = df[140:]
            
            # Create the line graph
            fig = px.line(x=df['Date'], y=df['Compound_Return'], labels={'x':'Date', 'y':'ROI'})
            
            # Customize the layout
            fig.update_layout(
                autosize=True,
                height=1000,
            )
            
            fig.update_yaxes(automargin=True)
            
            # Apply CSS styling to position the buttons in the top-right corner
            # Add CSS styling to adjust the button positioning
            st.markdown(
                """
                <style>
                .stButton button {
                    margin-right: 10px;
                }
                </style>
                """,
                unsafe_allow_html=True
            )
            # Create a container to hold the buttons
            button_container = st.container()
            
            # Add the buttons to the container
            with button_container:
                col1, col2 = st.columns(2)
                plot_button = col1.button("Graph")
                st.write("")
                table_button = col2.button("Data")
            
            # Create an empty placeholder for the content
            content_placeholder = st.empty()
    
            
            if plot_button:
                content_placeholder.plotly_chart(fig)
                
            if table_button:
                df = df[['Date','Investment','Gain','Avg_duration','Compound_Return']]
                content_placeholder.dataframe(df)
                
            else:
                # Display the graph in Streamlit
                content_placeholder.plotly_chart(fig)
            
            
            
    if report_options == 'Daywise Absolute Return':
        
        mode = st.sidebar.radio('Choose plot type' , (['Line Chart' , 'Bar Plot']))
        
        
        
        if mode == 'Line Chart':
            
            df = pd.read_csv('Annualised ROI/July07_2025/daywise_return.csv')
            
            
            # Create subplots and mention plot grid size
            fig = make_subplots(rows=2, cols=1, shared_xaxes=True, 
                                vertical_spacing=0.03, subplot_titles=('Absolute Return', 'Investment'), 
                                row_width=[0.2, 0.7])
            
            # Plot the absolute return on the first row
            fig.add_trace(go.Scatter(x=df['date'], y= df['annual_return'], mode='lines', name='return_amount'), row=1, col=1)
            
            # Bar trace for investment on the second row without legend
            fig.add_trace(go.Bar(x=df['date'], y=df['Investment'], showlegend=False), row=2, col=1)
            
            fig.update_layout(
                autosize=True,
                height=1000,
            )
            
            fig.update_yaxes(automargin=True)
            
            # Apply CSS styling to position the buttons in the top-right corner
            # Add CSS styling to adjust the button positioning
            st.markdown(
                """
                <style>
                .stButton button {
                    margin-right: 10px;
                }
                </style>
                """,
                unsafe_allow_html=True
            )
            # Create a container to hold the buttons
            button_container = st.container()
            
            # Add the buttons to the container
            with button_container:
                col1, col2 = st.columns(2)
                plot_button = col1.button("Graph")
                st.write("")
                table_button = col2.button("Data")
            
            # Create an empty placeholder for the content
            content_placeholder = st.empty()
    
            
            if plot_button:
                content_placeholder.plotly_chart(fig)
                
            if table_button:
                df = df[['date','annual_return']]
                content_placeholder.dataframe(df)
                
            else:
                # Display the graph in Streamlit
                content_placeholder.plotly_chart(fig)
            
            
            
        if mode == 'Bar Plot':
            
            df = pd.read_csv('Annualised ROI/July07_2025/daywise_return.csv')
            
            
            high_low_final=df['high_low'].tolist()
            
            # Initialize empty lists
            l = []
            h = []
            
            # Iterate over high_low_final
            for i in high_low_final:
                #i = [float(x) for x in i]
                #i=ast.literal_eval(i)
                low = i[0]
                high = i[-1]
                l.append(low)
                h.append(high)
            
            
            # Create subplots and mention plot grid size
            fig = make_subplots(rows=2, cols=1, shared_xaxes=True,
                                vertical_spacing=0.03, subplot_titles=('Absolute Return', 'Investment'),
                                row_width=[0.2, 0.7])
            
            # Add scatter plot for absolute return
            fig.add_trace(go.Scatter(x=df['date'], y=df['annual_return'], mode='markers', opacity=1.0, name='Absolute Return'))
            
            
            
            # Add bar plot for minimum
            fig.add_trace(go.Bar(x=df['date'], y=l, opacity=1.0, name='Minimum'))
            
            # Add bar plot for maximum
            fig.add_trace(go.Bar(x=df['date'], y=h, opacity=1.0, name='Maximum'))
            
            # Add bar plot for investment
            fig.add_trace(go.Bar(x=df['date'], y=df['Investment'], showlegend=True, name='Investment'), row=2, col=1)
            
            # Update layout
            fig.update_layout(autosize=True, height=1000)
            
            # Update y-axes
            fig.update_yaxes(automargin=True)
            
            # Apply CSS styling to position the buttons in the top-right corner
            # Add CSS styling to adjust the button positioning
            st.markdown(
                """
                <style>
                .stButton button {
                    margin-right: 10px;
                }
                </style>
                """,
                unsafe_allow_html=True
            )
            # Create a container to hold the buttons
            button_container = st.container()
            
            # Add the buttons to the container
            with button_container:
                col1, col2 = st.columns(2)
                plot_button = col1.button("Graph")
                st.write("")
                table_button = col2.button("Data")
            
            # Create an empty placeholder for the content
            content_placeholder = st.empty()
    
            
            if plot_button:
                content_placeholder.plotly_chart(fig)
                
            if table_button:
                df = df[['date','annual_return']]
                content_placeholder.dataframe(df)
                
            else:
                # Display the graph in Streamlit
                content_placeholder.plotly_chart(fig)

except FileNotFoundError:
        st.error("Data is unavailable. We are working on it.")
#except Exception as e:
    #st.error(e)
           
except:      
      st.error("There is an issue. We are looking into it")  

    




#st.set_option('deprecation.showPyplotGlobalUse', False)