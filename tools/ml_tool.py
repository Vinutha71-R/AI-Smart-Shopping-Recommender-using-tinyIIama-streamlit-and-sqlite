# Optional segmentation model
def segment_customer(age, gender):
    if age < 25:
        return "young"
    elif gender == "female":
        return "female_segment"
    else:
        return "general"
