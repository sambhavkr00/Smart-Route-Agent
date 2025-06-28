import streamlit as st
from chains.news_chain import get_recent_disruptions
from chains.traffic_chain import get_traffic_data
from chains.weather_chain import get_weather_forecast
from chains.summarize_chain import summarize_all

def main():
    st.title("Smart Route Agent")
    st.write("Enter delivery details to get a concise summary of risks and recommendations.")

    source = st.text_input("Source Address")
    destination = st.text_input("Destination Address")
    date_obj = st.date_input("Date of Delivery")
    date = date_obj.strftime("%Y-%m-%d") if date_obj else None

    if st.button("Get Delivery Summary"):
        if not source or not destination or not date:
            st.warning("Please fill in all fields.")
            return
        with st.spinner("Collecting news..."):
            disruptions = get_recent_disruptions(source, destination, date)
        with st.spinner("Checking traffic..."):
            traffic = get_traffic_data(source, destination)
        with st.spinner("Fetching weather..."):
            weather = get_weather_forecast(destination, date)
        with st.spinner("Generating summary..."):
            summary = summarize_all(disruptions, traffic, weather, source, destination, date)
        st.subheader("Delivery Summary")
        st.write(summary or "No summary generated.")

if __name__ == "__main__":
    main()
