import streamlit as st

def calculate_bmi(weight, height):
    return weight / ((height / 100) ** 2)  # converting height from cm to meters

def interpret_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    st.set_page_config(page_title="BMI Calculator", page_icon=":heart:")
    
    # Customizing the color and background
    st.markdown(
        """
        <style>
        .reportview-container {
            background: #f0f3f6;
        }
        .sidebar .sidebar-content {
            background: #33cccc;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.sidebar.title("About")
    st.sidebar.info(
        "This is a simple BMI (Body Mass Index) calculator. "
        "It takes your weight and height as input and calculates your BMI."
    )
    
    st.sidebar.title("Connect with Me")
    st.sidebar.info(
        "Follow me on [GitHub](https://github.com/muhammadibrahim313) | "
        "Connect with me on [LinkedIn](https://www.linkedin.com/in/muhammad-ibrahim-qasmi-9876a1297/) | "
        "Find me on [Kaggle](https://www.kaggle.com/muhammadibrahimqasmi)"
    )

    st.title("BMI Calculator")

    weight = st.sidebar.number_input("Enter your weight (in kg)", min_value=0.0)
    height = st.sidebar.number_input("Enter your height (in cm)", min_value=0.0)

    gender = st.sidebar.radio("Select your gender", ("Male", "Female", "Other"))

    if st.sidebar.button("Calculate BMI"):
        bmi = calculate_bmi(weight, height)
        result = interpret_bmi(bmi)

        st.write(f"Your BMI: {bmi:.2f}")
        st.write(f"Interpretation: {result}")

        # Adding download link for result
        download_link = f"Click here to download BMI result: [BMI Result]({bmi}, {result})"
        st.markdown(download_link, unsafe_allow_html=True)
    
    st.markdown(
        """
        <hr style="border: 1px solid white;">
        <p style="font-size: 12px; color: gray; text-align: center;">
        Developed with ❤️ by [MUHAMMAD IBRAHIM ]
        </p>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
