import random
import pandas as pd
import zipcodes as zips

def generate_life_insurance_data(num_records):
    '''
    Function generates synthetic life insurance data.
    '''

    # Get list of real zip codes for use in integrating in a geospatial model.
    zip_codes = []

    for zip in zips.list_all():

        zip_codes.append(zip['zip_code'])

    # Main dictionary of variables.
    data = {
        "Age": [], # Age of the insured.
        "BMI": [], # BMI of the insured.
        "ZIP Code": [], # Zip code the insured lives in.
        "Children": [], # How many children the insured has.
        "Annual Premium": [], # Annual premium amount paid by the insured.
        "Premium Amount": [], # Monthly premium amount.
        "Policy Lapsed": [], # Whether the policy has lapsed or not.
        "Policy Face Value": [], # Face value of the policy.
        "Rider Accidental Death": [], # Rider for accidental death.
        "Rider Critical Illness": [], # Rider for critical illness.
        "Rider Waiver of Premium": [], # Rider for waiver of premium.
        "Gender_Male": [], # If the insured is a male.
        "Gender_Female": [], # If the insured is a female.
        "Smoker_Yes": [], # If the imsured is a smoker.
        "Smoker_No": [], # If the insured is not a smoker.
        "Premium_Frequency_Monthly": [], # Whether the premium frequency is monthly.
        "Premium_Frequency_Quarterly": [], # Whether the premium frequency is quarterly.
        "Premium_Frequency_Semiannual": [], # Whether the premium frequency is semiannual.
        "Premium_Frequency_Annual": [] # Whether the premium frequency is annual.
    }
    
    # Define possible values for each attribute
    genders = ["Male", "Female"]
    smoker_status = ["Yes", "No"]
    zip_codes = zip_codes
    premium_frequencies = ["Monthly", "Quarterly", "Semiannual", "Annual"]
    face_values = list(range(50000, 2000001, 50000))  # $50,000 to $2,000,000 in $50,000 increments

    # Limit the number of lapsed policies tp 40 percent of the dataset.
    num_lapsed = max(int(num_records * 0.4), 1)  # At least 40% lapsed policies
    lapsed_indices = set(random.sample(range(num_records), num_lapsed))

    # For each row requested choose random figures for each attribute.
    for i in range(num_records):

        # Choose our randoms.
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
        data["Premium Amount"].append(round(premium_amount, 2))
        data["Policy Lapsed"].append(policy_lapsed)
        data["Policy Face Value"].append(face_value)
        data["Rider Accidental Death"].append(rider_accidental_death)
        data["Rider Critical Illness"].append(rider_critical_illness)
        data["Rider Waiver of Premium"].append(rider_waiver_of_premium)

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

    # Return the resulting pandas dataframe.
    return pd.DataFrame(data)

