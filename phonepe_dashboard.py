import pandas as pd
import plotly.express as pltexp
import streamlit as st
import warnings
import plotly.graph_objects as go
from plotly.subplots import make_subplots

warnings.filterwarnings("ignore")
st.set_page_config(layout="wide")

# DATASETS
Transaction_df = pd.read_csv(r'Transaction.csv')
User_Summary_df = pd.read_csv(r'Transaction_Summary.csv')
User_df = pd.read_csv(r'User_Table.csv')
Geo_Dataset = pd.read_csv(r'Data_Map_Districts_Longitude_Latitude.csv')
states = pd.read_csv(r'Data_Map_IndiaStates_TU.csv')
Map_Transaction_df = pd.read_csv(r'Map_Transaction.csv')
Map_User = pd.read_csv(r'Map_User.csv')
Indian_States = pd.read_csv(r'Longitude_Latitude_State_Table.csv')
colT1, colT2 = st.columns([2, 8])
with colT2:
    st.title('     :red[DATA ANALYSIS] :green[PHONPE] :money_with_wings:   ')

# INDIA MAP ANALYSIS

c1, c2 = st.columns(2)
with c1:
    Year = st.selectbox(
        'Select the Year',
        ('2018', '2019', '2020', '2021', '2022'))
with c2:
    Quarter = st.selectbox(
        'Select the Quarter',
        ('1', '2', '3', '4'))
year = int(Year)
quarter = int(Quarter)
Transaction_districts = Map_Transaction_df.loc[(Map_Transaction_df['Year'] == year) & (Map_Transaction_df['Quarter'] == quarter)].copy()
Transaction_States = Transaction_districts[Transaction_districts["State"] == "state"]
Transaction_districts.drop(Transaction_districts.index[(Transaction_districts["State"] == "state")], axis=0, inplace=True)

# Dynamic Scattergeo Data Generation
Transaction_districts = Transaction_districts.sort_values(by=['Place Name'], ascending=True)
Geo_Dataset = Geo_Dataset.sort_values(by=['District'], ascending=True)
Total_Amount = []
for i in Transaction_districts['Total Amount']:
    Total_Amount.append(i)
Geo_Dataset['Total Amount'] = pd.Series(Total_Amount)
Total_Transaction = []
for i in Transaction_districts['Total Transactions count']:
    Total_Transaction.append(i)
Geo_Dataset['Total Transactions'] = pd.Series(Total_Transaction)
Geo_Dataset['Year Quarter'] = str(year) + '-Q' + str(quarter)
# Dynamic Istates
Istates = states.sort_values(by=['state'], ascending=True)
Transaction_States = Transaction_States.sort_values(by=['Place Name'], ascending=True)
Transaction_States['State'] = states['state']
ta = Transaction_districts.groupby('State')['Total Amount'].sum()
ttc = Transaction_districts.groupby('State')['Total Transactions count'].sum()
Transaction_States['Total Amount'] = list(ta)
Transaction_States['Total Transactions count'] = list(ttc)
Total_Amount = []
for i in Transaction_States['Total Amount']:
    Total_Amount.append(i)
Istates['Total Amount'] = Total_Amount
Total_Transaction = []
for i in Transaction_States['Total Transactions count']:
    Total_Transaction.append(i)
Istates['Total Transactions'] = Total_Transaction

# FIGURE1 INDIA MAP
# scatter plotting the states codes
Indian_States = Indian_States.sort_values(by=['state'], ascending=True)
Indian_States['Registered Users'] = Istates['Registered_Users']
Indian_States['Total Amount'] = Istates['Total Amount']
Indian_States['Total Transactions'] = Istates['Total Transactions']
Indian_States['Year Quarter'] = str(year)+'-Q'+str(quarter)
fig0 = pltexp.scatter_geo(Indian_States,
                          lon=Indian_States['Longitude'],
                          lat=Indian_States['Latitude'],
                          text=Indian_States['code'],
                          hover_name="state",
                          hover_data=['Total Amount', "Total Transactions", "Year Quarter"],
                          )
