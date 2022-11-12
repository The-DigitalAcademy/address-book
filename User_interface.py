from sqlalchemy import create_engine, MetaData, Table, Column,insert, Integer, VARCHAR, update, delete,select, func
import pandas as pd
import streamlit as st

st.set_page_config(layout='wide',page_title='Address Book',page_icon='📚')

engine = create_engine("postgresql://postgres:postgres@localhost:5430/address_book")

# initialize the Metadata Object
meta = MetaData(bind=engine)
MetaData.reflect(meta)
  
# create a table schema
# create a table schema
details = Table(
    'details',meta , 
    Column('id', Integer, primary_key=True),
    Column('names', VARCHAR),
    Column('email', VARCHAR),
    Column('contact', VARCHAR),
    extend_existing=True
)

locations =  Table(
    'locations' ,meta ,
    Column('id', Integer, foreign_key=True),
    Column('street_name', VARCHAR),
    Column('house_number', VARCHAR),
    Column('city', VARCHAR),
    Column('postcode', VARCHAR),
    Column('province', VARCHAR),
    Column('search_count', Integer),
    extend_existing=True
)


def search_details():
    def search():
        with st.form(key='search'):
            details_df = pd.DataFrame(engine.execute("SELECT * FROM details").fetchall())
            search = st.text_input("Enter Search: ")
            if search in details_df[3].to_list():
                count = (update(details).where(details.c.address == search)).values(search_count=details.c.search_count + 1)
                engine.execute(count)
                st.write(details_df[3])
            st.form_submit_button('Sumbit!')
        st.write("Popular is search is:")
        st.write(details_df[3].loc[details_df[7].idxmax()],"searched",details_df[7].loc[details_df[7].idxmax()],"times")
        
        
    
    def display():
        with st.form(key='display'):
            details_df = pd.DataFrame(engine.execute("SELECT * FROM details").fetchall(),columns=['id','names','email','contact'])
            locations_df = pd.DataFrame(engine.execute("SELECT * FROM locations").fetchall(),columns=['id','street_name','house_number','city','postcode','province','search_count'])
            all_df = details_df.merge(locations_df, how = 'inner', on = ['id'])
            st.write(all_df)
            st.form_submit_button('Okay!')
                   
    
    with st.form(key='display options'):
        st.write("1. Display details\n")
        st.write("2. Search Address\n")
        option = st.text_input("Enter Option: ")
        st.form_submit_button('Submit!')
    
    while option is not False:
        
        if option == '1':
            display()
            break
        elif option == '2':
            search()
            break
        else:
            break
        
def insert_new():
    with st.form(key='insert'):
        new_id = st.text_input("Enter Your ID: ")
        new_email = st.text_input("Enter Your Email: ")
        new_add = st.text_input("Enter Address: ")
        new_contact = st.text_input("Enter Contact Number:")
        details_insert = details.insert().values(id=new_id,email=new_email,address=new_add,contact=new_contact,postcode=post_code,province=pro_vinces,search_count=0)
        engine.execute(details_insert)

        new_street_name = st.text_input("Enter Street Name:")
        new_house_number = st.text_input("Enter House Number:")
        new_city = st.text_input("Enter City:")
        post_code = st.text_input("Enter Postal code:")
        pro_vinces = st.text_input("Enter Province:")
        locations_insert = locations.insert().values(street_name=new_street_name,house_number=new_house_number,city=new_city,search_count=0)
        engine.execute(locations_insert)
        st.form_submit_button('Submit!')
        

def modify():
    with st.form(key='modify_details'):
        id = st.number_input("Enter ID for the Record you want to Modify:")
        new_name = st.text_input("Enter Your New Name and Surname: ")
        new_email = st.text_input("Enter Your New Email: ")
        phone = st.text_input("Enter Your New Phone Number: ")
        updated_details = update(details).where(details.c.id == id).values(names=new_name,email=new_email,contact=phone)
        engine.execute(updated_details)
        st.form_submit_button('Submit!')
        
    with st.form(key='modify_locations'):
        new_street_name = st.text_input("Enter Street Name: ")
        new_house_num = st.text_input("Enter House number: ")
        new_city = st.text_input("Enter City: ")
        post_code = st.text_input("Enter Postal code: ")
        pro_vinces = st.text_input("Enter Province: ")
        updated_locations = update(locations).where(locations.c.id == id).values(street_name=new_street_name,house_number=new_house_num,city=new_city,postcode=post_code,province=pro_vinces,search_count=0)
        engine.execute(updated_locations)
        st.form_submit_button('Submit!')
        

def delete_detail():
    with st.form(key='delete'):
        id = st.text_input("Enter ID for Record you want to Delete:")
        to_delete = delete(details).where(details.c.id == id)
        engine.execute(to_delete)
        st.form_submit_button('Submit!')
    



st.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
st.markdown("<h1 style='text-align: center; color: white;'>Address Book Service</h1>", unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; color: white;'>📚</h1>", unsafe_allow_html=True)
st.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
st.markdown("<h2 style='text-align: center; color: white;'>Welcome!</h2>", unsafe_allow_html=True)
st.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


with st.form(key='main menu'):
    st.markdown("<p style='text-align: center; color: white;'>1. Add details\n</p>",unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: white;'>2. Modify details\n</p>",unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: white;'>3. Delete details\n</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: white;'>4. Show all Details and Address count\n</p>",unsafe_allow_html=True)
    options = st.text_input("Enter option: ")
    st.form_submit_button('Go!')

while options is not False:
    
    if options == '1':
        insert_new()
        break
    elif options == '2':
        modify()
        break
    elif options == '3':
        delete_detail()
        break
    elif options == '4':
        search_details()
        break
    else:
        break
