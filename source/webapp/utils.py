def article_validate(description, detailed_description, price, remainder):
    errors = {}
    if not description:
        errors['description'] = "The description field is required."
    elif len(description) > 100:
        errors['description'] = "Description's len must be less than 200!!!"
    if not detailed_description:
        errors['detailed_description'] = "Detailed description field is required"
    elif len(detailed_description) > 2000:
        errors['detailed_description'] = "Detailed description's len must be less than 3000!!!"
    if not price:
        errors['price'] = "Price field is required"
    elif len(price) > 7:
        errors['price'] = "Prices' len must be less than 3000!!!"
    if not remainder:
        errors['remainder'] = "Remainder field is required"
    return errors