import random
import pandas as pd
import zipcodes as zips

def generate_life_insurance_data(num_records):

    zip_codes = []

    for zip in zips.list_all():

        zip_codes.append(zip['zip_code'])


    data = {
        "Age": [],
        "BMI": [],
        "ZIP Code": [],
        "Children": [],
        "Annual Premium": [],
        #"Premium Frequency": [],
        "Premium Amount": [],
        "Policy Lapsed": [],
        "Policy Face Value": [],
        "Rider_Accidental Death": [],
        "Rider_Critical Illness": [],
        "Rider_Waiver of Premium": [],
        "Gender_Male": [],
        "Gender_Female": [],
        "Smoker_Yes": [],
        "Smoker_No": [],
        "Premium_Frequency_Monthly": [],
        "Premium_Frequency_Quarterly": [],
        "Premium_Frequency_Semiannual": [],
        "Premium_Frequency_Annual": []
    }
    
    # Define possible values for each attribute
    genders = ["Male", "Female"]
    smoker_status = ["Yes", "No"]
    zip_codes = zip_codes
    premium_frequencies = ["Monthly", "Quarterly", "Semiannual", "Annual"]
    face_values = list(range(50000, 2000001, 50000))  # $50,000 to $2,000,000 in $50,000 increments

    num_lapsed = max(int(num_records * 0.4), 1)  # At least 40% lapsed policies
    lapsed_indices = set(random.sample(range(num_records), num_lapsed))

    for i in range(num_records):
        age = random.randint(18, 75)
        gender = random.choice(genders)
        smoker = random.choice(smoker_status)
        bmi = round(random.uniform(15.0, 40.0), 1)
        zip_code = random.choice(zip_codes)
        children = random.randint(0, 5)
        
        # Annual premium calculation
        base_premium = 100
        age_factor = age * 3
        smoker_factor = 500 if smoker == "Yes" else 0
        bmi_factor = (bmi - 25) * 20
        annual_premium = base_premium + age_factor + smoker_factor + bmi_factor
        annual_premium = max(annual_premium, 0)
        
        # Choose a premium frequency and calculate the premium amount accordingly
        frequency = random.choice(premium_frequencies)
        if frequency == "Monthly":
            premium_amount = annual_premium / 12
        elif frequency == "Quarterly":
            premium_amount = annual_premium / 4
        elif frequency == "Semiannual":
            premium_amount = annual_premium / 2
        else:  # Annual
            premium_amount = annual_premium

        # Determine if the policy is lapsed
        policy_lapsed = 1 if i in lapsed_indices else 0

        # Select a policy face value and type
        face_value = random.choice(face_values)

        # Determine the presence of riders (randomly include some)
        rider_accidental_death = random.choice([0, 1])
        rider_critical_illness = random.choice([0, 1])
        rider_waiver_of_premium = random.choice([0, 1])
        # Append data to the lists
        data["Age"].append(age)
        data["BMI"].append(bmi)
        data["ZIP Code"].append(zip_code)
        data["Children"].append(children)
        data["Annual Premium"].append(round(annual_premium, 2))
        #data["Premium Frequency"].append(frequency)
        data["Premium Amount"].append(round(premium_amount, 2))
        data["Policy Lapsed"].append(policy_lapsed)
        data["Policy Face Value"].append(face_value)
        data["Rider_Accidental Death"].append(rider_accidental_death)
        data["Rider_Critical Illness"].append(rider_critical_illness)
        data["Rider_Waiver of Premium"].append(rider_waiver_of_premium)

        # One-hot encoding for Gender
        data["Gender_Male"].append(1 if gender == "Male" else 0)
        data["Gender_Female"].append(1 if gender == "Female" else 0)

        # One-hot encoding for Smoker
        data["Smoker_Yes"].append(1 if smoker == "Yes" else 0)
        data["Smoker_No"].append(1 if smoker == "No" else 0)

        # One-hot encoding for Premium Frequency
        data["Premium_Frequency_Monthly"].append(1 if frequency == "Monthly" else 0)
        data["Premium_Frequency_Quarterly"].append(1 if frequency == "Quarterly" else 0)
        data["Premium_Frequency_Semiannual"].append(1 if frequency == "Semiannual" else 0)
        data["Premium_Frequency_Annual"].append(1 if frequency == "Annual" else 0)

    return pd.DataFrame(data)