fig0.update_traces(marker=dict(color="white", size=0.3))
fig0.update_geos(fitbounds="locations", visible=False, )
# scatter plotting districts
Geo_Dataset['col'] = Geo_Dataset['Total Transactions']
fig1 = pltexp.scatter_geo(Geo_Dataset,
                          lon=Geo_Dataset['Longitude'],
                          lat=Geo_Dataset['Latitude'],
                          color=Geo_Dataset['col'],
                          size=Geo_Dataset['Total Transactions'],
                          # text = Scatter_Geo_Dataset['District'], #It will display district names on map
                          hover_name="District",
                          hover_data=["State", "Total Amount", "Total Transactions", "Year Quarter"],
                          title='District',
                          size_max=22, )
fig1.update_traces(marker=dict(color="rebeccapurple", line_width=1))
# choropleth mapping india
fig_cp = pltexp.choropleth(
                    Istates,
                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                    featureidkey='properties.ST_NM',
                    locations='state',
                    color="Total Transactions",
                    )
fig_cp.update_geos(fitbounds="locations", visible=False, )
# combining districts states and choropleth
fig_cp.add_trace(fig0.data[0])
fig_cp.add_trace(fig1.data[0])
st.write("# **:blue[VISUALIZE ON MAP:earth_asia:]**")
colT1, colT2 = st.columns([6, 4])
with colT1:
    st.plotly_chart(fig_cp, use_container_width=True)
with colT2:
    st.info(
           """
    Details of Map:
    - The darkness of the state color represents the total transactions
    - The Size of the Circles represents the total transactions dictrict wise
    - The bigger the Circle the higher the transactions
    - Hover data will show the details like Total transactions, Total amount
    """
    )
    st.info(
            """
    Important Observations:
    - User can observe Transactions of PhonePe in both statewide and Districtwide.
    - We can clearly see the states with highest transactions in the given year and quarter
    - We get basic idea about transactions district wide
    """
    )
# FIGURE2 BARGRAPH
Istates = Transaction_States.sort_values(by=['Total Transactions count'])
fig = pltexp.bar(Istates, x='State', y='Total Transactions count', title=str(year) + " Quarter-" + str(quarter))
with st.expander("See Bar graph for the same data"):
    st.plotly_chart(fig, use_container_width=True)
    st.info('**:blue[The above bar graph showing the increasing order of PhonePe Transactions according to the states of India, Here we can observe the top states with highest Transaction by looking at graph]**')


# TRANSACTIONS ANALYSIS
st.write('# :green[TRANSACTIONS ANALYSIS :bar_chart:]')
tab1, tab2, tab3, tab4 = st.tabs(["STATEWISE ANALYSIS", "DISTRICTWISE ANALYSIS", "YEARWISE ANALYSIS", "OVERALL ANALYSIS"])

# FIGURE1 STATE ANALYSIS
with tab1:
    Transaction = Transaction_df.copy()
    Transaction.drop(
        Transaction.index[(Transaction["State"] == "india")], axis=0, inplace=True)
    S_PayMode = Transaction.copy()
    # st.write('### :green[State & PaymentMode]')
    col1, col2 = st.columns(2)
    with col1:
        mode = st.selectbox(
            'Please select the Mode',
            ('Recharge & bill payments', 'Peer-to-peer payments', 'Merchant payments', 'Financial Services', 'Others'),
            key='a')
    with col2:
        state = st.selectbox(
            'Please select the State',
            ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
             'assam', 'bihar', 'chandigarh', 'chhattisgarh',
             'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
             'haryana', 'himachal-pradesh', 'jammu-&-kashmir',
             'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep',
             'madhya-pradesh', 'maharashtra', 'manipur', 'meghalaya', 'mizoram',
             'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan',
             'sikkim', 'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
             'uttarakhand', 'west-bengal'), key='b')
    State = state
    Year_List = [2018, 2019, 2020, 2021, 2022]
    Mode = mode
    S_PayMode = S_PayMode.loc[
        (S_PayMode['State'] == State) & (S_PayMode['Year'].isin(Year_List)) &
        (S_PayMode['Payment Mode'] == Mode)]
    S_PayMode = S_PayMode.sort_values(by=['Year'])
    S_PayMode["Quarter"] = "Q" + S_PayMode['Quarter'].astype(str)
    S_PayMode["Year Quarter"] = S_PayMode['Year'].astype(str) + "-" + S_PayMode[
        "Quarter"].astype(str)
    fig = pltexp.bar(S_PayMode, x='Year Quarter', y='Total Transactions count', color="Total Transactions count",
                     color_continuous_scale="Viridis")

    colT1, colT2 = st.columns([7, 3])
    with colT1:
        st.write('#### ' + State.upper())
        st.plotly_chart(fig, use_container_width=True)
    with colT2:
        st.info(
            """
            Details of BarGraph:
            - This entire data belongs to state selected by you
            - X Axis is basically all years with all quarters 
            - Y Axis represents total transactions in selected mode        
            """
        )
        st.info(
            """
            Important Observations:
            - User can observe the pattern of payment modes in a State 
            - We get basic idea about which mode of payments are either increasing or decreasing in a state
            """
        )

