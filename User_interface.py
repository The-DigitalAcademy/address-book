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
    Column('address', VARCHAR),
    Column('postcode', Integer),
    Column('province', VARCHAR),
    Column('search_count', Integer),
    extend_existing=True
)




def search_details():
    def search():
        details_df = pd.DataFrame(engine.execute("SELECT * FROM details").fetchall())
        
        search = st.text_input("Enter Search: ")
        if search in details_df[3].to_list():
            count = (update(details).where(details.c.address == search)).values(search_count=details.c.search_count + 1)
            engine.execute(count)
            st.write(details_df[3])
        st.write("Popular is search is:",details_df[3].loc[details_df[7].idxmax()],"searched",details_df[7].loc[details_df[7].idxmax()],"times")
        
    
    def display():
        details_df = pd.DataFrame(engine.execute("SELECT * FROM details").fetchall())
        st.write(details_df)
    
    with st.form(key='dispaly options'):
        st.write("1. Display details\n")
        st.write("2. Search Address\n")
        option = st.text_input("Enter Option: ")
        st.form_submit_button('Go!')
    
    while option != '3':
        
        if option == '1':
            display()
            break
        elif option == '2':
            search()
            break
        else:
            break
        
def insert_new():

    new_name = st.text_input("Enter Your Name and Surname: ")
    new_email = st.text_input("Enter Your Email: ")
    new_add = st.text_input("Enter Address: ")
    phone = st.text_input("Enter Phone Number: ")
    post_code = st.number_input("Enter Postal code")
    pro_vinces = st.text_input("Enter Province ")

    inserting = details.insert().values(names=new_name,email=new_email,address=new_add,contact=phone,postcode=post_code,province=pro_vinces,search_count=0)
    engine.execute(inserting)
    st.write("Record Added Successfully")

def modify():

    name = st.text_input("Enter Name and Surname for Record you want to Modify:")
    new_name = st.text_input("Enter Your New Name and Surname: ")
    new_email = st.text_input("Enter Your New Email: ")
    new_add = st.text_input("Enter Your New Address: ")
    phone = st.text_input("Enter Your New Phone Number: ")
    post_code = st.number_input("Enter Postal code")
    pro_vinces = st.text_input("Enter Province ")

    updated = update(details).where(details.c.names == name).values(names=new_name,email=new_email,address=new_add,contact=phone,postcode=post_code,province=pro_vinces)
    engine.execute(updated)
    st.write("Record Updated Successfully")

def delete_detail():
    
    name = st.text_input("Enter Name and Surname for Record you want to Delete:")
    to_delete = delete(details).where(details.c.names == name)
    engine.execute(to_delete)
    st.write("Record Deleted Successfully")
    



st.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
st.markdown("<h1 style='text-align: center; color: white;'>Address Book Service</h1>", unsafe_allow_html=True)
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
    
st.multiselect('Locations', ['house num','str name','province','city','postcode'])
st.text_input('Enter Search: ')

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