with tab2:
    col1, col2, col3= st.columns(3)
    with col1:
        Year = st.selectbox(
            'Please select the Year',
            ('2022', '2021','2020','2019','2018'),key='y12')
    with col2:
        state = st.selectbox(
        'Please select the State',
        ('andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
        'assam', 'bihar', 'chandigarh', 'chhattisgarh',
        'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
        'haryana', 'himachal-pradesh', 'jammu-&-kashmir',
        'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep',
        'madhya-pradesh', 'maharashtra', 'manipur', 'meghalaya', 'mizoram',
        'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan',
        'sikkim', 'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
        'uttarakhand', 'west-bengal'),key='dk2')
    with col3:
        Quarter = st.selectbox(
            'Please select the Quarter',
            ('1', '2', '3','4'),key='qwe2')
    districts = Map_User.loc[(Map_User['State'] == state ) & (Map_User['Year']==int(Year))
                                          & (Map_User['Quarter']==int(Quarter))]
    l=len(districts)
    fig = pltexp.bar(districts, x='Place Name', y='App Openings',color="App Openings",
                 color_continuous_scale="reds")
    colT1,colT2 = st.columns([7,3])
    with colT1:
        if l:
            st.write('#### '+state.upper()+' WITH '+str(l)+' DISTRICTS')
            st.plotly_chart(fig,use_container_width=True)
        else:
            st.write('#### NO DISTRICTS DATA AVAILABLE FOR '+state.upper())

    with colT2:
        if l:
            st.info(
        """
        Details of BarGraph:
        - This entire data belongs to state selected by you
        - X Axis represents the districts of selected state
        - Y Axis represents App Openings       
        """
            )
            st.info(
        """
        Important Observations:
        - User can observe how App Openings are happening in districts of a selected state 
        - We can observe the leading district in a state 
        """
            )

with tab3:
    st.write('### :orange[Brand Share] ')
    col1, col2 = st.columns(2)
    with col1:
        state = st.selectbox(
            'Please select the State',
            ('india', 'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh',
             'assam', 'bihar', 'chandigarh', 'chhattisgarh',
             'dadra-&-nagar-haveli-&-daman-&-diu', 'delhi', 'goa', 'gujarat',
             'haryana', 'himachal-pradesh', 'jammu-&-kashmir',
             'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep',
             'madhya-pradesh', 'maharashtra', 'manipur', 'meghalaya', 'mizoram',
             'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan',
             'sikkim', 'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh',
             'uttarakhand', 'west-bengal'), key='Z')
    with col2:
        Y = st.selectbox(
            'Please select the Year',
            ('2018', '2019', '2020', '2021', '2022'), key='X')
    y = int(Y)
    s = state
    brand = User_df[User_df['Year'] == y]
    brand = User_df.loc[
        (User_df['Year'] == y) & (User_df['State'] == s)]
    myb = brand['Brand Name'].unique()
    x = sorted(myb).copy()
    b = brand.groupby('Brand Name').sum()
    b['brand'] = x
    br = b['Registered Users Count'].sum()
    labels = b['brand']
    values = b['Registered Users Count']  # customdata=labels,
    fig3 = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.4, textinfo='label+percent',
                                  texttemplate='%{label}<br>%{percent:1%f}', insidetextorientation='horizontal',
                                  textfont=dict(color='#000000'), marker_colors=pltexp.colors.qualitative.Prism)])

    colT1, colT2 = st.columns([7, 3])
    with colT1:
        st.write("#### ", state.upper() + ' IN ' + Y)
        st.plotly_chart(fig3, use_container_width=True)
    with colT2:
        st.info(
            """
            Details of Donut Chart:        
            - Initially we select data by means of State and Year
            - Percentage of registered users is represented with dounut chat through Device Brand
            """
        )
        st.info(
            """
            Important Observations:
            - User can observe the top leading brands in a particular state
            - Brands with less users
            - Brands with high users
            - Can make app download advices to growing brands
            """
        )

    b = b.sort_values(by=['Registered Users Count'])
    fig4 = pltexp.bar(b, x='brand', y='Registered Users Count', color="Registered Users Count",
                  title='In ' + state + 'in ' + str(y),
                  color_continuous_scale="oranges", )
    with st.expander("See Bar graph for the same data"):
        st.plotly_chart(fig4, use_container_width=True)

with tab4:
        years = Map_User.groupby('Year')
        years_List = Map_User['Year'].unique()
        years_Table = years.sum()
        del years_Table['Quarter']
        years_Table['year'] = years_List
        total_trans = years_Table['Registered Users Count'].sum()
        fig1 = pltexp.pie(years_Table, values='Registered Users Count', names='year',
                      color_discrete_sequence=pltexp.colors.sequential.RdBu, title='TOTAL REGISTERED USERS (2018 TO 2022)')
        col1, col2 = st.columns([0.7, 0.3])
        with col1:
            labels = ["US", "China", "European Union", "Russian Federation", "Brazil", "India",
                      "Rest of World"]

            # Create subplots: use 'domain' type for Pie subplot
            fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'domain'}, {'type': 'domain'}]])
            fig.add_trace(
                go.Pie(labels=years_Table['year'], values=years_Table['Registered Users Count'], name="REGISTERED USERS"),
                1, 1)
            fig.add_trace(go.Pie(labels=years_Table['year'], values=years_Table['App Openings'], name="APP OPENINGS"),
                          1, 2)

            # Use `hole` to create a donut-like pie chart
            fig.update_traces(hole=.6, hoverinfo="label+percent+name")

            fig.update_layout(
                title_text="USERS DATA (2018 TO 2022)",
                # Add annotations in the center of the donut pies.
                annotations=[dict(text='USERS', x=0.18, y=0.5, font_size=20, showarrow=False),
                             dict(text='APP', x=0.82, y=0.5, font_size=20, showarrow=False)])
            # st.plotly_chart(fig1)
            st.plotly_chart(fig)
        with col2:
            # st.write('#### :green[Year Wise Transaction Analysis in INDIA]')
            st.markdown(years_Table.style.hide(axis="index").to_html(), unsafe_allow_html=True)
            st.info(
                """
                Important Observation:
                -  We can see that the Registered Users and App openings are increasing year by year
    
                """
            )

# Top ranking of states
st.write('# :orange[:bulb: KNOW THE TOP:three: STATES ]')
c1, c2 = st.columns(2)
with c1:
    Year = st.selectbox(
        'Please select the Year',
        ('2022', '2021', '2020', '2019', '2018'), key='y1h2k')
with c2:
    Quarter = st.selectbox(
        'Please select the Quarter',
        ('1', '2', '3', '4'), key='qgwe2')
Data_Map_User_df = User_Summary_df.copy()
top_states = Map_User.loc[
    (Map_User['Year'] == int(Year)) & (Map_User['Quarter'] == int(Quarter))]
top_states_r = top_states.sort_values(by=['Registered Users Count'], ascending=False)
top_states_a = top_states.sort_values(by=['App Openings'], ascending=False)

top_states_T = Transaction_df.loc[
    (Transaction_df['Year'] == int(Year)) & (Transaction_df['Quarter'] == int(Quarter))]
topst = top_states_T.groupby('State')
x = topst.sum().sort_values(by=['Total Transactions count'], ascending=False)
y = topst.sum().sort_values(by=['Total Amount'], ascending=False)
col1, col2, col3, col4 = st.columns([2.5, 2.5, 2.5, 2.5])
with col1:
    rt = top_states_r[1:4]
    st.markdown("#### :red[:round_pushpin: Registered Users]")
    st.markdown(rt[['State', 'Registered Users Count']].style.hide(axis="index").to_html(), unsafe_allow_html=True)
with col2:
    at = top_states_a[1:4]
    st.markdown("#### :red[:round_pushpin: PhonePe App Openings]")
    st.markdown(at[['State', 'App Openings']].style.hide(axis="index").to_html(), unsafe_allow_html=True)
with col3:
    st.markdown("#### :red[:round_pushpin: Total Transactions]")
    st.write(x[['Total Transactions count']][1:4])
with col4:
    st.markdown("#### :red[:round_pushpin: Total Amount]")
    st.write(y['Total Amount'][1:4])
